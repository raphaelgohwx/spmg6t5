# Introduction
- Add your project logo.
- Write a short introduction to the project.
- If you are using badges, add them here.

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


