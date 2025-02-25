.. _troff:

============================================================
troff
============================================================

/T´rof/, /trof/, n\.

[Unix] The gray eminence of Unix text processing; a formatting and phototypesetting program, written originally in :ref:`PDP-11` assembler and then in barely-structured early C by the late Joseph Ossanna, modeled after the earlier ROFF which was in turn modeled after the :ref:`Multics` and :ref:`CTSS` program RUNOFF by Jerome Saltzer (*that* name came from the expression "to run off a copy").
A companion program, nroff, formats output for terminals and line printers.

In 1979, Brian Kernighan modified troff so that it could drive phototypesetters other than the Graphic Systems CAT.
His paper describing that work ("A Typesetter-independent troff," AT&T CSTR #97) explains troff's durability.
After discussing the program's "obvious deficiencies — a rebarbative input syntax, mysterious and undocumented properties in some areas, and a voracious appetite for computer resources" and noting the ugliness and extreme hairiness of the code and internals, Kernighan concludes:

.. code-block:: none


   None of these remarks should be taken as denigrating
   Ossanna's accomplishment with TROFF.  It has proven a
   remarkably robust tool, taking unbelievable abuse from a
   variety of preprocessors and being forced into uses that
   were never conceived of in the original design, all with
   considerable grace under fire.

The success of :ref:`TeX` and desktop publishing systems have reduced :code:`troff`\'s relative importance, but this tribute perfectly captures the strengths that secured :code:`troff` a place in hacker folklore; indeed, it could be taken more generally as an indication of those qualities of good programs that, in the long run, hackers most admire.

