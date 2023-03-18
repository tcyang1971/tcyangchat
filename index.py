import os
import openai

from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__)

openai.api_key = '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'

@app.route("/")
def index():
    # return "Hello 子青!"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="台灣大學評價如何？",
        max_tokens=128,
        temperature=0.5,
    )
    #message = response.choices[0].text
    message = "Hi"
    return message

if __name__ == "__main__":
   app.run()


