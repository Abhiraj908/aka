from flask import Flask, redirect, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myweb-data.db'

db = SQLAlchemy()
db.init_app(app)

class LegalModel(db.Model):
 
    id = db.Column(db.Integer, primary_key=True)
    case_num = db.Column(db.Integer, unique=True)
    court_name = db.Column(db.String(100), nullable=False)
    party_name1 = db.Column(db.String(500), nullable=False)
    party_name2 = db.Column(db.String(500), nullable=False)
    order_date = db.Column(db.DateTime, default = datetime.utcnow())
    judges = db.Column(db.String(500), nullable=False)
    held = db.Column(db.DateTime, default = datetime.utcnow())

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    # print('Helo world')
    return render_template('index.html')

@app.route('/tmp', methods=["GET","POST"])
def temp():
    # if request.method=="POST":
    casenum = random.randint(1,1000) 
    court_name = request.form.get('court_name')
    nofp = request.form.get('nofp')
    nofp2 = request.form.get('nofp2')
    dof = request.form.get('dof')
    jd = request.form.get('jd')
    held = request.form.get('held')
    obj = LegalModel(case_num=casenum,court_name=court_name,party_name1=nofp, 
                    party_name2=nofp2, judges=jd)
    db.session.add(obj)
    db.session.commit()
    # messge to show successful addition of record
    return render_template('index.html')
    
@app.route('/save')
def save():        
    return render_template('save_form.html')

# @app.route('/submit',method=['GET','POST'])
# def add_data():
#     info = LegalModel.query.all()
    

@app.route('/gtdata')
def get():
    info = LegalModel.query.all()
    return render_template('get_data.html', info=info)

# @app.route('/save')
# def save_data():
#     return render_template(url_for('table'))

if __name__ == "__main__":
    app.run(debug=True)