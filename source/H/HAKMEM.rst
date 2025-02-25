.. _HAKMEM:

============================================================
HAKMEM
============================================================

/hak´mem/, n\.

MIT AI Memo 239 (February 1972).
A legendary collection of neat mathematical and programming hacks contributed by many people at MIT and elsewhere.
(The title of the memo really is "HAKMEM", which is a 6-letterism for ‘hacks memo’.)
Some of them are very useful techniques, powerful theorems, or interesting unsolved problems, but most fall into the category of mathematical and computer trivia.
Here is a sampling of the entries (with authors), slightly paraphrased:

Item 41 (Gene Salamin): There are exactly 23,000 prime numbers less than :math:`2^{18}`\.

Item 46 (Rich Schroeppel): The most *probable* suit distribution in bridge hands is 4-4-3-2, as compared to 4-3-3-3, which is the most *evenly* distributed.
This is because the world likes to have unequal numbers: a thermodynamic effect saying things will not be in the state of lowest energy, but in the state of lowest disordered energy.

Item 81 (Rich Schroeppel): Count the magic squares of order 5 (that is, all the 5-by-5 arrangements of the numbers from 1 to 25 such that all rows, columns, and diagonals add up to the same number).
There are about 320 million, not counting those that differ only by rotation and reflection.

Item 154 (Bill Gosper): The myth that any given programming language is machine independent is easily exploded by computing the sum of powers of 2.
If the result loops with period ``= 1`` with sign ``+``\, you are on a sign-magnitude machine.
If the result loops with period ``= 1`` at ``-1``\, you are on a twos-complement machine.
If the result loops with period greater than 1, including the beginning, you are on a ones-complement machine.
If the result loops with period greater than 1, not including the beginning, your machine isn't binary — the pattern should tell you the base.
If you run out of memory, you are on a string or bignum system.
If arithmetic overflow is a fatal error, some fascist pig with a read-only mind is trying to enforce machine independence.
But the very ability to trap overflow is machine dependent.
By this strategy, consider the universe, or, more precisely, algebra: Let ``X =`` the sum of many powers of 2 = ...111111 (base 2).
Now add ``X`` to itself: ``X + X =`` ...111110.
Thus, ``2X = X - 1``\, so ``X = -1``\.
Therefore algebra is run on a machine (the universe) that is two's-complement.

Item 174 (Bill Gosper and Stuart Nelson): 21963283741 is the only number such that if you represent it on the :ref:`PDP-10` as both an integer and a floating-point number, the bit patterns of the two representations are identical.

Item 176 (Gosper): The "banana phenomenon" was encountered when processing a character string by taking the last 3 letters typed out, searching for a random occurrence of that sequence in the text, taking the letter following that occurrence, typing it out, and iterating.
This ensures that every 4-letter string output occurs in the original.
The program typed BANANANANANANANA.... We note an ambiguity in the phrase, "the ``N``\th occurrence of."
In one sense, there are five 00's in 0000000000; in another, there are nine.
The editing program TECO finds five.
Thus it finds only the first ANA in BANANA, and is thus obligated to type N next.
By Murphy's Law, there is but one NAN, thus forcing A, and thus a loop.
An option to find overlapped instances would be useful, although it would require backing up ``N`` − 1 characters before seeking the next ``N``\-character string.

Note: This last item refers to a :ref:`Dissociated-Press` implementation.
See also :ref:`banana-problem`\.

HAKMEM also contains some rather more complicated mathematical and technical items, but these examples show some of its fun flavor.

An HTML transcription of the entire document is available at `http://www.inwap.com/pdp10/hbaker/hakmem/hakmem.html <http://www.inwap.com/pdp10/hbaker/hakmem/hakmem.html>`_.

