todos = []
while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "edit":
            number = int(input("Enter the item to edit: "))
            number = number - 1
            new_todo = input("what is the new item to be added: ")
            todos[number] = new_todo
        case "exit":
            break
        case _:
            print("Kindly input either of the arguments (add, show or exit). Thanks")
print("bye!")
