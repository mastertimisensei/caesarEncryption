#caesar encryption
# Takes two argument, a string message and an integer key
def caesar_encryption(message, key):
    #create an empty string t
    t=""
    #create a for loop which goes through every character and encrypts it with the key
    #it encrypt the character by shifting their ascii code forward key number of times and
    #converting it back to character and appending it to t
    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            t += chr((ord(char) + key - 65) % 26 + 65)
        else:
            t += chr((ord(char) + key - 97) % 26 + 97)
    #return t (which is the encrypted message)
    return t

#caesar decryption
# Takes two argument, a string cipher and an integer key
def caesar_decryption(message, key):
    # create an empty string t
    t=""
    # create a for loop which goes through every character and decrypts it with the key
    # it decrypt the character by shifting their ascii code forward key number of times and
    # converting it back to character and appending it to t
    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            t += chr((ord(char) - key - 65) % 26 + 65)
        else:
            t += chr((ord(char) - key - 97) % 26 + 97)

    return t

    return t
print("Caesar Encryption :)")
print("__________________________")
word = input("Enter a word: ")
key = int(input("Enter an integer as the key: "))
ciph = caesar_encryption(word,key)
print (ciph)
print("\n")
print("Lets decrypt the cipher:")
print (caesar_decryption(ciph,key))