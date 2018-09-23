import os
import urllib


def get_webpage(url):
    #html = myHtml.get_webpage(url)
    req = urllib.request.Request(url , headers={'User-Agent': 'Mozilla/5.0'})
    return urllib.request.urlopen(req).read()

def main():
    url = 'http://feeds.bbci.co.uk/news/world/rss.xml'
    xml = get_webpage(url)
    print(xml)
    pass


def main01():
    pass


if __name__ == '__main__':
    main()
    pass


