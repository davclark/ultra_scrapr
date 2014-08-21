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
    entries = tree.xpath('//span[@class="txt"]')
    data_table = []
    for e in entries:
        try:
            price = e.xpath('.//span[@class="price"]/text()')[0]
            date = e.xpath('.//span[@class="date"]/text()')[0]
        except IndexError:
            continue
        # print e.text_content()
        data_table.append([date, price])

    print data_table

