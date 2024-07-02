.. _aliasing-bug:

============================================================
aliasing bug
============================================================

n\.

A class of subtle programming errors that can arise in code that does dynamic allocation, esp.
via :manpage:`malloc(3)` or equivalent.
If several pointers address (are aliases for) a given hunk of storage, it may happen that the storage is freed or reallocated (and thus moved) through one alias and then referenced through another, which may lead to subtle (and possibly intermittent) lossage depending on the state and the allocation history of the malloc :ref:`arena`\.
Avoidable by use of allocation strategies that never alias allocated core, or by use of higher-level languages, such as :ref:`LISP`\, which employ a garbage collector (see :ref:`GC`\).
Also called a :ref:`stale-pointer-bug`\.
See also :ref:`precedence-lossage`\, :ref:`smash-the-stack`\, :ref:`fandango-on-core`\, :ref:`memory-leak`\, :ref:`memory-smash`\, :ref:`overrun-screw`\, :ref:`spam`\.

Historical note: Though this term is nowadays associated with C programming, it was already in use in a very similar sense in the Algol-60 and FORTRAN communities in the 1960s.

