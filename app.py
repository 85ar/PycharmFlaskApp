from flask import Flask

app = Flask(__name__)
app.run(debug=True)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/view')
def view():
    return 'View'


if __name__ == '__main__':
    app.run()
