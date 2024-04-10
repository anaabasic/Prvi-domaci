from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Kreiranje SQLite baze podataka
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS students
             (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

# Veb servisi

# GET zahtev za sve studente
@app.route('/students', methods=['GET'])
def get_students():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('SELECT * FROM students')
    students = c.fetchall()
    conn.close()
    return jsonify(students)
