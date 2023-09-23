from flask import Flask
from flask_cors import CORS

import mysql.connector
import creds

# establish connection to database
def create_connection():
    connection = mysql.connector.connect(
        host=creds.host,
        user=creds.user,
        password=creds.password,
        database=creds.database
    )
    return connection

connection = create_connection()

app = Flask(__name__)
CORS(app)

@app.route("/getStaffRoles")
def retrieve_all_role_listings():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Role_Listing")
    rows = cursor.fetchall()
    cursor.close()

    json_list = []
    for row in rows:
        row_dict = {}
        row_dict["Role_Listing_ID"] = row[0]
        row_dict["Role_Name"] = row[1]
        row_dict["Date_Closed"] = row[2]
        row_dict["Role_Description"] = row[3]
        json_list.append(row_dict)
    return json_list

if __name__ == "__main__":
    app.run(debug=True, port=5001)