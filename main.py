from constants import *
from sha_functions import *
from preprocessing import *
from processing import *

#initial hash values
h0 = H(0)
h1 = H(1)
h2 = H(2)
h3 = H(3)
h4 = H(4)
h5 = H(5)
h6 = H(6)
h7 = H(7)

hashValue = input("Enter what data you want to hash: ")

'''
STEP 1: PREPARING THE DATA FOR HASHING

The message is turned into binary strings and their sizes are padded to 512 bits for
the hashing process

The message tends to be at 64 bits shorter than 512 as the last 64 bits are reserved for
the length of the messaage to be encoded in binary and added to the end of the binary  

For more than one block of 512 bits, the data is taken to the next multiple of 512 and 
broken into message blocks
'''

rawData = message_binary(hashValue)

paddedData = pad(rawData)

messageBlocks = blocks(paddedData)

""" 
STEP 2: MESSAGE SCHEDULE GENERATION

A message block is taken and then is divided into 16 bytes of 32 bits. The total
bytes in a message schedule are 64, so we create the 48 remaining bytes with the formula
next byte = σ1(t-2) + (t-7) + σ0(t-15) + (t-16)  ; where t is no. of bytes
"""

for block in messageBlocks:
    schedule = msgSchedule(block)

    """
    STEP 3: COMPRESSION OF DATA

    The message schedule is then compressed with various rotation functions onto some variables called the 
    state registers for every single message block and finally taken as hexadecimal values and concatenated
    """
    compressedValues = compression(schedule)
    h0 = compressedValues[0]
    h1 = compressedValues[1]
    h2 = compressedValues[2]
    h3 = compressedValues[3]
    h4 = compressedValues[4]
    h5 = compressedValues[5]
    h6 = compressedValues[6]
    h7 = compressedValues[7]


"""
STEP 4: MAKING THE HEXDIGEST

The values of state registers are taken and converted to hexadecimal strings. Then they are concatenated
to give us the final hex digest
"""
hexdigest = ""
for value in compressedValues:
    hexdigest += hexa(value)

print("HEXDIGEST :- ", hexdigest)    #this is the final hash digest
input("press enter to close the program")





