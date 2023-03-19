import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

from flask import Flask, request, make_response, jsonify
app = Flask(__name__)
#from waitress import serve


@app.route("/")
def index():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="靜宜大學資管系楊子青老師在獲獎方面？",
        max_tokens=128,
        temperature=0.5,
    )
    msg = response.choices[0].text
    return msg


@app.route("/webhook", methods=["POST"])
def webhook():
    # build a request object
    req = request.get_json(force=True)
    # fetch queryResult from json
    msg =  req.get("queryResult").get("queryText")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=msg,
        max_tokens=30,
        temperature=0.5,
    )
    info = "AI：" + response.choices[0].text
    return make_response(jsonify({"fulfillmentText": info}))


if __name__ == "__main__":
    app.run()
    #serve(app, host='0.0.0.0', port=8080)
