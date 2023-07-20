from database.connection import execute_query, create_connection
from create import create_hero
from read import read_hero
from delete import delete_hero
from update import update_hero

def start():
    while True:
        print("""
                ____  ______ _____ _____ _   _ 
               |  _ \|  ____/ ____|_   _| \ | |
               | |_) | |__ | |  __  | | |  \| |
               |  _ <|  __|| | |_ | | | | . ` |
               | |_) | |___| |__| |_| |_| |\  |
               |____/|______\_____|_____|_| \_|
                                 
              So what are ya'll wanting to do? (Enter a number)
              
              1: Create a new hero
              2: View the heroes
              3: Update a hero
              4: Delete a hero
              5: Exit
              """)
        menu()

def menu():
    answer = input("Pick a number: ")
    if answer == "1": 
        create_hero("", "", "")
    elif answer == "2":
        read_hero()
    elif answer == "3":
        update_hero("", "")
    elif answer == "4":
        delete_hero("")
    elif answer == "5":
        print("""
             ______     ________ 
            |  _ \ \   / /  ____|
            | |_) \ \_/ /| |__   
            |  _ < \   / |  __|  
            | |_) | | |  | |____ 
            |____/  |_|  |______|
                      """)
        exit() 
    else:
        print("Nope, try again.")

if __name__ == "__main__":
    start()


