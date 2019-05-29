def rotating_xor(inputa, inputb):
    byte = bytearray(len(inputa))
    for charnum in range(len(inputa)):
        byte[charnum] = inputa[charnum] ^ inputb[charnum%len(inputb)]
    return(byte)

lines = [
    "Burning 'em, if you ain't quick and nimble\n",
    "I go crazy when I hear a cymbal",
]

text = "".join(lines)
bytetext = bytes(rotating_xor(bytes(text,'ascii'), bytes('ICE','ascii')))
print(bytetext.hex())