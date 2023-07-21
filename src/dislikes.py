from database.connection import execute_query, create_connection

def add_dislikes():
    query = """
    ALTER TABLE heroes 
    ADD COLUMN likes 
    """
    execute_query(query)

add_dislikes()