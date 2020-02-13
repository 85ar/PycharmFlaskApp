from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('auth.html')

@app.route('/names')
def names():
    entities = list()
    with open('names.txt', encoding='utf-8') as f:
        for raw_line in f:
            entities.append(raw_line.strip())
    return render_template('names.html', entities=entities)

@app.route('/about')
def about():
    return 'Это программа Калькулятор'


if __name__ == '__main__':
    app.run(debug=True)
