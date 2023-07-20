from database.connection import execute_query, create_connection

def update_hero(current_name, new_name): 
    query = """
        UPDATE heroes
        SET name = %s
        WHERE name = %s
        """
    execute_query(query,(new_name, current_name))

update_hero("Slogger", "Fish")

#Add the interactive terminal stuff later. Just make sure the basic functions work first!