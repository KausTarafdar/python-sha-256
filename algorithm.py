from tqdm import tqdm
import ntpath

from constants import *
from sha_functions import *
from preprocessing import *
from processing import *


def py_SHA256(path : str) -> str :

    input_file = open(path, "rb")

    input_string = input_file.read()

    output_file = open("output.txt", "w+")

    output_file.write(f"File hashed = {ntpath.basename(path)}\n\n")

    hashValue = input_string

    '''
    STEP 1: PREPARING THE DATA FOR HASHING

    The message is turned into binary strings and their sizes are padded to 512 bits for
    the hashing process.

    The message tends to be at 64 bits shorter than 512 as the last 64 bits are reserved for
    the length of the messaage to be encoded in binary and added to the end of the binary.  

    For more than one block of 512 bits, the data is taken to the next multiple of 512 and 
    broken into message blocks.
    '''

    hashValue, bin_length = fileToBinary(hashValue)

    hashValue = input_padding(hashValue, bin_length)

    messageBlocks = chunkinator(hashValue)

    """ 
    STEP 2: MESSAGE SCHEDULE GENERATION

    A message block is taken and then is divided into 16 messages of 32 bits. The total
    messages in a message schedule is 64, so we create the 48 remaining bytes with the formula
    next message = σ1(t-2) + (t-7) + σ0(t-15) + (t-16); where t is index of message.
    """

    a = S_map["a"]
    b = S_map["b"]
    c = S_map["c"]
    d = S_map["d"]
    e = S_map["e"]
    f = S_map["f"]
    g = S_map["g"]
    h = S_map["h"]

    for block in tqdm(messageBlocks):
        schedule = msgSchedule(block)

        """
        STEP 3: COMPRESSION OF DATA

        The message schedule is then compressed with various rotation functions onto some variables 
        called the state registers for every single message block and finally taken as hexadecimal 
        values and concatenated.
        """

        compressedValues = compression(schedule, a, b, c, d, e, f, g, h)
        
        a, b, c, d, e, f, g, h = map(str, compressedValues)
        

    """
    STEP 4: MAKING THE HEXDIGEST

    The values of state registers are taken and converted to hexadecimal strings. Then they are 
    concatenated to give us the final hex digest.
    """
    hex_digest = ""
    for idx, value in enumerate(compressedValues):
        hex_val = hex_string(value)
        if len(hex_string) != 8:
            hex_val.zfill(8)
        output_file.write(f"H{idx} : {value} => {hex_val}\n")
        hex_digest += hex_val
    
    output_file.write(f"\nHexDigest or SHA265 encoded string :- {hex_digest}")

    input_file.close()
    output_file.close()

    print("Your String has been Successfully Hashed")




