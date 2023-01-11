def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    file = open(a,encoding='utf8')
    data = file.read()
    data = data.rstrip()
    data = data.replace('\n','')
    list = []
    for i in data:
        if i >= '0' and i <= '9':
            list.append(i)
    max = list[0]
    i = 1
    for i in list:
        if i > max:
            max = i
    return int(max)
a = 'txt_file/data08.txt'
print(main(a))
# Read data from file