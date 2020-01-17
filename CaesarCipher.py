# File     : CaesarCipher.py
# Project  : PracticalCryptography
# Product  : PyCharm
# Created  : 7:44 PM, 17-Jan-20
# Author   : Mobarak Hosen Shakil
# E-mail   : mh.ice.iu@gmail.com
# Blog     : http://codefighter.cf
# Information & Communication Technology
# Islamic University, Kushtia, Bangladesh

global k


def __encryption__():

    print("Enter Message to encrypt: ")

    s = str(input())

    print("Enter shift Key: ")

    kk = int(input())

    global k
    k = kk

    msg = encrypt(s, k)

    print("Normal Message:", s)
    print("Encrypted Message:", msg)
    print("Encrypted Key:", k, '\n')


def __decryption__():
    
    print("Enter Message to decrypt: ")
    s = str(input())
    msg = decrypt(s, k)

    print("Normal Message:", s)
    print("Decrypted Message:", msg)
    print("Decrypted Key:", k, '\n')


def encrypt(message, key):
    
    encrypted_message = ""

    for i in range(len(message)):
        char = message[i]

        if char.isupper():
            encrypted_message += chr((ord(char) + key - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        elif char.islower():
            encrypted_message += chr((ord(char) + key - 97) % 26 + 97)
        else:
            encrypted_message += char
            
    return encrypted_message


def decrypt(message, key):

    decrypted_message = ""

    for i in range(len(message)):
        char = message[i]

        if char.isupper():
            decrypted_message += chr((ord(char) + key - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        elif char.islower():
            decrypted_message += chr((ord(char) + key - 97) % 26 + 97)
        else:
            decrypted_message += char

    return decrypted_message

