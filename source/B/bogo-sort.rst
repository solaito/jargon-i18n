.. _bogo-sort:

============================================================
bogo-sort
============================================================

/boh\`goh·sort´/, n\.

(var.
: stupid-sort) The archetypical perversely awful algorithm (as opposed to :ref:`bubble-sort`\, which is merely the generic *bad* algorithm).
Bogo-sort is equivalent to repeatedly throwing a deck of cards in the air, picking them up at random, and then testing whether they are in order.
It serves as a sort of canonical example of awfulness.
Looking at a program and seeing a dumb algorithm, one might say "Oh, I see, this program uses bogo-sort."
Esp.
appropriate for algorithms with factorial or super-exponential running time in the average case and probabilistically infinite worst-case running time.
Compare :ref:`bogus`\, :ref:`brute-force`\.

A spectacular variant of bogo-sort has been proposed which has the interesting property that, if the Many Worlds interpretation of quantum mechanics is true, it can sort an arbitrarily large array in linear time.
(In the Many-Worlds model, the result of any quantum action is to split the universe-before into a sheaf of universes-after, one for each possible way the state vector can collapse; in any one of the universes-after the result appears random.)
The steps are: 1.
Permute the array randomly using a quantum process, 2.
If the array is not sorted, destroy the universe (checking that the list is sorted requires O(n) time).
Implementation of step 2 is left as an exercise for the reader.

