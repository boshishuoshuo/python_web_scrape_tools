#! python

import requests
import bs4

with open('example.html', 'r') as exampleFile:
    exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
    print(type(exampleSoup))
    elems = exampleSoup.select('#author')
    print(type(elems))
    print(len(elems))
    print(elems[0].get_text())
    print(str(elems[0]))
    print(type(elems[0]))
    print(elems[0].attrs)
    
    p_elems = exampleSoup.select('p')
    for i in range(len(p_elems)):
        print(p_elems[i].get_text())
        print(str(p_elems[i]))
        
    span_elems = exampleSoup.select('span')
    for i in range(len(span_elems)):
        print(str(span_elems[i]))
        print(span_elems[i].attrs)
        print(span_elems[i].get('id'))
        print(span_elems[i].get('some_nonexistent_addr'))
    