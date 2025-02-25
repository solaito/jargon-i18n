.. _big-endian:

============================================================
big-endian
============================================================

adj\.

[common; From Swift's *Gulliver's Travels* via the famous paper *On Holy Wars and a Plea for Peace* by Danny Cohen, USC/ISI `IEN 137 <http://khavrinen.lcs.mit.edu/wollman/ien-137.txt>`_, dated April 1, 1980]

1.
   Describes a computer architecture in which, within a given multi-byte numeric representation, the most significant byte has the lowest address (the word is stored ‘big-end-first’).
   Most processors, including the IBM 370 family, the :ref:`PDP-10`\, the Motorola microprocessor families, and most of the various RISC designs are big-endian.
   Big-endian byte order is also sometimes called network order.
   See :ref:`little-endian`\, :ref:`middle-endian`\, :ref:`NUXI-problem`\, :ref:`swab`\.

2.
   An Internet address the wrong way round.
   Most of the world follows the Internet standard and writes email addresses starting with the name of the computer and ending up with the name of the country.
   In the U.K.: the Joint Academic Networking Team had decided to do it the other way round before the Internet domain standard was established.
   Most gateway sites have :ref:`ad-hockery` in their mailers to handle this, but can still be confused.
   In particular, the address :samp:`me\@uk.ac.bris.pys.as` could be interpreted in JANET's big-endian way as one in the U.K. (domain :samp:`uk`\) or in the standard little-endian way as one in the domain :samp:`as` (American Samoa) on the opposite side of the world.

