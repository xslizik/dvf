from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{os.getenv("DB_USER")}:{os.getenv("PASSWORD")}@{os.getenv("HOST")}:{os.getenv("PORT")}/{os.getenv("DATABASE")}'
db = SQLAlchemy(app)

class SportType(db.Enum):
    Basketball = 'Basketball'
    Soccer = 'Soccer'
    Tennis = 'Tennis'
    Golf = 'Golf'
    Football = 'Football'

class SportsEvents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, nullable=False)
    sport_type = db.Column(db.Enum(SportType.Basketball, SportType.Soccer, SportType.Tennis, SportType.Golf, SportType.Football, name='sport_type'), nullable=False)

class Logins(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        login = request.form.get('login')
        password = request.form.get('password')
        user = Logins.query.filter_by(login=login, password=password).first()
        if user:
            return render_template("login.html", error_message=f"Hello {user.login}")
        else:
            return render_template('login.html', error_message='Logins unsuccessful.')

@app.route('/union', methods = ["POST", "GET"])
def union():
    if request.method == "GET":
        return render_template("union.html")
    else:
        sport_type = request.form.get('sport_type')
        try:
            results = SportsEvents.query.filter_by(sport_type=sport_type).all()
        except:
            results = None
        return render_template('union.html', results=results)

@app.route('/blind', methods=['GET', 'POST'])
def check_event():
    if request.method == "GET":
        return render_template("blind.html")
    else:
        id = request.form.get('id')
        try:
            result = SportsEvents.query.get(id)
        except:
            result = None

        if result:
            return render_template('blind.html', error_message='Sports event exists')
        else:
            return render_template('blind.html', error_message='Sports event is missing')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/migrate')
def migrate():
    sports_events = [
        SportsEvents(id=1, name='All-Star Game', date='2023-02-19', sport_type=SportType.Basketball),
        SportsEvents(id=2, name='UEFA Champions', date='2023-06-10', sport_type=SportType.Soccer),
        SportsEvents(id=3, name='US Open', date='2023-08-28', sport_type=SportType.Tennis),
        SportsEvents(id=4, name='Vegas Showdown', date='2024-03-01', sport_type=SportType.Basketball)
    ]
    logins = [
        Logins(id=10, login='plato', password='potato'),
        Logins(id=1, login='admin', password='sadmin'),
        Logins(id=2, login='derrida', password='notapipe')
    ]
    with app.app_context():
        db.create_all()
        db.session.add_all(sports_events)
        db.session.add_all(logins)
        db.session.commit()
    return "True"

if __name__ == '__main__':
    app.run(debug=True, port=8000)