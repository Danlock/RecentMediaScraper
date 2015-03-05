import requests
import bs4
import re
from multiprocessing import Pool


def show_video_stats(options):
    pool = Pool(8)
    video_page_urls = get_video_page_urls()
    results = pool.map(get_video_data, video_page_urls)

def get_video_page_urls():
    response = requests.get(index_url)
    soup = bs4.BeautifulSoup(response.text)
    return [a.attrs.get('href') for a in soup.select('div.video-summary-data a[href^=/video]')]

def get_video_data(video_page_url):
    video_data = {}
    response = requests.get(root_url + video_page_url)
    soup = bs4.BeautifulSoup(response.text)
    video_data['title'] = soup.select('div#videobox h3')[0].get_text()
    video_data['speakers'] = [a.get_text() for a in soup.select('div#sidebar a[href^=/speaker]')]
    video_data['youtube_url'] = soup.select('div#sidebar a[href^=http://www.youtube.com]')[0].get_text()

    response = requests.get(video_data['youtube_url'])
    soup = bs4.BeautifulSoup(response.text)

    video_data['views'] = int(re.sub('[^0-9]', '',
                                     soup.select('.watch-view-count')[0].get_text().split()[0]))
    #video_data['likes'] = int(re.sub('[^0-9]', '',
     #                                soup.select('.likes-count')[0].get_text().split()[0]))
    #video_data['dislikes'] = int(re.sub('[^0-9]', '', 
    #                                    soup.select('.dislikes-count')[0].get_text().split()[0]))
    return video_data

root_url = 'http://pyvideo.org'


#response = requests.get('http://pyvideo.org/category/50/pycon-us-2014')
#soup = bs4.BeautifulSoup(response.text)
#links = [a.attrs.get('href') for a in soup.select('div.video-summary-data a[href^=/video]')]


root_url = 'http://pyvideo.org'
index_url = root_url + '/category/50/pycon-us-2014'
v_urls = get_video_page_urls()
for x in v_urls:
    print get_video_data(x)


#print(get_video_page_urls())
