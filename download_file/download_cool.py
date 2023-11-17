#! python

# download every single XKCD comic.

import requests, os, bs4, sys
from datetime import date

import string
import random

def generate_random_string(length):
  """Generates a random string of the specified length."""
  characters = string.ascii_lowercase + string.digits
  random_string = ''.join(random.choice(characters) for _ in range(length))
  return random_string

if __name__ == "__main__":
    today = date.today()

    today_str = today.strftime("%m/%d/%y")
    date_str = today.strftime("%Y%m%d")
    print('Getting updated pix for ' + today_str)

    url = 'https://www.cool18.com/bbs/'

    if not os.path.isdir('cool'):
        os.makedirs('cool', exist_ok=True)

    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    postElems = soup.select('div#d_list.main_right_margin > ul > li > a')

    if len(postElems) == 0:
        print('Could not find any post, exiting...')
        sys.exit(1)

    postElems_filtered = [ x for x in postElems if x.get('href').startswith('index')]

    dateElems = soup.select('div#d_list.main_right_margin ul li i')

    n = min(len(postElems_filtered), len(dateElems))

    postElems_filtered_today_updated = []
    for i in range(n):
        if (dateElems[i].text == today_str) and (not os.path.isdir('cool/' + date_str + '_' + postElems_filtered[i].text)):
            postElems_filtered_today_updated.append(postElems_filtered[i])

    updated_posts_no = len(postElems_filtered_today_updated)

    if updated_posts_no == 0:
        print("No updated posts to download.")
        sys.exit()
    else:
        print(str(updated_posts_no) + " updated posts to download.")

    for i in range(updated_posts_no):
        print("checking " + postElems_filtered_today_updated[i].text)
        new_sub_dir = 'cool/' + date_str + '_' + postElems_filtered_today_updated[i].text
        if not os.path.isdir(new_sub_dir):
            os.makedirs(new_sub_dir, exist_ok = True)
        next_link = url + postElems_filtered_today_updated[i].get('href')
        res = requests.get(next_link)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        imgElems = soup.select('img[mydatasrc]')
        if len(imgElems) == 0:
            continue
        for i in range(len(imgElems)):
            img_url = imgElems[i].get('mydatasrc')
            print('downloading ' + img_url)
            res = requests.get(img_url)
            res.raise_for_status()
            if os.path.isfile(os.path.join(new_sub_dir, os.path.basename(img_url))):
                image_name = os.path.join(new_sub_dir, generate_random_string(5) + os.path.basename(img_url))
            else:
                image_name = os.path.join(new_sub_dir, os.path.basename(img_url))
            with open(os.path.join(new_sub_dir, os.path.basename(img_url)), 'wb') as imageFile:
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)

    print('Done.')