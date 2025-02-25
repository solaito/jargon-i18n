.. _bottom-up-implementation:

============================================================
bottom-up implementation
============================================================

n\.

Hackish opposite of the techspeak term top-down design.
It has been received wisdom in most programming cultures that it is best to design from higher levels of abstraction down to lower, specifying sequences of action in increasing detail until you get to actual code.
Hackers often find (especially in exploratory designs that cannot be closely specified in advance) that it works best to *build* things in the opposite order, by writing and testing a clean set of primitive operations and then knitting them together.
Naively applied, this leads to hacked-together bottom-up implementations; a more sophisticated response is middle-out implementation, in which scratch code within primitives at the mid-level of the system is gradually replaced with a more polished version of the lowest level at the same time the structure above the midlevel is being built.

