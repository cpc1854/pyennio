import json
import mylib
import requests
import urllib
import datetime

def do_parsing(name='youtube.search.heroes', q='cnn%2Bheroes'):
    rss_channel = getRss_Channel(name, q)
    result = mylib.generate_rss(rss_channel)
    return result

def getRss_Channel(name='youtube.search.heroes', q='cnn%2Bheroes'):
    u = 'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&publishedAfter=2018-02-12T00:00:00Z&q={0}&key=AIzaSyAKw-hbjHCj_JXWRoZVd9eVPiTmElBPxX0'
    u = u.format(q)
    
    with urllib.request.urlopen(u) as r:
        data = json.loads(r.read().decode())

    #with open('output.html', 'wb') as f:
    #    f.write(response.content)
    #print(data)
    '''
    for item in data['items']:
        print(item['id']['videoId'])
        print(item['snippet']['title'])
        print(item['snippet']['description'])        
    '''
    rss_items = []
    for item in data['items']:
        videoId = item['id']['videoId']
        href = 'https://www.youtube.com/watch?v=' + videoId
        title = item['snippet']['title']
        description = item['snippet']['description']
        item = mylib.mRss_Item(
            title = title,
            link = href,
            description = description,
            guid = href,
            pubdate = str(datetime.datetime.utcnow())
        )
        rss_items.append(item)    
        #print('href:', href, '\r' ,title)
        #print('-----------------------')
    print('rss_items cn:', len(rss_items))
    rss_channel = mylib.mRss_Channel(title=name, link=u, items=rss_items)
    return rss_channel


if __name__ == '__main__':
    #print('-------------')
    #print(do_parsing())
    pass
