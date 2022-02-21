from flask import Flask
from flask import render_template
from flask.helpers import url_for

application = app = Flask(__name__)

@app.route('/')
def quest():
    return render_template('index.html')

@app.route('/Sad.html')
def emotion1():
    return render_template('Sad.html')

@app.route('/Neutral.html')
def emotion2():
    return render_template('Neutral.html')

@app.route('/Happy.html')
def emotion3():
    return render_template('Happy.html')

@app.route('/Strong.html')
def emotion4():
    return render_template('Strong.html')

if __name__ == "__main__":
    app.run()
