# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()
    #file object
    #read the temperature from a  file
    file_object = open("temp.txt","r")
    mesg = file_object.readline()
    # Add a message and respond to received number
    resp.message(mesg)
    file_object.close()

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
