def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    file = open(a,encoding='utf8')
    data = file.read()
    list = []
    i = 0
    for i in data:
        if i >= '0' and i <= '9':
            list.append(i)
    return list
a = 'txt_file/data03.txt'
print(main(a))
# Read data from file