import psycopg2
from config import host, user, password, db_name

# connect to database
connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
try:
    # the cursor for performing database operations
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")
    # create users table
    with connection.cursor() as cursor:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (\
            id SERIAL PRIMARY KEY,\
            name TEXT NOT NULL,\
            phone_number VARCHAR(12) NOT NULL,\
            telegram_id TEXT);"
        )
    with connection.cursor() as cursor:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS rent (\
            id SERIAL PRIMARY KEY,\
            sport_type VARCHAR(9) NOT NULL,\
            rent_date TIMESTAMP NOT NULL,\
            rental_duration INTERVAL NOT NULL,\
            users_id INTEGER REFERENCES users(id));"
        )
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         "INSERT INTO rent(sport_type, rent_date, rental_duration) VALUES ('Баскетбол', '2022-05-03 11:30', '2 hours')"
    #     )
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM users;"
        )
        print(cursor.fetchall())
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM rent;"
        )
        print(cursor.fetchall())
    with connection.cursor() as cursor:
        cursor.execute(
            "DELETE FROM rent;"
        )
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")

# TRUNCATE TABLE users RESTART IDENTITY CASCADE