"""script to build dataframe to be consumed by frontend"""

from loguru import logger
from typing import List

from utils.person import Person
from utils.race import Race
from utils.participant import Participant

from utils.membership import create_people_from_membership_list
from utils.races import create_races
from utils.participants import get_participants
from utils.scoring import get_df_row


def test_get_df_row():
    people: List[Person] = create_people_from_membership_list()
    races: List[Race] = create_races()
    participants_for_scoring: List[Participant] = get_participants(people=people, races=races, for_scoring=True)
    p = participants_for_scoring[0]  # take the first participant
    logger.info(f"participant {p.person.name()}: {[r.get_name() for r in p.races]}")
    i, s, r, a = get_df_row(participant=p, participants=participants_for_scoring, race=p.races[0])
    logger.info(f"row: {i}, {s}, {r}, {a}")