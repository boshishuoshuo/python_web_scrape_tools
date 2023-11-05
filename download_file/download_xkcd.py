#! python

# download every single XKCD comic.

import requests, os, bs4

url = 'https://xkcd.com/'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    # TODO: Download the page.
    
    # TODO: Find the URL of the comic image.
    
    # TODO: Download the image.
    
    # TODO: Save the image to ./xkcd
    
    # TODO: Get the Prev button's url.
    break

print('Done.')