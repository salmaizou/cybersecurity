
# 🔐 Cryptography Lab

### Python Implementations | Encryption Algorithms | Cybersecurity

## Overview

**Cryptography Lab** is a Python-based educational project focused on exploring fundamental cryptographic mechanisms and their role in information security.

The repository brings together practical exercises involving encryption, decryption, and frequency analysis, alongside an introduction to secure communication architectures.

## Project Modules

| File | Topic | Objective |
|------|-------|-----------|
| `chiffrementSymetrique.py` | Symmetric Cryptography | Explore encryption using shared keys |
| `ChiffrementAsymetrique.py` | Asymmetric Cryptography | Understand RSA and public/private key operations |
| `frequency.py` | Cryptanalysis | Analyze character frequencies and statistical patterns |

## Core Security Concepts

### 🔑 Encryption
Understanding how plaintext is transformed into ciphertext to protect sensitive information.

### 🛡️ Public-Key Cryptography
Exploring RSA and the relationship between public and private keys.

### 📊 Cryptanalysis
Studying frequency distributions and their relevance to classical encryption techniques.

### 🌐 Network Security
Understanding how TLS and HTTPS use cryptographic mechanisms to establish secure connections.

## Secure Communication Workflow

```text
           USER / CLIENT
                 |
           DNS Resolution
                 |
           TCP Connection
                 |
           TLS Handshake
                 |
       +---------+---------+
       |                   |
 Certificate           ECDHE Key
 Verification          Agreement
       |                   |
       +---------+---------+
                 |
          Session Keys
                 |
       Authenticated Encryption
       AES-GCM / ChaCha20-Poly1305
                 |
          HTTPS Traffic
```

## Technologies

**Programming Language:** Python

**Development Tools:** Git, GitHub

**Security Topics:** RSA, Encryption, Cryptanalysis, TLS, HTTPS, PKI

## Learning Outcomes

This project strengthens my ability to:

- Implement and explore cryptographic techniques using Python.
- Understand encryption and decryption mechanisms.
- Analyze data patterns relevant to cryptanalysis.
- Explain the foundations of secure network communication.
- Document and organize cybersecurity experiments.

## Future Development

- Add SHA-256 hashing demonstrations.
- Explore digital signatures and verification.
- Implement AES-GCM examples using established libraries.
- Introduce automated testing.
- Extend documentation with practical TLS experiments.

## Security Notice

This repository is intended for learning and experimentation. Its educational implementations are not designed for production security applications.

---

**Developed by Salma IZOUGHAR**

Engineering Student — École Centrale de Lyon

*Python · Cryptography · Cybersecurity*
