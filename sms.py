from twilio.rest import Client 
 
account_sid = 'Type your twilio account sid' 
auth_token = 'Type your twilio auth token' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+TypeNumber',  
                              body="I Am The Hacker!",      
                              to='+TypeNumber' 
                          ) 
 
print(message.sid)