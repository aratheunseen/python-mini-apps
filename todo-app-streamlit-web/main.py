import streamlit as st
from controllers import get_todos, set_todos

FILEPATH = 'todos.txt'

st.title('YourNote')
st.write('Welcome to YourNote, a simple note taking app.')

todos = get_todos(FILEPATH)

def add_todo():
    new_todo = st.session_state['new_todo']
    todos.append(new_todo+'\n')
    set_todos(FILEPATH,todos)
    st.session_state['new_todo'] = ''

def delete_todo():
    for todo in todos:
        if st.session_state[todo]:
            todos.remove(todo)
            set_todos(FILEPATH,todos)

for id,todo in enumerate(todos):
    st.checkbox(todo,on_change=delete_todo,key=todo)

st.text_input("",placeholder="Add a todo",on_change=add_todo,key='new_todo')