from database.connection import execute_query, create_connection

def delete_hero(hero_name): 
    hero_name = input("What is the name of the hero you want to delete? ")
    query = """
        DELETE FROM heroes
        WHERE name = %s
        """
    execute_query(query,(hero_name,))

#Add the interactive terminal stuff later. Just make sure the basic functions work first!