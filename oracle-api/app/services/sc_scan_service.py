import json
from typing import Union
import requests
from web3 import Web3

from app.services.utils.bytecode_to_opcode import bytecode_to_opcode
from app.services.utils.network import get_api, get_rpc, get_key
from app.services.utils.get_signatures import get_signatures
from app.services.utils.decrypt import decrypt
from app.services.constants import ENCRYPTION_KEY

class ScScan:
    def __init__(self, network: str) -> None:
        self.network = network
        self.rpc_url = get_rpc(self.network)
        key = get_key(self.network)
        self.key = None
        if key:
            self.key = decrypt(key, ENCRYPTION_KEY)
        pass

    def preconditions(self, contract: str):
        if not Web3.is_address(contract):
            raise Exception("Invalid contract address")

        if not self.rpc_url:
            raise Exception("Invalid network")
        
    def get_opcode(self, contract: str) -> [[], []]:
        self.preconditions(contract)

        bytecode = self.get_bytecode(contract)
        if not bytecode:
            raise Exception("Invalid contract on network. No bytecode found")

        opcode = [[], []]
        if bytecode:
            opcode = bytecode_to_opcode(bytecode)

        return opcode

    def get_bytecode(self, contract: str) -> str:
        self.preconditions(contract)
    
        web3 = Web3(Web3.HTTPProvider(self.rpc_url))
        check_sum_address = Web3.to_checksum_address(contract)
        bytecode = web3.eth.get_code(check_sum_address)
        # print("Bytecode: ", bytecode)

        print(self.rpc_url)
        if bytecode.hex() == '0x':
            return ''
        if bytecode.hex().startswith('0x'):
            return bytecode.hex()[2:]
        return ''
    
    def get_abi(self, contract: str) -> Union[dict, None]:
        self.preconditions(contract)

        api_url = f"{get_api(self.network)}/api?module=contract&action=getabi&address={contract}"
        if self.key:
            api_url += f"&apikey={self.key}"
        print(api_url)
        response = requests.get(api_url)

        if response.status_code != 200:
            print(f"Request failed with status code: {response.status_code}")
            return None

        data = response.json()

        if data.get("status") == "0":
            print(data.get("result"))  # error message
            return None

        try:
            contract_abi = json.loads(data.get("result"))
            return contract_abi
        except Exception as e:
            print(e)
            return None

    def get_selectors(self, opcode: [[], []]) -> list[str]:
        """
        Extracts unique selectors from an array of opcodes that start with "PUSH4".

        Parameters:
        - opcodes (List[List[str]]): An array of opcode sub-arrays.

        Returns:
        - List[str]: An array of unique selectors.
        """
        selectors = {op[1] for op in opcode if op and op[0] == "PUSH4"}

        return list(selectors)
    
    def get_events(self, opcode: [[], []]) -> list[str]:
        """
        Extracts unique event values from an array of opcodes where the first element is "PUSH32"
        and the second element does not represent a zero or F value.

        Parameters:
        - opcodes (List[List[str]]): An array of opcode sub-arrays.

        Returns:
        - List[str]: An array of unique event values.
        """
        unique_events = set()

        for op in opcode:
            if op and op[0] == "PUSH32" and not (op[1] == "zero" or op[1] == "F"):
                unique_events.add(op[1])

        return list(unique_events)
    
    def get_signatures(self, opcode: [[], []]) -> dict:
        fns = self.get_selectors(opcode)
        evts = self.get_events(opcode)
        return get_signatures(",".join(fns), ",".join(evts))
    
    def get_data(self, contract: str) -> dict:
        opcode = self.get_opcode(contract)
        on_chain_abi = self.get_abi(contract)

        signatures = self.get_signatures(opcode)
        verified = False
        abi = []
        if on_chain_abi:  
            verified = True
            # If on-chain, then add signature to abi
            result_dict = {"function": {}, "event": {}}
            for result in signatures["functions"]:
                result_dict["function"][result["name"]] = result["signature"]
            for result in signatures["events"]:
                result_dict["event"][result["name"]] = result["signature"]

            for item in on_chain_abi:
                if "name" not in item:
                    continue
                name = item["name"]
                item_type = item["type"]
                if not (item_type == "function" or item_type == "event"):
                    continue
                
                if name in result_dict[item_type]:
                    item["signature"] = result_dict[item_type][name]
            
            abi.extend(on_chain_abi)
        else:
            abi.extend(signatures["functions"])
            abi.extend(signatures["events"])

        return {"abi": abi, "verified": verified}