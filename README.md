# Caesar Encryption and Decryption
<p>The Caesar cipher is a classic example of ancient cryptography and is said to have been used by Julius Caesar. The Caesar cipher is based on transposition and involves shifting each letter of the plaintext message by a certain number of letters, historically three </p>
<p>The ciphertext can be decrypted by applying the same number of shifts in the opposite direction. This type of encryption is known as a substitution cipher, due to the substitution of one letter for another in a consistent fashion.</p>
Code for this is in this github repo

# Caesar Cipher Attack (Brute Force)
As the system only has 25 non-trivial keys it is easy even for a human to cycle through all the possible keys until they find one which allows the ciphertext to be converted into plaintext.
Code for this is in this github repo

# Frequency Analysis
This takes less time as the brute force attack<br>
By graphing the frequencies of letters in the ciphertext and those in the original language of the plaintext, a human can spot the value of the key but looking at the displacement of particular features of the graph. For example in the English language the frequencies of the letters Q,R,S,T have a particularly distinctive pattern.

Computers can also do this trivially by means of an auto-correlation function.
 
