from loguru import logger

from utils.gensim_models import word2vec_distance

def test_word2vec_distance():
    d = word2vec_distance("Scott King", "James Scott King")
    logger.info(f"d(Scott King, James Scott King) = {d}")
    d = word2vec_distance("Scott King", "Scott Michael")
    logger.info(f"d(Scott King, Scott Michael) = {d}")
    d = word2vec_distance("asdf", "asdf")
    logger.info(f"d(asdf, asdf) = {d}")