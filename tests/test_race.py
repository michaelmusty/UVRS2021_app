from loguru import logger
from typing import List, Dict, Any
from utils.races import create_races
from utils.racer import Racer

def test_race_attrs():

    races = create_races()

    inds: List[int] = [x.get_index() for x in races]
    assert len(inds) == len(races)
    logger.info(f"race inds = {inds}")

    inds_str: List[str] = [x.get_index_as_str() for x in races]
    assert len(inds_str) == len(races)
    logger.info(f"inds_str = {inds_str}")

    names: List[str] = [x.get_name() for x in races]
    assert len(names) == len(races)
    logger.info(f"names = {names}")

    race_distances_used_for_scoring: List[str] = [x.get_race_distance_used_for_scoring() for x in races]
    assert len(race_distances_used_for_scoring) == len(races)
    logger.info(f"race_distances_used_for_scoring = {race_distances_used_for_scoring}")

    datetime_strs: List[str] = [x.get_datetime_str() for x in races]
    assert len(datetime_strs) == len(races)
    logger.info(f"datetime_strs = {datetime_strs}")

    datetimes: List[str] = [x.get_datetime() for x in races]
    assert len(datetimes) == len(races)
    logger.info(f"datetimes = {datetimes}")

    race_distances: List[List[str]] = [x.get_distances() for x in races]
    assert len(race_distances) == len(races)
    logger.info(f"race_distances = {race_distances}")

    dataframes: List[Dict[str,Any]] = [x.get_dataframes() for x in races]  # list of dicts
    assert len(dataframes) == len(races)
    logger.info(f"dfs = {dataframes}")

    all_racers: List[Dict[str,List[Racer]]]= [x.get_racers() for x in races]  # list of dicts
    assert len(all_racers) == len(races)