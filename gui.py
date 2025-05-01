import functions
import FreeSimpleGUI as sg
label = sg.Text("Type in a Task")
input_box = sg.InputText(tooltip="Enter todo",key="add_todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),
                      key="edit_todo",
                      enable_events=True,
                      size=[45, 10])
edit_button = sg.Button("Edit")
del_button = sg.Button("Completed")
window = sg.Window("TO-DO APP",
                   layout=[[label],[input_box],[add_button,edit_button,del_button],[list_box]],
                   font=("Ember", 20))

while True:
    event, value = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = value["add_todo"]+"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["edit_todo"].update(values=todos)
        case sg.WIN_CLOSED:
            break
        case "Edit":
            todo_to_edit = value["edit_todo"][0]
            print(todo_to_edit)
            new_todo = value["add_todo"]
            print(new_todo)
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
            window["edit_todo"].update(values=todos)
        case "Completed":
            todo_to_remove = value["edit_todo"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_remove)
            functions.write_todos(todos)
            window["edit_todo"].update(values=todos)
        case "edit_todo":
            window["add_todo"].update(value=value['edit_todo'][0])



    print(event)
    print(value)
window.close()