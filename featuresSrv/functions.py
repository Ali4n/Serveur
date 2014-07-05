__author__ = 'Thomas BOTTON, IGOR ZECEVIC, Daoud MOUSTIR'

import random
import hashlib


def sha512(password):
    return hashlib.sha512(password.encode()).hexdigest()

def logserver(message):
    fichier='server.log'
    of = open(fichier,'a')
    of.write(message + '\n')
    of.close()