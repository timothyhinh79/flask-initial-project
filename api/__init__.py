from api.models import Crime

from flask import Flask, jsonify
import psycopg2

def get_db(user, password, database):
    conn = psycopg2.connect(database=database, user=user, password=password)
    return conn.cursor()

def create_app(user, password, database):
    app = Flask(__name__)

    @app.route('/')
    def home():
        return 'Welcome!'

    @app.route('/crimes')
    def index():
        cursor = get_db(user, password, database)
        cursor.execute('SELECT * FROM crimes;')
        crimes = cursor.fetchall()
        return jsonify(crimes)

    @app.route('/crimes/<id>')
    def show(id):
        cursor = get_db(user, password, database)
        cursor.execute('SELECT * FROM crimes WHERE id = %s', vars = (id,))
        crime = cursor.fetchone()
        return jsonify(crime)

    return app