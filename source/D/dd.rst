.. _dd:

============================================================
dd
============================================================

/dee·dee/, vt\.

[Unix: from IBM :ref:`JCL`\] Equivalent to :ref:`cat` or :ref:`BLT`\.
Originally the name of a Unix copy command with special options suitable for block-oriented devices; it was often used in heavy-handed system maintenance, as in "Let's :code:`dd` the root partition onto a tape, then use the boot PROM to load it back on to a new disk".
The Unix :manpage:`dd(1)` was designed with a weird, distinctly non-Unixy keyword option syntax reminiscent of IBM System/360 JCL (which had an elaborate DD ‘Dataset Definition’ specification for I/O devices); though the command filled a need, the interface design was clearly a prank.
The jargon usage is now very rare outside Unix sites and now nearly obsolete even there, as :manpage:`dd(1)` has been :ref:`deprecated` for a long time (though it has no exact replacement).
The term has been displaced by :ref:`BLT` or simple English ‘copy’.

