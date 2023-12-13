import os
import sqlite3
import sys


DB = "test.db"  #! Set DB NAME

db_exists = os.path.exists(DB)


def ensure_connection(sqlite_query):
    def query(*args, **kwargs):
        try:
            print("Connection to database")
            with sqlite3.connect(DB, timeout=20) as sqlite_connection:
                print("Connection to SQLite database successfully established")
                response = sqlite_query(connection=sqlite_connection, *args, **kwargs)
            return response
        except Exception as ex:
            print(f"Error while connecting to database: '{ex}'")
        finally:
            print("The SQLite connection is closed\n")

    return query


@ensure_connection
def init_sqlite(connection):
    cursor = connection.cursor()

    cursor.execute("SELECT sqlite_version();")
    (version,) = cursor.fetchone()
    print(f"SQLite Database version is: {version}")
    print("Database successfully created")


@ensure_connection
def delete_table(connection):
    cursor = connection.cursor()

    cursor.execute(
        """--sql
        DROP TABLE IF EXISTS pupils
    """
    )
    connection.commit()
    print("Table pupils successfully deleted")


def main():
    init_sqlite()

    db_exists = os.path.exists(DB)

    if db_exists:
        delete_table()  #! Do something
    else:
        print("Database does not exists, create a new database.")


if __name__ == "__main__":
    main()
