from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Подключение к БД
def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        host=os.environ['DB_HOST']
    )
    return conn

# Создание таблицы, если не существует
def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS visits (
            id SERIAL PRIMARY KEY,
            visit_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()

@app.route('/')
def hello():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO visits DEFAULT VALUES')
    conn.commit()

    cur.execute('SELECT COUNT(*) FROM visits')
    count = cur.fetchone()[0]

    cur.close()
    conn.close()
    return f"<h1>Hello Danil, i love you!</h1><p>Visits: {count}</p>"

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
