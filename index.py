import os

import openai
from flask import Flask



app = Flask(__name__)
openai.api_key = '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'

@app.route("/")
def index():
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="chatBot",
        temperature=1,
    )
    return response.choices[0].text

if __name__ == "__main__":
    app.run()

