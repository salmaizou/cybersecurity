
# 🔐 Applied Cryptography with Python

**A practical introduction to cryptographic algorithms and secure communication protocols.**

## 📌 Introduction

This repository documents my exploration of cryptography through Python programming.

It focuses on understanding encryption mechanisms, experimenting with cryptographic techniques, and studying how modern systems protect information during transmission.

## ⚙️ Project Components

### 01 — Symmetric Encryption
Explore encryption and decryption mechanisms based on shared secret keys.

**File:** `chiffrementSymetrique.py`

### 02 — Asymmetric Encryption
Study public-key cryptography and the mathematical principles behind RSA.

**File:** `ChiffrementAsymetrique.py`

### 03 — Frequency Analysis
Analyze character distributions to understand statistical patterns relevant to classical cryptanalysis.

**File:** `frequency.py`

## 🌐 From Cryptography to HTTPS

Modern secure communication relies on multiple complementary mechanisms.

| Mechanism | Purpose |
|-----------|---------|
| Symmetric encryption | Protects data confidentiality |
| Asymmetric cryptography | Supports authentication and other public-key operations |
| Digital certificates | Bind identities to public keys |
| ECDHE | Establishes a shared secret |
| TLS | Secures communication between endpoints |
| HTTPS | Carries HTTP over TLS |

### Simplified TLS 1.3 Flow

```text
Client                          Server
  |                               |
  |-------- ClientHello --------->|
  |                               |
  |<------- ServerHello ----------|
  |                               |
  |       Key Agreement           |
  |          (ECDHE)              |
  |                               |
  |<---- Certificate + Proof -----|
  |                               |
  |------ Finished -------------->|
  |                               |
  |     Encrypted Application     |
  |<========== Data =============>|
```

*This diagram is conceptual and omits some TLS handshake messages.*

## 🧰 Technologies

`Python` · `Cryptography` · `RSA` · `Git` · `GitHub`

## 🎓 Learning Goals

- Translate cryptographic theory into Python experiments.
- Understand the differences between encryption techniques.
- Explore basic cryptanalysis.
- Develop a conceptual understanding of TLS and PKI.
- Strengthen analytical and programming skills.

## 🔮 Next Steps

- Add practical examples of hashing and digital signatures.
- Explore authenticated encryption using AES-GCM.
- Add unit tests and reproducible examples.
- Document certificate verification and TLS 1.3.

## ⚠️ Disclaimer

The implementations in this repository are intended for educational purposes and should not be used to protect sensitive production data.

---

**Salma IZOUGHAR**  
Engineering Student — École Centrale de Lyon

*Cybersecurity Learning Project · Phase 5*
