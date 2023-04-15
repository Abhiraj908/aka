from flask import Flask, redirect, request, render_template, url_for, flash
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import validates
# from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myweb-data.db'
app.config['SECRET_KEY'] = "bgcwugweucbeug"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)

COURT_NAMES=["Supreme Court Delhi", "Allahabad High Court", "Bombay High Court", "Calcutta High Court", "Chhattisgarh High Court", "Delhi High Court", "Gauhati High Court", "Gujarat High Court", "Himachal Pradesh High Court", "Jammu & Kashmir and Ladakh High Court", "Jharkhand High Court", "Karnataka High Court", "Kerala High Court", "Madhya Pradesh High Court", "Madras High Court", "Manipur High Court", "Meghalaya High Court", "Orissa High Court", "Patna High Court", "	Punjab and Haryana High Court", "Rajasthan High Court", "Sikkim High Court", "	Telangana High Court", "Tripura High Court", "Uttarakhand High Court"]

class LegalModel(db.Model):
 
    case_num = db.Column(db.Integer, primary_key=True)
    court_name = db.Column(db.String(100), default = COURT_NAMES[0])
    party_name1 = db.Column(db.String(500), nullable=False)
    party_name2 = db.Column(db.String(500), nullable=False)
    # order_date = db.Column(db.DateTime)
    judges = db.Column(db.String(500), nullable=False)
    # held = db.Column(db.DateTime)

# with app.app_context():
#     db.create_all()


@app.route('/')
def index():
    # print('Helo world')
    return render_template('index.html')

@app.route('/save-data', methods=["GET","POST"])
def temp():
    
    if request.method=="POST":
        court_name = request.form['court_name']
        nofp = request.form['nofp']
        nofp2 = request.form['nofp2']
        # dof = request.form['dof']
        jd = request.form['jd']
        # held = request.form['held']
        obj = LegalModel(court_name=court_name,party_name1=nofp, 
                    party_name2=nofp2, judges=jd)

        db.session.add(obj)
        db.session.commit()
        flash("Case entry successful!") 
        return render_template('index.html')
    
    return render_template('case_form.html', court=COURT_NAMES)
    
# @app.route('/save')
# def save():        
#     return render_template('save_form.html')

@app.route('/get-data')
def get():
    info = LegalModel.query.all()
    print(f"Info : {info}")
    return render_template('get_data.html', info=info)

if __name__ == "__main__":
    app.run(debug=True)