import os

import openai
from flask import Flask, redirect, render_template, request, url_for

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

