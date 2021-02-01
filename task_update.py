import requests
import json
from pprint import pprint

token='1601845406:AAFjsTNp2FSn-Et3Vamlhv1xkX9RaRvt_WE'

url=f'https://api.telegram.org/bot{token}/getUpdates'

r=requests.get(url)

data=r.json()['result']

for i in data:
    user=i['message']['from']

    first_name=user.get('first_name',"")

    last_name=user.get('last_name',"")

    print(f"{first_name}  {last_name}")



    
 