from twilio.rest import Client

TWILIO_ACCOUNT_SID='AC5276dc9459e0c7a26a29344600fa7054'
TWILIO_AUTH_TOKEN='4c60774047dd308c18c388669cba30b7'


client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

client.messages.create(from_='+12028758483' ,
                       to='+18657220550',
                       body='This is Nick Brown, test me on my other number')




                       
