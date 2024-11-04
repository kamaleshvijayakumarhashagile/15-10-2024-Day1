from flask import Flask, request,jsonify
import psycopg2
from psycopg2 import sql
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

DB_HOST = 'localhost'
DB_NAME = 'user_db'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'

# Flask endpoint to load data
@app.route('/load', methods=['POST'])
def load_data():
    data = request.json
    if not isinstance(data, list):
        return jsonify({"error": "Invalid data input"}), 400

    try:
        db_connection = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = db_connection.cursor()

        for user in data:
            insert_data = sql.SQL("""
                INSERT INTO user_details 
                x
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s , %s , %s)
            """)

            cursor.execute(insert_data, (
                user['first_name'],
                user['last_name'],
                user['email'],
                user['phone_no'],
                user['experience'],
                user['notice_period'],
                user['education'],
                user['year_of_passing'],
                user['college'],
                user['location'],
                user['internship_experience_in_months'],
                user['technical_skills']
            ))

        db_connection.commit()  # Move commit here for efficiency
        return jsonify({"message": "Data loaded successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    finally:
        if cursor:
            cursor.close()
        if db_connection:
            db_connection.close()

if __name__ == '__main__':
    app.run(debug=True)
