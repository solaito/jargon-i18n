.. _Alice-and-Bob:

============================================================
Alice and Bob
============================================================

n\.

The archetypal individuals used as examples in discussions of cryptographic protocols.
Originally, theorists would say something like: "A communicates with someone who claims to be B, So to be sure, A tests that B knows a secret number K. So A sends to B a random number X.
B then forms Y by encrypting X under key K and sends Y back to A" Because this sort of thing is quite hard to follow, theorists stopped using the unadorned letters A and B to represent the main players and started calling them Alice and Bob.
So now we say "Alice communicates with someone claiming to be Bob, and to be sure, Alice tests that Bob knows a secret number K. Alice sends to Bob a random number X.
Bob then forms Y by encrypting X under key K and sends Y back to Alice".
A whole mythology rapidly grew up around the metasyntactic names; see `http://www.conceptlabs.co.uk/alicebob.html <http://www.conceptlabs.co.uk/alicebob.html>`_.

In Bruce Schneier's definitive introductory text *Applied Cryptography* (2nd ed., 1996, John Wiley & Sons, ISBN 0-471-11709-9) he introduced a table of dramatis personae headed by Alice and Bob.
Others include Carol (a participant in three- and four-party protocols), Dave (a participant in four-party protocols), Eve (an eavesdropper), Mallory (a malicious active attacker), Trent (a trusted arbitrator), Walter (a warden), Peggy (a prover) and Victor (a verifier).
These names for roles are either already standard or, given the wide popularity of the book, may be expected to quickly become so.

