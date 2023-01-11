def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(a,encoding = 'utf8')
    data = f.read()
    lst = data.split(',')
    i = 0
    list = []
    for i in lst:
        b = int(i)
        list.append(b)
    return list

a = 'txt_file/data01.txt'
print(main(a))





    
# Read data from file