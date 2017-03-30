byteMap = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J",
10: "K", 11: "L", 12: "M", 13: "N", 14: "O", 15: "P", 16: "Q", 17: "R", 18: "S", 19: "T",
20: "U", 21: "V", 22: "W", 23: "X", 24: "Y", 25: "Z", 26: "a", 27: "b", 28: "c", 29: "d",
30: "e", 31: "f", 32: "g", 33: "h", 34: "i", 35: "j", 36: "k", 37: "l", 38: "m", 39: "n",
40: "o", 41: "p", 42: "q", 43: "r", 44: "s", 45: "t", 46: "u", 47: "v", 48: "w", 49: "x",
50: "y", 51: "z", 52: "0", 53: "1", 54: "2", 55: "3", 56: "4", 57: "5", 58: "6", 59: "7",
60: "8", 61: "9", 62: "+", 63: "/"}

def hexToBase64(hexStr):
    if (len(hexStr) < 2):
        return "===="
    arr = bytearray.fromhex(hexStr)
    full = ""
    maxIndex = len(arr)
    curStart = 0
    curEnd = 3 
    while(curEnd <= maxIndex):
        full += hexToBase64Helper(arr[curStart:curEnd])
        curStart = curEnd
        curEnd = curStart + 3
    if (curStart != maxIndex):
        full += hexToBase64Helper(arr[curStart:])
    return full
    
def hexToBase64Helper(byt):
    first = findBase64Str(byt[0] >> 2)
    if (len(byt) == 1):
        second = findBase64Str((byt[0] & 3) << 4)
        return first + second + "=="
    if (len(byt) == 2):
        second = findBase64Str(((byt[0] & 3) << 4) | byt[1] >> 4)
        third = findBase64Str((byt[1] & 15) << 2) 
        return first + second + third + "="
    if (len(byt) == 3):
        second = findBase64Str(((byt[0] & 3) << 4) | byt[1] >> 4)
        third = findBase64Str(((byt[1] & 15) << 2) | byt[2] >> 6) 
        fourth = findBase64Str(byt[2] & 63)
        return first + second + third + fourth

def findBase64Str(byt):
    return byteMap[byt]
    


