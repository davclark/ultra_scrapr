__author__ = 'Dav Clark'

import requests
# import io
from lxml import html
from ultra_scrapr_lib import save_web_to_file

jay_z_master_page = 'http://genius.com/artists/Jay-z'

r = requests.get(jay_z_master_page)
tree = html.fromstring(r.text)
songs_section = tree.xpath('//section[@class="all_songs"]')[0]

# Note - we just get the top of the list
# The site is set to update with javascript as we scroll down
# Probably need to use a headless option like phantomJS
for url in songs_section.xpath('.//li/a/@href'):
    save_web_to_file(url)


