import os

import openai
from flask import Flask
#from waitress import serve



app = Flask(__name__)
openai.api_key = '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'

@app.route("/")
def index():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="台灣大學評價如何？",
        max_tokens=128,
        temperature=0.5,
    )
    return response.choices[0].text

if __name__ == "__main__":
    app.run()
    #serve(app, host='0.0.0.0', port=8080)


