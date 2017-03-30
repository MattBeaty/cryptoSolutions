def fixedXOR(firstHexStr, secondHexStr):
    str = ""
    
    for i in range(len(firstHexStr)):
        a = int(firstHexStr[i], 16)
        b = int(secondHexStr[i], 16)
        c = a ^ b
        str += format(c, 'x')
    return str
        
