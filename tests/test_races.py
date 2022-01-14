from loguru import logger
from utils.races import get_dirnames_and_dirpaths
from utils.races import PATH_TO_RACES

def test_get_dirnames_and_dirpaths():
    d = get_dirnames_and_dirpaths(path_to_dir = PATH_TO_RACES)
    logger.info(d)
    assert len(d['dirnames']) == len(d['dirpaths'])
    assert len(d['dirnames']) == 7