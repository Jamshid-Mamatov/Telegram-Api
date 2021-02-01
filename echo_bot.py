import requests

import json



token="1636539811:AAE7pYJmxdLFXTLD32Ery6EXFFJwRRbqYWs"

url=f"https://api.telegram.org/bot{token}/getUpdates"

r=requests.get(url).json()

data=r['result'][-1]
id=data['message']['from']['id']
text=data['message']['text']

url=f"https://api.telegram.org/bot{token}/sendMessage"

payload={
    'chat_id':id,
    'text':text
}
r=requests.get(url,params=payload)