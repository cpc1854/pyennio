import urllib
from bs4 import BeautifulSoup
import requests
import datetime

import mylib

def do_parsing(u, name, inurls, not_inurls, intitles, not_intitles, minlen_title=5):
    rss_channel = getRss_Channel(u, name, inurls, not_inurls, intitles, not_intitles, minlen_title)
    result = mylib.generate_rss(rss_channel)
    return result
    


def getRss_Channel(u, name, inurls, not_inurls, intitles, not_intitles, minlen_title=5):
    if u == None: u = 'https://edition.cnn.com/specials/cnn-heroes'
    response = requests.get(u)

    #with open('output.html', 'wb') as f:
    #    f.write(response.content)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [link for link in soup.find_all('a') if link.has_attr('href')]
    
    if inurls == None: inurls = 'cnnheroes,html'
    for s in inurls.split(','):
        if s != None: 
            links = [link for link in links if s in link['href'] ]
    
    if not_inurls == None: not_inurls = 'faq'
    for s in not_inurls.split(','):
        if s != None: 
            links = [link for link in links if s not in link['href'] ]
    
    if minlen_title > 0:
        links = [link for link in links if len(link.text.strip()) >  minlen_title]    
    
    rss_items = []
    for link in links:
        href = mylib.get_absolute_url(u, link['href']) 
        title = link.text.strip()
        item = mylib.mRss_Item(
            title = title,
            link = href,
            description = '',
            guid = href,
            pubdate = str(datetime.datetime.utcnow())
        )
        rss_items.append(item)    
        #print('href:', href, '\r' ,title)
        #print('-----------------------')
    rss_channel = mylib.mRss_Channel(title=name, link=u, items=rss_items)
    return rss_channel
