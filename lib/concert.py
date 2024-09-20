import sqlite3

class Concert:
    def __init__(self, band_id, venue_id, date):
        self.band_id = band_id
        self.venue_id = venue_id
        self.date = date

    @staticmethod
    def connect_db():
        return sqlite3.connect('concert_domain.db')

    def save(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO concerts (band_id, venue_id, date)
            VALUES (?, ?, ?)
        """, (self.band_id, self.venue_id, self.date))
        conn.commit()
        conn.close()

    @staticmethod
    def find_concerts():
        conn = Concert.connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT c.date, b.name, v.title
            FROM concerts c
            JOIN bands b ON c.band_id = b.id
            JOIN venues v ON c.venue_id = v.id
        """)
        concerts = cursor.fetchall()
        conn.close()
        return concerts
