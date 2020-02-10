# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    operators = []
    with open('operands.txt', encoding='utf8') as f
        for opers in f:
            operators.append(opers.strip())
    return render_template('index.html')

@app.route('/names')
def names():
    name = 'Артур'
    return render_template('names.html', name=name)

@app.route('/about')
def about():
    return 'Это программа Калькулятор'


if __name__ == '__main__':
    app.run(debug=True)
