import sqlite3

class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown

    @staticmethod
    def connect_db():
        return sqlite3.connect('concert_domain.db')

    def save(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO bands (name, hometown) VALUES (?, ?)", (self.name, self.hometown))
        conn.commit()
        conn.close()

    @staticmethod
    def get_concerts(band_name):
        conn = Band.connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT c.date, v.title, v.city
            FROM concerts c
            JOIN venues v ON c.venue_id = v.id
            JOIN bands b ON c.band_id = b.id
            WHERE b.name = ?
        """, (band_name,))
        concerts = cursor.fetchall()
        conn.close()
        return concerts
