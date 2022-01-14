from loguru import logger
from typing import List, Dict
from utils.races import create_races
from utils.racer import Racer

def test_racer_attrs_and_methods():

    races = create_races()
    l: List[Dict[str,List[Racer]]] = [race.get_racers() for race in races]
    assert len(l) == 7

    for race in races:
        d: Dict[str, List[Racer]] = race.get_racers()
        for k in d.keys():
            assert k in ["5k", "10k", "12k"]
            logger.info(f"{race.get_name()}_{k}")
            racers = d[k]
            racers_names: List[str] = [x.get_name() for x in racers]
            assert len(racers_names) == len(racers)
            logger.info(f"racers_names = {racers_names}")
            racers_net_times: List = [x.get_net_time() for x in racers]
            assert len(racers_net_times) == len(racers)
            logger.info(f"racers_net_times = {racers_net_times}")