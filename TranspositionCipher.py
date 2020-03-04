# File     : TranspositionCipher.py
# Project  : PracticalCryptography
# Product  : PyCharm
# Created  : 10:44 PM,3/2/20
# Author   : Mobarak Hosen Shakil
# E-mail   : mh.ice.iu@gmail.com
# Blog     : http://iuconvergent.wordpress.com
# Information & Communication Technology
# Islamic University, Kushtia-7003, Bangladesh


def do_encryption(msg, key):

    encs = ""
    pointer_matrix = [['\n' for i in range(len(msg))] for j in range(key)]
    row = 0
    isDown = True

    for col in range(len(msg)):
        if row == key-1:
            isDown = False
        if row == 0:
            isDown = True
        # print(row, col)
        pointer_matrix[row][col] = '*'
        if isDown:
            row += 1
        else:
            row -= 1

    for i in range(key):
        # print(i, ": ")
        for j in range(len(msg)):
            if pointer_matrix[i][j] == '*':
                encs += msg[j]

    return encs


def do_decryption(msg, key):
    encs =""
    pointer_matrix = [['\n' for i in range(len(msg))] for j in range(key)]
    row = 0
    isDown = True

    for col in range(len(msg)):
        if row == key-1:
            isDown = False
        if row == 0:
            isDown = True

        pointer_matrix[row][col] = '*'

        if isDown:
            row += 1
        else:
            row -= 1
    idx = 0
    for i in range(key):
        for j in range(len(msg)):
            if pointer_matrix[i][j] == '*' and idx < len(msg):
                pointer_matrix[i][j] = msg[idx]
                idx += 1
    row = 0
    isDown = True

    for col in range(len(msg)):
        if row == key - 1:
            isDown = False
        if row == 0:
            isDown = True

        if pointer_matrix[row][col] != '*':
            encs += pointer_matrix[row][col]

        if isDown:
            row += 1
        else:
            row -= 1
    return encs


def main():

    msg, key = str(input("Please enter your message: ")), int(input("Please enter a key: "))

    cipher_text = do_encryption(msg, key)
    plain_text = do_decryption(cipher_text, key)
    print("Cipher Text:", cipher_text)
    print("Plain Text: ", plain_text)


main()
