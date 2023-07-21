from database.connection import execute_query, create_connection

def read_hero():
    query = """
        SELECT name, about_me, biography FROM heroes
    """ 
    hero_info = execute_query(query).fetchall()
    
    for value in hero_info:
        name, about_me, biography = value
        print(f"Name: {name}\nAbout Me: {about_me}\nBiography: {biography}\n")
        
#Add the interactive terminal stuff later. Just make sure the basic functions work first!