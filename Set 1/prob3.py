def single_xor(inputa, inputb):
    bin = bytearray(len(inputa))
    for charnum in range(len(inputa)):
        bin[charnum] = inputa[charnum] ^ inputb
    return(bin)

def charscore(words):
    score = 0

    try:    
        words = str.lower(str(words, "utf-8"))
    except UnicodeDecodeError:
        words = ''

    #from: https://en.wikipedia.org/wiki/Letter_frequency except for ' ', that was experimental.
    wordfreq = (('a',0.08167),('b',0.01492),('c',0.02782),('d',0.04253),('e',0.12702),('f',0.02228),('g',0.02015),('h',0.06094),('i',0.06966),('j',0.00153),('k',0.00772),('l',0.04025),('m',0.02406),('n',0.06749),('o',0.07507),('p',0.01929),('q',0.00095),('r',0.05987),('s',0.06327),('t',0.09056),('u',0.02758),('v',0.00978),('w',0.02360),('x',0.00150),('y',0.01974),('z',0.00074),(' ',0.28040))

    for char in words:
        try:
            score += [key[1] for key in wordfreq if key[0] == char][0]
        except IndexError:
            pass
    
    return(score)

inpa = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

hs = 0
for i in range(255):
    inpb = i
    words = bytes(single_xor(inpa, inpb))
    if charscore(words) >= hs:
        svword = words
        hs = charscore(words)

print(svword, hs)