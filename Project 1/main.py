
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()               #this will return a list of item in the file as a list of items.
            file.close()
            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)                      # \n is added to the code so that the data going to the text file will not be merged together, thus each item added be on different line in the text file.
            file.close()
        case "show":
            file = open('todos.txt', 'r')
            todos = file.readlines()            #file.readlines always return a list generated from the external text file. file, read will return string if it was used.i.e todos is a list in this case.
            file.close()
            for index, item in enumerate(todos):
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
