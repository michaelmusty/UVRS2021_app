"""Person Class"""

from typing import Dict, List
from datetime import datetime
from loguru import logger

def is_date_str(s) -> bool:
    """determine if we can construct a date from s
    """
    if type(s) is not str:
        return False
    else:
        splits = [int(x) for x in s.split("/")]
        if len(splits) != 3:
            return False
        else:
            month, day, year = splits
            try:
                datetime(year, month, day)
                return True
            except Exception as e:
                return False


def is_row_valid(row: Dict) -> bool:
    """determine if we can construct a person from a row
    """
    condition1 = all(x is not None for x in [row[x] for x in row.keys()])
    condition2 = is_date_str(row["DOB"])
    condition3 = is_date_str(row["Date"])
    # logger.debug(f"row={row}")
    # logger.debug(f"all values not none={condition1}")
    # logger.debug(f"DOB is a date={condition2}")
    # logger.debug(f"Date is a date={condition3}")
    return condition1 and condition2 and condition3

class Person:

    def __init__(
        self,
        *,
        first: str,
        last: str,
        dob_str: str,
        gender: str,
        date_str: str,
    ):
        self.first = first
        self.last = last
        self.dob_str = dob_str
        self.gender = gender
        self.date_str = date_str

    def name(self) -> str:
        """name of person"""
        return f"{self.first} {self.last}"

    def date_of_birth(self):
        """date of birth of person"""
        month, day, year = [int(x) for x in self.dob_str.split("/")]
        return datetime(year, month, day)

    def date_joined(self):
        """date the person joined UVRC"""
        month, day, year = [int(x) for x in self.date_str.split("/")]
        return datetime(year, month, day)

    # def age_group(self,*,races: List[Race]) -> Optional[str]:
    #     """age group of person determined by the age of person on the day of their first race in the series"""
    #     first_race = get_first_race(person = self, races = races)

    # def to_participant(self,*,races: List[Race]) -> Optional[Participant]:
    #     """if possible construct a participant from a person"""
    #     pass


# def get_first_race(person: Person, races: List[Race]) -> Optional[Race]:
#     """returns race with smallest timestamp or None
#     """
#     matched_races: List[Race] = get_matched_races(person = person, races = races)
#     pass


# def get_matched_races(person: Person, races: List[Race]) -> List[Race]:
#     """returns races from races where person matches a racer in race"""
#     matched_races: List[Race] = []
#     for race in races:
#         b: bool, r: Racer = is_matched_race(person = person, race = race)
#         if b