import urllib
#import datetime

nn = 'dsfsdf'

def get_webpage(url):
    #html = myHtml.get_webpage(url)
    req = urllib.request.Request(url , headers={'User-Agent': 'Mozilla/5.0'})
    return urllib.request.urlopen(req).read()

def get_absolute_url(baseUrl, relativeUrl):
    return urllib.parse.urljoin(baseUrl, relativeUrl)

######### RSS ##########
class mRss_Item():
   def __init__(self,title,link,description=None,guid =None,pubdate=None):    
       self.title = title
       self.link = link
       self.description = description
       self.guid = guid if guid!=None else self.link
       self.pubdate = pubdate if pubdate!=None else '' #str(datetime.datetime.utcnow())

class mRss_Channel():
   def __init__(self,title,link, items ,description=None,pubdate=None,language='zh-TW'):    
       self.title = title
       self.link = link
       self.items = items
       
       self.description = description
       self.pubdate = pubdate if pubdate!=None else '' #str(datetime.datetime.utcnow())
       self.language = language       



def generate_rss(channel):
    rss_template = '''
<rss version="2.0">
    <channel>
        <title>{title}</title>
        <link>{link}</link>
        <description></description>
        <pubDate>{pubDate}</pubDate>
        <copyright></copyright>
        <language>zh-TW</language>
        <ttl>10</ttl>
        {items}
    </channel>
</rss>'''

    item_template = '''
        <item>
            <title>{title}</title>
            <link>{link}</link>
            <pubDate>{pubDate}</pubDate>
            <description>
            <![CDATA[
            {description}
            ]]>
            </description>
            <guid isPermaLink="false">{guid}</guid>
        </item>
''' 
    items_template = ''
    for o in channel.items:
        items_template += item_template.format(title=o.title,link=o.link,guid=o.guid,pubDate=o.pubdate,description=o.description) 
    
    result = rss_template.format(title=channel.title, link=channel.link,pubDate=channel.pubdate, items= items_template)
    return result

def get_rss_items(content):
    items = []
    soup = bs4.BeautifulSoup(content, 'xml')
    tags = soup.find_all('item')
    for tag in tags:
        item = ModulesRss(
            title = tag.find('title').get_text(),
            link = tag.find('link').get_text(),
            description = tag.find('title').prettify(),
            guid = tag.find('guid').get_text(),
            pubdate = tag.find('pubDate').get_text()
        )
        items.append(item)
    return items
    