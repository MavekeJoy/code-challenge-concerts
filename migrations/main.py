import sqlite3

def connect_db():
    conn = sqlite3.connect('concert_domain.db')
    return conn

def run_migrations():
    conn = connect_db()
    with open('migrations/create_tables.sql', 'r') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

if __name__ == '__main__':
    run_migrations()
