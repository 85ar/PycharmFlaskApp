from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/auth/<name>')
def auth(name):
    return render_template('auth.html', name=name)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/loging')
def loging():
    return render_template('loging.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/logout')
def logout():
    return render_template('auth.html')

if __name__ == '__main__':
    app.run(debug=True)
