import os
import requests
from pprint import pprint 
token=os.environ['token']

def sendMsg(markdown_list):
    url=f'https://api.telegram.org/bot{token}/sendMessage'
    for text in markdown_list:
        payload={
            'chat_id':937691492,
            'text':text,
            'parse_mode':'MarkdownV2'
        }
        r=requests.get(url,payload)

markdown=['_Mamatov_','*Jamshid*','__python__','~tuit~','*_~__student__~_*',
'[Jamshid](https://t.me/Jamshid_Mamatov)','[codeschool](https://t.me/codeschooluz)']
sendMsg(markdown)

