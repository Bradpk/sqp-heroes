from database.connection import execute_query, create_connection

execute_query("SELECT * FROM heroes;")

def start():
    input("""
          So what are ya'll wanting to do? (Pick an option)
          
          1: Create a new hero
          2: View the heroes
          3: Update a hero
          4: Delete a hero
          """)
    
start()


