from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    port=3307,  # important (your docker port)
    user="root",
    password="1234",
    database="practice_db"
)

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    name = data['name']
    email = data['email']

    cursor = db.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    db.commit()

    return jsonify({"message": "User added successfully"})

@app.route('/get_users', methods=['GET'])
def get_users():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()

    users = []
    for row in result:
        users.append({
            "id": row[0],
            "name": row[1],
            "email": row[2]
        })

    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)