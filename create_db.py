from psycopg2 import connect, OperationalError
import psycopg2.errors

CREATE_DATABASE = """CREATE DATABASE project_db;"""

CREATE_TABLE_USERS = """CREATE TABLE user(
    id serial primary key, 
    username varchar(255), 
    hashed_password varchar(80));"""

CREATE_TABLE_MESSAGES = """CREATE TABLE messages(
    id serial primary key,
    from_id int not null ON DELETE CASCADE,
    to_id int not null ON DELETE CASCADE,
    text text(500),
    received_date timestamp default current_timestamp,
    foreign key (from_id) references user(id),
    foreign key (to_id) references user(id));"""

USERNAME = "postgres"
PASSWORD = "coderslab"
HOST = "localhost"

# try:
#     cnx = connect(user=USERNAME, password=PASSWORD, host=HOST, database="postgres")
#     cnx.autocommit = True
#     cursor = cnx.cursor()
#     try:
#         cursor.execute(CREATE_DATABASE)
#         print("Database created")
#     except DuplicateDatabase:
#         print("Database already exists")
#     cnx.close()
# except OperationalError:
#     print("Operational Error..")

try:
    cnx = connect(user=USERNAME, password=PASSWORD, host=HOST, database="project_db")
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(CREATE_TABLE_USERS)
        print("Table users created")
    except DuplicateTable:
        print("Table users already exists")
    try:
        cursor.execute(CREATE_TABLE_MESSAGES)
        print("Table messages created")
    except DuplicateTable:
        print("Table messages already exists")
    cnx.close()
except OperationalError:
    print("Operational Error..")
