from os import remove


def create_file(file_name):
    with open(f"./txt.files/{file_name}", 'w') as file:
        file.close()


def add_to_file(file_name, content):
    with open(f"./txt.files/{file_name}", 'a') as file:
        file.write(content + "\n")
        file.close()


def replace_to_file(file_name, old_string, new_string):
    try:
        with open(f"./txt.files/{file_name}") as file:
            string = file.read().replace(old_string, new_string)
            file.close()
            with open(f"./txt.files/{file_name}", 'w') as file:
                file.write(string)
                file.close()
    except FileNotFoundError:
        print('An error occurred')


def delete_file(file_name):
    try:
        remove(f'./txt.files/{file_name}')
    except FileNotFoundError:
        print('An error occurred')


while True:
    command = input()

    if command == 'End':
        break
    command = command.split('-')
    function, file_name = command[0], command[1]

    if function == 'Create':
        create_file(file_name)
    elif function == 'Add':
        content = command[2]
        add_to_file(file_name, content)
    elif function == 'Replace':
        old_string, new_string = command[2], command[3]
        replace_to_file(file_name, old_string, new_string)
    else:
        delete_file(file_name)
