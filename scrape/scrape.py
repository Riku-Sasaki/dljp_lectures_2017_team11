from bs4 import BeautifulSoup
import urllib, json, os
from time import sleep
from tqdm import tqdm

all_url_list = []
for i in tqdm(range(115)):
    page_id = i + 1
    url = 'http://www.irasutoya.com/sitemap.xml?page=' + str(page_id)
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, "lxml")
    loc = soup.find_all('loc')

    url_list = []
    for each_loc in loc:
        each_url = each_loc.text.strip()
        url_list.append(each_url)
    all_url_list.extend(url_list)

save_json = 'meta/all_pages.json'
with open(save_json, 'w') as f:
    json.dump(all_url_list, f)
