import psycopg2
from flask import Flask, request, render_template
from dotenv import load_dotenv
import os

app = Flask(__name__)

def connect_to_database():
    return psycopg2.connect(
            database = os.getenv('DATABASE'),
            user     = os.getenv('USER'),
            password = os.getenv('PASSWORD'),
            host     = os.getenv('HOST'),
            port     = os.getenv('PORT')
        )

@app.route("/login", methods=["POST", "GET"])
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

@app.route('/union', methods = ["POST", "GET"])
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
    return render_template('vul_union.html', results=results)

@app.route('/blind', methods=['GET', 'POST'])
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

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    load_dotenv()
    app.run(debug=True, port=8000)