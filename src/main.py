from database.connection import execute_query, create_connection


execute_query("SELECT * FROM heroes;")

def test():
    print("""HI ME OLD MATE""")

test()

def start():
    print("""
          1: Create
          2: Read
          3: Update
          4: Delete
          """)
    
start()
#------------------------
