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

import binascii
from typing import List


def fileToBinary(input_file : str) -> str :
    scale = 16
    #Convert the file to hexadecimal string
    hex_string = binascii.hexlify(input_file)
    #Convert the hexadecimal string to a binary string
    res = bin(int(hex_string, scale)).zfill(8)

    # Getting the actual hashing input string and lenght of string as binary
    hashvalue = res[2:len(res)]
    len_value = "{0:b}".format(len(hashvalue))

    return hashvalue, len_value

def input_padding(hashvalue : str, len_value : str) -> str :
    #Checking is the file length can be assigned to 64 bit binary
    if len(hashvalue) > 18446744073709551615:
        print("File cannot be processed as the length of binary file is over 64 bit")
        exit()

    #padding the length to 64 bits
    len_value = len_value.zfill(64)

    #Calculating the next multiple of 512, the string length fits into
    temp_hashvalue = hashvalue + len_value

    #Padding hashvalue and concatenating length to the end
    req_len = len(temp_hashvalue)
    if (len(temp_hashvalue)%512):
        req_len = len(temp_hashvalue) + (512 - len(temp_hashvalue) % 512)
        hashvalue = hashvalue[::-1].zfill(req_len-64)[::-1]
        hashvalue = hashvalue + len_value
        return hashvalue
    else:
        hashvalue = temp_hashvalue
        return hashvalue

def chunkinator(value : str) -> List[str]:
    n = 512
    chunks = [value[i:i+n] for i in range(0, len(value), n)]
    return chunks

