# Problem Statement: Design an algorithm to encode a list of strings into a single string.
# The encoded string is then decoded back to the original list of strings.

# Examples: 
# Input: ["lint","code","love","you"]
# Encoded: "4#lint4#code4#love3#you"
# Decoded: ["lint","code","love","you"]

# Solution:-


def encode(Input):

    Encoded = ""

    for char in Input:

        length_of_input = str(len(char))    
        encode_string = "#".join([length_of_input,char])
        Encoded += encode_string
    return Encoded 

print(encode(["lint","code","love","you"]))


def decode (encoded):

    Decoded = []
    i = 0
    while i < len(encoded):
        j = i
        while encoded[j] != "#":
            j += 1
        length = int(encoded[i:j])
        word = encoded[j+1 : j+1+length]
        Decoded.append(word)
        i = j + 1 + length
    return Decoded

print(decode("4#lint4#code4#love3#you"))

