.. _heisenbug:

============================================================
heisenbug
============================================================

/hi:´zen·buhg/, n\.

[from Heisenberg's Uncertainty Principle in quantum physics] A bug that disappears or alters its behavior when one attempts to probe or isolate it.
(This usage is not even particularly fanciful; the use of a debugger sometimes alters a program's operating environment significantly enough that buggy code, such as that which relies on the values of uninitialized memory, behaves quite differently.)
Antonym of :ref:`Bohr-bug`\; see also :ref:`mandelbug`\, :ref:`schroedinbug`\.
In C, nine out of ten heisenbugs result from uninitialized auto variables, :ref:`fandango-on-core` phenomena (esp.
lossage related to corruption of the malloc :ref:`arena`\) or errors that :ref:`smash-the-stack`\.

