"""script to build dataframe to be consumed by frontend"""

from loguru import logger
from typing import List

from utils.person import Person
from utils.race import Race
from utils.participant import Participant

from utils.membership import create_people_from_membership_list
from utils.races import create_races
from utils.participants import get_participants
from utils.scoring import build_df, build_filtered_df, build_participation_snapshot

def main():

    # setup
    logger.info("BUILD SETUP")
    people: List[Person] = create_people_from_membership_list()
    races: List[Race] = create_races()
    participants_for_scoring: List[Participant] = get_participants(people=people, races=races, for_scoring=True)  # participants in races for scoring
    participants_all: List[Participant] = get_participants(people=people, races=races, for_scoring=False)  # participants in any eligible race

    # build output_data tables
    logger.info("BUILD TABLE")
    build_df(participants=participants_for_scoring)  # does not filter top races
    logger.info("BUILD FILTERED TABLE")
    build_filtered_df(participants=participants_for_scoring, N=5)  # filters top N races

    # build output_data/participation/snapshot_YYYYMMDDHHMMSS.csv
    # build_participation_snapshot(participants=participants_all)

if __name__ == "__main__":
    main()