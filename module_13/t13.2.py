import json
from flask import Flask
import mariadb

config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "1234",
    "database": "flight_game"
}

app = Flask(__name__)

@app.route("/airport/<icao>")
def get_airport(icao):
    try:
        conn = mariadb.connect(**config)
        cursor = conn.cursor()

        sql = "SELECT ident, name, municipality FROM airport WHERE ident = ?"
        cursor.execute(sql, (icao,))
        row = cursor.fetchone()

        if row is None:
            return {"message": "airport not found"}, 404

        response = {
            "ICAO": row[0],
            "Name": row[1],        # ✅ fixed
            "Location": row[2]
        }

        return response

    except mariadb.Error as err:
        return {"status": "error", "message": str(err)}, 500

    finally:
        if 'conn' in locals():
            conn.close()

@app.errorhandler(404)
def page_not_found(error):
    return {"message": "Invalid endpoint", "status": 404}, 404

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)