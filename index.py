import os
import openai

from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__)

openai.api_key = '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'

@app.route("/")
def index():
    # return "Hello 子青!"
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
        max_tokens=128,
        temperature=0.5,
        messages=[
            {"role": "user", "content": "靜宜大學資管系楊子青老師"},
            {"role": "assistant", "content": "原來你是 子青老師 呀"},
            {"role": "user", "content": "請問楊子青老師的教學特色？"}
        ]
    )
    #message = response.choices[0].text
    message = "Hi"
    return message

if __name__ == "__main__":
   app.run()


