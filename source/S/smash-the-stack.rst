.. _smash-the-stack:

============================================================
smash the stack
============================================================

n\.

[C programming] To corrupt the execution stack by writing past the end of a local array or other data structure.
Code that smashes the stack can cause a return from the routine to jump to a random address, resulting in some of the most insidious data-dependent bugs known to mankind.
Variants include trash the stack, :ref:`scribble` the stack, :ref:`mangle` the stack; the term \*\* :ref:`mung` the stack is not used, as this is never done intentionally.
See :ref:`spam`\; see also :ref:`aliasing-bug`\, :ref:`fandango-on-core`\, :ref:`memory-leak`\, :ref:`memory-smash`\, :ref:`precedence-lossage`\, :ref:`overrun-screw`\.

