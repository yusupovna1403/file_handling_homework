def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    file = open(a,encoding='utf8')
    data = file.readlines()
    list = []
    i = 0
    data = [data.rstrip() for data in data]
    for i in data:
        list.append(len(i))
    return list   
    
a = 'txt_file/data06.txt'
print(main(a))
# Read data from file