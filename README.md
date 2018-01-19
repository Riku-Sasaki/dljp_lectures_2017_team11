# dljp_lectures_2017_team11

文章から画像生成するモデルをPython3系列でも動くように変更

動作環境はtext-to-image/requirement.txtに記載

編集元のgithubはhttps://github.com/paarthneekhara/text-to-image

# Example 

To generate an image drawn like an irasutoya illustration from your caption you run:
```
python main.py --title="This flower is a red rose" 
```
This will firstly generate your image through a GAN and then apply style transfer with the most related irasutoya image.
The output image will be created in the main directory under the name ```result.jpg```.
