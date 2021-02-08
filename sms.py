from twilio.rest import Client 
 
account_sid = 'AC976f69c721ed0e8f338d1a7de0a1fa33' 
auth_token = '6aacbfc34511cdd7aefa86848dc29b11' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+13343784054',  
                              body="I Am The Hacker!",      
                              to='+YourNumber' 
                          ) 
 
print(message.sid)