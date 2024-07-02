.. _precedence-lossage:

============================================================
precedence lossage
============================================================

/pre´s\@·dens los'\@j/, n\.

[C programmers] Coding error in an expression due to unexpected grouping of arithmetic or logical operators by the compiler.
Used esp.
of certain common coding errors in C due to the nonintuitively low precedence levels of :code:`&`\, :code:`\|`\, :code:`^`\, :code:`<<`\, and :code:`>>` (for this reason, experienced C programmers deliberately forget the language's :ref:`baroque` precedence hierarchy and parenthesize defensively).
Can always be avoided by suitable use of parentheses.
:ref:`LISP` fans enjoy pointing out that this can't happen in *their* favorite language, which eschews precedence entirely, requiring one to use explicit parentheses everywhere.
See :ref:`aliasing-bug`\, :ref:`memory-leak`\, :ref:`memory-smash`\, :ref:`smash-the-stack`\, :ref:`fandango-on-core`\, :ref:`overrun-screw`\.

