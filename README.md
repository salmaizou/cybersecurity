
# 🔐 Phase 5 — Cryptographie et cybersécurité

## 📌 Présentation du projet

Ce projet est consacré à l'étude et à l'implémentation des principaux mécanismes cryptographiques utilisés en cybersécurité.

Il a pour objectif de comprendre les principes fondamentaux du chiffrement, d'explorer les différences entre la cryptographie symétrique et asymétrique, et d'analyser leur utilisation dans les protocoles de communication sécurisés.

Les différentes implémentations sont réalisées en **Python**.

## 🎯 Objectifs pédagogiques

- Comprendre les principes de confidentialité, d'intégrité et d'authenticité des données.
- Étudier les mécanismes de chiffrement symétrique et asymétrique.
- Explorer le fonctionnement de l'algorithme RSA.
- Comprendre les techniques d'analyse fréquentielle.
- Découvrir les certificats numériques et les infrastructures à clés publiques (PKI).
- Comprendre les mécanismes de sécurisation des communications avec TLS et HTTPS.

## 📂 Structure du projet

```text
Phase-5-Cryptographie/
│
├── ChiffrementAsymetrique.py
├── chiffrementSymetrique.py
├── frequency.py
└── README.md
```

## 🛠️ Technologies utilisées

- **Langage :** Python
- **Domaine :** Cybersécurité et cryptographie
- **Outils :** Git et GitHub
- **Concepts :** RSA, chiffrement symétrique, analyse fréquentielle, TLS, HTTPS et PKI

## 🔍 Comprendre HTTPS et TLS

L'un des objectifs principaux de ce projet est de comprendre comment les mécanismes cryptographiques interviennent dans l'établissement d'une connexion HTTPS sécurisée.

### Schéma simplifié d'une connexion HTTPS

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
    ├── Certificat numérique
    │       └── PKI / Autorité de certification
    │
    ├── Authentification du serveur
    │
    ├── Échange de clés
    │       └── ECDHE
    │
    └── Clés de session
            │
            ▼
    Chiffrement symétrique
    AES-GCM / ChaCha20-Poly1305
            │
            ▼
       Données HTTP
```

### Principales étapes

1. **DNS :** résolution du nom de domaine en adresse IP.
2. **TCP :** établissement de la connexion réseau.
3. **TLS :** négociation des paramètres de sécurité et authentification du serveur.
4. **ECDHE :** établissement d'un secret partagé permettant de dériver les clés de session.
5. **Chiffrement symétrique :** protection des données échangées.
6. **HTTPS :** transmission sécurisée des requêtes et réponses HTTP.

## 📚 Compétences développées

Ce projet permet de renforcer les compétences suivantes :

- Programmation Python appliquée à la cybersécurité.
- Compréhension des algorithmes cryptographiques.
- Analyse des mécanismes de protection des données.
- Compréhension des protocoles de communication sécurisés.
- Organisation et documentation d'un projet technique.

## 🚀 Perspectives

Les prochaines étapes pourront inclure :

- L'étude des fonctions de hachage cryptographiques.
- L'implémentation de signatures numériques.
- L'analyse des certificats X.509.
- L'expérimentation des échanges de clés.
- L'étude approfondie de TLS 1.3.

---

**Projet académique — Phase 5 : Cryptographie**
