from flask import Flask, request, render_template, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for using flash messages

# Configure MySQL connection
def get_db_connection():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'knights'
    }
    connection = mysql.connector.connect(**config)
    return connection

# Route to render the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Route to add user to the database
@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    age = request.form['age']

    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Create table if not exists
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                age INT
            )
        ''')

        # Insert user into 'users' table
        cursor.execute('INSERT INTO users (name, age) VALUES (%s, %s)', (name, age))
        connection.commit()
        cursor.close()
        connection.close()

        flash('Record inserted successfully!', 'success')
    except Exception as e:
        flash(f'Error: {e}', 'error')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')

