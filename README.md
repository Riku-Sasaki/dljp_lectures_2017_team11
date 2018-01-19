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

# Required files

#### For Style Transfer
  
  The require file for Style Transfer is the .mat pretrained VGG9 file available [here](http://www.vlfeat.org/matconvnet/models/imagenet-vgg-verydeep-19.mat), put this file in a 'style-transfer/pre_trained_model' directory.

#### For Word2Vec
  The require file for Word2Vec is the .bin.gz file available [here](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing), unzip this file in the 'word2vec/weights' directory.

