def data_reader(file_name:str):
    with open(file_name) as f:
        file_content = f.read().splitlines()
        return file_content
    
def multiply_list(myList):
    result = 1
    for x in myList:
        result *= x
    return result