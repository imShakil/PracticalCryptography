# File     : CaesarCipher.py
# Project  : PracticalCryptography
# Product  : PyCharm
# Created  : 8:12 PM,3/2/20
# Author   : Mobarak Hosen Shakil
# E-mail   : mh.ice.iu@gmail.com
# Blog     : http://iuconvergent.wordpress.com
# Information & Communication Technology
# Islamic University, Kushtia-7003, Bangladesh


def do_encryption(msg, key):
    enc_text = ""

    for ch in msg:
        if ch.isupper():
            enc_text += chr((ord(ch) - 65 + key) % 26 + 65)
        elif ch.islower():
            enc_text += chr((ord(ch) - 97 + key) % 26 + 97)
        else:
            enc_text += ch

    return enc_text


def do_decryption(msg, key):
    enc_text = ""

    for ch in msg:
        if ch.isupper():
            enc_text += chr((ord(ch) - key - 65) % 26 + 65)
        elif ch.islower():
            enc_text += chr((ord(ch) - key - 97) % 26 + 97)
        else:
            enc_text += ch

    return enc_text


def main():
    while 1:
        op_code = int(input("Enter a value to perform an operation:\n1. Encryption\n2. Decryption\n3. Exit\n"))

        if op_code == 1:
            Message, key = str(input("Enter message to encrypt: ")), int(input("Enter a key between (1-26): "))
            print("Plain Text: ", Message)
            print("Cipher Text: ", do_encryption(Message, key))
        elif op_code == 2:
            Cipher_Text, key = str(input("Enter Encrypted message: ")), int(input("Enter valid key: "))
            print("Cipher Text: ", Cipher_Text)
            print("Plain Text: ", do_decryption(Cipher_Text, key))
        else:
            break


main()
