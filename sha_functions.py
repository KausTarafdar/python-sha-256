"""
Following are the sha_functions required during the SHA256 encoding process.
"""


"""PRIMITIVE FUNCTIONS :-"""
"""----------------------------------------------------------------------------------------------------------------------------------------"""
"""
{*} Bit Rotation : Rotates the bits in the binary string. The w value determines how many times the bits are rotated
"""

def rotr(w : str, initial : int) -> str:                   
    workingInitial = str(initial)
    l = []
    final = ""
    for i in workingInitial:
        l.append(i)
    l.reverse()
    for i in range(0, w):
        val = l.pop(0)
        l.append(val)
    l.reverse()
    for i in l:
        final += i
    #print(f"rotr{w} : ", final)
    return final


"""
{*} Bit Shift : The Bits are shifted and replaced with 0s. The w value determines how many times the bits are shifted
"""
def shr(w : str, initial : int) -> str:                   
    workingInitial = str(initial)
    l = []
    final = ""
    for i in workingInitial:
        l.append(i)
    newList = []
    if w >= len(workingInitial):
        for i in workingInitial:
            newList.append("0")
    else:
        for i in range(0, w):
            newList.append("0")
        for i in range(0, len(l) - w):
            newList.append(l[i])
    for i in newList:
        final += i
    #print(f"shr{w} : ", final)
    return final


"""
{*} XOR : Basic binary xor for 3 bits
"""
def xor(arg1 : str, *argv : str) -> str:                    
    for arg in argv:
        wval1, wval2 = str(arg1), str(arg)
        if len(wval1) != len(wval2):
            diff = abs(len(wval1)-len(wval2))
            if len(wval1) > len(wval2):
                wval2 = "0"*diff + wval2
            elif len(wval2) > len(wval1):
                wval1 = "0"*diff + wval1
        xorSum = ""
        for i in range(len(wval2)):
            if (wval1[i] == '0' and wval2[i] == '0') or (wval1[i] == '1' and wval2[i] == '1'):
                xorSum += "0"
            else:
                xorSum += "1" 
        arg1 = xorSum
    #print("xor : ", xorSum)
    return xorSum


"""
{*} Binary Sum : Basic binary addition function for 3 bits
"""
def bitsum(arg1 : str, *argv : str) -> str:                     
    newarg = ""
    for arg in argv:
        l1, l2 = [], []
        warg1, warg = str(arg1), str(arg)
        if len(warg1) != len(warg):
            diff = abs(len(warg1)-len(warg))
            if len(warg1) > len(warg):
                warg = "0"*diff + warg
            elif len(warg) > len(warg1):
                warg1 = "0"*diff + warg1
        for i in range(len(warg1)):
            l1 += warg1[i]
            l2 += warg[i]
        l1.reverse()
        l2.reverse()
        add = []
        carry = "0"
        for i in range(len(l1)):
            if (l1[i] == "0" and l2[i] == "0" and carry == "0"):
                add.append("0")
                carry = "0"
            elif (l1[i] == "1" and l2[i] == "0" and carry == "0") or (l1[i] == "0" and l2[i] == "1" and carry == "0") or (l1[i] == "0" and l2[i] == "0" and carry == "1"):
                add.append("1")
                carry = "0"
            elif (l1[i] == "1" and l2[i] == "1" and carry == "0") or (l1[i] == "0" and l2[i] == "1" and carry == "1") or (l1[i] == "1" and l2[i] == "0" and carry == "1"):
                add.append("0")
                carry = "1"
            elif (l1[i] == "1" and l2[i] == "1" and carry == "1"):
                add.append("1")
                carry = "1"
        if carry == "1":
            add.append("1")
        add.reverse()
        for i in add:
            newarg += i
        if len(newarg) < 32:
            newarg = "0"*(abs(len(newarg)-32)) + newarg
        if len(newarg) > 32:
            difference = abs(len(newarg) - 32)
            newarg = newarg[difference:len(newarg)]
        arg1 = newarg
    #print("binary sum : ", newarg)
    return newarg

"""--------------------------------------------------------------------------------------------------------------------------------------"""

"""
{*} SIGMA FUNCTIONS
----------------------------------------------------------------------------------------------------
|  -  The following functions handle complex rotations and shifts.                                 |
|  -  All Sigma functions are a combination of the primitive rotation, shift and bitwise Xor       |
|     functions with initial inputs for the operations.                                            |
----------------------------------------------------------------------------------------------------
"""

def Lsigma0(x : str) -> str:
    rotr7 = rotr(7, x)
    rotr18 = rotr(18, x)
    shr3 = shr(3, x)
    value = xor(rotr7, rotr18, shr3)
    #print("σ0 : ", value)
    return value



def Lsigma1(x : str) -> str:
    rotr17 = rotr(17, x)
    rotr19 = rotr(19, x)
    shr10 = shr(10, x)
    value = xor(rotr17, rotr19, shr10)
    #print("σ1 : ", value)
    return value



def Usigma0(x : str) -> str:
    rotr2 = rotr(2, x)
    rotr13 = rotr(13, x)
    rotr22 = rotr(22, x)
    value = xor(rotr2, rotr13, rotr22)
    #print("Σ0 : ", value)
    return value



def Usigma1(x : str) -> str:
    rotr6 = rotr(6, x)
    rotr11 = rotr(11, x)
    rotr25 = rotr(25, x)
    value = xor(rotr6, rotr11, rotr25)
    #print("Σ1 : ", value)
    return value

"""
{*} CHOICE
-------
Chooses between y and z value based on the value of the x. If x = 1, y is chosen. If x = 0, z is chosen.
Example :-
1 0 1 1
0 0 1 0
1 0 0 1
-------
0 0 1 0 => Answer
"""

def choice(x : str, y : str, z : str) -> str:
    final = ''
    for i in range(len(x)):
        if x[i] == "1":
            final += y[i]
        else:
            final += z[i]
    #print("choice : ", final)
    return final 

"""
{*} MAJORITY 
---------
Checks the majority of 3 bits in a column and sets the output to the majority bit
Example :-
1 0 1 0 1
1 0 1 1 0
1 0 1 0 0
---------
1 0 1 0 1 => Answer
"""
def majority(x : str, y : str,z : str) -> str:
    final = ''
    for i in range(len(y)):
        sum = 0
        sum = int(x[i]) + int(y[i]) + int(z[i])
        if sum >= 2:
            final += "1"
        else: 
            final += "0"
    #print("majority : ", final)
    return final

"""
{*} Hexadecimal : The Binary bit streams are converted to hexadecimal
"""
def hex_string(value : str) -> str:
    value = int(value, 2)
    value = hex(value)
    value = value[2:len(value)]
    print("hexadecimal value : ", value)
    return value

