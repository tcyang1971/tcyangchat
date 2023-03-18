import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

from flask import Flask
app = Flask(__name__)
from waitress import serve


@app.route("/")
def index():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="靜宜大學資管系楊子青老師在App開發方面？",
        max_tokens=128,
        temperature=0.5,
    )
    msg = response.choices[0].text
    return msg

if __name__ == "__main__":
    #app.run()
    serve(app, host='0.0.0.0', port=8080)
