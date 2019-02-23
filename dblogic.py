import sqlite3


connection = sqlite3.connect('{}.db'.format("Messedup"))
c = connection.cursor()


def getTouristLocations():
    c.execute("SELECT location, latitude, longitude, geo_zone, state FROM trip ")
    rows = c.fetchall()
    tourist_centers = {}
    for row in rows:
        tourist_centers[row[0]] = [row[1], row[2], row[3], row[4]]
    return tourist_centers
