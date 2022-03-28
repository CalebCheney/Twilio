#install venv
#pip install twilio
from cgitb import text
from twilio.rest import Client

accountSID = 'AC70e306e427e8042b64e6e5831952001a'

authToken = '1e6aad7f145a6b2f87fee73ad755e387'

client = Client(accountSID,authToken)

TwilioNumber = '+15734051710'

mycellphone = '+17134999094'

textmessage = client.messages.create(to=mycellphone,from_=TwilioNumber,body="Hello World!")



print(textmessage.status)

#make a phone call
call = client.calls.create(url='http://demo.twilio.com/docs/voice.xml',to=mycellphone,from_=TwilioNumber)

