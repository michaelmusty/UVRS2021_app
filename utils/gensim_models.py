"""Utilities for word2vec models using gensim package"""

from loguru import logger

import numpy as np

from gensim.test.utils import common_texts
from gensim.models import Word2Vec

# cache model to file
# load most recent
# preprocessing of text
# train on corpus of names

def word2vec_distance(x: str, y: str) -> float:
    model = Word2Vec(sentences=common_texts, vector_size=100, window=5, min_count=1, workers=4)
    model.train([[x],[y]], total_examples=model.corpus_count, epochs=1)
    xv = model.wv[x]
    yv = model.wv[y]
    return np.linalg.norm(xv-yv)