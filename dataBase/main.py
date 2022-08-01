import psycopg2
from dataBase.config import host, user, password, db_name

def connect():
    connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
    return connection

def data_processing(tg_id, data):
    connection = connect()
    timestamp = f'2022-{data[2][3:5]}-{data[2][0:2]}' + ' ' + f'{data[3]}'
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO RENT (sport_type, rent_date, rental_duration) VALUES ('%s', '%s', '%s'); " %(data[1], timestamp, data[4])
        )
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO USERS (name, phone_number, telegram_id) VALUES ('%s', '%s', '%s'); " %(data[-2], data[-1], tg_id)
        )
    connection.commit()
    if connection:
        connection.close()