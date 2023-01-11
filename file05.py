def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    file = open(a,encoding='utf8')
    data = file.read()
    list = []
    i = 0
    num = 0
    str = 0
    data = data.rstrip()
    for i in data:
        if i >= '0' and i <= '9':
            num+=1
        else:
            str+=1
    list.append(num)
    list.append(str)
    return list
a = 'txt_file/data05.txt'
print(main(a))
# Read data from file