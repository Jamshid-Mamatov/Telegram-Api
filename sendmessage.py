import requests
import json
from pprint import pprint



def sendMsg(id_u):
    token='1601845406:AAFjsTNp2FSn-Et3Vamlhv1xkX9RaRvt_WE'
    url=f'https://api.telegram.org/bot{token}/sendMessage'
    
    payload={
        'chat_id':id_u,
        'text':'ok'
    }
    r=requests.get(url,params=payload)


token='1601845406:AAFjsTNp2FSn-Et3Vamlhv1xkX9RaRvt_WE'
url=f'https://api.telegram.org/bot{token}/getUpdates'
r=requests.get(url).json()
data=r['result']
ids=[]
for i in data:
    id=i['message']['from']['id']
    if id not in  ids:
        ids.append(id)

sendMsg(ids)