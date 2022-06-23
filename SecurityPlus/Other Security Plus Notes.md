---
Tags: OtherSecurityPlusNotes
date: 06-12-2022
---

[Security Plus](../SecurityPlus/SecurityPlus.md)

---



- Encryption supporting confidentiality is used for both data-at-rest (file encryption) and data-in-transit (transport encryption):

-   File encryption—the user is allocated an asymmetric cipher key pair. The private key is written to secure storage—often a trusted platform module (TPM)—and is only available when the user has authenticated to his or her account. The public key is used to encrypt a randomly generated AES cipher key. When the user tries to encrypt or decrypt files, the AES cipher key is decrypted using the private key to make it available for the encryption or decryption operation.
-   Transport encryption—this uses either digital envelopes or perfect forward secrecy. For HTTPS, a web server is allocated a key pair and stores the private key securely. The public key is distributed to clients via a digital certificate. The client and server use the key pair to exchange or agree on one or more AES cipher keys to use as session keys.

---


