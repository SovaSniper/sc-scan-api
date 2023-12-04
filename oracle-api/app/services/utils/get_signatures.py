import requests
from typing import Dict, List, Any

from app.services.constants import OPEN_CHAIN_API

def get_signatures(fn: str = None, evt: str = None) -> Dict[str, List[Dict[str, Any]]]:
    response = requests.get(f"{OPEN_CHAIN_API}/lookup?function={fn}&event={evt}&filter=true")
    data = response.json()

    functions = []
    events = []

    def process_function(key, info, type):
        inputs = get_params(info["name"])
        outputs = []
        name = info["name"].split("(")[0]
        # labelhash = hashlib.sha3_256(info['name'].encode()).hexdigest()

        abi = {
            "signature": key,
            "inputs": [],
            "name": name,
            "type": type,
        }

        for index, input in enumerate(inputs):
            abi["inputs"].append(
                {"internalType": input, "name": f"param_{index}", "type": input}
            )

        if type == "function":
            functions.append(abi)
            abi["stateMutability"] = ""
            abi["outputs"] = []

            for index, output in enumerate(outputs):
                abi["outputs"].append(
                    {"internalType": output, "name": f"param_{index}", "type": output}
                )
        else:
            events.append(abi)

    fns = data["result"]["function"] if "function" in data["result"] else {}
    for key, info in fns.items():
        if info and info[0]["name"]:
            process_function(key, info[0], "function")

    evts = data["result"]["event"] if "event" in data["result"] else {}
    for key, info in evts.items():
        if info and info[0]["name"]:
            process_function(key, info[0], "event")

    return {"functions": functions, "events": events}

def get_params(method: str) -> List[str]:
    open_paren_index = method.find('(')
    close_paren_index = method.find(')')

    if open_paren_index == -1 or close_paren_index == -1 or open_paren_index >= close_paren_index:
        return []

    params_str = method[open_paren_index + 1:close_paren_index]

    params = []
    param_start = 0
    nested_parentheses = 0

    for i in range(len(params_str)):
        if params_str[i] == '(':
            nested_parentheses += 1
        elif params_str[i] == ')':
            nested_parentheses -= 1

        if nested_parentheses == 0 and params_str[i] == ',':
            params.append(params_str[param_start:i].strip())
            param_start = i + 1

    params.append(params_str[param_start:].strip())

    return params
