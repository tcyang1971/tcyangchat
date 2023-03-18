import os
import openai
import requests

from flask import Flask, request
app = Flask(__name__)

openai.api_key = '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'

@app.route("/")
def index():
    # return "Hello 子青!"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="台灣大學評價如何？",
        max_tokens=50,
        temperature=1,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=[" END"]
        )
    message = response.choices[0].text
    return message

if __name__ == "__main__":
   app.run()
