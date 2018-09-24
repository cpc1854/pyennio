import mylib
import pr_weblinks
import urllib
from bs4 import BeautifulSoup
import requests
import datetime



def main():
    print('---------------')
    
    u =  'https://edition.cnn.com/specials/cnn-heroes'
    name = 'cnn heroes'
    inurls = 'cnnheroes,html'
    not_inurls = 'fag'
    intitles = ''
    not_intitles = ''
    
    #rss_channel = pr_weblinks.getRss_Channel(u, name, inurls, not_inurls, intitles, not_intitles)
    #r = mylib.generate_rss(rss_channel)
    r = pr_weblinks.do_parsing(u, name, inurls, not_inurls, intitles, not_intitles)
    print(r)
    print('---------------')    
    pass


def main01():
    pass


if __name__ == '__main__':
    main()
    pass


