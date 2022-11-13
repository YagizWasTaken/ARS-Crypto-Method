print("ARS crypto method 2 made by YagizWasTaken")

uncrypto_word1 = input("Enter the word you want encrypted:  ")
uncrypto_word2 = ""
uncrypto_word3 = ""
dizi = []

for i in uncrypto_word1:
    dizi.append(i)

for k in uncrypto_word1:
    uncrypto_word2 = uncrypto_word2 + str(ord(k) - 96)

print(uncrypto_word2)

for a in uncrypto_word2:
    uncrypto_word3 = uncrypto_word3 + bin(int(uncrypto_word2))

print (uncrypto_word3)