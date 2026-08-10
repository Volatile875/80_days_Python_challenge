import sqlite3
import os
from typing import Any
from unittest import result
from schemas import ShipmentCreate, ShipmentUpdate


class Database:
        def __init__(self):
                #making the connnection wiht database
                self.conn = sqlite3.connect("sqlite.db", check_same_thread=False)
                # Get cursor to execute queries and fetch data
                self.cur = self.conn.cursor()
                #Create the table if not exists
                self.create_table()


        def create_table(self):
        # 1. Creat a table with columns
                self.cur.execute("""
                        CREATE TABLE IF NOT EXISTS shipment (
                                id INTEGER PRIMARY KEY,
                                content TEXT,
                                weight REAL,
                                destination TEXT,
                                status TEXT
                        )
                """)
        def create(self, shipment: ShipmentCreate) -> int:
                #Find a new ID
                self.cur.execute("SELECT MAX(id) FROM shipment")
                result = self.cur.fetchone()

                if result[0] is None:
                        new_id = 1
                else:
                        new_id = result[0] + 1

                        # Insert values in the table 
                self.cur.execute("""
                        INSERT INTO shipment
                        VALUES (:id, :content, :weight,:destination , :status) 
                        """,
                        {
                                "id": new_id,
                                **shipment.model_dump(),
                                "status": "placed",
                        }       
                )
                self.conn.commit()

                return new_id


        def get(self, id: int) -> dict[str, Any] | None:
                self.cur.execute("""
                        SELECT * FROM shipment
                        WHERE id = ?
                        """, (id, ))
                row = self.cur.fetchone()

                if row is None:
                        return None
                
                return {
                        "id": row[0],
                        "content": row[1],
                        "weight": row[2],
                        "destination": row[3],
                        "status": row[4]
                }

        def update(self,id: int, shipment: ShipmentUpdate) -> dict[str, Any] | None:
                # Update the shipment with given id
                self.cur.execute("""
                        UPDATE shipment SET status = :status
                        WHERE id = :id
                """, 
                        {
                                "id": shipment_id,
                                **shipment.model_dump()
                        }
                )
                self.conn.commit()

                return self.get(shipment_id)

        def delete(self, id:int):
                self.cur.execute("""
                        DELETE FROM shipment
                        WHERE id = ?
                        """, (id,))
                self.conn.commit()

        def close(self):
              self.conn.close()
                
               

#DELETINg the whole database:----------------------------
# self.cur.execute("DROP TABLE shipment")
# self.conn.commit()


#2. Add the shipment data :-
# insert values in the table
# self.cur.execute("""
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
# abc=cursor.execute("":
# "
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

# #6. Delete ashipment by it's ID:
# cursor.execute("""
# DELETE FROM shipment
#                 WHERE id = 12704 """)

# connection.commit()
# # Finally, to cloas the connection when done:
# connection.close()