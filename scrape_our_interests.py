__author__ = 'Dav Clark'

import requests
import io
from lxml import html

from ultra_scrapr_lib import save_web_to_file

# test_urls = ['http://statsforchange.org',
#             'http://sfbay.craigslist.org/mca/']

with io.open('urls.txt', 'r', encoding='utf8') as url_list:
    test_urls = url_list.readlines()

for curr_url in test_urls:
    curr_url = curr_url.strip()
    # save_web_to_file(curr_url)
    r = requests.get(curr_url)
    tree = html.fromstring(r.text)
    print tree.body.text_content()[:100]

