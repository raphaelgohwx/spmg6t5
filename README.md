# Introduction
The Skill-Based Role Portal (SBRP) empowers users with various roles, namely Human Resource Personnel, Managers, and Staff, to perform specific actions in line with their access permissions. Human Resource Personnel can assess the skills of role applicants, while Staff members can browse and refine role listings based on their search preferences and submit applications for roles that pique their interest. Furthermore, the system offers a feature called Role-Skill Match, which illustrates the alignment and gaps between role requirements and the current skillsets of Staff members as a percentage.

## Index
- [Setup](#setup)
  - [Pre-Requisites](#pre-requisites)
  - [Database Setup](#database-setup)
  - [Install Dependencies](#install-dependencies)
  - [Launching the Webpage](#launching-the-webpage)
  - [Running the Backend](#running-the-backend)
  - [Run pytests](#run-pytest)

## Setup
### Pre-Requisites
- Code Editor
- SQL Workbench

### Database Setup
The backend application uses a AWS RDS MySQL server for data persistence. To create and connect your own AWS RDS Mysql instance, refer to AWS's documentation here: https://aws.amazon.com/getting-started/hands-on/create-mysql-db/
1. Open MySQL workbench, set up new connection using AWS RDS MySQL endpoint details
2. Once MySQL is connected, update account details in creds.py
3. cd into backend, run setup_sql.py to populate MySQL database

### Install Dependencies
```
$ cd frontend
$ npm install
```

### Launching the Webpage
On a new terminal:
```
$ cd frontend
$ npm run dev
```

### Running the Backend
On a new terminal:
```
$ cd backend
$ python app.py
```

### Run pytests
1. cd into root folder
2. run python -m pytest to run all unit tests


