from typing import Any

print("Merhaba, Yağız Arslan tarafından yazılan ARS şifreleme botunu kullandığınız için teşekkür ederiz.")  
print("Detaylı bilgi: www.yagizarslan.net/bloglar/ars_sifreleme_metodu")
secenek = input("Şifreleme yapmak isterseniz 'ş' , Anti-şifreleme yapmak isterseniz 'a' yazın  =   ")



def şifreleme():
    print("Şifreleme çalıştırılıyor...")
    def int_to_binary(num):
        return bin(num)[2:].zfill(5)

    def encrypt_message(message):
        letter_to_num = {
            ' ' : 0,'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 
            'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 
            'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 
            'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 
            'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 
            'Z': 26
        }
        encrypted_message = ""
        for letter in message:
            num = letter_to_num.get(letter.upper())
            if num is not None:
                binary = int_to_binary(num)
                encrypted_message += binary + "/"
        return encrypted_message[:-1]

    message = input("Şifrelemek istediğiniz Sözcük: ")
    encrypted_message = encrypt_message(message)
    print("Şifrelenmiş Sözcük:", encrypted_message)

def antişifreleme():
    print("Anti-şifreleme çalıştırılıyor...")

    def binary_to_int(binary: str) -> int:
        return int(binary, 2)

    def decrypt_message(encrypted_message: Any) -> str:
        num_to_letter = {
            0 : ' ' ,1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E',
            6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
            11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O',
            16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T',
            21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y',
            26: 'Z'
        }
        decrypted_message = ""
        binary_list = encrypted_message.split("/")
        for binary in binary_list:
            num = binary_to_int(binary)
            if num in num_to_letter:
                letter = num_to_letter[num]
                decrypted_message += letter
        return decrypted_message

    encrypted_message = input("Anti-şifrelemek istediğiniz Sözcük: ")
    decrypted_message = decrypt_message(encrypted_message)
    print("Anti-şifrelenmiş Sözcük:", decrypted_message)


    

if secenek == "ş" or secenek =="Ş" or secenek=="s" or secenek=="S":
    şifreleme()
if secenek =="a" or secenek=="A":
    antişifreleme()