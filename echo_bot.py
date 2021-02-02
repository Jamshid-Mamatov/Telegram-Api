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
    date=data[-1]['message']['date']
    return message,id,date


last_date=None
while True :
    
    text,id,date=update()
    if last_date!=date:
        sendMsg(id,text)
        last_date=date
    





