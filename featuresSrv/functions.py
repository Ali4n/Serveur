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


def file_hash(file):

    sha512_hash = hashlib.sha512()

    try:
        open_file = open(file, "rb")
        data = open_file.read()
    except:
        print("Le fichier '" + file + "' n'existe pas ")

    sha512_hash.update(data)
    hashed_data = sha512_hash.hexdigest()
    open_file.close()

    return hashed_data