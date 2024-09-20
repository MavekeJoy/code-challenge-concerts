import sqlite3
from lib.band import Band
from lib.venue import Venue
from lib.concert import Concert

# Function to connect to the database
def connect_db():
    conn = sqlite3.connect('concert_domain.db')
    return conn

# Function to run migrations and create tables
def run_migrations():
    conn = connect_db()
    with open('migrations/create_tables.sql', 'r') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

# Testing function
def test_project():
    # Create bands and venues
    band1 = Band('The Rolling Stones', 'London')
    band1.save()
    
    venue1 = Venue('Madison Square Garden', 'New York')
    venue1.save()

    # Schedule a concert
    concert = Concert(1, 1, '2024-09-30')  # Assuming IDs 1 for both
    concert.save()

    # Fetch concerts for a band
    concerts = Band.get_concerts('The Rolling Stones')
    print('Concerts for The Rolling Stones:', concerts)

    # Fetch concerts for a venue
    venue_concerts = Venue.get_concerts('Madison Square Garden')
    print('Concerts at Madison Square Garden:', venue_concerts)

# Main entry point
if __name__ == '__main__':
    run_migrations()
    test_project()
