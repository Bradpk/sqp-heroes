from database.connection import execute_query, create_connection

def create_hero(name, about_me, biography):
    name = input("Hero's name? ")
    about_me = input("Tell me about your hero? ")
    biography = input("Write a little bio? ")
    query = """
        INSERT INTO heroes (name, about_me, biography)
        VALUES (%s, %s, %s)
        """
    execute_query(query,(name, about_me, biography))

create_hero("Clayton", "Me Little Strong", "Grocery Manager")

#Add the interactive terminal stuff later. Just make sure the basic functions work first!