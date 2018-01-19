#!/usr/bin/env python
import argparse
import os
from word2vec.cos_similarity_with_word2vec import get_url_similar_image
import nltk
nltk.download('punkt')
# Gather our code in a main() function
def main(args):
	title = args.title
	#Create the caption file
	f = open('text-to-image/Data/sample_captions.txt', 'w')
	f.write(title)
	f.close()

	print 'Caption file created'

	# Generate an image through the GAN model 
	print 'Generate image'
	os.system('python -m text-to-image.generate_thought_vectors --caption_file="text-to-image/Data/sample_captions.txt" --data_dir="text-to-image/Data"')
	os.system('python -m text-to-image.generate_images --n_images 1 --data_dir="text-to-image/Data" --model_path="text-to-image/Data/Models/model_after_flowers_epoch_100.ckpt" --caption_thought_vectors="text-to-image/Data/sample_caption_vectors.hdf5"')
	print 'Images generated'
	content_path = "text-to-image/Data/val_samples/combined_image_0.jpg"

	# Select Irasutoya image
	print 'Get similar image'
	image = get_url_similar_image(title)
	style_path =  'scrape/data/'+image['save_name'] # 'images/##.png'
	print style_path
	print 'Irasutoya image found'

	# Do style transfer
	os.system("python style-transfer/run_main.py --model_path=style-transfer/pre_trained_model --content "+ content_path +" --style "+ style_path +" --output result.jpg --num_iter 1000 --max_size 64")

 
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = "Irasutoya image generator")
	parser.add_argument('-t', 
						'--title',
						help='Caption of the generated image', 
						required=True)

	args = parser.parse_args()
	main(args)