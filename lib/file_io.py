def write_file(file_name, file_content):
    pass
    with open(f'{file_name}.txt', mode='w') as my_file:
        my_file.write(file_content)

def append_file(file_name, append_content):
    pass
    with open(f'{file_name}.txt', mode ='a' ) as file:
        file.write(append_content)

def read_file(file_name):
    pass
    with open(f'{file_name}.txt', mode ='r') as mine:
        my_content = mine.read()
        return my_content