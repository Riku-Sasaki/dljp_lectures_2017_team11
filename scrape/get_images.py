from bs4 import BeautifulSoup
import urllib, json, os
from time import sleep
from tqdm import tqdm

json_path = 'data/all_pages.json'
with open(json_path, 'r') as f:
    url_list = json.load(f)

print('downloading images...')

all_data = []

for i, page_url in enumerate(tqdm(url_list)):
    try:
        req = urllib.request.Request(page_url)
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")
        post_data = soup.find(id='post')

        # 1ページに複数画像がある場合を除く
        if len(post_data.find_all(class_='separator')) > 2:
            continue
        elif len(post_data.find_all(class_='separator')[0]) > 2:
            continue

        title = post_data.find(class_='title').text.strip()   # タイトル
        desc =  post_data.find_all(class_="separator")[1].text.strip()    # 説明文
        image_url = post_data.find(class_='separator').find('a').attrs['href']    # 画像URL
        category = [x.text.strip() for x in post_data.find(class_='category').find_all('a')]    #カテゴリー

        save_name = "images/" + str(i+1) + ".png"

        each_data = {}
        each_data['title'] = title
        each_data['desc'] = desc
        each_data['page_url'] = page_url
        each_data['image_url'] = image_url
        each_data['category'] = category
        each_data['save_name'] = save_name
        all_data.append(each_data)

        # ダウンロード
        if not os.path.isfile(save_name):
            urllib.request.urlretrieve(image_url, save_name)

        sleep(1)
    except:
        continue

    save_json = 'meta/image_data.json'
    with open(save_json, 'w') as f:
        json.dump(all_data, f)
