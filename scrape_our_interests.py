__author__ = 'Dav Clark'

from lxml import html
import requests
import io

# r = requests.get('http://statsforchange.org')
# print 'status:', r.status_code
# print 'initial text:', r.text[:40]
# tree = html.fromstring(r.text)

test_urls = ['http://statsforchange.org',
             'http://sfbay.craigslist.org/mca/']

# print tree.body.text_content()

def save_web_to_file(url):
    '''Use requests to fetch url, then save to a file'''
    r = requests.get(url)
    # Might be a problem if URL doesn't start with http://
    stripped_url = url.split('//')[1]
    filename = stripped_url.replace('/', '_')
    with io.open(filename, 'w', encoding='utf8') as outfile:
        outfile.write(r.text)

for curr_url in test_urls:
    save_web_to_file(curr_url)