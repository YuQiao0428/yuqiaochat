from flask import Flask
app = Flask(__name__)
import openai
import os
openai.api_key = os.getenv("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")
@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json(force=True)
    msg =  req["queryResult"]["queryText"]
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=msg,
        max_tokens=100,
        temperature=0.5,
    )
    info = "AI：" + response.choices[0].text
    return make_response(jsonify({"fulfillmentText": info}))

if __name__ == "__main__":
    app.run()
