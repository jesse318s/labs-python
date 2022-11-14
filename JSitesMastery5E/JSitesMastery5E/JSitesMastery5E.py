import sqlite3 as s1

# create/connect to the database named movies.db
con = s1.connect('movies.db')

# Once you have a Connection, you can create a Cursor object and call its execute() method to perform SQL commands
c = con.cursor()

#get the count of tables with the name
c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='MOVIE' ''')

#if the count is 1, then table exists
if c.fetchone()[0]==1 :
    print('Table exists.')
else :
    # does not exist, create
    print('Table does not exist')

    # create a table with a primary key and other fields
    with con:
        con.execute("""
            CREATE TABLE MOVIE (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                movie_name TEXT,
                genre TEXT,
                release_date INTEGER
            );
        """)

    #create sql to insert data into the table
    sql = 'INSERT INTO MOVIE (id, movie_name, genre, release_date) values(?, ?, ?, ?)'
    data = [
        (1, 'Pacific Rim', 'Sci-Fi', 2013),
        (2, 'Pacific Rim 2', 'Sci-Fi', 2018),
        (3, 'The Fellowship of the Ring', 'Fantasy', 2001),
        (4, 'The Two Towers', 'Fantasy', 2002),
        (5, 'The Return of the King', 'Fantasy', 2003),
        (6, 'Doctor Strange', 'Fantasy', 2016),
        (7, 'X-Men', 'Sci-Fi', 2000),
        (8, 'Titanic', 'Romance', 1997),
        (9, 'Monty Python and the Holy Grail', 'Comedy', 1975),
        (10, 'Multiverse of Madness', 'Fantasy', 2022)
    ]

    # run sql query
    with con:
        con.executemany(sql, data)

# connect and read back data
with con:
    data = con.execute("SELECT * FROM MOVIE WHERE release_date >= 2000")
    for row in data:
        print(row)

    print()

    data = con.execute("SELECT * FROM MOVIE WHERE release_date < 2000")
    for row in data:
        print(row)
