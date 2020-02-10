# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/names')
def names():
    name = 'Владимир'
    return render_template('names.html', name = name)


if __name__ == '__main__':
    app.run(debug=True)
