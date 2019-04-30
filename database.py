import sqlite3
import os


## Create the connection to the MySQL database..
#db = MySQLdb.connect("localhost","testuser","test123","TESTDB")

## Create the cursor object for our commands...
#cursor = db.cursor()

## Run the command to get the version of MySQL..
#cursor.execute('SELECT * FROM dbtable')

## Fetch all rows and print them out.
#data = cursor.fetchall()
#print(data)

## Perfrom good housekeeping..
#db.close()



dbpath =b'\Users\jp.c\Desktop\Django\Users\jp.c\Network Script\cisco'

connection = sqlite3.connect(dbpath)
c = connection.cursor()




def db_create(c):
    try:
        c.execute("""CREATE TABLE IF NOT EXISTS proddb
        ( serial TEXT PRIMARY KEY NOT NULL,
        hostname TEXT,
        ios TEXT,
        location TEXT)""")

    except sql3.OperationalError as opError:
        print('Database already exists!')
        print('Exception caught: ------>', opError)




def db_insert(c, serialNumber, hostname, ios, location):
    try:
        with connection:
            c.execute('INSERT INTO dbinventory VALUES(?, ?, ?, ?);', (serialNumber, hostname, ios, location))

    except sqlite3.IntegrityError as sqlError:
        print('That entry already exists! SQLite Error ----->',sqlError)

    else:
        pass


def db_select(c):
    select = "SELECT * FROM proddb"
    retrieve = c.execute(select)
    fulltable = c.fetchall()
    for x in fulltable:
        print(x)
    print(fulltable)

def dbremove():
    pass


def main():
    """This is the program main function"""
    print()
    print('Welcome to the Python SQLite3 Database Inventory Program!')
    print()
    print('Please make your selection from the options below:')
    print()
    print("1. Create a prod.db database")
    print("2. Insert an entry into database")
    print("3. Display the database contents")
    print("4. Remove an entry from the database")
    print("5. Exit... ")

    choice = input("Please choose between 1, 2, 3, 4, and 5: ")

    if choice == '1':
        db_create(c)

    elif choice == '2':
        serialNumber = input('Enter Serial Number: ')
        hostname = input('Enter hostname: ')
        ios = input('Enter IOS version: ')
        location = input('Enter the location: ')

        db_insert(c,serialNumber,hostname,ios,location)
        q = input("Would you like to commit these changes? ('yes' or 'no')")
        connection.commit()

    elif choice == '3':
        show_rows(c)

    elif choice == '4':
        dbremove()

    elif choice == '5':
        exit(99)



if __name__ == '__main__':
    main()
#connection.commit()
#select = "SELECT * FROM dbinventorytable"
#retrieve = c.execute(select)
#for row in retrieve:
#   print(row)

