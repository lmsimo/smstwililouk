from twilio.rest import TwilioRestClient
from credentials import account_sid, auth_token, my_cell, my_twilio

# Find these values at https://twilio.com/user/account
client = TwilioRestClient(ACb021cf2144a7dbc92a717abcb315f4f7, 32fc5d5d9dba1eadd8809d56363429d5)

my_msg = "hey ipran service"

message = client.mesages.create(to=my_cell, from_=my_twilio,
                                     body=my_msg)
