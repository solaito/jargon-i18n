.. _live-data:

============================================================
live data
============================================================

n\.

1.
   Data that is written to be interpreted and takes over program flow when triggered by some un-obvious operation, such as viewing it.
   One use of such hacks is to break security.
   For example, some smart terminals have commands that allow one to download strings to program keys; this can be used to write live data that, when listed to the terminal, infects it with a security-breaking :ref:`virus` that is triggered the next time a hapless user strikes that key.
   For another, there are some well-known bugs in :ref:`vi` that allow certain texts to send arbitrary commands back to the machine when they are simply viewed.

2.
   In C code, data that includes pointers to function :ref:`hook`\s (executable code).

3.
   An object, such as a :ref:`trampoline`\, that is constructed on the fly by a program and intended to be executed as code.

