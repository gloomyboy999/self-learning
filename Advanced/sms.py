from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC0bab2db4d8ea4af00718789c4af5bbad"
# Your Auth Token from twilio.com/console
auth_token  = "35ddde55a6ff28e59e048424b6f52b59"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+886952692652", 
    from_="+13252402161",
    body="大家好,  吃飽了嗎?")

print(message.sid)