def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    file = open(a,encoding='utf8')
    data = file.readlines()
    data = [data.rstrip() for data in data]
    max = len(data[0])
    i = 1
    for i in data:
        if len(i) > max:
            max = len(i)
    return max  
a = 'txt_file/data10.txt'
print(main(a))

# Read data from file