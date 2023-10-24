#! python

'''
launch_map.py - launches a map in the browser using an address
from the command line or clipboard. 
'''

import webbrowser, sys

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])

webbrowser.open(address)