from controllers import get_todos, set_todos
from datetime import datetime
import os

FILEPATH = 'todos.txt'

if not os.path.exists(FILEPATH):
    with open(FILEPATH, 'w') as file:
        pass

while True:
    user_action = input(f"YourNote ({datetime.now().strftime("%H:%M%p")}) > ")
    user_action = user_action.strip()
    
    if user_action.startswith("add "):
        todo = user_action[4:]
        todos = get_todos(FILEPATH)
        todos.append(todo+"\n")
        set_todos(FILEPATH,todos)

    elif user_action.startswith("show"):
        todos = get_todos(FILEPATH)
        for todo_id, todo in enumerate(todos):
            print(todo_id+1,"-",todo.strip())

    elif user_action.startswith("edit "):
        try:
            number = int(user_action[5:7])
            new_todo = user_action[7:]
            todos = get_todos(FILEPATH)
            todos[number-1] = new_todo + '\n'
            set_todos(FILEPATH,todos)

        except ValueError:
            print("Invalid command.")

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos(FILEPATH)
            completed_todo = todos.pop(number-1)
            set_todos(FILEPATH,todos)
            print(f"{completed_todo.strip()} is removed from the todo list.")
        
        except ValueError:
            print("Error in value.")

        except IndexError:
            print("Error in Index.")

        except SyntaxError:
            print("LoL in Syntex")

    elif user_action.startswith("exit"):
        break

    elif user_action.startswith("help "):
        command = user_action[5:]
        if command == 'add':
            print("\n\tType 'add <your_note>' to add a new note.\n")
        elif command == 'show':
            print("\n\tType 'show' to view all todo items.\n")
        elif command == 'edit':
            print("\n\tType 'edit <number_of_old_todo> <new_note>'" 
                   " to view all todo items.\n")

    else:
        print("Invalid input.")