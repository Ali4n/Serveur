__author__ = 'N3o'

import random
import hashlib


def randomLoginOrPassword(choix):

    loginOrPassword = ""
    i = 0

    if choix == 0:
        lenghLogin = int(input("Choisisez la taille de votre login: "))
    elif choix == 1:
        lenghPassword = int(input("Choisisez la taille de votre mot de passe: "))

    while i > 0:
        loginOrPassword += random.choice('AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn123456789&é^$ù*,;:!?./§/*-+')
        i -= 1

    if choix == 0:
        print("Votre login est : " % loginOrPassword)
    elif choix == 1:
        print("Votre mot de passe est : " % loginOrPassword)

    return loginOrPassword


def createLoginOrPassword(choix):

    loginOrPassword = ""

    if choix == 0:
        loginOrPassword = input("Saisisez votre login: ")
    elif choix == 1:
        loginOrPassword = input("Saisisez votre mot de passe: ")

    return loginOrPassword


def sha512(password):

    hash_object = hashlib.sha512(password.encode())
    passwordHash = hash_object.hexdigest()
    print("Le hash de votre mot de passe est:" % passwordHash)

    return passwordHash


def getlogin():
    login = input("Saisir le login")
    return login
def getmdp():
    mdp = input("Saisir le mot de passe")
    return mdp


def bdd():
    print("bdd")
