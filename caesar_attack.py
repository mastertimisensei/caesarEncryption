def caesar_attack(plain):
    # We try 1 - 26(number of alphabets) as keys
    for j in range(26):
        attack = ""
        for i in range(len(plain)):
            char = plain[i]
            if char.isupper():
                attack += chr((ord(char) - j - 65) % 26 + 65)
            else:
                attack += chr((ord(char) - j - 97) % 26 + 97)
        # We print each of the key's resulted plain
        print(attack)

inp = input("What message do you want to test caesar attack on: ")
caesar_attack(inp);