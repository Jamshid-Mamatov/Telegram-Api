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
    print(r.url)


url=f"https://api.telegram.org/bot{token}/getUpdates"
r=requests.get(url).json()
data=r['result']
user_msg={}
ids=[]
for i in data:
    id=i['message']['from']['id']
    text=i['message']['text']
    sendMsg(id,text)

