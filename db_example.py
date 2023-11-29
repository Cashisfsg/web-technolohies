import os
import sqlite3
import sys


DB = ""  #! Set DB NAME

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


def main():
    if db_exists:
        pass  #! Do something
    else:
        print("Database does not exists, create a new database.")


if __name__ == "__main__":
    main()
