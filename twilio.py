from twilio.rest import Client

account_sid = 'INSERT ACCOUNT SID HERE'
auth_token = 'INSERT AUTH TOKEN HERE'

client = Client(account_sid, auth_token)

sms = input("Enter the phone message: ")
number = input("Enter the phone number: ")  

message = client.messages.create(
    from_='INSERT TWILIO PHONE NUMBER HERE',
    body=sms,
    to=number
)

print(message.sid)
