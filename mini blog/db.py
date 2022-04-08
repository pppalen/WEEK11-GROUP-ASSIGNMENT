import psycopg2


def db_connection():
    """ function to open connection """
    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        database='db_blog',
        user='postgres',
        password='12345678'
    )
    return conn