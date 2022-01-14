"""Utilities to help parse club membership data"""

import pandas as pd
import glob
import os
from loguru import logger
from utils.person import Person, is_row_valid
from typing import List

PATH_TO_MEMBERSHIP = "input_data/rosters_private"

def get_latest_filename(path_to_dir: str) -> str:
    """returns filename of latest file in a directory with specified path
    """
    path = os.path.abspath(path_to_dir)  # absolute path without / at the end
    list_of_filenames = glob.glob(f"{path}/*")
    return max(list_of_filenames, key=os.path.getctime)


def get_latest_membership():
    """returns membership list as pandas dataframe with a subset of (nonprivate) columns and drop missing
    """
    df = pd.read_csv(get_latest_filename(path_to_dir=PATH_TO_MEMBERSHIP))
    df = df[["First", "Last", "DOB", "Gender", "Date"]]
    return df.dropna(how="all")


def create_people_from_membership_list() -> List[Person]:
    """builds a list of people (Person objects) from most recent membership list
    """
    df = get_latest_membership()  # most recent membership data
    people: List[Person] = []  # a list of people
    for i,row in df.iterrows():
        # logger.info(f"building data for row {i} out of {df.shape[0]} rows:\n{row}")
        row = row.to_dict()
        if is_row_valid(row):
            person = Person(
                first=row["First"],
                last=row["Last"],
                dob_str=row["DOB"],
                gender=row["Gender"],
                date_str=row["Date"]
            )
            people.append(person)
            # logger.info(f"Person built for row {i}: {person}")
        # else:
        #     logger.info(f"Person could not be built for row {i}")
    logger.info(f"Created {len(people)} people")
    return people
