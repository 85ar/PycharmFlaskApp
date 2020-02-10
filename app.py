# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
<<<<<<< HEAD
=======
    operators = []
    with open('operands.txt', encoding='utf8') as f
        for opers in f:
            operators.append(opers.strip())
>>>>>>> ce463b481a20634a0fb7921d9212efe13cc08e36
    return render_template('index.html')

@app.route('/names')
def names():
    name = 'Артур'
    return render_template('names.html', name=name)

<<<<<<< HEAD
@app.route('/names')
def names():
    name = 'Владимир'
    return render_template('names.html', name = name)
=======
@app.route('/about')
def about():
    return 'Это программа Калькулятор'
>>>>>>> ce463b481a20634a0fb7921d9212efe13cc08e36


if __name__ == '__main__':
    app.run(debug=True)
