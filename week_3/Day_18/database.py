import sqlite3
import os
from unittest import result

connection = sqlite3.connect("sqlite3.db")

cursor = connection.cursor()


def create_table(self, name:str):


# 1. Creat a table with columns
                self.cur.execute("""
                        CREATE TABLE IF NOT EXISTS ?
                                (id INTEGER PRIMARY KEY,
                                content TEXT,
                                weight REAL,
                                destination TEXT,
                                status TEXT)
                        """)


#DELETINg the whole database:----------------------------
# cursor.execute("DROP TABLE shipment")
# connection.commit()


#2. Add the shipment data :-
# insert values in the table
# cursor.execute("""
#     INSERT INTO shipment VALUES
#     (12701, 'metal gears', 12, 'New York', 'placed'),
#     (12702, 'plam trees', 20, 'California', 'placed'),
#     (12703, 'plastic chairs', 15, 'Texas', 'placed'),
#     (12704, 'wooden tables', 25, 'Florida', 'placed'),
#     (12705, 'glass bottles', 10, 'Nevada', 'placed')
#     """)

#commit the changes to the database
# connection.commit()




# # To show all data in the table:
# cursor.execute("SELECT * FROM shipment")
# print(cursor.fetchall())

# 3. Read the shipment by ID;
# cursor.execute("""
#                SELECT * FROM shipment 
#                """)
# result = cursor.fetchmany(2)
# cursor.execute("""
#                SELECT * FROM shipment WHERE id = 12702 
#                """)
# result= cursor.fetchone()
# print(result)
# abc=cursor.execute("""
#                 SELECT id,status FROM shipment
#                WHERE content = 'plam trees'
#                """)
# efg=cursor.fetchall()
# print(efg)


# 4. DELETE A SHIPMENT:

# cursor.execute(""" DELETE FROM shipment
#                 WHERE id = 12705""")

# connection.commit()
# result = cursor.fetchone()

# # 4. Update the shipment:--------------------(it will update all the values in the datatbase)
# cursor.execute("""
# UPDATE shipment SET status = "in_transit" 
# connection.commit()
# WHERE id = 12703
# """)

# connection.commit()

# # For changing a single value we have to use Query Parameter.
# id = 1001
# status= "out_of_delivery"
# cursor.execute("""
#          UPDATE shipment SET status = ?
#                WHERE id =?
#                """, (status, id))

# connection.commit()

#6. Delete ashipment by it's ID:
cursor.execute("""
DELETE FROM shipment
                WHERE id = 12704 """)

connection.commit()
# Finally, to cloas the connection when done:
connection.close()