import json
from flask import Flask, request, jsonify
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=["GET", "POST"])
def command():

    try:
        body = request.form.get("Body")
        
        resp = MessagingResponse()
        resp.message(body)
        return str(resp)
    
    except Exception as e:
        resp = MessagingResponse()
        resp.message("An error occured, please try again!")

        return str(resp)
    
if __name__ == "__main__":
    app.run(port=8000, debug=True)