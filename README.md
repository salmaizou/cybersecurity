
# 🔐 Cryptography & Secure Systems

### Exploring Cryptographic Algorithms Through Python

## 📖 Project Description

This repository presents a collection of Python exercises dedicated to understanding the foundations of cryptography and information security.

The project combines algorithmic exploration, practical programming, and security concepts to illustrate how cryptographic mechanisms contribute to protecting digital information.

## 🎯 Objectives

The main objectives are to:

- Explore symmetric and asymmetric encryption techniques.
- Understand the mathematical foundations of RSA.
- Study frequency analysis in classical cryptography.
- Strengthen Python programming and algorithmic reasoning.
- Understand the role of cryptography in secure network protocols.

## 🗂️ Repository Structure

```text
cryptography-project/
│
├── ChiffrementAsymetrique.py
├── chiffrementSymetrique.py
├── frequency.py
└── README.md
```

## 🔬 Technical Exploration

### 1. Symmetric Cryptography

Study encryption techniques in which the sender and receiver use the same secret key.

**Python module:** `chiffrementSymetrique.py`

### 2. Asymmetric Cryptography

Explore RSA and the principles of public-key and private-key cryptography.

**Python module:** `ChiffrementAsymetrique.py`

### 3. Frequency Analysis

Investigate character frequency distributions and their applications in classical cryptanalysis.

**Python module:** `frequency.py`

## 🌍 Real-World Application: HTTPS

Cryptography plays a central role in protecting web communications.

A simplified HTTPS connection follows these steps:

1. **DNS resolution:** Identify the server's IP address.
2. **TCP connection:** Establish a network connection.
3. **TLS handshake:** Negotiate cryptographic parameters.
4. **Certificate validation:** Authenticate the server through PKI.
5. **Key agreement:** Establish shared secrets using ECDHE.
6. **Secure communication:** Protect HTTP traffic with authenticated encryption.

### Communication Architecture

```text
        CLIENT
           |
           v
     DNS Resolution
           |
           v
     TCP Connection
           |
           v
      TLS Handshake
           |
     +-----+------+
     |            |
 Certificate    ECDHE
 Validation     Exchange
     |            |
     +-----+------+
           |
           v
      Session Keys
           |
           v
    AES-GCM / ChaCha20
       Poly1305
           |
           v
    Encrypted HTTP
```

## 🛠️ Technical Environment

| Category | Technologies / Concepts |
|----------|-------------------------|
| Programming | Python |
| Version Control | Git, GitHub |
| Cryptography | Symmetric Encryption, RSA |
| Security Analysis | Frequency Analysis |
| Network Security | TLS, HTTPS, PKI |
| Key Agreement | ECDHE |

## 📈 Skills & Knowledge

This project supports the development of:

- Python programming and algorithm implementation.
- Understanding of cryptographic principles.
- Analytical thinking and problem-solving.
- Foundations of secure communication protocols.
- Technical documentation and project organization.

## 🚧 Future Extensions

- Hash functions and message integrity.
- Digital signatures and verification.
- Authenticated encryption demonstrations.
- Automated unit tests.
- TLS certificate inspection using Python.

## ⚠️ Educational Disclaimer

The code is intended for educational exploration only. It has not been security-audited and must not be used as a production cryptographic solution.

---

### 👩‍💻 Author

**Salma IZOUGHAR**

Engineering Student | École Centrale de Lyon

**Focus:** Python • Cybersecurity • Cryptographic Algorithms
