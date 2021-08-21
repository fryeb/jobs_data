from csv import DictReader
from typing import NamedTuple
import os
import os.path

class OccupationDescription(NamedTuple):
    code: int
    title: str
    description: str


OCCUPATION_DESCRIPTIONS: dict[str, OccupationDescription] = dict()

with open('data/occupation_descriptions.csv', encoding='utf-8-sig') \
        as csvreader:
            reader = DictReader(csvreader)
            for r in reader:
                o = OccupationDescription(int(r['ANZSCO_Code']), r['ANZSCO_Title'], r['ANZSCO_Desc'])
                OCCUPATION_DESCRIPTIONS[o.code] = o


