


### Usage
#### Download data
- Download all image data from [images.zip](https://drive.google.com/file/d/1Z_6P4Pfq9OQWAGR0h6dS6GvjfN_qxOkc/view?usp=sharing) (4GB)
- Download image meta data from [image_data.json](https://drive.google.com/file/d/16RtiKhKyas25vP4FxHxrn9LLrkGiHyqJ/view?usp=sharing) (9.1MB)

#### about data
- `image_data.json`

      {
        'category': ['お風呂', '道具'],
      'desc': '洗面器の中に水やお湯が入れられているイラストです。',
      'image_url': 'http://3.bp.blogspot.com/-Sg9VCmfS6oM/WerK_d3MAjI/AAAAAAABHsI/EQP1PpFYrogSO4mgm159bmDfoVkYTuwwgCLcBGAs/s800/ofuro_sentaku_senmenki_water.png',
      'page_url': 'http://www.irasutoya.com/2017/11/blog-post_270.html',
      'save_name': 'images/1.png',
      'title': '水を張った洗面器のイラスト'
      }


### others
- `scrape.py` and `get_images.py` are used for scraping irasutoya and download images from the website. You do not need to execute these code.
- if you want to execute these code, you need some libraries
  - BeautifulSoup4 (bs4)
  - tqdm
