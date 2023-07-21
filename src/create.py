from database.connection import execute_query, create_connection

def create_hero():
    name = input("Heroes name? ")
    about_me = input("Tell me about your hero? ")
    biography = input("Write a little bio for your hero? ")
    query = """
        INSERT INTO heroes 
        VALUES (%s, %s, %s)
        """
    execute_query(query,(name, about_me, biography))

#Add the interactive terminal stuff later. Just make sure the basic functions work first!