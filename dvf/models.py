from db import db

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
