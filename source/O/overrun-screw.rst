.. _overrun-screw:

============================================================
overrun screw
============================================================

n\.

[C programming] A variety of :ref:`fandango-on-core` produced by scribbling past the end of an array (C implementations typically have no checks for this error).
This is relatively benign and easy to spot if the array is static; if it is auto, the result may be to :ref:`smash-the-stack` — often resulting in :ref:`heisenbug`\s of the most diabolical subtlety.
The term overrun screw is used esp.
of scribbles beyond the end of arrays allocated with :manpage:`malloc(3)`\; this typically trashes the allocation header for the next block in the :ref:`arena`\, producing massive lossage within malloc and often a core dump on the next operation to use :manpage:`stdio(3)` or :manpage:`malloc(3)` itself.
See :ref:`spam`\, :ref:`overrun`\; see also :ref:`memory-leak`\, :ref:`memory-smash`\, :ref:`aliasing-bug`\, :ref:`precedence-lossage`\, :ref:`fandango-on-core`\, :ref:`secondary-damage`\.

