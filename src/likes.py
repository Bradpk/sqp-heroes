from database.connection import execute_query, create_connection

def add_likes():
    query = """
    ALTER TABLE heroes 
    ADD COLUMN likes 
    """
    execute_query(query)

add_likes()