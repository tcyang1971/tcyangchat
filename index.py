import os
import openai
import requests

from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__)

openai.api_key = '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'

@app.route("/")
def index():
    # return "Hello 子青!"
    #response = openai.Completion.create(
    #    model="text-davinci-003",
    #    prompt="台灣大學評價如何？",
    #    max_tokens=128,
    #    temperature=0.5,
    #)
    #message = response.choices[0].text

    response = requests.post(
        'https://api.openai.com/v1/engine/davinci-codex/completions',
        headers={
            'Content-Type': 'application/json',
            'Authorization': 'Bearer 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'
        },
        json={
            'prompt': "台灣大學評價如何？",
            'max_tokens': 50,
            'n': 1,
            'stop': '\n'
        }
    )

    # 解析回復，並返回生成的回復
    message = response.json()['choices'][0]['text'].strip()

    message = "Hi"
    return message

if __name__ == "__main__":
   app.run()


