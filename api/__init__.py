from api.models import Crime
from api.orm import *

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
        crime_records = cursor.fetchall()
        crimes = [build_record(Crime, crime_record) for crime_record in crime_records]
        return jsonify([crime.__dict__ for crime in crimes])

    @app.route('/crimes/<id>')
    def show(id):
        cursor = get_db(user, password, database)
        cursor.execute('SELECT * FROM crimes WHERE id = %s', vars = (id,))
        crime_record = cursor.fetchone()
        crime = build_record(Crime, crime_record)
        return jsonify(crime.__dict__)

    return app