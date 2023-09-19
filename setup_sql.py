''' run this file only if you want to delete and redo database'''

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

def delete_tables(table):
    cursor = connection.cursor()
    query = "DROP TABLE IF EXISTS {}".format(table)
    cursor.execute(query)
    connection.commit()
    cursor.close()

############################################################################################
''' Creation of tables'''
def create_staff_table():
    cursor = connection.cursor()
    query = "CREATE TABLE Staff(Staff_ID int NOT NULL PRIMARY KEY, Staff_FName VARCHAR(50) NOT NULL, Staff_LName VARCHAR(50) NOT NULL, Role_Name VARCHAR(20) NOT NULL, Dept VARCHAR(50) NOT NULL, COUNTRY VARCHAR(50) NOT NULL, Email VARCHAR(50) NOT NULL, Access_Rights VARCHAR(50) NOT NULL)"
    cursor.execute(query)
    connection.commit()
    cursor.close()


def create_staff_skill_table():
    cursor = connection.cursor()
    query = "CREATE TABLE Staff_Skill (Staff_ID int NOT NULL, Skill_Name VARCHAR(50) NOT NULL, PRIMARY KEY (Staff_ID, Skill_Name), FOREIGN KEY (Staff_ID) REFERENCES Staff(Staff_ID))"
    cursor.execute(query)
    connection.commit()
    cursor.close()

def create_role_skill_table():
    cursor = connection.cursor()
    query = "CREATE TABLE Role_Skill (Role_Name VARCHAR(20) NOT NULL, Skill_Name VARCHAR(50) NOT NULL, PRIMARY KEY (Role_Name, Skill_Name))"
    cursor.execute(query)
    connection.commit()
    cursor.close()


def create_role_listing_table():
    cursor = connection.cursor()
    query = "CREATE TABLE Role_Listing (Role_Listing_ID int NOT NULL PRIMARY KEY, Role_Name VARCHAR(20) NOT NULL, Date_Closed DATE NOT NULL, Role_Description VARCHAR(100) NOT NULL, FOREIGN KEY (Role_Name) REFERENCES Role_Skill (Role_Name))"
    cursor.execute(query)
    connection.commit()
    cursor.close()

def create_role_application_table():
    cursor = connection.cursor()
    query = "CREATE TABLE Role_Application (Role_Listing_ID int NOT NULL, Staff_ID INT NOT NULL, PRIMARY KEY (Role_Listing_ID, Staff_ID), FOREIGN KEY (Role_Listing_ID) REFERENCES Role_Listing(Role_Listing_ID), FOREIGN KEY (Staff_ID) REFERENCES Staff(Staff_ID));"
    cursor.execute(query)
    connection.commit()
    cursor.close()

#############################################################################################
''' Inserting data into tables '''
def insert_data_staff(Staff_ID, Staff_FName, Staff_LName, Role_Name, Dept, Country, Email, Access_Rights):
    cursor = connection.cursor()
    query = "INSERT INTO Staff (Staff_ID, Staff_FName, Staff_LName, Role_Name, Dept, Country, Email, Access_Rights) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (Staff_ID, Staff_FName, Staff_LName, Role_Name, Dept, Country, Email, Access_Rights))
    connection.commit()
    cursor.close()

def insert_data_staff_skill(Staff_ID, Skill_Name):
    cursor = connection.cursor()
    query = "INSERT INTO Staff_Skill (Staff_ID, Skill_Name) VALUES (%s, %s)"
    cursor.execute(query, (Staff_ID, Skill_Name))
    connection.commit()
    cursor.close()

def insert_data_role_skill(Role_Name, Skill_Name):
    cursor = connection.cursor()
    query = "INSERT INTO Role_Skill (Role_Name, Skill_Name) VALUES (%s, %s)"
    cursor.execute(query, (Role_Name, Skill_Name))
    connection.commit()
    cursor.close()

def insert_data_role_listing(Role_Listing_ID, Role_Name, Date_Closed, Role_Description):
    cursor = connection.cursor()
    query = "INSERT INTO Role_Listing (Role_Listing_ID, Role_Name, Date_Closed, Role_Description) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (Role_Listing_ID, Role_Name, Date_Closed, Role_Description))
    connection.commit()
    cursor.close()

def insert_data_role_application(Role_Listing_ID, Staff_ID):
    cursor = connection.cursor()
    query = "INSERT INTO Role_Application (Role_Listing_ID, Staff_ID) VALUES (%s, %s)"
    cursor.execute(query, (Role_Listing_ID, Staff_ID))
    connection.commit()
    cursor.close()

#############################################################################################

delete_tables("Role_Application")
delete_tables("Role_Listing")
delete_tables("Role_Skill")
delete_tables("Staff_Skill")
delete_tables("Staff")

create_staff_table()
create_staff_skill_table()
create_role_skill_table()
create_role_listing_table()
create_role_application_table()

'''inserting data into Staff table'''
insert_data_staff(1, "Elijah", "Khor", "HR Team", "HR and Admin", "Singapore", "elijah@email.com", "HR")
insert_data_staff(2, "Raphael", "Goh", "Senior Engineer", "Engineering Operation Division", "Singapore", "raphael@email.com", "Manager")
insert_data_staff(3, "Wei Sheng", "Ang", "Junior Engineer", "Engineering Operation Division", "Singapore", "weisheng@email.com", "Staff")
insert_data_staff(4, "Anirban", "Ghosh", "Sales Manager", "Sales", "Singapore", "ban@email.com", "Manager")
insert_data_staff(5, "Kenneth", "Lim", "Finance Manager", "Finance", "Singapore", "kenneth@email.com", "Manager")
insert_data_staff(6, "Daryl", "Teo", "Junior Engineer", "Engineering Operation Division", "Singapore", "daryl@email.com", "Staff")

''' inserting data into Staff_Skill table'''
insert_data_staff_skill(1, "Communication")
insert_data_staff_skill(1, "Creative Thinking")
insert_data_staff_skill(1, "Teamwork")

insert_data_staff_skill(2, "Analytical Skills")
insert_data_staff_skill(2, "Attention to Detail")
insert_data_staff_skill(2, "Coding")
insert_data_staff_skill(2, "Communication")
insert_data_staff_skill(2, "Creative Thinking")
insert_data_staff_skill(2, "Data Analytics")
insert_data_staff_skill(2, "Project Management")
insert_data_staff_skill(2, "Stakeholder Management")
insert_data_staff_skill(2, "Teamwork")

insert_data_staff_skill(3, "Analytical Skills")
insert_data_staff_skill(3, "Attention to Detail")
insert_data_staff_skill(3, "Coding")
insert_data_staff_skill(3, "Data Analytics")
insert_data_staff_skill(3, "Project Management")
insert_data_staff_skill(3, "Teamwork")
insert_data_staff_skill(3, "Adaptability")
insert_data_staff_skill(3, "Critical Thinking")

insert_data_staff_skill(4, "Adaptability")
insert_data_staff_skill(4, "Communication")
insert_data_staff_skill(4, "Creative Thinking")
insert_data_staff_skill(4, "Project Management")
insert_data_staff_skill(4, "Stakeholder Management")

insert_data_staff_skill(5, "Analytical Skills")
insert_data_staff_skill(5, "Attention to Detail")
insert_data_staff_skill(5, "Communication")
insert_data_staff_skill(5, "Creative Thinking")
insert_data_staff_skill(5, "Data Analytics")
insert_data_staff_skill(5, "Project Management")
insert_data_staff_skill(5, "Stakeholder Management")
insert_data_staff_skill(5, "Teamwork")

insert_data_staff_skill(6, "Analytical Skills")
insert_data_staff_skill(6, "Attention to Detail")
insert_data_staff_skill(6, "Coding")
insert_data_staff_skill(6, "Data Analytics")
insert_data_staff_skill(6, "Project Management")
insert_data_staff_skill(6, "Teamwork")

'''inserting data into Role_Skill table'''
insert_data_role_skill("Sales Manager", "Adaptability")
insert_data_role_skill("Sales Manager", "Communication")
insert_data_role_skill("Sales Manager", "Creative Thinking")
insert_data_role_skill("Sales Manager", "Project Management")
insert_data_role_skill("Sales Manager", "Stakeholder Management")

insert_data_role_skill("Account Manager", "Attention to Detail")
insert_data_role_skill("Account Manager", "Stakeholder Management")

insert_data_role_skill("Consultant", "Analytical Skills")
insert_data_role_skill("Consultant", "Adaptability")
insert_data_role_skill("Consultant", "Communication")
insert_data_role_skill("Consultant", "Creative Thinking")
insert_data_role_skill("Consultant", "Project Management")
insert_data_role_skill("Consultant", "Stakeholder Management")

insert_data_role_skill("Developer", "Analytical Skills")
insert_data_role_skill("Developer", "Attention to Detail")
insert_data_role_skill("Developer", "Coding")

insert_data_role_skill("Support Team", "Adaptability")
insert_data_role_skill("Support Team", "Communication")
insert_data_role_skill("Support Team", "Project Management")
insert_data_role_skill("Support Team", "Teamwork")

insert_data_role_skill("Senior Engineer", "Analytical Skills")
insert_data_role_skill("Senior Engineer", "Attention to Detail")
insert_data_role_skill("Senior Engineer", "Coding")
insert_data_role_skill("Senior Engineer", "Communication")
insert_data_role_skill("Senior Engineer", "Creative Thinking")
insert_data_role_skill("Senior Engineer", "Data Analytics")
insert_data_role_skill("Senior Engineer", "Project Management")
insert_data_role_skill("Senior Engineer", "Stakeholder Management")
insert_data_role_skill("Senior Engineer", "Teamwork")

insert_data_role_skill("Junior Engineer", "Analytical Skills")
insert_data_role_skill("Junior Engineer", "Attention to Detail")
insert_data_role_skill("Junior Engineer", "Coding")
insert_data_role_skill("Junior Engineer", "Data Analytics")
insert_data_role_skill("Junior Engineer", "Project Management")
insert_data_role_skill("Junior Engineer", "Teamwork")

insert_data_role_skill("Call Centre", "Analytical Skills")
insert_data_role_skill("Call Centre", "Communication")
insert_data_role_skill("Call Centre", "Teamwork")

insert_data_role_skill("Operation Planning Team", "Analytical Skills")
insert_data_role_skill("Operation Planning Team", "Adaptability")
insert_data_role_skill("Operation Planning Team", "Attention to Detail")
insert_data_role_skill("Operation Planning Team", "Communication")
insert_data_role_skill("Operation Planning Team", "Teamwork")

insert_data_role_skill("HR Team", "Communication")
insert_data_role_skill("HR Team", "Creative Thinking")
insert_data_role_skill("HR Team", "Teamwork")

insert_data_role_skill("L&D Team", "Analytical Skills")
insert_data_role_skill("L&D Team", "Adaptability")
insert_data_role_skill("L&D Team", "Communication")
insert_data_role_skill("L&D Team", "Creative Thinking")
insert_data_role_skill("L&D Team", "Stakeholder Management")
insert_data_role_skill("L&D Team", "Teamwork")

insert_data_role_skill("Admin Team", "Attention to Detail")
insert_data_role_skill("Admin Team", "Communication")
insert_data_role_skill("Admin Team", "Stakeholder Management")

insert_data_role_skill("Finance Manager", "Analytical Skills")
insert_data_role_skill("Finance Manager", "Attention to Detail")
insert_data_role_skill("Finance Manager", "Communication")
insert_data_role_skill("Finance Manager", "Critical Thinking")
insert_data_role_skill("Finance Manager", "Data Analytics")
insert_data_role_skill("Finance Manager", "Project Management")
insert_data_role_skill("Finance Manager", "Stakeholder Management")
insert_data_role_skill("Finance Manager", "Teamwork")

insert_data_role_skill("Finance Executive", "Analytical Skills")
insert_data_role_skill("Finance Executive", "Attention to Detail")
insert_data_role_skill("Finance Executive", "Communication")
insert_data_role_skill("Finance Executive", "Critical Thinking")
insert_data_role_skill("Finance Executive", "Data Analytics")
insert_data_role_skill("Finance Executive", "Teamwork")

insert_data_role_skill("IT Team", "Adaptability")
insert_data_role_skill("IT Team", "Attention to Detail")
insert_data_role_skill("IT Team", "Communication")
insert_data_role_skill("IT Team", "Critical Thinking")
insert_data_role_skill("IT Team", "Teamwork")

'''inserting data into Role_Listing table'''
insert_data_role_listing(1, "IT Team", "2023-09-10", "IT Team description is here")
insert_data_role_listing(2, "Sales Manager", "2023-09-10", "Sales Manager description is here")
insert_data_role_listing(3, "Consultant", "2023-09-10", "Consultant description is here")

'''inserting data into Role_Application table'''
insert_data_role_application(1,3)
insert_data_role_application(1,6)
insert_data_role_application(2,5)