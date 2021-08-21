from csv import DictReader
from typing import NamedTuple
import os
import os.path


class OccupationDescription(NamedTuple):
    code: str
    title: str
    description: str


OCCUPATION_DESCRIPTIONS: list[OccupationDescription] = []
with open('data/occupation_descriptions.csv', encoding='utf-8-sig') \
        as csvreader:
    reader = DictReader(csvreader)
    OCCUPATION_DESCRIPTIONS = [
            OccupationDescription(
                r['ANZSCO_Code'], r['ANZSCO_Title'], r['ANZSCO_Desc'])
            for r in reader]
