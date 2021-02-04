import os
import requests
from pprint import pprint 
token=os.environ['token']

def sendMsg(texts):
    url=f'https://api.telegram.org/bot{token}/sendMessage'
    for text in texts:
        payload={
            'chat_id':937691492,
            'text':text,
            'parse_mode':'HTML'
            }
        r=requests.get(url,payload)

html="""
<b>bold</b>, <strong>bold</strong>
<i>italic</i>, <em>italic</em>
<u>underline</u>, <ins>underline</ins>
<s>strikethrough</s>, <strike>strikethrough</strike>, <del>strikethrough</del>
<b>bold <i>italic bold <s>italic bold strikethrough</s> <u>underline italic bold</u></i> bold</b>
<a href="http://www.example.com/">inline URL</a>
<a href="tg://user?id=123456789">inline mention of a user</a>
<code>inline fixed-width code</code>
<pre>pre-formatted fixed-width code block</pre>
<pre><code class="language-python">pre-formatted fixed-width code block written in the Python programming language</code></pre>
"""
k=html.split(',')

sendMsg(k)

