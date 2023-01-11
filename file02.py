def main(data:str):
    """
    The data:str is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    
    file = open('txt_file/data02.txt','r')
    data = file.read()
    return len(data)
    file.close()

a = 'txt_file/data02.txt'
print(main(a))

    
    
    

# Read data from file