import psycopg2

connection = psycopg2.connect(database="sentinet", user="sentinet", password="sentinet", host="127.0.0.1", port="5432")