from controllers import get_todos, set_todos
import PySimpleGUI as sg
import os

FILEPATH = 'todos.txt'

if not os.path.exists(FILEPATH):
    with open(FILEPATH, 'w') as file:
        pass

# Declare Variables
label = sg.Text('To-do(s): ', justification='left', font=('Open Sans', 16), size=(51, 1))
input = sg.InputText(tooltip='Type a todo', size=(51, 1), background_color='lightgrey', key='todo')
add_button = sg.Button('Add', size=(14, 1), button_color=('white', 'green'))
edit_button = sg.Button('Edit', size=(14, 1), button_color=('white', 'darkblue'))
complete_button = sg.Button('Complete', size=(12, 1), button_color=('white', 'red'))

listbox = sg.Listbox(get_todos('todos.txt'), size=(50, 10), key='todos', enable_events=True, background_color='lightgrey', font=('Open Sans', 16))
sg.set_options(font=('Open Sans', 16))

# Define Layout
layout = [
    [label],
    [listbox],
    [input],
    [add_button, edit_button, complete_button],
]

# Create Window
window = sg.Window('YourNote', layout, margins=(10, 10), element_justification='center')

# Event Loop
while True:
    todos = get_todos('todos.txt')
    event, value = window.read()

    if event == 'todos':
        val = value['todos'][0].strip("\n")
        window['todo'].update(value=val)
    
    elif event == "Add":
        new_todo = value['todo'] + '\n'
        print(value)
        todos.append(new_todo)
        set_todos('todos.txt', todos)
        window['todos'].update(values=todos)
        window['todo'].update(value='')

    elif event == 'Edit':
        index = todos.index(value['todos'][0])
        todos[index] = value['todo'] + '\n'
        set_todos('todos.txt', todos)
        window['todos'].update(values=todos)
        window['todo'].update(value='')

    elif event == 'Complete':
        select_to_check = value['todos'][0]
        todos.remove(select_to_check)
        set_todos('todos.txt', todos)
        window['todos'].update(values=todos)
        window['todo'].update(value='')
    
    elif event == sg.WIN_CLOSED:
        break

    else:
        print('Event not found')
        
window.close()
