"""
This file incorporartes the preprocessing step functions of algorithm. 
Contents:
1. message_binary() :
2. pad() :
3. blocks() :
"""


def message_binary(value):
    str_value = str(value)
    valueStr = ""
    for i in str_value:
        if i.isnumeric():
            i = bin(ord(i))
            valueStr += ("0" + i[2:len(i)])
        else:
            i = bin(ord(i))
            valueStr += ("0" + i[2:len(i)])
    print("Binary form of message :- \n", "\n", valueStr)
    return valueStr

def pad(value):
    length = len(value)
    len_binary = bin(length)
    strBinary = str(len_binary)
    strBinary = "0" + strBinary[2:len(len_binary)]
    paddedValue = ""
    if length < 512:
        paddedValue = value + "1"
        while len(paddedValue) < 448:
            paddedValue += "0"
        while len(strBinary) < 64:
            strBinary = "0" + strBinary
        paddedValue += strBinary
    if length > 512:
        multiple = (length//512) + 1
        variablePadding = (512 * multiple) - 64
        paddedValue = value + "1"
        while len(paddedValue) < variablePadding:
            paddedValue += "0"
        while len(strBinary) < 64:
            strBinary = "0" + strBinary
        paddedValue += strBinary
    print("Padding the value to multiple of 512 bytes : ", paddedValue)
    return paddedValue

def blocks(value):
    n = 512
    chunks = [value[i:i+n] for i in range(0, len(value), n)]
    print("The different chunks are : \n", chunks)
    return chunks

