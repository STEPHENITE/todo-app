FILENAME = "todos.txt"


def get_todos(filename=FILENAME):
    with open(filename, "r") as file:
        todos = file.readlines()
        return todos

def write_todos(old_list,filename=FILENAME):
    with open(filename, "w") as file:
        file.writelines(old_list)
