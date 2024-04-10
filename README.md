# Flask Student Management API

This is a simple Flask API for managing student records. It allows you to perform CRUD (Create, Read, Update, Delete) operations on student data stored in a SQLite database.

## Installation

1. Make sure you have Python installed on your computer. If not, you can download and install it from the [official Python website](https://www.python.org/).

2. Install Flask and SQLite3 libraries using pip:
    ```
    pip install flask
    ```

3. Clone this repository to your local machine:
    ```
    git clone https://github.com/your_username/your_project.git
    ```

4. Navigate to the project directory:
    ```
    cd your_project
    ```

5. Run the Flask application:
    ```
    python app.py
    ```

6. Access the API at `http://127.0.0.1:5000/` in your web browser or using tools like Postman.

## API Endpoints

- `GET /students`: Get all students
- `GET /students/<student_id>`: Get student by ID
- `POST /students`: Add a new student
- `PUT /students/<student_id>`: Update student by ID
- `DELETE /students/<student_id>`: Delete student by ID
- `GET /students/search?name=<student_name>`: Search students by name
- `DELETE /students`: Delete all students

## Database

The SQLite database (`example.db`) contains a single table `students` with columns `id`, `name`, and `age`. You can use SQLite browser tools to interact with the database.

## Usage

You can use tools like Postman to interact with the API endpoints. Here are some example requests:

- To get all students: `GET http://127.0.0.1:5000/students`
- To add a new student: `POST http://127.0.0.1:5000/students` with JSON body `{"name": "John Doe", "age": 20}`
- To update a student: `PUT http://127.0.0.1:5000/students/<student_id>` with JSON body `{"name": "Jane Doe", "age": 22}`
- To delete a student: `DELETE http://127.0.0.1:5000/students/<student_id>`

## Author

[Ana](https://github.com/anaabasic)

## License

This project is licensed under the [MIT License](LICENSE).
