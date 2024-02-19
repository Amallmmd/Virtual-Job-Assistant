# building URL dynamically
from flask import Flask,url_for,redirect,request,render_template
from cs50 import sql

db = sql.SQL("sqlite:////Users/amallmuhammed/Desktop/newproject/flask/hi.db")
res=db.execute('select * from job')
print(res)
## create object for WSGI application
app = Flask(__name__)

## when the webpage loads the home page
@app.route('/')
def welcome():
    return render_template('index.html')
@app.route('/new/<int:score>')
def newpage(score):
    return 'NEW PAGE LOADED'+str(score)


@app.route('/result/<text>')
def text(number):

    return render_template('result.html',number=number)

@app.route('/submit')
def submit():
    
    return render_template('result.html')
    


if __name__=='__main__':
    app.run(debug=True)



# @app.route('/members/<int:mark>')
    #  def member(mark):
    
    
#     page = 'newpage'
#     return redirect(url_for(page,score=mark))