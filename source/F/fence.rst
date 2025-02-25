.. _fence:

============================================================
fence
============================================================

n\.

1.
   A sequence of one or more distinguished ( :ref:`out-of-band`\) characters (or other data items), used to delimit a piece of data intended to be treated as a unit (the computer-science literature calls this a sentinel).
   The NUL (ASCII 0000000) character that terminates strings in C is a fence.
   Hex FF is also (though slightly less frequently) used this way.
   See :ref:`zigamorph`\.

2.
   An extra data value inserted in an array or other data structure in order to allow some normal test on the array's contents also to function as a termination test.
   For example, a highly optimized routine for finding a value in an array might artificially place a copy of the value to be searched for after the last slot of the array, thus allowing the main search loop to search for the value without having to check at each pass whether the end of the array had been reached.

3.
   [among users of optimizing compilers] Any technique, usually exploiting knowledge about the compiler, that blocks certain optimizations.
   Used when explicit mechanisms are not available or are overkill.
   Typically a hack: "I call a dummy procedure there to force a flush of the optimizer's register-coloring info" can be expressed by the shorter "That's a fence procedure".

