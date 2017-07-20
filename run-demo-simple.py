from flask import Flask, render_template, redirect, request, jsonify
#from squad.demo_prepro import prepro
from demo_cnsl import Demo
import json
import requests

import pdb


app = Flask(__name__)
demo = Demo()

@app.route('/')
def main():
    pdb.set_trace()
    return render_template('index.html')


def getAnswer(paragraph, question):
    return demo.run(paragraph, question)


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    paragraph = request.args.get('paragraph')
    question = request.args.get('question')
    answer = getAnswer(paragraph, question)
    return answer

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="1990", threaded=True)

    # Added by Ken
    r = requests.get(
        'http://0.0.0.0:1990/submit',
        params={'question': 'who are you?', 'paragraph': 'sample passage'})

    print(r)