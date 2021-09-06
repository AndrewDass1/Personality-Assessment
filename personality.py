#https://www.bellaonline.com/articles/art22573.asp

#HTML Button:
#https://www.bitdegree.org/learn/html-
#List of functions:
#https://html.com/input-type-button/


#Javascript:
#https://www.programiz.com/javascript/examples/add-number
#https://www.w3schools.com/html/html_scripts.asp


#Need to do:
#Insert return page for each score, use <a href> 
#Add number counter, keep track of score

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def quest():
    return render_template('questions.html')

@app.route('/result0.html')
def res0():
    return render_template('result0.html')

@app.route('/result1.html')
def res1():
    return render_template('result1.html')

@app.route('/result2.html')
def res2():
    return render_template('result2.html')

@app.route('/result3.html')
def res3():
    return render_template('result3.html')

@app.route('/result4.html')
def res4():
    return render_template('result4.html')

@app.route('/result5.html')
def res5():
    return render_template('result5.html')

@app.route('/result6.html')
def res6():
    return render_template('result6.html')

@app.route('/result7.html')
def res7():
    return render_template('result7.html')

@app.route('/result8.html')
def res8():
    return render_template('result8.html')

@app.route('/result9.html')
def res9():
    return render_template('result9.html')

@app.route('/result10.html')
def res10():
    return render_template('result10.html')

if __name__ == "__main__":
    app.run()