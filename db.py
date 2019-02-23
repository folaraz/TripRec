import sqlite3
import csv


connection = sqlite3.connect('{}.db'.format("Messedup"))
c = connection.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS trip(location TEXT PRIMARY KEY, state TEXT , "
              "geo_zone TEXT, tourism_type TEXT, rating FLOAT , longitude FLOAT , latitude FLOAT)")


def InsertionQuery(path):
    with open (path, 'r') as f:
        reader = csv.reader(f)
        columns = next(reader)
        query = 'insert into trip({0}) values ({1})'
        query = query.format(','.join(columns), ','.join('?' * len(columns)))
        c.execute('BEGIN TRANSACTION')
        for data in reader:
            try:
             c.execute(query, data)
            except Exception as e:
                pass
        connection.commit()


if __name__ == '__main__':
    create_table()
    InsertionQuery('data/places.csv')


