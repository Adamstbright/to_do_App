# from functions import get_todos, write_todos

import functions  # another way of importing functions.
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):

        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")  # This is used to remove the \n at added to the todos list, this is necessary
            # because if not added the list will have unnecessary line brake. you can remove it to see the output.

            row = F"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            number = number - 1

            todos = functions.get_todos()

            new_todo = input("what is the new item to be added: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid. please input >> edit follow by the serial number of todo to edit")
            continue


    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
        except IndexError:
            print("There is no item with that number !")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("You have entered a wrong command")

print("bye!")
