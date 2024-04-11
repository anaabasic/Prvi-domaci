from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS students
             (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students', methods=['GET'])
def get_students():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('SELECT * FROM students')
    students = c.fetchall()
    conn.close()
    return jsonify(students)

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('SELECT * FROM students WHERE id = ?', (student_id,))
    student = c.fetchone()
    conn.close()
    return jsonify(student)

@app.route('/students', methods=['POST'])
def add_student():
    new_student = request.json
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('INSERT INTO students (name, age) VALUES (?, ?)', (new_student['name'], new_student['age']))
    conn.commit()
    conn.close()
    return 'Student added successfully', 201

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    updated_student = request.json
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('UPDATE students SET name = ?, age = ? WHERE id = ?', (updated_student['name'], updated_student['age'], student_id))
    conn.commit()
    conn.close()
    return 'Student updated successfully'

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()
    return 'Student deleted successfully'
    
@app.route('/students/search', methods=['GET'])
def search_students_by_name():
    name = request.args.get('name')
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('SELECT * FROM students WHERE name = ?', (name,))
    students = c.fetchall()
    conn.close()
    return jsonify(students)

@app.route('/students', methods=['DELETE'])
def delete_all_students():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('DELETE FROM students')
    conn.commit()
    conn.close()
    return 'All students deleted successfully'

if __name__ == '__main__':
    app.run(debug=True)