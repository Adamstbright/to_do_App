
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"     # \n is added to the code so that the data going to the text file will not be merged together, thus each item added be on different line in the text file.

            file = open('todos.txt', 'r')
            todos = file.readlines()               # this will return a list of item in the file as a list of items.
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case "show":
            file = open('todos.txt', 'r')
            todos = file.readlines()            # file.readlines always return a list generated from the external text file. file, read will return string if it was used.i.e todos is a list in this case.
            file.close()

            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip("\n")             # This is used to remove the \n at added to the todos list, this is neccessary because if not added the list will have unneccsary line brake. you can remove it to see the output.
                row = F"{index + 1}-{item}"
                print(row)
        case "edit":
            number = int(input("Enter the item to edit: "))
            number = number - 1
            new_todo = input("what is the new item to be added: ")
            todos[number] = new_todo
        case "complete":
            number = int(input("Number of item to complete: "))
            todos.pop(number - 1)
        case "exit":
            break
        case _:
            print("Kindly input either of the arguments (add, show, edit, complete or exit). Thanks")
print("bye!")





