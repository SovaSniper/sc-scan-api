from app.services.constants import ETHERSCAN_API_TOKEN, POLYGONSCAN_API_TOKEN, FTMSCAN_API_TOKEN

class ChainID:
    """
    A class to define chain IDs for various blockchain networks.

    This class contains constants representing the chain IDs for Ethereum, Polygon (formerly Matic), and Fantom networks.
    These constants can be used when working with different blockchain networks.
    """
    ETHEREUM_MAINNET = '1'
    ETHEREUM_GOERLI = '5'
    ETHEREUM_SEPOLIA = '11155111'
    POLYGON_MAINNET = '137'
    POLYGON_MUMBAI = '80001'
    AVALANCHE_MAINNET = '43114'
    AVALANCHE_FUJI = '43113'
    FANTOM_MAINNET = '250'
    FANTOM_TESTNET = '4002'

def get_rpc(network: ChainID) -> str:
    """
    Get the RPC (Remote Procedure Call) endpoint for a given blockchain network.

    This function takes a `ChainID` representing the network and returns the corresponding RPC endpoint URL for that network.

    Args:
        network (ChainID): A chain identifier representing the blockchain network.

    Returns:
        str: The RPC endpoint URL for the specified network. Returns an empty string if the network is not found.

    Example:
        >>> get_rpc(ChainID.ETHEREUM_MAINNET)
        'https://rpc.ankr.com/eth'
    """
    return {
        ChainID.ETHEREUM_MAINNET: 'https://rpc.ankr.com/eth',
        ChainID.ETHEREUM_GOERLI: 'https://rpc.ankr.com/eth_goerli',
        ChainID.ETHEREUM_SEPOLIA: 'https://rpc.ankr.com/eth_sepolia',
        ChainID.POLYGON_MAINNET: 'https://rpc.ankr.com/polygon',
        ChainID.POLYGON_MUMBAI: 'https://rpc.ankr.com/polygon_mumbai',
        ChainID.FANTOM_MAINNET: 'https://rpc.ankr.com/fantom',
        ChainID.FANTOM_TESTNET: 'https://rpc.ankr.com/fantom_testnet',
        ChainID.AVALANCHE_MAINNET: 'https://1rpc.io/avax/c',
        ChainID.AVALANCHE_FUJI: 'https://endpoints.omniatech.io/v1/avax/fuji/public',
    }.get(network, "")

def get_api(network: str) -> str:
    """
    Get the API endpoint for a given blockchain network.

    This function takes a network identifier as a parameter and returns the corresponding API endpoint for that network.
    
    Args:
        network (str): A string representing the network identifier.

    Returns:
        str: The API endpoint URL for the specified network. Defaults to Ethereum Mainnet's API if the network is not found.

    Example:
        >>> get_api(ChainID.ETHEREUM_MAINNET)
        'https://api.etherscan.io/'
    """
    return {
        ChainID.ETHEREUM_MAINNET: 'https://api.etherscan.io',
        ChainID.ETHEREUM_GOERLI: 'https://api-goerli.etherscan.io',
        ChainID.ETHEREUM_SEPOLIA: 'https://api-sepolia.etherscan.io',
        ChainID.POLYGON_MAINNET: 'https://api.polygonscan.com',
        ChainID.POLYGON_MUMBAI: 'https://api-testnet.polygonscan.com',
        ChainID.AVALANCHE_MAINNET: 'https://api.routescan.io/v2/network/mainnet/evm/43114/etherscan',
        ChainID.AVALANCHE_FUJI: 'https://api.routescan.io/v2/network/testnet/evm/43113/etherscan',
        ChainID.FANTOM_MAINNET: 'https://api.ftmscan.com',
        ChainID.FANTOM_TESTNET: 'https://api-testnet.ftmscan.com',
    }.get(network, '')

def get_key(network: str) -> str:
    return {
        ChainID.ETHEREUM_MAINNET: ETHERSCAN_API_TOKEN,
        ChainID.ETHEREUM_GOERLI: ETHERSCAN_API_TOKEN,
        ChainID.ETHEREUM_SEPOLIA: ETHERSCAN_API_TOKEN,
        ChainID.POLYGON_MAINNET: POLYGONSCAN_API_TOKEN,
        ChainID.POLYGON_MUMBAI: POLYGONSCAN_API_TOKEN,
        ChainID.FANTOM_MAINNET: FTMSCAN_API_TOKEN,
        ChainID.FANTOM_TESTNET: FTMSCAN_API_TOKEN
    }.get(network, '')