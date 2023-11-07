#! python

# download every single XKCD comic.

import requests, os, bs4

url = 'https://www.cool18.com/bbs/index.php'
os.makedirs('cool', exist_ok=True)

# Download the page.
print('Downloading page %s ...' % url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Find the URL of the comic image.
postElems = soup.select('ul li a')
if postElems == []:
    print('Could not find any post.')
else:
    print(len(postElems))
    print(postElems[0])
    for i in range(10):
        print(i)
        print(str(postElems[i]))
    # Download the image.
    # print('Downloading image %s ...' % (comicUrl))
    # res = requests.get('https:' + comicUrl)
    # res.raise_for_status()

# Save the image to ./xkcd
# with open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb') as imageFile:
#     for chunk in res.iter_content(100000):
#         imageFile.write(chunk)

# Get the Prev button's url.
# prevLink = soup.select('a[rel="prev"]')
# url = 'https://xkcd.com/'+prevLink[0].get('href')

# print(url)

print('Done.')