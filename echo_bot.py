import requests

import json

#@echo_jamshid_bot

token="1407685639:AAH8rpMbq64izZqkxxDieN6MpQof-DOCmIk"

def sendMsg(id,text,msg_id):
    url=f"https://api.telegram.org/bot{token}/sendMessage"
    
    payload={
        'chat_id':id,
        'text':text,
        'reply_to_message_id':msg_id
    }
    r=requests.get(url,params=payload)


def stikerSend(id,file_id,msg_id):
    url=f"https://api.telegram.org/bot{token}/sendSticker"
    payload={
        'chat_id':id,
        'sticker':file_id,
        'reply_to_message_id':msg_id
    }
    r=requests.get(url,params=payload)



def update():

    url=f"https://api.telegram.org/bot{token}/getUpdates"
    
    r=requests.get(url).json()
    data=r['result']
    message=data[-1]['message'].get('text')
    message_stckr=data[-1]['message'].get('sticker')
    if message_stckr!=None:
        message_stckr=message_stckr['file_id']
    id=data[-1]['message']['chat']['id']
    msg_id=data[-1]['message']['message_id']
    return message,message_stckr,id,msg_id




last_msg_id=None
while True :
    
    text,message_stckr,chat_id,msg_id=update()
    
    if last_msg_id!=msg_id:
        last_msg_id=msg_id
        if text!=None :
            sendMsg(chat_id,text,msg_id)
        else:
            stikerSend(chat_id,message_stckr,msg_id)
        
    





