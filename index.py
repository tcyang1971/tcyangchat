#import os

import openai
from flask import Flask

app = Flask(__name__)
openai.api_key = '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'

@app.route("/")
def index():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="靜宜大學評價如何？",
        max_tokens=128,
        temperature=0.5,
    )
    msg = response.choices[0].text
    return msg

if __name__ == "__main__":
    app.run()