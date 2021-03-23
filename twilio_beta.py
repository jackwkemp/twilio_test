from twilio.rest import Client
from flask import Flask, render_template, request

app = Flask(__name__)

account_sid = 'INSERT ACCOUNT SID HERE'
auth_token = 'INSERT AUTH TOKEN HERE'
client = Client(account_sid, auth_token)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send', methods=['POST'])
def send():
    message = client.messages.create(
        from_='INSERT TWILIO PHONE NUMBER HERE',
        body=request.form['sms'],
        to=request.form['number']
    )

    return message.sid


if __name__ == '__main__':
    app.run(debug=True)
