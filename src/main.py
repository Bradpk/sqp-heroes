from database.connection import execute_query, create_connection
from create import create_hero
from read import read_hero
from delete import delete_hero
from update import update_hero

execute_query("SELECT * FROM heroes;")

def start():
    input("""
          So what are ya'll wanting to do? (Pick an option)
          
          1: Create a new hero
          2: View the heroes
          3: Update a hero
          4: Delete a hero
          """)
    input_menu()
start()


def input_menu():
    answer = input(" Pick a number ")
    if answer == "1": 
        create_hero()
    elif answer == "2":
        read_hero()
    elif answer == "3":
        update_hero()
    elif answer == "4":
        delete_hero()

