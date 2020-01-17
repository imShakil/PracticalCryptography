# File     : RunTest.py
# Project  : PracticalCryptography
# Product  : PyCharm
# Created  : 8:12 PM, 17-Jan-20
# Author   : Mobarak Hosen Shakil
# E-mail   : mh.ice.iu@gmail.com
# Blog     : http://codefighter.cf
# Information & Communication Technology
# Islamic University, Kushtia, Bangladesh

import CaesarCipher


def __main__():
    isOk = False
    chk = 0
    while chk is not 3:
        print("Enter a value to choose an option: \n \t 1. Encryption \n \t 2. Decryption \n \t 3. Exit \n")
        chk = int(input())
        if chk == 2:
            if not isOk:
                print("Choose Encryption First\n")
            else:
                CaesarCipher.__decryption__()
        elif chk == 1:
            isOk = True
            CaesarCipher.__encryption__()
        else:
            break


__main__()
