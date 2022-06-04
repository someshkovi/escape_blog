import sqlite3
from sqlite3 import Error
import os.path
from pathlib import Path
import pandas as pd
import json

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def show_tables(conn):
    cur = conn.cursor()
    cur.execute('SELECT name from sqlite_master where type= "table"')
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_all_products(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT url,name,target_price FROM jobs_product")

    rows = cur.fetchall()

    return rows


def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def update_products_info(conn):
    df = pd.read_sql_query("SELECT * FROM jobs_product", conn)
    df = df[df.id >= 1]
    # Write the new DataFrame to a new SQLite table
    df.to_sql("jobs_product", conn, if_exists="replace")

def export_products_info(conn):
    df = pd.read_sql_query("SELECT * FROM jobs_product", conn)
    # Write the new DataFrame to a new SQLite table
    df.to_csv('products_info.csv', index=True, encoding='utf-8')

def get_json_response(conn):
    pass

def get_connection():
    BASE_DIR = Path(__file__).resolve().parent
    database = os.path.join(BASE_DIR, 'src', "db.sqlite3")
    conn = create_connection(database)
    return conn

def main():
    BASE_DIR = Path(__file__).resolve().parent
    database = os.path.join(BASE_DIR, 'src', "db.sqlite3")

    # create a database connection
    conn = create_connection(database)
    with conn:
        # print("1. Query task by priority:")
        # select_task_by_priority(conn, 1)

        # print('Show Tables')
        # show_tables(conn)

        print("2. Query all products")
        select_all_products(conn)
        print('export products')
        export_products_info(conn)


if __name__ == '__main__':
    main()