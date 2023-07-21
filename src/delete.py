from database.connection import execute_query, create_connection

def delete_hero(hero_name): 
    hero_name = input("What is the name of the hero you want to delete? ")

    query_check = "SELECT COUNT(*) FROM heroes WHERE name = %s"
    result = execute_query(query_check, (hero_name,)).fetchone()

    if result[0] == 0:
        print("Not a valid hero name.")
        return

    query = """
        DELETE FROM heroes
        WHERE name = %s
        """
    execute_query(query, (hero_name,))

#Add the interactive terminal stuff later. Just make sure the basic functions work first!