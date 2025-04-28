from functions import get_todos,write_todos
import time
now = time.strftime("%d-%B-%Y  %H:%M:%S")
print("For knowing the time, look down")
print("Currently its ",now)
while True:
    user_prompt = input("type add,show,edit,complete or exit :- \n").strip()
    if user_prompt.startswith("add"):
        todo = user_prompt[4:].title()
        todos = get_todos("todos.txt")
        todos.append(todo + "\n")
        write_todos(filename="todos.txt",old_list=todos)
    elif user_prompt.startswith("show"):
        todos = get_todos("todos.txt")
        for i,j in enumerate(todos):
            j = j.strip("\n")
            print(i+1,". ",j)
    elif user_prompt.startswith("complete"):
        try:
            comp_todo = int(user_prompt[9:]) - 1
            todos = get_todos("todos.txt")

            with open("todos.txt", "w") as file:
                hero = todos[comp_todo]
                todos.pop(comp_todo)
                file.writelines(todos)
                print(f"Congratulations on behalf of completion of {hero}")
        except IndexError:
            print("No Item exists with that number")
    elif user_prompt.startswith("edit"):
        try:
            todos = get_todos("todos.txt")
            for idx,i in enumerate(todos):
                i = i.strip("\n")
                print(idx+1,". ",i)
            old = int(user_prompt[5:])
            old -=1
            new_text = input("Enter the new todo :- ").title()
            todos[old] = new_text+"\n"
            write_todos(filename="todos.txt",old_list=todos)
        except ValueError:
            print("Enter a valid input")
            continue
    elif "exit" in user_prompt:
        break
print("Bye!")