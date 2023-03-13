FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ reads a text file and return the list
     of to_do items.
     """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ write a to_do items list in the text file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":   # this is use to protect any command under the if statement to run in any file where this function file is imported.
    print("Hello")
    print(get_todos())
