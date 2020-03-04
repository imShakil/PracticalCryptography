# File     : CaesarCipherBruteForceAttack.py
# Project  : PracticalCryptography
# Product  : PyCharm
# Created  : 9:56 PM,3/2/20
# Author   : Mobarak Hosen Shakil
# E-mail   : mh.ice.iu@gmail.com
# Blog     : http://iuconvergent.wordpress.com
# Information & Communication Technology
# Islamic University, Kushtia-7003, Bangladesh


def do_brute_force_attack(msg):
    for i in range(0, 26):
        encs = ""
        for ch in msg:
            if ch.isupper():
                encs += chr((ord(ch) - 65 - i) % 26 + 65)
            elif ch.islower():
                encs += chr((ord(ch) - 97 - i) % 26 + 97)
            else:
                encs += ch
        print("Hacking Key #" + str(i) + ": " + encs)


def main():
    do_brute_force_attack("GIEWIV GMTLIV HIQS")


main()
