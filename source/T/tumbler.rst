.. _tumbler:

============================================================
tumbler
============================================================

n\.

1.
   [Originally from the Xanadu hypertext project] A tumbler is a :ref:`magic-cookie` generated as part of a record or message to give it a unique identity.
   Usually a tumbler includes an encoded form of its creation date, but if a software system has more than one concurrent process that could generate tumblers it must also include an encoding of the process ID.
   If tumblers will be shared across multiple network hosts, they must also include the host name or network address.
   Tumblers often include a hash of the rest of the message or record content so that it is possible to verify the correctness of the data the tumbler is attached to.

2.
   Variant text added to spam instances (often in the Subject line) to make them unique.
   This kind of tumbler is used to defeat schemes that check an exact hash of an incoming message against known spam signatures; it also compromises some kinds of statistical spam recognition.

