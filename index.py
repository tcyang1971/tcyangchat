from flask import Flask
app = Flask(__name__)

import openai
import os
openai.api_key = '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'

@app.route("/")
def index():
    # return "Hello 子青!"
    message = "Gi"
    return message

if __name__ == "__main__":
   app.run()


