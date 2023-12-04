import json
from hugchat import hugchat

async def generate_ai_summary(abi):
    verified = "verified" if abi["verified"] else "not verified"
    abi = minify_json(abi)
    prompt = f"""Is this a token, dex, liquidity pool, ens? I'm not sure if its any, but given the ABI what might this smart contract be given its ABI. {abi}"""
    with open("app/data/cookie.json", "r") as f:
        cookies = json.load(f)

    chatbot = hugchat.ChatBot(cookies=cookies)  
    chatbot.switch_llm(4)       # switch to openchat
    # print(f"Using {chatbot.active_model.name}")
    
    # response = chatbot.query(prompt)
    # return response
    for response in chatbot.query(prompt,stream=True):
        if response is None:
            break
        text = response["token"]
        yield text.encode("utf-8")

def minify_json(data):
    """
    Minify a JSON string by removing whitespace characters.

    This function takes a JSON string, removes all whitespace characters, and returns the minified JSON string.

    Args:
        data (str): A JSON string.

    Returns:
        str: The minified JSON string.

    Example:
        >>> data = '{"name": "John", "age": 30}'
        >>> minified_data = minify_json(data)
        >>> print(minified_data)
        '{"name":"John","age":30}'

    This function can be useful for reducing the size of JSON data by removing unnecessary whitespace.
    """
    json_string = json.dumps(data)
    return "".join(json_string.split())
