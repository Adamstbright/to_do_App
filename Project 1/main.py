def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):

        todo = user_action[4:]

        todos = get_todos('todos.txt')

        todos.append(todo + "\n")

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("show"):

        todos = get_todos('todos.txt')

        for index, item in enumerate(todos):
            item = item.strip(
                "\n")  # This is used to remove the \n at added to the todos list, this is neccessary because if not added the list will have unneccsary line brake. you can remove it to see the output.

            row = F"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            number = number - 1

            todos = get_todos('todos.txt')

            new_todo = input("what is the new item to be added: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid. please input >> edit follow by the serial number of todo to edit")
            continue


    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos('todos.txt')

            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
        except IndexError:
            print("There is no item with that number !")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("You have entered a wrong command")

print("bye!")
