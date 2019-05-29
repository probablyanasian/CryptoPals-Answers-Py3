def hextobin(hexinput):
    hexinput = str(hexinput)
    output = ''
    hexbin = (('0','0000'),('1','0001'),('2','0010'),('3','0011'),('4','0100'),('5','0101'),('6','0110'),('7','0111'),('8','1000'),('9','1001'),('a','1010'),('b','1011'),('c','1100'),('d','1101'),('e','1110'),('f','1111'))
    for hexa in hexinput:
        try:
            hexa = str.lower(hexa)
        except TypeError:
            pass
        output = output + str([key[1] for key in hexbin if key[0] == hexa][0])
    return(output)

def bintohex(bininput):
    bininput = str(bininput)
    output = ''
    hexbin = (('0','0000'),('1','0001'),('2','0010'),('3','0011'),('4','0100'),('5','0101'),('6','0110'),('7','0111'),('8','1000'),('9','1001'),('a','1010'),('b','1011'),('c','1100'),('d','1101'),('e','1110'),('f','1111'))
    split = [bininput[i:i+4] for i in range(0, len(bininput), 4)]
    for fourbin in split:
        output = output + str([key[0] for key in hexbin if key[1] == fourbin][0])
    return(output)

def xor(inputa, inputb):
    bin = ''
    for charnum in range(len(inputa)):
        bin = bin + str(int(inputa[charnum]) ^ int(inputb[charnum]))
    return(bin)

inpa = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
inpb = '88888888888888888888888888888888888888888888888888888888888888888888'

print(bintohex(xor(hextobin(inpa), hextobin(inpb))))