#install venv
#pip install pywin32
import win32com.client
from twilio.rest import Client

outlook = win32com.client.Dispatch("Outlook.Application")
outlook_ns = outlook.GetNamespace('MAPI')

#folders are case sensitive
myfolder = outlook_ns.Folders['caleb_cheney1@baylor.edu'].Folders['Inbox']

messages = myfolder.Items

messagecount = 0

for message in messages:
    messagecount += 1

accountSID = 'AC70e306e427e8042b64e6e5831952001a'

authToken = '1e6aad7f145a6b2f87fee73ad755e387'

client = Client(accountSID,authToken)

TwilioNumber = '+15734051710'

mycellphone = '+17134999094'

textmessage = client.messages.create(to=mycellphone,from_=TwilioNumber,body='you have ' + str(messagecount) + ' emails in your inbox.')



print(textmessage.status)
print(messagecount)


'''
for message in messages:
    if message.UnRead == True:
        print(message.sender)
        print(message.subject)

        if 'absence' in message.subject:
            print('Found message with absence')

            Msg = outlook.CreateItem(0)
            Msg.Importance = 1
            Msg.Subject = 'Got your ' + message.subject + ' email'
            Msg.HTMLBody = 'Hi' + str(message.sender) + '\n' + ' sorry you are not well'

            Msg.To = message.sender.GetExchangeUser().PrimarySmtpAddress
            Msg.ReadReceiptRequested = True

            Msg.Send()
'''