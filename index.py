#import os

import openai
from flask import Flask

app = Flask(__name__)
openai.api_key = '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'

@app.route("/")
def index():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="靜宜大學資管系楊子青老師在指導專題方面？",
        max_tokens=128,
        temperature=0.5,
    )
    msg = response.choices[0].text
    return msg

if __name__ == "__main__":
    app.run()