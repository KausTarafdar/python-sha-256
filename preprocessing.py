"""
This file incorporartes the preprocessing step functions of algorithm. 
Contents:
1. message_binary() : The function takes the ascii input and converts into binary format 
for the first step of the algorithm.
2. pad() : The function takes the binary string and pads it with 0s to 512 bits. If the 
binary string is more the 512 bit, the message is up-ed to the next multiple of 512.
The last 64 bits encode the length of message in the message block.
3. blocks() : The encoded message is divided into blocks of 512 and put into the message
scheduling.
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

