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
        
    # [for frontend] retrieve all dept names in staff table to send to role creation form for dropdown
    def get_all_dept_names():
        cursor = connection.cursor()
        cursor.execute("select distinct Dept from Staff")
        rows = cursor.fetchall()
        cursor.close()

        json_list = []
        for row in rows:
            json_list.append(row[0])
        return json_list

    def get_staff_skills_by_staff_id(self, staff_id):
        cursor = connection.cursor()
        cursor.execute("select Skill_Name from Staff_Skill where Staff_ID = {}".format(staff_id))
        rows = cursor.fetchall()
        cursor.close()

        json_list = []
        for row in rows:
            json_list.append(row[0])
        return json_list


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
            return "Error: Role Listing ID already exists."
        elif self.role_listing_is_not_empty() == False or self.role_listing_is_not_null() == False:
            return "Error: One or more fields are empty."
        elif self.is_not_past_date() == False:
            return "Error: Date closed is in the past."
        elif (self.same_role_name_and_date(self.Role_Name, self.Date_Closed, self.Dept) == False):
            return "Error: Role Listing with same Role Name and Date already exists."
        else:
            
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Role_Listing VALUES (%s, %s, %s, %s, %s)", (self.Role_Listing_ID, self.Role_Name, self.Date_Closed, self.Role_Description, self.Dept))
            connection.commit()
            cursor.close()
            return "Success"
        
    def delete_Role_Listing(self):
        if (self.Role_Listing_ID) in Role_Listing.retrieve_all_role_listing_ID(self):
            cursor = connection.cursor(self)
            cursor.execute("DELETE FROM Role_Listing WHERE Role_Listing_ID = %s", (self.Role_Listing_ID,))
            connection.commit()
            cursor.close()
            return True
        else:
            return False
        
    def same_role_name_and_date(self, Role_Name, Date_Closed, Dept):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Role_Listing WHERE Role_Name = %s AND Date_Closed = %s AND Dept = %s", (Role_Name, Date_Closed, Dept))
        rows = cursor.fetchall()
        cursor.close()

        if len(rows) > 0:
            return False
        else:
            return True

    
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
    
    def retrieve_active_role_listings_ID(self):
        cursor = connection.cursor()
        cursor.execute("SELECT Role_Listing_ID, Date_Closed FROM Role_Listing")
        rows = cursor.fetchall()
        cursor.close()

        json_list = []
        for row in rows:
            today = date.today()
            if today < row[1]:
                json_list.append(row[0])
        return json_list
    
    # retrieve highest roleListingID to be used for creating new role listings
    def get_max_role_listing_id():
        cursor = connection.cursor()
        cursor.execute("select Role_Listing_ID from Role_Listing")
        rows = cursor.fetchall()
        cursor.close()

        max_id = 0
        for row in rows:
            if row[0] > max_id:
                max_id = row[0] 
        return max_id 
    
    # [for frontend] retrieve all dept names in role_listing table to send to role creation form for dropdown
    def get_all_dept_names():
        cursor = connection.cursor()
        cursor.execute("select distinct Dept from Role_Listing")
        rows = cursor.fetchall()
        cursor.close()

        json_list = []
        for row in rows:
            json_list.append(row[0])
        return json_list

    def get_all_role_listing_id():
        cursor = connection.cursor()
        cursor.execute("select distinct Role_Listing_ID from Role_Listing order by Role_Listing_ID")
        rows = cursor.fetchall()
        cursor.close()

        json_list = []
        for row in rows:
            json_list.append(row[0])
        return json_list
    
    def updateRoleListing(self):
        if (self.Role_Listing_ID) in Role_Listing.retrieve_all_role_listing_ID(self):
            cursor = connection.cursor(self)
            cursor.execute("UPDATE Role_Listing SET Role_Name = %s, Date_Closed = %s, Role_Description = %s, Dept = %s WHERE Role_Listing_ID = %s", (self.Role_Name, self.Date_Closed, self.Role_Description, self.Dept, self.Role_Listing_ID))
            connection.commit()
            cursor.close()
            return "Success"
        else:
            return "Listing does not exist"
        
    def filter_role_listing_by_skill_name(self, Skill_Name):
        cursor = connection.cursor()
        sql_query = "SELECT * FROM Role_Listing INNER JOIN Role_Skill ON Role_Listing.Role_Name = Role_Skill.Role_Name WHERE Skill_Name = '{}' ORDER BY Date_Closed ASC".format(Skill_Name)
        cursor.execute(sql_query)
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
    
    def filter_role_listing_by_dept(self, Dept):
        cursor = connection.cursor()
        sql_query = "SELECT * FROM Role_Listing WHERE Dept = '{}' ORDER BY Date_Closed ASC".format(Dept)
        cursor.execute(sql_query)
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
    
    def filter_role_listing_by_date(self, endDate):
        cursor = connection.cursor()
        sql_query = "SELECT * FROM Role_Listing ORDER BY Date_Closed ASC"
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        cursor.close()
        
        print(endDate)
        end_date_obj = datetime.datetime.strptime(endDate, '%Y-%m-%d').date()
        
        json_list = []
        for row in rows:
            row_dict = {}
            today = date.today()
            if today < row[2] <= end_date_obj:
                row_dict["Role_Listing_ID"] = row[0]
                row_dict["Role_Name"] = row[1]
                row_dict["Date_Closed"] = row[2]
                row_dict["Role_Description"] = row[3]
                row_dict["Dept"] = row[4]
                json_list.append(row_dict)  
        return json_list
    
    def get_role_skills(Role_Listing_ID):
        cursor = connection.cursor()
        role_listing_sql_query = "SELECT Role_Skill.Skill_Name from Role_Listing INNER JOIN Role_Skill on Role_Listing.Role_Name = Role_Skill.Role_Name WHERE Role_Listing_ID = {}".format(Role_Listing_ID)
        cursor.execute(role_listing_sql_query)
        role_skill_rows = cursor.fetchall()
        cursor.close()

        role_listing_list = []
        for role_skill in role_skill_rows:
            role_listing_list.append(role_skill[0])

        return role_listing_list
    
    def skill_match(self, Role_Listing_ID, Staff_ID):
        role_listing_list = Role_Listing.get_role_skills(Role_Listing_ID)

        cursor = connection.cursor()
        staff_skill_sql_query = "SELECT * FROM Staff_Skill WHERE Staff_ID = {}".format(Staff_ID)
        cursor.execute(staff_skill_sql_query)
        staff_skill_rows = cursor.fetchall()
        cursor.close()

        count = 0
        for staff_skill in staff_skill_rows:
            if staff_skill[1] in role_listing_list:
                count += 1

        role_skill_match_percentage = count / len(role_listing_list)
        return jsonify(role_skill_match_percentage)

    def skill_match_from_Staff_ID(self, Staff_ID):
        cursor = connection.cursor()
        Staff_Skill_sql_query = "SELECT Skill_Name FROM Staff_Skill WHERE StafF_ID = {}".format(Staff_ID)
        cursor.execute(Staff_Skill_sql_query)
        staff_skill_rows = cursor.fetchall()
        cursor.close()

        staff_skill_list = []
        for row in staff_skill_rows:
            staff_skill_list.append(row[0])

        cursor = connection.cursor()
        Role_Application_sql_query = "SELECT * FROM Role_Listing INNER JOIN Role_Skill ON Role_Listing.Role_Name = Role_Skill.Role_Name"
        cursor.execute(Role_Application_sql_query)
        role_listing_rows = cursor.fetchall()
        cursor.close()

        role_listing_dict = {}

        for row in role_listing_rows:
            today = date.today()
            if today < row[2]:
                if row[0] not in role_listing_dict:
                    role_listing_dict[row[0]] = [row[6]]
                else:
                    role_listing_dict[row[0]].append(row[6])

        role_skill_match_percentage_dict = {}
        
        for k,v in role_listing_dict.items():
            count = 0
            missing_skill = []

            for role_skill in v:
                if role_skill in staff_skill_list:
                    count += 1
                else:
                    missing_skill.append(role_skill)
            role_skill_match_percentage_dict[k] = [count/len(v), missing_skill]

        return role_skill_match_percentage_dict
    
    def select_Role_Listing_by_ID(self, Role_ID):
        if (Role_ID) in Role_Listing.retrieve_all_role_listing_ID(self):
            cursor = connection.cursor(self)
            cursor.execute("SELECT * FROM Role_Listing WHERE Role_Listing_ID = %s", (Role_ID,))
            result = cursor.fetchall()
            cursor.close()
            return result[0]
        else:
            return "Not found"

class Role_Application(db.Model):
    __tablename__ = 'Role_Application'

    Role_Listing_ID = db.Column(db.Integer, primary_key=True)
    Staff_ID = db.Column(db.Integer, primary_key=True)

    def __init__(self, Role_Listing_ID, Staff_ID):
        self.Role_Listing_ID = Role_Listing_ID
        self.Staff_ID = Staff_ID

    # CRUD functions for Role_Application table
    def create_role_application(self, Role_Listing_ID, Staff_ID):
        if (Role_Listing_ID not in Role_Listing.retrieve_active_role_listings_ID(self)):
            return "Error: Role Listing ID does not exist or is closed."
        elif (Staff_ID not in Staff.retrieve_all_Staff_ID(self)):
            return "Error: Staff ID does not exist."
        elif ((Staff_ID, Role_Listing_ID) in Role_Application.retrieve_all_role_application(self)):
            return "Error: Role Application already exists."
        else:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Role_Application VALUES (%s, %s)", (Role_Listing_ID, Staff_ID))
            connection.commit()
            cursor.close()
            return "Role Application was created successfully!"

    def delete_role_application(self):
        cursor = connection.cursor(self)
        cursor.execute("DELETE FROM Role_Application WHERE Role_Listing_ID = %s AND Staff_ID = %s", (self.Role_Listing_ID, self.Staff_ID))
        connection.commit()
        cursor.close()
        return True

    def retrieve_all_role_application(self):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Role_Application")
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def role_application_is_not_empty(self):
        if (self.Role_Listing_ID == "" or self.Staff_ID == ""):
            return False
        else:
            return True

    # def role_application_is_not_null(self):
    #     if (self.Role_Listing_ID == None or self.Staff_ID == None):
    #         return False
    #     else:
    #         return True
        
    def get_staff_skills_from_role_application(self):
        cursor = connection.cursor(self)
        cursor.execute("SELECT * FROM Role_Application")
        rows = cursor.fetchall()
        cursor.close()

        role_application_dict = {}
        for row in rows:
            Role_Listing_ID = row[0]
            Staff_Listing_ID = row[1]
            
            if Role_Listing_ID not in role_application_dict:

                cursor = connection.cursor(self)
                cursor.execute("SELECT * FROM Staff_Skill WHERE Staff_ID = {}".format(Staff_Listing_ID))
                rows = cursor.fetchall()
                cursor.close()

                staff_skill_dict = {}
                staff_skill_dict[Staff_Listing_ID] = []
                for row in rows:
                    staff_skill_dict[Staff_Listing_ID].append(row[1])
                
                role_application_dict[Role_Listing_ID] = [staff_skill_dict]

            else:
                cursor = connection.cursor(self)
                cursor.execute("SELECT * FROM Staff_Skill WHERE Staff_ID = {}".format(Staff_Listing_ID))
                rows = cursor.fetchall()
                cursor.close()

                staff_skill_dict = {}
                staff_skill_dict[Staff_Listing_ID] = []
                for row in rows:
                    staff_skill_dict[Staff_Listing_ID].append(row[1])

                role_application_dict[Role_Listing_ID].append(staff_skill_dict)

        return jsonify(role_application_dict)
    

# class Role_Skill(db.Model):
#     __tablename__ = 'Role_Skill'

#     Role_Name = db.Column(db.String(20) , nullable=False)
#     Skill_Name = db.Column(db.String(50), nullable=False)

#     def __init__(self, Role_Name, Skill_Name):
#         self.Role_Name = Role_Name
#         self.Skill_Name = Skill_Name

#     # retrieve all role names in role_skill table to send to role creation form for dropdown
#     def get_all_role_names():
#         cursor = connection.cursor()
#         cursor.execute("select distinct Role_Name from Role_Skill")
#         rows = cursor.fetchall()
#         cursor.close()

#         json_list = []
#         for row in rows:
#             json_list.append(row[0])
#         return json_list

@app.route("/getAllRoleListings")
def get_all_role_listings():
    return Role_Listing.retrieve_all_role_listings(self=Role_Listing)

@app.route("/getActiveRoleListings")
def get_active_role_listings():
    return Role_Listing.retrieve_active_role_listings(self=Role_Listing)

@app.route("/getAllStaffName")
def get_all_staff_name():
    return Staff.retrieve_all_staff(self=Staff)

@app.route("/createRoleListing", methods=["POST"])
def createRoleListing():
    # Get the next available Role_Listing_ID
    next_id = Role_Listing.get_max_role_listing_id() + 1

    data = request.get_json()
    newListing = Role_Listing(next_id, data["Role_Name"], data["Date_Closed"], data["Role_Description"], data["Dept"])

    return newListing.create_Role_Listing()

 # need to uncomment line 274-294 before running this
# # [for frontend] get all role names from skill table for dropdown in role creation form
# @app.route("/getRoleNames")
# def get_role_names():
#     return Role_Skill.get_all_role_names()

# [for frontend] get all dept names from staff and role_listing table for dropdown in role creation form
@app.route("/getDeptNames")
def get_dept_names():
    deptNames = Role_Listing.get_all_dept_names()
    for dept in Staff.get_all_dept_names():
        if dept not in deptNames:
            deptNames.append(dept)
    return jsonify(deptNames)


#functions for update role listing table
@app.route("/getAllRoleListingIds/")
def retrieve_all_role_listing_id():
    return Role_Listing.get_all_role_listing_id()


@app.route("/updateRoleListing", methods=["PUT"])
def update_role_listing():
    data = request.get_json()
    role_listing_id = data["Role_Listing_ID"]
    role_name = data["Role_Name"]
    date_closed = data["Date_Closed"]
    role_description = data["Role_Description"]
    dept = data["Dept"]
    newListing = Role_Listing(role_listing_id, role_name, date_closed, role_description, dept)
    return newListing.updateRoleListing()

@app.route("/getAllRoleApplications")
def get_all_role_applications():
    return Role_Application.retrieve_all_role_application(self=Role_Application)

@app.route("/filterRoleListingsBySkill/<string:Skill_Name>")
def filter_role_listings_by_skill(Skill_Name):
    return Role_Listing.filter_role_listing_by_skill_name(self = Role_Listing, Skill_Name = Skill_Name)

@app.route("/filterRoleListingsByDept/<string:Dept>")
def filter_role_listings_by_dept(Dept):
    return Role_Listing.filter_role_listing_by_dept(self = Role_Listing, Dept = Dept)

@app.route("/filterRoleListingsByEndDate/<string:endDate>")
def filter_role_listings_by_date(endDate):
    return Role_Listing.filter_role_listing_by_date(self = Role_Listing, endDate=endDate)

@app.route("/roleSkillMatch/<string:Role_Listing_ID>/<string:Staff_ID>")
def role_skill_match(Role_Listing_ID, Staff_ID):
    return Role_Listing.skill_match(self = Role_Listing, Role_Listing_ID = Role_Listing_ID, Staff_ID = Staff_ID)

@app.route("/roleSkillMatch/<string:Staff_ID>")
def role_skill_match_staff_ID(Staff_ID):
    return Role_Listing.skill_match_from_Staff_ID(self = Role_Listing, Staff_ID=Staff_ID)

@app.route("/getStaffSkills")
def get_staff_skills():
    return Role_Application.get_staff_skills_from_role_application(self = Role_Application)

# @app.route("/roleListing/<string:Role_ID>")
# def select_Role_Listing_by_ID(Role_ID):
#     return Role_Listing.skill_match_from_Staff_ID(self = Role_Listing, Role_ID=Role_ID)

@app.route("/apply/<int:Staff_ID>/<int:Role_Listing_ID>", methods=["POST"])
def staff_apply_role_listing(Staff_ID, Role_Listing_ID):
    return Role_Application.create_role_application(self = Role_Application, Staff_ID=Staff_ID, Role_Listing_ID=Role_Listing_ID)

@app.route("/getStaffSkills/<int:Staff_ID>")
def get_staff_skills_by_staff_id(Staff_ID):
    return Staff.get_staff_skills_by_staff_id(self = Staff, staff_id=Staff_ID)

if __name__ == "__main__":
    app.run(debug=True, port=5001)