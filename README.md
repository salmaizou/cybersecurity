
# 🔐 Cryptography & Cybersecurity — Phase 5

## 📖 Overview

This project explores the fundamental concepts of cryptography and their applications in cybersecurity through practical Python implementations.

The main objective is to understand how encryption algorithms protect sensitive information and how cryptographic mechanisms secure modern communications.

## 🎯 Project Objectives

- Understand symmetric and asymmetric encryption.
- Explore RSA public-key cryptography.
- Implement cryptographic concepts using Python.
- Perform letter frequency analysis.
- Understand digital certificates and Public Key Infrastructure (PKI).
- Explore secure communication protocols such as TLS and HTTPS.

## 📂 Project Structure

```text
Cryptography/
│
├── ChiffrementAsymetrique.py    # Asymmetric encryption
├── chiffrementSymetrique.py     # Symmetric encryption
├── frequency.py                # Letter frequency analysis
└── README.md                   # Project documentation
```

## 🛠️ Technologies & Concepts

**Programming:** Python

**Tools:** Git, GitHub

**Cybersecurity concepts:**
- Symmetric encryption
- Asymmetric encryption (RSA)
- Frequency analysis
- Digital certificates
- TLS / HTTPS
- Public Key Infrastructure (PKI)

## 🔒 How HTTPS Works

A secure HTTPS connection combines several cryptographic mechanisms:

```text
Client
  │
  ▼
DNS Resolution
  │
  ▼
TCP Connection (Port 443)
  │
  ▼
TLS Handshake
  │
  ├── Certificate Verification (PKI)
  │
  ├── Server Authentication
  │
  └── Key Exchange (ECDHE)
          │
          ▼
     Session Keys
          │
          ▼
Symmetric Encryption
(AES-GCM / ChaCha20-Poly1305)
          │
          ▼
Secure HTTP Communication
```

## 📚 Learning Outcomes

Through this project, I developed a stronger understanding of:

- Cryptographic algorithms and their applications.
- Secure data transmission.
- Encryption and decryption principles.
- Python programming for cybersecurity.
- The role of cryptography in modern network security.

## 👩‍💻 Author

**Salma IZOUGHAR**

Engineering Student — École Centrale de Lyon

*Academic project | Cybersecurity & Cryptography*
