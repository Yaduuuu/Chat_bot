from flask import Flask, render_template, request, jsonify, redirect, url_for, abort
from flask_cors import CORS
from chat import get_response
import sqlite3

app = Flask(__name__)
CORS(app)
 

# Function to create the database table if not exists
def create_table():
    conn = sqlite3.connect('pro.db')  # Use the same database file
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            message TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Create the table on application start
create_table()

@app.route('/')
def index():
    return render_template('contact.html')

print("Just before /submit invocation")

@app.route('/submit' , methods=['POST'])
def submit():
    try:
        # if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        message = data.get('message')

        print(f"Received data: Name={name}, Email={email}, Phone={phone}, Message={message}")

        # Insert data into the database (use the same database file 'pro.db')
        conn = sqlite3.connect('pro.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO submissions (name, email, phone, message) VALUES (?, ?, ?, ?)
        ''', (name, email, phone, message))
        conn.commit()
        conn.close()

    except Exception as e:
        # Log the exception
        print(f"An error occurred: {str(e)}")
        abort(500)

    return redirect(url_for('index'))

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO: Check if the text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)