__author__ = 'pv'

import psycopg2

db_name = "bpn"
db_user = "postgres"
db_table_name = "testing"


def insert_row(user, inputs="", output="", text=""):
    # Connect to an existing database
    conn = psycopg2.connect("dbname=" + db_name + " user=" + db_user)
    cur = conn.cursor()
    cur.execute("INSERT INTO " + db_table_name + " (user_name, input, out, text) VALUES (%s, %s, %s, %s)",
                (user, inputs, output, text))
    # Make the changes to the database persistent
    conn.commit()
    cur.close()
    conn.close()


def get_user_data(user):
    # Connect to an existing database
    conn = psycopg2.connect("dbname=" + db_name + " user=" + db_user)
    cur = conn.cursor()
    cur.execute("SELECT * FROM " + db_table_name + " where user_name=\'" + user + "\';")
    result = cur.fetchone()
    # Make the changes to the database persistent
    cur.close()
    conn.close()
    return result


def test():
    insert_row("daniel johanisburg", "facebuke", "twter", "these are all the words i typed ever")
    print get_user_data("daniel johanisburg")