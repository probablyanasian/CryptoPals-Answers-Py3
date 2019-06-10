def b64tobin(b64input):
    output = ''
    b64bin = (('A','000000'),('B','000001'),('C','000010'),('D','000011'),('E','000100'),('F','000101'),('G','000110'),('H','000111'),('I','001000'),('J','001001'),('K','001010'),('L','001011'),('M','001100'),('N','001101'),('O','001110'),('P','001111'),('Q','010000'),('R','010001'),('S','010010'),('T','010011'),('U','010100'),('V','010101'),('W','010110'),('X','010111'),('Y','011000'),('Z','011001'),('a','011010'),('b','011011'),('c','011100'),('d','011101'),('e','011110'),('f','011111'),('g','100000'),('h','100001'),('i','100010'),('j','100011'),('k','100100'),('l','100101'),('m','100110'),('n','100111'),('o','101000'),('p','101001'),('q','101010'),('r','101011'),('s','101100'),('t','101101'),('u','101110'),('v','101111'),('w','110000'),('x','110001'),('y','110010'),('z','110011'),('0','110100'),('1','110101'),('2','110110'),('3','110111'),('4','111000'),('5','111001'),('6','111010'),('7','111011'),('8','111100'),('9','111101'),('+','111110'),('/','111111'))
    for char in b64input:
        try:
            output += [key[1] for key in b64bin if key[0] == char][0]
        except IndexError:
            pass
    return(output)

def bitstring_to_bytes(inpbits):
    return int(inpbits, 2).to_bytes(len(inpbits+7) // 8, byteorder='big')

def rotating_xor(inputa, inputb):
    byte = bytearray(len(inputa))
    for charnum in range(len(inputa)):
        byte[charnum] = inputa[charnum] ^ inputb[charnum%len(inputb)]
    return(byte)

def hamming_dist(inputa, inputb):
    diff = 0
    for byte in rotating_xor(inputa, inputb):
        for binary in bin(byte):
            if binary == '1':
                diff += 1
    return(diff)

filein = list(open("prob6.txt", "r"))
fileout = open("prob6.out.txt", "w")

fileincomb = b64tobin("".join(filein))
filebin = ''

