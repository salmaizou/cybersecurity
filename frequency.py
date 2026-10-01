from collections import Counter
import string


def analyse_frequence(texte):
    # Mettre tout en majuscules
    texte = texte.upper()

    # Garder uniquement les lettres A-Z
    lettres = [c for c in texte if c in string.ascii_uppercase]

    # Compter les occurrences
    compteur = Counter(lettres)

    # Nombre total de lettres
    total = len(lettres)

    print("=== ANALYSE DE FRÉQUENCE ===")
    print(f"Nombre total de lettres : {total}\n")

    # Afficher toutes les lettres, même celles absentes
    for lettre in string.ascii_uppercase:
        nombre = compteur[lettre]

        if total > 0:
            pourcentage = (nombre / total) * 100
        else:
            pourcentage = 0

        print(f"{lettre} : {nombre:3d} fois ({pourcentage:5.2f}%)")


texte = """
OD FUBSWRJUDSKLH HVW SDVVLRQQDQWH
"""

analyse_frequence(texte)
