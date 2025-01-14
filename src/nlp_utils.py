# ------------------------------------------------------------------------------
# ChatGPTを使用するためのプログラム
# ------------------------------------------------------------------------------

import re
import os
import openai  # pip install openai
from dotenv import load_dotenv  # pip install python-dotenv

# 環境変数の読み込み
load_dotenv()

# APIキーの設定
openai.api_key = os.environ['CHATGPI_API_KEY']

class ChatGPT:
    """ChatGPT処理クラス"""

    # ChatGPTのモデル名
    MODEL35 = "gpt-3.5-turbo"
    MODEL4 = "gpt-4-turbo-preview"

    @staticmethod
    def get_exact_model_name(args_chatgpt: str) -> str:
        """ChatGPTのモデル名の正式名称を取得"""
        if args_chatgpt is None:
            return ChatGPT.MODEL35
        if re.match(r'^$', args_chatgpt):
            return ChatGPT.MODEL35
        if re.match(r'^3\.5', args_chatgpt):
            return ChatGPT.MODEL35
        if re.match(r'^4', args_chatgpt):
            return ChatGPT.MODEL4
        if re.match(r'^gpt-3\.5', args_chatgpt):
            return ChatGPT.MODEL35
        if re.match(r'^gpt-4', args_chatgpt):
            return ChatGPT.MODEL4
        return ChatGPT.MODEL35



# API Document
# https://platform.openai.com/docs/api-reference/chat/create
# Chat Usage Example
# https://cookbook.openai.com/examples/how_to_format_inputs_to_chatgpt_models

if __name__ == '__main__':
    import sys

    def yes_no_input(question: str):
        while True:
            choice = input(question + " [y/N]: ").lower()
            if choice in ['y', 'ye', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False

    prompt = f"""
    最も有名なRFCは何番ですか
    """

    print(f"[+] prompt: \n{prompt}")
    print(f"")
    if yes_no_input("[?] 上記の内容でChatGPTに質問します。よろしいですか？"):
        pass
    else:
        sys.exit(0)

    model = ChatGPT.MODEL35
    response = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    # GPTからの応答の表示
    text = response.choices[0].message.content
    print(f"[+] " + "-" * 80)
    print(f"[+] output: \n{text}")
    print(f"[+] " + "-" * 80)
    print(f"[ ] ")
