print("ARS crypto method made by YagizWasTaken")

uncrypto_word1 = input("Enter the word you want encrypted:  ")
uncrypto_word2 = ""
uncrypto_word3 = ""
dizi = []

for i in uncrypto_word1:
    dizi.append(i)

for k in dizi:
    uncrypto_word2 = uncrypto_word2 + str(ord(k) - 96)

print(uncrypto_word2)

uncrypto_word2_list = list(uncrypto_word2)
print(uncrypto_word2_list)

uncrypto_word2_eleman = len(uncrypto_word2_list)
for x in range(int(uncrypto_word2_eleman)-1):
    uncrypto_word2_list[x] =int(uncrypto_word2_list[x])

for b in range(int(uncrypto_word2_eleman)-1):
    uncrypto_word3 = uncrypto_word3, bin(uncrypto_word2_list[b])

print (uncrypto_word3)

