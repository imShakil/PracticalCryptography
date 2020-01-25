# File     : SimplaHash.py
# Project  : caesar-cipher-imShakil
# Product  : PyCharm
# Created  : 8:00 PM, 25-Jan-20
# Author   : Mobarak Hosen Shakil
# E-mail   : mh.ice.iu@gmail.com
# Blog     : http://codefighter.cf
# Information & Communication Technology
# Islamic University, Kushtia, Bangladesh


def get_sha1(data):

    from hashlib import sha1

    data_bytes = data.encode()

    print("SHA1 hash value of "+data+": "+sha1(data_bytes).hexdigest())


def get_md5(data):

    from hashlib import md5

    print("MD5 hash value of "+data+": "+md5(data.encode()).hexdigest())


def main():

    data1 = "Practical Cryptography"
    data2 = "Mobarak Hosen Shakil"

    get_sha1(data1)
    get_sha1(data2)

    get_md5(data1)
    get_md5(data2)


main()
