# -*- coding: utf-8 -*-
import h5py
import numpy as np
import os
import tqdm
from scipy import misc
import json
from tqdm import tqdm

def create_h5_dataset(output_filename, data_root='data'):
		"""
		Create a H5 file from the images and its json

		Inputs:
			output_fn: filename for the created file
			data_root: data folder path (images/ + json ..)
		"""
		with h5py.File(output_filename, 'w') as f:
			f.create_group('training_set')

			images_metadata = json.load(open(os.path.join(data_root,'image_data.json')))
			descriptions = [str.encode(x['desc']) for x in images_metadata]
			titles = [str.encode(x['title']) for x in images_metadata]

			total_images = len(images_metadata)

			dt = h5py.special_dtype(vlen=bytes)
			f['training_set'].create_dataset('titles', (len(titles),1), dtype=dt, data=titles)
			f['training_set'].create_dataset('descriptions', (len(descriptions),1),dtype=dt, data=descriptions)

			shape = (total_images, 100, 100, 3)

			dset = f['training_set'].create_dataset('data', shape=shape, compression="lzf")

			files_list = os.listdir(os.path.join(data_root,'images'))
			files_list.remove('.DS_Store')
			files_list.remove('.gitkeep')
			files_list = sorted(files_list, key=lambda filename: int(filename[:-4]))   # sort by age
			print(len(files_list))
			print(total_images)

			images = []

			for i, filename in tqdm(enumerate(files_list), total=total_images):
				image = misc.imread(os.path.join(data_root, 'images', filename))
				image = misc.imresize(image, size=(shape[1],shape[2]))[:,:,:shape[3]]
				images += [image]

			dset[...] = np.array(images)

def decode_string(b):
	return b.decode('utf-8')

class Dataset:

	# Open the H5 file
	def __init__(self, filename='images.h5', shuffle=True):
		np.random.seed(42)
		h5 = h5py.File(filename, 'r')
		dataset = h5['training_set']

		self.titles = dataset['titles']
		self.descriptions = dataset['descriptions']
		self.data = dataset['data']

		self.total_items = self.data.shape[0]

		self.index_map = np.arange(self.total_items)
		np.random.shuffle(self.index_map)

		self.current_idx = 0


	def next_batch(self, batch_size = 10):

		batch_range = range(self.current_idx,self.current_idx+batch_size)

		batch_x_images = np.array([self.data[idx] for idx in self.index_map[batch_range]])
		batch_x_descriptions = np.array([decode_string(self.descriptions[idx][0]) for idx in self.index_map[batch_range]])
		batch_x_titles = np.array([decode_string(self.titles[idx][0]) for idx in self.index_map[batch_range]])

		return batch_x_images, batch_x_descriptions, batch_x_titles

		
d = Dataset()
for i in range(10):
	print(d.next_batch(2)[0].shape)