.. _hidden-flag:

============================================================
hidden flag
============================================================

n\.

[scientific computation] An extra option added to a routine without changing the calling sequence.
For example, instead of adding an explicit input variable to instruct a routine to give extra diagnostic output, the programmer might just add a test for some otherwise meaningless feature of the existing inputs, such as a negative mass.
The use of hidden flags can make a program very hard to debug and understand, but is all too common wherever programs are hacked on in a hurry.

