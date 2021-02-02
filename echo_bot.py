import requests

import json

#@echo_jamshid_bot

token="1407685639:AAH8rpMbq64izZqkxxDieN6MpQof-DOCmIk"

def sendMsg(id,text,msg_id):
    url=f"https://api.telegram.org/bot{token}/sendMessage"
    
    payload={
        
        'reply_to_message_id':msg_id
    }
    r=requests.get(url,params=payload)
    


def update():

    url=f"https://api.telegram.org/bot{token}/getUpdates"
    r=requests.get(url).json()
    data=r['result']
    message=data[-1]['message']['text']
    id=data[-1]['message']['chat']['id']
    msg_id=data[-1]['message']['message_id']
    return message,id,msg_id


last_msg_id=None
while True :
    
    text,id,msg_id=update()
    
    if last_msg_id!=msg_id:
        last_msg_id=msg_id
        sendMsg(id,text,msg_id)
        
    





