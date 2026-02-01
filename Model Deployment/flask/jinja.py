# Building url dynamically and variable rule and  Jinja 2 template engine

# jinja 2 template engine
'''
{{ }} expression to print output in html 
{%...% } conditions, for loops
{#...#} this is for comments
'''

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return '<html><body><h1>Welcome to this Flask app!. This must be amazing journey!</h1></body></html>'

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     if request.method == 'POST':
#         name =  request.form['name']
#         return f'Hello {name}!'
#     return render_template('form.html')

# variable rule
@app.route('/sucess/<int:score>')
def sucess(score):
    res =''
    if score >= 50:
        res = "PASSED"
    else:
        res = 'FAILED'

    return render_template('result.html', results = res)

@app.route('/sucessres/<int:score>')
def sucessres(score):
    res =''
    if score >= 50:
        res = "PASSED"
    else:
        res = 'FAILED'
    
    exp={'score':score, 'res':res}

    return render_template('result1.html', results = exp)

@app.route('/sucessif/<int:score>')
def sucessif(score):
    return render_template('result2.html', results = score)


@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html', results = score)


@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('sucessres',score=total_score))


if __name__ == '__main__':
    app.run(debug=True)