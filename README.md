# 🔐 Phase 5 — Cryptographie

> Objectif : maîtriser les fondamentaux de la cryptographie appliquée à la cybersécurité, comprendre les principaux algorithmes et être capable d'expliquer comment ils sont utilisés ensemble dans TLS, HTTPS et PKI.

---

# 🎯 Objectif final

À la fin de cette phase, je dois être capable de comprendre une connexion HTTPS de bout en bout :

```text
Utilisateur
    │
    │ https://example.com
    ▼
   DNS
    │
    ▼
Adresse IP
    │
    ▼
   TCP
    │
    ▼
Port 443
    │
    ▼
   TLS
    │
    ├── Certificat
    │      │
    │      └── PKI / CA
    │
    ├── Authentification
    │
    ├── Échange de clés
    │      │
    │      └── ECDHE
    │
    └── Clé de session
           │
           ▼
   Chiffrement symétrique
      AES-GCM / ChaCha20-Poly1305
           │
           ▼
          HTTP
