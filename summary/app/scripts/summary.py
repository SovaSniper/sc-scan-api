import json
from hugchat import hugchat
from hugchat.login import Login

def generate_cookies():
    # Save cookies to the local directory
    user = ""
    password = ""
    sign = Login(user, password)
    cookies = sign.login()

    # Save cookies to the local directory
    cookie_path_dir = "../data"
    sign.saveCookiesToDir(cookie_path_dir)

def main():
    with open("../data/cookie.json", "r") as f:
        cookies = json.load(f)

    chatbot = hugchat.ChatBot(cookies=cookies)  

    chatbot.get_available_llm_models()
    for i in chatbot.get_available_llm_models():
        print(i)

    chatbot.switch_llm(4)   # openchat/openchat_3.5
    print(chatbot.active_model.name)

if __name__ == '__main__':
    generate_cookies()
    # main()