from csv import DictReader
from typing import NamedTuple
import os
import os.path

def csvrows(path: str):
    with open(path, encoding='utf-8-sig') as csvreader:
        reader = DictReader(csvreader)
        for row in reader:
            yield row


class OccupationDescription(NamedTuple):
    code: int
    title: str
    description: str

class CoreCompetency(NamedTuple):
    name: str
    score: int

OCCUPATION_DESCRIPTIONS: dict[int, OccupationDescription] = dict()
OCCUPATION_CORE_COMPETENCIES: dict[int, list[CoreCompetency]] = dict()
OCCUPATION_TECHNOLOGY_TOOLS: dict[int, list[str]] = dict()
TITLE_TO_CODE: dict[str, int] = dict()

SPECIALIST_TASKS: dict[int, dict[str, dict[str, list[str]]]] = dict()

for r in csvrows('data/occupation_descriptions.csv'):
    o = OccupationDescription(int(r['ANZSCO_Code']), r['ANZSCO_Title'], r['ANZSCO_Desc'])
    OCCUPATION_DESCRIPTIONS[o.code] = o
    TITLE_TO_CODE[o.title] = o.code

for r in csvrows('data/core_competencies.csv'):
    code = int(r['ANZSCO_Code'])

    if code not in OCCUPATION_CORE_COMPETENCIES:
        OCCUPATION_CORE_COMPETENCIES[code] = []

    OCCUPATION_CORE_COMPETENCIES[code].append(
            CoreCompetency(r['Core_Competencies'], int(r['Score'])))

for r in csvrows('data/technology_tools.csv'):
    code = int(r['ANZSCO_Code'])
    if code not in OCCUPATION_TECHNOLOGY_TOOLS:
        OCCUPATION_TECHNOLOGY_TOOLS[code] = []
    OCCUPATION_TECHNOLOGY_TOOLS[code].append(r['Technology_tool'])

for r in csvrows('data/specialist_tasks.csv'):
    code = int(r['ANZSCO_Code'])
    if code not in SPECIALIST_TASKS:
        SPECIALIST_TASKS[code] = dict()

    cluster_family = r['Cluster_Family']
    if cluster_family not in SPECIALIST_TASKS[code]:
        SPECIALIST_TASKS[code][cluster_family] = dict()

    specialist_cluster = r['Specialist_Cluster']
    if specialist_cluster not in SPECIALIST_TASKS[code][cluster_family]:
        SPECIALIST_TASKS[code][cluster_family][specialist_cluster] = []

    specialist_task = r['Specialist_Task']
    SPECIALIST_TASKS[code][cluster_family][specialist_cluster].append(specialist_task)
