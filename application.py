

'''
    Calculates the result of the polynomial
    (x^12 + x^11 + x^10 + x^4 + 1)
'''
def polynomial(bitarray):

    #bit mask for bit 12
    mask = int('100000000000',2)

    if mask & bitarray == 0:
        bit12 = 0
    else:
        bit12 = 1

    #bit mask for bit 11
    mask = int('010000000000',2)

    #bit12= mask & bitarray
    if mask & bitarray == 0:
        bit11 = 0
    else:
        bit11 = 1

    #bit mask for bit 10
    mask = int('001000000000',2)

    if mask & bitarray == 0:
        bit10 = 0
    else:
        bit10 = 1

    #bit mask for bit 4
    mask = int('000000001000',2)

    if mask & bitarray == 0:
        bit4 = 0
    else:
        bit4 = 1

    ''' now we calculate the actual polynomial result '''

    result = bit12 ^ bit11
    result = result ^ bit10
    result = result ^ bit4
    result = result ^ int('1',2)


    return result



'''
    This method returns the binary result of a single step
    for the polynomial:  (x^12 + x^11 + x^10 + x^4 + 1)
'''
def step(bitarray):


    # get the polynomial result
    polynomialResult = polynomial(bitarray)


    #this is too prevent overflow of 12 bits
    mask = (2 ** 12 - 1)

    #now shift all the bits the left by 1 bit
    bitarray = (bitarray << 1) & mask

    #now place the polynomialResult the first bit position
    bitarray = bitarray | polynomialResult

    return bitarray



def test():
    bitTest1 = int('011111111111',2)

    bitTest2 = int('111111111110',2)
    print(bin(step(bitTest1)))
    print(bin(step(bitTest2)))
    print("tests")




test()