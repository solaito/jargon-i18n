.. _dead-beef-attack:

============================================================
dead beef attack
============================================================

n\.

[cypherpunks list, 1996] An attack on a public-key cryptosystem consisting of publishing a key having the same ID as another key (thus making it possible to spoof a user's identity if recipients aren't careful about verifying keys).
In PGP and GPG the key ID is the last eight hex digits of (for RSA keys) the product of two primes.
The attack was demonstrated by creating a key whose ID was 0xdeadbeef (see :ref:`DEADBEEF`\).

