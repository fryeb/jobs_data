#!/usr/bin/env python3

from flask import Flask, request, render_template, jsonify
from models import TITLE_TO_CODE, OCCUPATION_DESCRIPTIONS, OCCUPATION_CORE_COMPETENCIES, OCCUPATION_TECHNOLOGY_TOOLS

app = Flask(__name__)


@app.route('/', methods=['GET'])
def search():
    current_occupation = request.args.get('current_occupation')
    return render_template('search.html',
            current_occupation=current_occupation,
            occupations=OCCUPATION_DESCRIPTIONS.values())

@app.route('/occupations/<int:code>', methods=['GET'])
def detail(code: int):
    current_title = request.args.get('current_occupation')
    current_occupation = OCCUPATION_DESCRIPTIONS[TITLE_TO_CODE[current_title]]
    current_tech_tools = OCCUPATION_TECHNOLOGY_TOOLS[current_occupation.code]
    current_core_competencies = OCCUPATION_CORE_COMPETENCIES[current_occupation.code]

    occupation = OCCUPATION_DESCRIPTIONS[code]
    occupation_core_competencies = OCCUPATION_CORE_COMPETENCIES[code]
    technology_tools = OCCUPATION_TECHNOLOGY_TOOLS[code]

    # This is a very hacky way to do this
    core_competencies = []
    for oc_comp in occupation_core_competencies:
        for cur_comp in current_core_competencies:
            if oc_comp.name == cur_comp.name:
                core_competencies.append({'name': oc_comp.name, 'score': oc_comp.score, 'current': cur_comp.score})

    return render_template(
            'detail.html',
            occupation=occupation,
            core_competencies=core_competencies,
            technology_tools=technology_tools,
            current_occupation=current_occupation,
            current_tech_tools=current_tech_tools)


if __name__ == '__main__':
    app.run()
