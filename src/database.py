# TODO: Not currently used, research whether it makes sense to do db setup in this file or in directory_setup.py



import sqlite3

# create a connection
conn = sqlite3.connect('atracktive.db')

# create a cursor
c = conn.cursor()

# # create a table
# c.execute("""CREATE TABLE atracktive (directory)""")
c.execute("""CREATE TABLE userDirectory (directory)""")
# commit our command
conn.commit()

# close our connection
conn.close()


