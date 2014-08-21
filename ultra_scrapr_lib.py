__author__ = 'oski'

import requests
import io

def save_web_to_file(url):
    '''Use requests to fetch url, then save to a file'''
    r = requests.get(url)
    # Might be a problem if URL doesn't start with http://
    stripped_url = url.split('//')[1]
    filename = stripped_url.replace('/', '_')
    with io.open(filename, 'w', encoding='utf8') as outfile:
        outfile.write(r.text)