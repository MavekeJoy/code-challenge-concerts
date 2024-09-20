import sqlite3

class Venue:
    def __init__(self, title, city):
        self.title = title
        self.city = city

    @staticmethod
    def connect_db():
        return sqlite3.connect('concert_domain.db')

    def save(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO venues (title, city) VALUES (?, ?)", (self.title, self.city))
        conn.commit()
        conn.close()

    @staticmethod
    def get_concerts(venue_title):
        conn = Venue.connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT c.date, b.name, b.hometown
            FROM concerts c
            JOIN venues v ON c.venue_id = v.id
            JOIN bands b ON c.band_id = b.id
            WHERE v.title = ?
        """, (venue_title,))
        concerts = cursor.fetchall()
        conn.close()
        return concerts
