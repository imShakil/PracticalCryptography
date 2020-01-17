# File     : KamaSutra.py
# Project  : caesar-cipher-imShakil
# Product  : PyCharm
# Created  : 11:20 PM, 17-Jan-20
# Author   : Mobarak Hosen Shakil
# E-mail   : mh.ice.iu@gmail.com
# Blog     : http://codefighter.cf
# Information & Communication Technology
# Islamic University, Kushtia, Bangladesh

import random

global key_value


def __generate_key__():
    key = list()
    for i in range(26):
        key.append(i)
    random.shuffle(key)

    global key_value
    key_value = ""

    for i in range(26):
        char = chr(key[i] + 65)
        key_value += char

    print("Generated Key: ", key_value)

    keymap = [0 for i in range(150)]

    for i in range(13):
        keymap[key[i]] = key[13 + i]
        keymap[key[13 + i]] = key[i]

    return keymap


def __cipher__():

    global key_map
    ok = False
    chk = int(3)
    while chk is not 4:
        print("Enter a valid value to choose an option: \n \t 1. Generate Secret Key \n \t 2. Encryption \n \t 3. "
              "Decryption \n \t 4. Exit \n")

        chk = int(input())

        if chk == 1:
            key_map = __generate_key__()
            ok = True
        elif chk == 2 or chk == 3:
            if not ok:
                print("First Generate a secret Key.")
            else:
                print("Enter Message: ")
                msg = str(input())
                new_msg = ""

                for i in range(len(msg)):
                    char = msg[i]

                    if char.isupper():
                        #   print('u', ord(char) - 65)
                        new_msg += chr(key_map[ord(char) - 65] + 65)
                    elif char.islower():
                        #   print('l', ord(char) - 97)
                        new_msg += chr(key_map[ord(char) - 97] + 97)
                    else:
                        new_msg += char

                print("Given Message: ", msg)
                print("Cipher Message: ", new_msg)
                print("Secret Key: ", key_value)
        elif chk == 4:
            break
        else:
            print("Please choose a valid option")


__cipher__()
