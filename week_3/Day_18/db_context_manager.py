import sqlite3
from typing import Any
from schemas import ShipmentCreate, ShipmentUpdate



class Database:
        def connect_to_db(self):
                #making the connnection wiht database
                
                self.conn = sqlite3.connect("sqlite.db", check_same_thread=False)
                # Get cursor to execute queries and fetch data
                self.cur = self.conn.cursor()
                print("connected to sqlite.db")


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
                # Only include fields the client actually provided
                fields = shipment.model_dump(exclude_unset=True)

                if not fields:
                        # Nothing to update, just return the current row (or None)
                        return self.get(id)

                # Build the SET clause dynamically from the provided fields
                set_clause = ", ".join(f"{field} = :{field}" for field in fields)

                self.cur.execute(f"""
                        UPDATE shipment SET {set_clause}
                        WHERE id = :id
                """,
                        {
                                "id": id,
                                **fields
                        }
                )
                self.conn.commit()

                return self.get(id)

        def delete(self, id:int):
                self.cur.execute("""
                        DELETE FROM shipment
                        WHERE id = ?
                        """, (id,))
                self.conn.commit()

        def close(self):
              print("Connection closed...")
              self.conn.close()
              
        def __enter__(self):
                print("Entering the Context")
                self.connect_to_db()
                self.create_table()
                return self
        
        def __exit__(self, *arg):
                print("Exit the context")
                self.close()


#Usage
with Database() as db:
        print(db.get(12701))
        print(db.get(12702))     