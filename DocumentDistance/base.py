import math
def inner_product(L1, L2):
    """[inner product between two vectors, where vectors 
    are represented as alphabetically sorted (word, freq) pairs]
    
    [description]
    
    Arguments:
        L1 {[type]} -- [description]
        L2 {[type]} -- [description]
    """
    sum = 0.0
    i = 0
    j = 0
    while i<len(L1) and j<len(L2):
        if L1[i][0] == L2[j][0]:
            sum += L1[i][1] * L2[j][1]
            i += 1
            j += 1
        elif L1[i][0] < L2[j][0]:
            i += 1

        else:
            j += 1
    return sum

def vector_angle(L1, L2):
    numerator = inner_product(L1, L2)
    denominator = math.sqrt(inner_product(L1, L2)* inner_product(L2, L2))
    return math.cos(numerator/denominator)


    
    