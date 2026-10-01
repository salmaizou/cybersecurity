"""
Chiffrement asymétrique avec RSA
--------------------------------

RSA utilise une paire de clés :

    - clé publique : peut être partagée
    - clé privée   : doit rester secrète

Dans cet exemple :
    1. Génération des clés
    2. Chiffrement avec la clé publique
    3. Déchiffrement avec la clé privée

Installation :
    pip install cryptography
"""

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


# ============================================================
# 1. GÉNÉRATION DES CLÉS
# ============================================================

def generer_cles():
    """
    Génère une paire de clés RSA :
        - clé privée
        - clé publique
    """

    cle_privee = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    cle_publique = cle_privee.public_key()

    return cle_privee, cle_publique


# ============================================================
# 2. CHIFFREMENT
# ============================================================

def chiffrer(message, cle_publique):
    """
    Chiffre un message avec la clé publique.
    """

    message = message.encode("utf-8")

    message_chiffre = cle_publique.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(
                algorithm=hashes.SHA256()
            ),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return message_chiffre


# ============================================================
# 3. DÉCHIFFREMENT
# ============================================================

def dechiffrer(message_chiffre, cle_privee):
    """
    Déchiffre un message avec la clé privée.
    """

    message = cle_privee.decrypt(
        message_chiffre,
        padding.OAEP(
            mgf=padding.MGF1(
                algorithm=hashes.SHA256()
            ),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return message.decode("utf-8")


# ============================================================
# 4. PROGRAMME PRINCIPAL
# ============================================================

if __name__ == "__main__":

    # Génération des clés
    cle_privee, cle_publique = generer_cles()

    print("=== CLÉS RSA GÉNÉRÉES ===")
    print("Clé privée :", cle_privee)
    print("Clé publique :", cle_publique)

    # Message original
    message = "Bonjour Salma !"

    print("\n=== MESSAGE ORIGINAL ===")
    print(message)

    # Chiffrement avec la clé publique
    message_chiffre = chiffrer(
        message,
        cle_publique
    )

    print("\n=== MESSAGE CHIFFRÉ ===")
    print(message_chiffre)

    # Déchiffrement avec la clé privée
    message_original = dechiffrer(
        message_chiffre,
        cle_privee
    )

    print("\n=== MESSAGE DÉCHIFFRÉ ===")
    print(message_original)
