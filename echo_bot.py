import requests

import json

token="1636539811:AAE7pYJmxdLFXTLD32Ery6EXFFJwRRbqYWs"

def sendMsg(id,text):
    url=f"https://api.telegram.org/bot{token}/sendMessage"

    payload={
        'chat_id':id,
        'text':text

    }
    r=requests.get(url,params=payload)
    


def update():

    url=f"https://api.telegram.org/bot{token}/getUpdates"
    r=requests.get(url).json()
    data=r['result']
    message=data[-1]['message']['text']
    id=data[-1]['message']['from']['id']
    return message,id


last_text=""
while True :
    
    text,id=update()
    if last_text!=text:
        sendMsg(id,text)
        last_text=text
    





