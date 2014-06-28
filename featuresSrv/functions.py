__author__ = 'Thomas BOTTON, IGOR ZECEVIC, Daoud MOUSTIR'

import random
import hashlib


def sha512(password):
    hash_object = hashlib.sha512(password.encode())
    return hash_object.hexdigest()
