
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"     # \n is added to the code so that the data going to the text file will not be merged together, thus each item added be on different line in the text file.

            with open('todos.txt', 'r') as file:
                todos = file.readlines()                 # this will return a list of item in the file as a list of items.

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case "show":
            with open('todos.txt', 'r') as file:
                todos = file.readlines()            # file.readlines always return a list generated from the external text file. file, read will return string if it was used.i.e todos is a list in this case.

            for index, item in enumerate(todos):
                item = item.strip("\n")             # This is used to remove the \n at added to the todos list, this is neccessary because if not added the list will have unneccsary line brake. you can remove it to see the output.
                row = F"{index + 1}-{item}"
                print(row)
        case "edit":
            number = int(input("Enter the item to edit: "))
            number = number - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("what is the new item to be added: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case "complete":
            number = int(input("Number of item to complete: "))
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."

        case "exit":
            break
        case _:
            print("Kindly input either of the arguments (add, show, edit, complete or exit). Thanks")
print("bye!")





