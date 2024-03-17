from typing import List

from constants import *
from sha_functions import *
from preprocessing import *

"""
A message is 32 bits long.
The messages schedule is 16 messages long. However the message schedule needs to be 64 messages long.
Therefore new messages are generated using previous bits, to get it upto 64 bits.
"""
def msgSchedule(msgBlock : str) -> List[str]:
    n = 32
    chunks = [msgBlock[i:i+n] for i in range(0, len(msgBlock), n)]
    nextChunk = ''
    for i in range(0,48):
        nextChunk = bitsum(Lsigma1(chunks[-2]),chunks[-7],Lsigma0(chunks[-15]),chunks[-16])
        chunks.append(nextChunk)
    return chunks

def compression(schedule : List[str], a : str, b : str, c : str, d : str, e : str, f : str, g : str, h : str) -> List[str]:

    #working values
    word = ''
    k = ''
    T1 = ''
    T2 = ''
    #temporary words
    for i in range(len(schedule)):   #OPERATIONS
        word = schedule[i]
        k = K_map[i]
        T1 = bitsum(Usigma1(e), choice(e, f, g), h, word, k)
        T2 = bitsum(Usigma0(a), majority(a, b, c))
        h, g, f, e, d, c, b = g, f, e, d, c, b, a
        a = bitsum(T1,T2)
        e = bitsum(e,T1)
    a = bitsum(a, S_map["a"])
    b = bitsum(b, S_map["b"])
    c = bitsum(c, S_map["c"])
    d = bitsum(d, S_map["d"])
    e = bitsum(e, S_map["e"])
    f = bitsum(f, S_map["f"])
    g = bitsum(g, S_map["g"])
    h = bitsum(h, S_map["h"])

    return [a, b, c, d, e, f, g, h]
    




    






