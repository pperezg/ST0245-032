#!/usr/bin/python

import HES

# La clave es una permutación de abcdefghijkl
def decrypt_attempt(key):
    result = HES.decrypt_from_file("encryptedFile.txt", key)
    if "90" in result:
        return result
    return False

def permutacion(s):
    permutations("",s)

def permutations(base, s):
    if len(s)==0:
        return base
    else:
        x = s[1:]
        permutations(base+s[0], x)
        permutations(base, x)

decrypt_attempt(permutacion("abcdefghijkl"))
