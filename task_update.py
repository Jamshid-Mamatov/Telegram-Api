import requests
import json
from pprint import pprint
token = '1601845406:AAFjsTNp2FSn-Et3Vamlhv1xkX9RaRvt_WE'
url = f'https://api.telegram.org/bot{token}/getUpdates'
r = requests.get(url)
# print(r.url)
data = r.json()
updates = data['result']
for update in updates:
    user=update['message']['from']
    if user.get('last_name'):
        first_name=user['first_name']
        last_name=user['last_name']
        print(last_name,first_name)

    
 