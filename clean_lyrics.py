__author__ = 'Dav Clark'

from io import open
from glob import glob
from lxml import html

for raw_lyrics_file in glob('rap.genius.com*'):
    # with open(raw_lyrics_file) as raw_lyrics:
    print raw_lyrics_file.center(40, '*')
    parsed_lyrics = html.parse(raw_lyrics_file)

    extracted_lyrics = parsed_lyrics.\
                        xpath('//div[@class="lyrics_container"]//p')

    outname = raw_lyrics_file.split('_', 1)[1]

    with open(outname, 'w', encoding='utf8') as outfile:
        outfile.write(unicode(extracted_lyrics[0].text_content()))



