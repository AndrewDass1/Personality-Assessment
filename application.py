from flask import Flask
from flask import render_template
from flask.helpers import url_for

application = app = Flask(__name__)

@app.route('/')
def quest():
    return render_template('questions.html')

@app.route('/1507.html')
def res0():
    return render_template('1507.html')

@app.route('/4715.html')
def res1():
    return render_template('4715.html')

@app.route('/1721.html')
def res2():
    return render_template('1721.html')

@app.route('/4535.html')
def res3():
    return render_template('4535.html')

@app.route('/2549.html')
def res4():
    return render_template('2549.html')

@app.route('/5751.html')
def res5():
    return render_template('5751.html')

@app.route('/4162.html')
def res6():
    return render_template('4162.html')

@app.route('/5675.html')
def res7():
    return render_template('5675.html')

@app.route('/8685.html')
def res8():
    return render_template('8685.html')

@app.route('/2191.html')
def res9():
    return render_template('2191.html')

@app.route('/3510.html')
def res10():
    return render_template('3510.html')



if __name__ == "__main__":
    app.run()