from loguru import logger
from utils.membership import get_latest_membership, create_people_from_membership_list

def test_get_latest_membership():
    df = get_latest_membership()
    logger.info(df)
    assert df.shape[1] == 5


def test_create_people_from_membership_list():
    people = create_people_from_membership_list()
    assert len(people) > 0