# CRUD create read update delete
# sql - structure quality language

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn=None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)

def create_students(conn, students):
    sql = '''INSERT INTO students(full_name, hobby, mark , date, is_working)
    VALUES (?, ?, ?, ?, ?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, students)
        conn.commit()
    except Error as e:
        print(e)


database =r'nasa11.db'

sql_create_students_table = '''
CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
full_name VARCHAR(100) NOT NULL,
hobby TEXT DEFAULT NULL,
mark DOUBLE (5, 2) NOT NULL DEFAULT NULL,
date DATE NOT NULL,
is_working BOOLEAN NOT NULL DEFAULT FALSE
);
'''

connection = create_connection(database)

if connection is not None:
    print('Connection established')

    # create_table(connection, sql_create_students_table)
    create_students(connection, ('байель', 'gaming', 99.9, '01-04-2007', False))
