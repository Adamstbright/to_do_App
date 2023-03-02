

todos = []
while True:
    user_action  = input("Type add, show or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "exit":
            break
        case _:
            print("Kindly input either of the arguments (add, show or exit). Thanks")
print("bye!")




