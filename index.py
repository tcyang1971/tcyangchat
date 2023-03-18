from flask import Flask
app = Flask(__name__)

import openai
openai.api_key = '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'

@app.route("/")
def index():
    # return "Hello 子青!"

    return "Hello 子青!"

if __name__ == "__main__":
    app.run()