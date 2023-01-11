def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    file = open(a,encoding='utf8')
    data = file.read()
    data = data.rstrip()
    data = data.replace('\n','')
    sum = 0
    for i in data:
        if i >= '0' and i <= '9':
            sum+=int(i)
    return sum
a = 'txt_file/data07.txt'
print(main(a))
# Read data from file