from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import mysql.connector
import creds

from datetime import date, datetime
import datetime
import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{}:{}@{}/{}'.format(creds.user, creds.password, creds.host, creds.database)

db = SQLAlchemy(app)

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

# app = Flask(__name__)
CORS(app)

# setting up classes for database
class Staff(db.Model):
    __tablename__ = 'Staff'

    Staff_ID = db.Column(db.Integer, primary_key=True)
    Staff_Fname = db.Column(db.String(50) , nullable=False)
    Staff_Lname = db.Column(db.String(50) , nullable=False)
    Role_Name = db.Column(db.String(20) , nullable=False)
    Dept = db.Column(db.String(50) , nullable=False)
    Country = db.Column(db.String(50) , nullable=False)
    Email = db.Column(db.String(50) , nullable=False)
    Access_Rights = db.Column(db.String(50) , nullable=False)

    def __init__(self, Staff_ID, Staff_Fname, Staff_Lname, Role_Name, Dept, Country, Email, Access_Rights):
        self.Staff_ID = Staff_ID
        self.Staff_Fname = Staff_Fname
        self.Staff_Lname = Staff_Lname
        self.Role_Name = Role_Name
        self.Dept = Dept
        self.Country = Country
        self.Email = Email
        self.Access_Rights = Access_Rights

    # CRUD functions for Staff table
    def retrieve_all_Staff_ID(self):
        cursor = connection.cursor()
        cursor.execute("SELECT Staff_ID FROM Staff")
        rows = cursor.fetchall()
        cursor.close()

        json_list = []
        for row in rows:
            json_list.append(row[0])
        return json_list
    
    def retrieve_all_staff(self):
        cursor = connection.cursor()
        cursor.execute("SELECT Staff_ID, Staff_Fname, Staff_Lname, Access_Rights FROM Staff")
        rows = cursor.fetchall()
        cursor.close()

        row_dict = {}
        for row in rows:
            staff_list = []
            staff_list.append(row[1])
            staff_list.append(row[2])
            staff_list.append(row[3])
            row_dict[row[0]] = staff_list
        return row_dict
    
    def create_staff(self):
        if (self.Staff_ID) in Staff.retrieve_all_Staff_ID(self):
            return False
        elif (self.is_not_empty() == False) or (self.is_not_null() == False):
            return False
        else:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Staff VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (self.Staff_ID, self.Staff_Fname, self.Staff_Lname, self.Role_Name, self.Dept, self.Country, self.Email, self.Access_Rights))
            connection.commit()
            cursor.close()
            return True

    def delete_staff(self):
        if (self.Staff_ID) in Staff.retrieve_all_Staff_ID(self):
            cursor = connection.cursor(self)
            cursor.execute("DELETE FROM Staff WHERE Staff_ID = %s", (self.Staff_ID,))
            connection.commit()
            cursor.close()
            return True
        else:
            return False

    # boolean logic for Staff table
    def have_access(self):
        if (self.Access_Rights == "HR" or self.Access_Rights == "Manager"):
            return True
        else:
            return False
    
    def is_not_empty(self):
        if (self.Staff_ID == "" or self.Staff_Fname == "" or self.Staff_Lname == "" or self.Role_Name == "" or self.Dept == "" or self.Country == "" or self.Email == "" or self.Access_Rights == ""):
            return False
        else:
            return True
        
    def is_not_null(self):
        if (self.Staff_ID == None or self.Staff_Fname == None or self.Staff_Lname == None or self.Role_Name == None or self.Dept == None or self.Country == None or self.Email == None or self.Access_Rights == None):
            return False
        else:
            return True

class Role_Listing(db.Model):
    __tablename__ = 'Role_Listing'

    Role_Listing_ID = db.Column(db.Integer, primary_key=True)
    Role_Name = db.Column(db.String(20) , nullable=False)
    Date_Closed = db.Column(db.DateTime, nullable=False)
    Role_Description = db.Column(db.String(100) , nullable=False)
    Dept = db.Column(db.String(50) , nullable=False)

    def __init__(self, Role_Listing_ID, Role_Name, Date_Closed, Role_Description, Dept):
        self.Role_Listing_ID = Role_Listing_ID
        self.Role_Name = Role_Name
        self.Date_Closed = Date_Closed
        self.Role_Description = Role_Description
        self.Dept = Dept

    # CRUD functions for Role_Listing table
    def is_not_past_date(self):
        today = date.today()
        date_str = self.Date_Closed
        datetime_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        if today < datetime_obj:
            return True
        else:
            return False
        
    def retrieve_all_role_listing_ID(self):
        cursor = connection.cursor()
        cursor.execute("SELECT Role_Listing_ID FROM Role_Listing")
        rows = cursor.fetchall()
        cursor.close()

        json_list = []
        for row in rows:
            json_list.append(row[0])
        return json_list
    
    def create_Role_Listing(self):
        if (self.Role_Listing_ID) in Role_Listing.retrieve_all_role_listing_ID(self):
            return False
        elif self.role_listing_is_not_empty() == False or self.role_listing_is_not_null() == False:
            return False
        elif self.is_not_past_date() == False:
            return False
        else:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Role_Listing VALUES (%s, %s, %s, %s, %s)", (self.Role_Listing_ID, self.Role_Name, self.Date_Closed, self.Role_Description, self.Dept))
            connection.commit()
            cursor.close()
            return True

        
    def delete_Role_Listing(self):
        if (self.Role_Listing_ID) in Role_Listing.retrieve_all_role_listing_ID(self):
            cursor = connection.cursor(self)
            cursor.execute("DELETE FROM Role_Listing WHERE Role_Listing_ID = %s", (self.Role_Listing_ID,))
            connection.commit()
            cursor.close()
            return True
        else:
            return False
    
    # boolean logic for Role_Listing table
    def role_listing_is_not_empty(self):
        if (self.Role_Listing_ID == "" or self.Role_Name == "" or self.Date_Closed == "" or self.Role_Description == "" or self.Dept == ""):
            return False
        else:
            return True
        
    def role_listing_is_not_null(self):
        if (self.Role_Listing_ID == None or self.Role_Name == None or self.Date_Closed == None or self.Role_Description == None or self.Dept == None):
            return False
        else:
            return True
    
    # retrieves all role listings regardless of whether they are closed or not
    def retrieve_all_role_listings(self):
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
            row_dict["Dept"] = row[4]
            json_list.append(row_dict)
        return json_list
    
    # will only retrieve role listings that are not closed
    def retrieve_active_role_listings(self):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Role_Listing")
        rows = cursor.fetchall()
        cursor.close()

        json_list = []
        for row in rows:
            row_dict = {}
            today = date.today()
            if today < row[2]:
                row_dict["Role_Listing_ID"] = row[0]
                row_dict["Role_Name"] = row[1]
                row_dict["Date_Closed"] = row[2]
                row_dict["Role_Description"] = row[3]
                row_dict["Dept"] = row[4]
                json_list.append(row_dict)
        return json_list
        

@app.route("/getAllRoleListings")
def get_all_role_listings():
    return Role_Listing.retrieve_all_role_listings(self=Role_Listing)

@app.route("/getActiveRoleListings")
def get_active_role_listings():
    return Role_Listing.retrieve_active_role_listings(self=Role_Listing)

@app.route("/getAllStaffName")
def get_all_staff_name():
    return Staff.retrieve_all_staff(self=Staff)

if __name__ == "__main__":
    app.run(debug=True, port=5001)