from database.connection import execute_query, create_connection

def update_hero(): 
    current_name = input("What is the name of the hero you want to update? ")
    new_name = input("What do you want their new name to be? ")

    check = "SELECT COUNT(*) FROM heroes WHERE name = %s"
    result = execute_query(check, (current_name,)).fetchone()

    if result[0] == 0:
        print("Not a valid hero name.")
        return

    query = """
        UPDATE heroes
        SET name = %s
        WHERE name = %s
        """
    execute_query(query, (new_name, current_name))
    
#Add the interactive terminal stuff later. Just make sure the basic functions work first!