from loguru import logger
from datetime import date, timedelta
from typing import List

from utils.participant import Participant

from utils.membership import create_people_from_membership_list
from utils.races import create_races
from utils.participants import get_participants
from utils.participant import compute_age_group

def test_compute_age_group():
    date_of_birth = date(year=1985, month=12, day=12)
    race_date = date(year=2021, month=7, day=4)
    assert compute_age_group(date_of_birth=date_of_birth, race_date=race_date, gender="M") == "M3039"


def test_is_participant():
    people = create_people_from_membership_list()
    races = create_races()
    participants_for_scoring: List[Participant] = get_participants(people=people, races=races, for_scoring=True)
    participants_all: List[Participant] = get_participants(people=people, races=races, for_scoring=False)
    assert len(participants_for_scoring) > 0
    assert len(participants_all) > 0
    assert len(participants_all) > len(participants_for_scoring)