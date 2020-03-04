# File     : CaesarCipher.py
# Project  : PracticalCryptography
# Product  : PyCharm
# Created  : 8:12 PM,3/2/20
# Author   : Mobarak Hosen Shakil
# E-mail   : mh.ice.iu@gmail.com
# Blog     : http://iuconvergent.wordpress.com
# Information & Communication Technology
# Islamic University, Kushtia-7003, Bangladesh


def do_reverse(s):
    return "".join(reversed(s))


def do_encryption(msg):
    print("Cipher Text: ", do_reverse(msg))


def do_decryption(msg):
    print("Normal Message: ", do_reverse(msg))


def main():
    while 1:

        print("Enter a value to choose an option: \n1. Encryption\n2. Decryption\n3. Exit")
        op_code = int(input())

        if op_code == 1:
            NormalMsg = str(input("Enter a message: "))
            print("Normal Message: ", NormalMsg)
            do_encryption(NormalMsg)

        elif op_code == 2:
            CipherTxt = str(input("Enter Cipher Text: "))
            print("Cipher Text: ", CipherTxt)
            do_decryption(CipherTxt)

        else:
            exit(op_code)


main()
