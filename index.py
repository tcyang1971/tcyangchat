from flask import Flask
app = Flask(__name__)

import openai
import os
openai.api_key = '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'

@app.route("/")
def index():
    # return "Hello 子青!"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="靜宜大學評價如何？",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

# 接收到回覆訊息後，移除換行符號
    message = response.choices[0].text.strip()
    return message

if __name__ == "__main__":
    app.run()


