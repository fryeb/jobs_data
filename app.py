#!/usr/bin/env python3

from flask import Flask, request, render_template, jsonify
from models import TITLE_TO_CODE, OCCUPATION_DESCRIPTIONS, OCCUPATION_CORE_COMPETENCIES, OCCUPATION_TECHNOLOGY_TOOLS, SPECIALIST_TASKS

app = Flask(__name__)

def compare_occupations(a: str, b: str):
    a_comps = OCCUPATION_CORE_COMPETENCIES[TITLE_TO_CODE[a]]
    b_comps = OCCUPATION_CORE_COMPETENCIES[TITLE_TO_CODE[b]]
    total = 0
    for a_comp in a_comps:
        for b_comp in b_comps:
            if a_comp.name == b_comp.name:
                total += abs(a_comp.score - b_comp.score)
    return total

@app.route('/', methods=['GET'])
def search():
    current_occupation = request.args.get('current_occupation')
    if current_occupation:
        occupations = sorted(
                OCCUPATION_DESCRIPTIONS.values(),
                key=lambda occupation: compare_occupations(occupation.title, current_occupation))
    else:
        occupations = OCCUPATION_DESCRIPTIONS.values()

    return render_template('search.html',
            current_occupation=current_occupation,
            occupations=occupations)

@app.route('/occupations/<int:code>', methods=['GET'])
def detail(code: int):
    current_title = request.args.get('current_occupation')
    if current_title:
        current_occupation = OCCUPATION_DESCRIPTIONS[TITLE_TO_CODE[current_title]]
        current_tech_tools = OCCUPATION_TECHNOLOGY_TOOLS[current_occupation.code]
        current_core_competencies = OCCUPATION_CORE_COMPETENCIES[current_occupation.code]
    else:
        current_occupation = None
        current_tech_tools = None

    occupation = OCCUPATION_DESCRIPTIONS[code]
    occupation_core_competencies = OCCUPATION_CORE_COMPETENCIES[code]
    if code in OCCUPATION_TECHNOLOGY_TOOLS:
        technology_tools = OCCUPATION_TECHNOLOGY_TOOLS[code]
    else:
        technology_tools = []

    # This is a very hacky way to do this
    core_competencies = []
    for oc_comp in occupation_core_competencies:
        if current_occupation:
            for cur_comp in current_core_competencies:
                if oc_comp.name == cur_comp.name:
                    core_competencies.append({'name': oc_comp.name, 'score': oc_comp.score, 'current': cur_comp.score})
        else:
            core_competencies.append({'name': oc_comp.name, 'score': oc_comp.score})

    # Specialist Tasks
    task_cluster_families = SPECIALIST_TASKS[code]

    return render_template(
            'detail.html',
            occupation=occupation,
            core_competencies=core_competencies,
            technology_tools=technology_tools,
            current_occupation=current_occupation,
            current_tech_tools=current_tech_tools,
            task_cluster_families=task_cluster_families)


if __name__ == '__main__':
    app.run()
