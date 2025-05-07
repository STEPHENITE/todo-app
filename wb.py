import streamlit
import streamlit as stl

import functions

todos = functions.get_todos()
def add_todo():
    other_todo = stl.session_state["new_todo"] + "\n"
    todos.append(other_todo)
    functions.write_todos(todos)

stl.title("My To-do App ")
stl.subheader("This is a todo app")
for index,i in enumerate(todos):
    checkbox = stl.checkbox(i,key=i)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del stl.session_state[i]
        streamlit.rerun()

stl.text_input(label="",placeholder="Enter a todo.......",on_change=add_todo,key="new_todo")
