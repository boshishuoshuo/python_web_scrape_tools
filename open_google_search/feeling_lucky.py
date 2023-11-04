#! python

# feeling_lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Googling...')
print('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
    
# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result.
linkElems = soup.select('a[data-ved]')

# with open('feeling_lucky_result.html', 'wb') as f:
#     for chunk in res.iter_content(100000):
#         f.write(chunk)

# for i in range(len(linkElems)):
#     print(linkElems[i].get('href'))

numOpen = min(5, len(linkElems))

for i in range(numOpen):
    print('https://google.com'+ linkElems[i].get('href'))
    webbrowser.open('https://google.com'+ linkElems[i].get('href'))