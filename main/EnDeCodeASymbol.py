import math
def FindER(m):
    '''
    @param m: the size of input symbol sources
    '''
    e = math.floor(math.log2(m))
    r = m-(2**e)
    return [e, r]

def Encode(e, r, k):
    '''
    @param k: the numerical order of ak in input symbol sources {a1, a2, ..., ak,..., am}
    @return: the binary string encoded of ak
    '''
    if(1 <= k <= 2*r) :
        # ak = k-1 using e+1 bit
        return '{0:b}'.format(k-1).zfill(e+1)
    else:
        # ak = k-r-1 using e bit
        return '{0:b}'.format(k - r - 1).zfill(e)
        
def Decode(e, r, encodedArray):
    '''
    @param encodedArray: the binary array encoded
    @return p: the symbol being decoded
    '''
    p = int("".join(encodedArray[:e]), 2)
    if(p < r): 
        p = int("".join(encodedArray[:e+1]), 2) + 1
        del encodedArray[:e+1]
    else:
        del encodedArray[:e]
        p = p + r + 1
    return p