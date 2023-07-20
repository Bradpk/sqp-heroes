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
def get_all_heroes():
    query = """
        SELECT name FROM heroes
    """ 
    names = execute_query(query).fetchall()
    for count, value in enumerate(names):
        print(f"{count + 1}: {value[0]}")

get_all_heroes()

#------------------------
