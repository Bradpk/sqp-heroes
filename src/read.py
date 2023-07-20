from database.connection import execute_query, create_connection

def read_hero():
    query = """
        SELECT name, about_me, biography FROM heroes
    """ 
    hero_data = execute_query(query).fetchall()
    for count, value in enumerate(hero_data):
        name, about_me, biography = value
        print(f"{count + 1}: Name: {name}\nAbout Me: {about_me}\nBiography: {biography}\n")


#Add the interactive terminal stuff later. Just make sure the basic functions work first!