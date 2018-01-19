# coding: utf-8
import numpy as np
import json
from scipy.linalg import norm
import gensim

def title2vec(model, title_en):
    stopword = set(['Illustration', 'all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', 'before', 'herself', 'had', 'should', 'to', 'only', 'under', 'ours', 'has', 'do', 'them', 'his', 'very', 'they', 'not', 'during', 'now', 'him', 'nor', 'did', 'this', 'she', 'each', 'further', 'where', 'few', 'because', 'doing', 'some', 'are', 'our', 'ourselves', 'out', 'what', 'for', 'while', 'does', 'above', 'between', 't', 'be', 'we', 'who', 'were', 'here', 'hers', 'by', 'on', 'about', 'of', 'against', 's', 'or', 'own', 'into', 'yourself', 'down', 'your', 'from', 'her', 'their', 'there', 'been', 'whom', 'too', 'themselves', 'was', 'until', 'more', 'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'he', 'me', 'myself', 'these', 'up', 'will', 'below', 'can', 'theirs', 'my', 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself', 'at', 'have', 'in', 'any', 'if', 'again', 'no', 'when', 'same', 'how', 'other', 'which', 'you', 'after', 'most', 'such', 'why', 'a', 'off', 'i', 'yours', 'so', 'the', 'having', 'once'])

    new_title = []
    for word in title_en.split(" "):
        if not word in stopword:
            new_title.append(word)

    word2vec_avg = []
    for word in new_title:
        try:
            word2vec_avg.append(model.word_vec(word))
        except:
            continue
    word2vec_avg = np.average(word2vec_avg, 0)
    return word2vec_avg

def cos_similarity(a, title2_mat):
    return title2_mat.dot(a) / (norm(title2_mat, axis=1) * norm(a))

def similar_index(a, title2_mat, index_list):
    return index_list[cos_similarity(a, title2_mat).argmax()]

def get_url_similar_image(title):
    # Load Google's pre-trained Word2Vec model.
    model = gensim.models.KeyedVectors.load_word2vec_format('word2vec/weights/GoogleNews-vectors-negative300.bin', binary=True)
    f = open('word2vec/misc/image_data.json', 'r')
    json_dict = json.load(f)

    index_list = []
    title2_mat = []
    for i, j in enumerate(json_dict):
        if not title2vec(model, j["title_en"]).size == 1:   # nanのとき以外
            title2_mat.append(title2vec(model, j["title_en"]))
            index_list.append(i)
            
    title2_mat = np.array(title2_mat)

    index = similar_index(title2vec(model, title), title2_mat, index_list)
    return json_dict[index]

# print get_url_similar_image("red rose")
