from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

# -------------------------
# 1. Génération d'une clé
# -------------------------
key = AESGCM.generate_key(bit_length=256)   # 256 bits

# -------------------------
# 2. Création de l'objet AES
# -------------------------
aes = AESGCM(key)

# -------------------------
# 3. Message à chiffrer
# -------------------------
message = b"Bonjour Ismail, ceci est un message secret."

# -------------------------
# 4. Nonce (12 octets)
# -------------------------
nonce = os.urandom(12)

# -------------------------
# 5. Chiffrement
# -------------------------
ciphertext = aes.encrypt(nonce, message, None)

print("Message original :", message)
print("Message chiffré :", ciphertext)

# -------------------------
# 6. Déchiffrement
# -------------------------
plaintext = aes.decrypt(nonce, ciphertext, None)

print("Message déchiffré :", plaintext.decode())
