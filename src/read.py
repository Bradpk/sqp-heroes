from database.connection import execute_query, create_connection

def read_heroes():
    query = """
        SELECT name FROM heroes
    """ 
    names = execute_query(query).fetchall()
    for count, value in enumerate(names):
        print(f"{count + 1}: {value[0]}")

read_heroes()

#Add the interactive terminal stuff later. Just make sure the basic functions work first!