#!/usr/bin/env python3

from flask import Flask, request, render_template, jsonify
from models import OCCUPATION_DESCRIPTIONS, OCCUPATION_CORE_COMPETENCIES

app = Flask(__name__)


@app.route('/', methods=['GET'])
def search():
    search_occupation = request.args.get('search_occupation')
    return render_template('search.html',
                           search_occupation=search_occupation,
                           occupations=OCCUPATION_DESCRIPTIONS.values())

@app.route('/occupations/<int:code>', methods=['GET'])
def detail(code: int):
    occupation = OCCUPATION_DESCRIPTIONS[code]
    core_competencies = OCCUPATION_CORE_COMPETENCIES[code]
    return render_template(
            'detail.html',
            occupation=occupation,
            core_competencies=core_competencies)


if __name__ == '__main__':
    app.run()
