import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="vk_wall_check_bot",
    user="postgres",
    password="762341Aa",
    port=5432
)

psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)


def lever_down():
    cur = conn.cursor()
    cur.execute('update lever set active=False;')
    conn.commit()
    cur.close()


def lever_up():
    cur = conn.cursor()
    cur.execute('update lever set active=True;')
    conn.commit()
    cur.close()