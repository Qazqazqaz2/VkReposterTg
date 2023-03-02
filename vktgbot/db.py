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

cur = conn.cursor()

def lever_check():
    cur.execute('select active from lever;')
    res = cur.fetchone()
    return res[0]

def lever_down():
    cur.execute('update lever set active=False;')
    conn.commit()


def lever_up():
    cur.execute('update lever set active=True;')
    conn.commit()