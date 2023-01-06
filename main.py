
from flask import Flask, render_template
from utils import *

app = Flask(__name__)


@app.route('/')
def main_page():
    candidates = load_candidates('candidates.json')
    candidate_name = load_candidates('candidates.json')[1]['name']
    return render_template('list.html', candidates=candidates, name_candidate=candidate_name)


@app.route('/candidate/<x>')
def candidate_page(x):
    list_candidate = get_candidate(int(x))
    return render_template('single.html', list_candidate=list_candidate)


app.run()
