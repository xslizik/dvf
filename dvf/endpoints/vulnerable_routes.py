from psycopg2 import connect
from os import environ as env
from flask import Blueprint, render_template, request

vulnerable = Blueprint('vulnerable', __name__)

def connect_to_database():
    return connect(
            database = env['DATABASE'],
            user     = env['DB_USER'],
            password = env['PASSWORD'],
            host     = env['HOST'],
            port     = env['PORT']
        )

@vulnerable.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        conn = connect_to_database()
        cur = conn.cursor()
        login = request.form.get('login')
        password = request.form.get('password')
        query = f"SELECT * FROM logins WHERE login = '{login}' AND password = '{password}';"
        cur.execute(query)
        user = cur.fetchall()
        conn.close()
        if user:
            return render_template("login.html", error_message=f"Hello {user.pop()[1]}")
        else:
            return render_template('login.html', error_message='Login unsuccessful.')

@vulnerable.route('/union', methods = ["POST", "GET"])
def union():
    conn = connect_to_database()
    cur = conn.cursor()
    sport_type = request.form.get('sport_type')
    if sport_type:
        query = f"SELECT * FROM sports_events WHERE sport_type = '{sport_type}';"
    else:
        query = "SELECT * FROM sports_events"
    cur.execute(query)
    results = cur.fetchall()
    conn.close()
    return render_template('union.html', results=results)

@vulnerable.route('/blind', methods=['GET', 'POST'])
def check_user():
    if request.method == "GET":
        return render_template("blind.html")
    else:
        conn = connect_to_database()
        cur = conn.cursor()
        id = request.form.get('id')
        query = f"SELECT id FROM sports_events WHERE id = {id};"
        cur.execute(query)
        results = cur.fetchone()
        conn.close()

        if results:
            return render_template('blind.html', error_message='Sports event exists')
        else:
            return render_template('blind.html', error_message='Sports event is missing')

@vulnerable.route('/')
def index():
    return render_template('index.html')