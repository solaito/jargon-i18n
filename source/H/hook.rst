.. _hook:

============================================================
hook
============================================================

n\.

A software or hardware feature included in order to simplify later additions or changes by a user.
For example, a simple program that prints numbers might always print them in base 10, but a more flexible version would let a variable determine what base to use; setting the variable to 5 would make the program print numbers in base 5.
The variable is a simple hook.
An even more flexible program might examine the variable and treat a value of 16 or less as the base to use, but treat any other number as the address of a user-supplied routine for printing a number.
This is a :ref:`hairy` but powerful hook; one can then write a routine to print numbers as Roman numerals, say, or as Hebrew characters, and plug it into the program through the hook.
Often the difference between a good program and a superb one is that the latter has useful hooks in judiciously chosen places.
Both may do the original job about equally well, but the one with the hooks is much more flexible for future expansion of capabilities ( :ref:`EMACS`\, for example, is *all* hooks).
The term user exit is synonymous but much more formal and less hackish.

