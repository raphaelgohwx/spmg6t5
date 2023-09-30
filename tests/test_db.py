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


# test connection to mysql db
def test_connection():
    assert connection.is_connected() == True