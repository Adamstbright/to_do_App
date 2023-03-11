def get_todos(filepath='todos.txt'):
    """ reads a text file and return the list
     of to_do items.
     """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """ write a to_do items list in the text file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):

        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos(todos)

    elif user_action.startswith("show"):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")  # This is used to remove the \n at added to the todos list, this is neccessary because if not added the list will have unneccsary line brake. you can remove it to see the output.

            row = F"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            number = number - 1

            todos = get_todos()

            new_todo = input("what is the new item to be added: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print("Your command is not valid. please input >> edit follow by the serial number of todo to edit")
            continue


    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
        except IndexError:
            print("There is no item with that number !")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("You have entered a wrong command")

print("bye!")
