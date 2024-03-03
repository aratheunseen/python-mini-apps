def get_todos(filepath):
    """ Read a text file and return the list of todos from the file. """
    with open(filepath, 'r') as get_file:
        todos_loc = get_file.readlines()
    return todos_loc

def set_todos(filepath,todos):
    """ Write the todo items list int the text file. """
    with open(filepath, 'w') as set_file:
        set_file.writelines(todos)