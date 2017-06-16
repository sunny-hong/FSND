from twilio.rest import Client

#Your account SID and auth token
account_sid = "ACcc7c0c18375b1f5948b58a8eac82eb99"
auth_token = "dfe0c3711bfcad620b23b418f3b44041"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body = "Hello! Sending from Twilio - Sunny ",
    to="+15734242344",
    from_= "+16782637476"
)
print message.sid

#emergency code C7BRcXNT/bj4Vyz3aFxTINiURQy8IvefbmpZuZtM
