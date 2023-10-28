#! python

import requests

res = requests.get('https://www.gutenberg.org/cache/epub/1112/pg1112.txt.utf8')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

with open('Romeo_and_Juliet.txt', 'wb') as f:
    for chunk in res.iter_content(100000):
        f.write(chunk)
