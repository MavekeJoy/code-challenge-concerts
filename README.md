# code-challenge-concerts
## OVERVIEW
 - This is a simple Python application that manages concerts, bands, and venues using SQLite. It allows you to manage bands, venues, and concerts by providing an interface to create, view, and manage data related to concerts, including which bands are performing at which venues and on what dates.

 ## FEATURES
 - Create and manage bands (name and hometown).
 - Create and manage venues (title and city).
 - Schedule concerts with specific bands at different venues on particular dates.
 - Retrieve concerts for specific bands or venues.
 - Simple SQLite database integration.

## INSTALLATION
 1. Cloning the repo (git clone )
 2. Install SQlite and check for its version( sqlite3 --version)
 3. Run the migrations (python main.py)
 
## USAGE 
### Creating Bands and Venues
- You can create a new bands and venues by using the Band and Venues classes.

### Scheduling Concerts
- You can schedule concerts once bands and venues are created.

### Viewing Concerts by Band or Venue

- You can view concerts based on the band or venue using the static method provided for getting concerts.


### DATABASE STRUCTURE
 1. Bands
    - id (INTEGER)
    - name (TEXT)
    - hometown (TEXT)

 2. Venues
    - id (INTEGER)
    - title (TEXT)
    - CITY (TEXT)

 3. Concerts
    - id(INTEGER)
    - band_id(INTEGER)
    - venue_id(INTEGER)
    - date(TEXT)


# LICENSE
 - This project is licensed under the MIT License. See the LICENSE file for details.

