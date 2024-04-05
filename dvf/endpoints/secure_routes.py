from flask import Blueprint, render_template, request
from models import Logins, SportsEvents

secure = Blueprint('secure', __name__)

@secure.route("/login_secure", methods=["POST", "GET"])
def login_secure():
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

@secure.route('/union_secure', methods = ["POST", "GET"])
def union_secure():
    if request.method == "GET":
        return render_template("union.html")
    else:
        sport_type = request.form.get('sport_type')
        if sport_type:
            try:
                results = SportsEvents.query.filter_by(sport_type=sport_type).all()
            except:
                results = None
        else:
            results = SportsEvents.query.all()

        for i in range(len(results)):
            output = ["uwu"]
            output.append(results[i].name)
            output.append(results[i].date)
            output.append(results[i].sport_type)                
            results[i] = output

        return render_template('union.html', results=results)

@secure.route('/blind_secure', methods=['GET', 'POST'])
def check_event_secure():
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

@secure.route('/secure')
def index_secure():
    return render_template('index_secure.html')
