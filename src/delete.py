from database.connection import execute_query, create_connection

def delete_hero(hero_name):
    query = """
        DELETE FROM heroes
        WHERE name = %s
        """
    execute_query(query,(hero_name,))

delete_hero("Ben")

#Add the interactive terminal stuff later. Just make sure the basic functions work first!