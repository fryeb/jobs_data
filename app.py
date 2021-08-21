#!/usr/bin/env python3

from flask import Flask, request, render_template, jsonify
from models import OCCUPATION_DESCRIPTIONS

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
    return render_template('detail.html', occupation=occupation)


if __name__ == '__main__':
    app.run()
