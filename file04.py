def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    file = open(a,encoding='utf8')
    data = file.read()
    list = []
    i = 0
    num = ['0','1','2','3','4','5','6','7','8','9']
    for i in data:
        if i not in num:
            list.append(i)
    return list
a = 'txt_file/data04.txt'
print(main(a))
    
# Read data from file