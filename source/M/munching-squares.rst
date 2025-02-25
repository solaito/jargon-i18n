.. _munching-squares:

============================================================
munching squares
============================================================

n\.

A :ref:`display-hack` dating back to the PDP-1 (ca.
1962, reportedly discovered by Jackson Wright), which employs a trivial computation (repeatedly plotting the graph Y = X XOR T for successive values of T — see :ref:`HAKMEM` items 146--148) to produce an impressive display of moving and growing squares that devour the screen.
The initial value of T is treated as a parameter, which, when well-chosen, can produce amazing effects.
Some of these, later (re)discovered on the LISP machine, have been christened munching triangles (try AND for XOR and toggling points instead of plotting them), munching w's, and munching mazes.
More generally, suppose a graphics program produces an impressive and ever-changing display of some basic form, foo, on a display terminal, and does it using a relatively simple program; then the program (or the resulting display) is likely to be referred to as munching foos.
[This is a good example of the use of the word :ref:`foo` as a :ref:`metasyntactic-variable`\.]

