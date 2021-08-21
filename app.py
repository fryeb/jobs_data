#!/usr/bin/env python3

from flask import Flask, request, render_template
from models import OCCUPATION_DESCRIPTIONS

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    search_occupation = request.args.get('search_occupation')
    return render_template('search.html',
                           search_occupation=search_occupation,
                           occupations=OCCUPATION_DESCRIPTIONS)


if __name__ == '__main__':
    app.run()
