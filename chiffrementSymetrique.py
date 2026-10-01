# Renvoie les lettres les plus présentes dans un texte
def rechercheOcc(texte):
    listeOcc = list()

    for i in range(26):
        listeOcc += [[0, chr(i+65)]]

    texte = texte.upper()
    for i in texte:
        if 65 <= ord(i) <= 65+25:
            listeOcc[ord(i)-65][0] += 1

    renvoie = list()
    for _ in range(5):
        max = listeOcc[0][0]
        indice = 0
        for i in range(len(listeOcc)):
            if max < listeOcc[i][0]:
                max = listeOcc[i][0]
                indice = i
        renvoie += [listeOcc[indice]]
        del (listeOcc[indice])
    return (renvoie)


# Fonction de décalage d'un caractère dans l'alphabet
def decalage(caract, dis):

    if 65 <= ord(caract) <= 90:
        return (chr(((ord(caract)-65)+dis) % 26 + 65))

    if 97 <= ord(caract) <= 122:
        return (chr(((ord(caract)-97)+dis) % 26 + 97))

    return (chr(ord(caract)+dis))


# Cryptage César
def cryptageCesar():

    print("\n\n")
    texte = raw_input("Message a crypter : ")
    dec = raw_input("Decalage : ")
    print("\n\n")
    print("Message crypte : {}".format(crypterConstant(texte, int(dec))))


def decryptageCesar():

    print("\n\n")
    texte = raw_input("Message a decrypter : ")
    dec = raw_input("Decalage : ")
    print("\n\n")
    print("Message original : {}".format(decrypterConstant(texte, int(dec))))


def crypterConstant(texte, dec):

    renvoi = ""
    for i in texte:
        if i == ' ':
            renvoi += ' '
        elif i == "'":
            renvoi += "'"
        elif i == "-":
            renvoi += "-"
        elif i == ".":
            renvoi += "."
        else:
            renvoi += decalage(i, dec)
    return (renvoi)


def decrypterConstant(texte, dec):

    return (crypterConstant(texte, 26-dec))


# Cryptage Vigenere
def cryptageVigenere():

    print("\n\n")
    texte = raw_input("Message a crypter : ")
    cle = raw_input("Cle de chiffrement : ")
    print("\n\n")
    print("Message crypte : {}".format(crypterCle(texte, cle)))


def decryptageVigenere():

    print("\n\n")
    texte = raw_input("Message a decrypter : ")
    cle = raw_input("Cle de chiffrement : ")
    print("\n\n")
    print("Message original : {}".format(decrypterCle(texte, cle)))


def crypterCle(texte, cle):

    renvoi = ""
    c = 0  # permet de décaler si jamais espace ou apostrophe
    for i in range(len(texte)):

        if texte[i] == ' ':
            renvoi += ' '
            c += 1
        elif texte[i] == "'":
            renvoi += "'"
            c += 1
        elif texte[i] == "-":
            renvoi += "-"
            c += 1
        elif i == ".":
            renvoi += "."
            c += 1
        else:
            temp = ord(cle[(i-c) % len(cle)])
            if 65 <= temp <= 90:
                temp -= 65
            else:
                temp -= 97
            renvoi += decalage(texte[i], temp)
    return (renvoi)


def decrypterCle(texte, cle):

    renvoi = ""
    c = 0  # permet de décaler si jamais espace ou apostrophe
    for i in range(len(texte)):

        if texte[i] == ' ':
            renvoi += ' '
            c += 1
        elif texte[i] == "'":
            renvoi += "'"
            c += 1
        elif texte[i] == "-":
            renvoi += "-"
            c += 1
        elif texte[i] == ".":
            renvoi += "."
            c += 1
        else:
            temp = ord(cle[(i-c) % len(cle)])
            if 65 <= temp <= 90:
                temp -= 65
            else:
                temp -= 97
            renvoi += decalage(texte[i], 26-temp)
    return (renvoi)
