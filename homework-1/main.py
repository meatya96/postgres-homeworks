"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import pandas as pd
def opening_naruto(value):

    df = pd.read_csv(value)
    values_list = df.values.tolist()
    return values_list
conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='89088800080'
)

cur = conn.cursor()

print(opening_naruto('north_data/employees_data.csv'))
cur.executemany("INSERT INTO customers VALUES (%s, %s, %s)", opening_naruto('north_data/customers_data.csv'))
cur.executemany("INSERT INTO employees VALUES (%i, %s, %s, %s, %d, %s)", opening_naruto('north_data/employees_data.csv'))
cur.executemany("INSERT INTO orders VALUES (%i, %s, %i, %d, %s)", opening_naruto('north_data/orders_data.csv'))

conn.commit()