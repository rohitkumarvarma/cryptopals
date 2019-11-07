def repeatxor(str1,key):
    outstr = b''
    index = 0
    for string in str1:
        outstr+= bytes([string^key[index]])
        if (index+1) == len(key):
            index = 0
        else:
            index=index+1
    return outstr
def main():
    str1 = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = b"ICE"
    ciphertext = repeatxor(str1,key)
    print(ciphertext.hex())

main()
