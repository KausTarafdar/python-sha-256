from constants import *
from sha_functions import *
from preprocessing import *

"""
A message is 32 bits long.
The messages schedule is 16 messages long. However the message schedule needs to be 64 messages long.
Therefore new messages are generated using previous bits, to get it upto 64 bits.
"""
def msgSchedule(msgBlock):
    n = 32
    print("CHUNKS : ")
    print("-"*100)
    chunks = [msgBlock[i:i+n] for i in range(0, len(msgBlock), n)]
    nextChunk = ''
    for i in range(0,48):
        nextChunk = bitsum(Lsigma1(chunks[-2]),chunks[-7],Lsigma0(chunks[-15]),chunks[-16])
        chunks.append(nextChunk)
    print("\n")
    print("Chunk : - ", chunks)
    return chunks

h0 = H(0)
h1 = H(1)
h2 = H(2)
h3 = H(3)
h4 = H(4)
h5 = H(5)
h6 = H(6)
h7 = H(7)

a, b, c, d, e, f, g, h = "", "", "", "", "", "", "", ""

def compression(block):
    #state registers
    a = H(0)
    b = H(1)
    c = H(2)
    d = H(3)
    e = H(4)
    f = H(5)
    g = H(6)
    h = H(7)

    #working values
    w = ''
    k = ''
    T1 = ''
    T2 = ''
    #temporary words
    for i in range(len(block)):   #OPERATIONS
        w = block[i]
        k = K(i)
        T1 = bitsum(Usigma1(e), choice(e, f, g), h, w, k)
        T2 = bitsum(Usigma0(a), majority(a, b, c))
        h, g, f, e, d, c, b = g, f, e, d, c, b, a
        a = bitsum(T1,T2)
        e = bitsum(e,T1)
    a = bitsum(a, h0)
    b = bitsum(b, h1)
    c = bitsum(c, h2)
    d = bitsum(d, h3)
    e = bitsum(e, h4)
    f = bitsum(f, h5)
    g = bitsum(g, h6)
    h = bitsum(h, h7)
    return [a, b, c, d, e, f, g, h]
    




    






