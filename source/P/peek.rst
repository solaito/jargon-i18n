.. _peek:

============================================================
peek
============================================================

n\.,vt\.

(and :ref:`poke`\) The commands in most microcomputer BASICs for directly accessing memory contents at an absolute address; often extended to mean the corresponding constructs in any :ref:`HLL` (peek reads memory, poke modifies it).
Much hacking on small, non-MMU micros used to consist of peeking around memory, more or less at random, to find the location where the system keeps interesting stuff.
Long (and variably accurate) lists of such addresses for various computers circulated.
The results of pokes at these addresses may be highly useful, mildly amusing, useless but neat, or (most likely) total :ref:`lossage` (see :ref:`killer-poke`\).

Since a :ref:`real-operating-system` provides useful, higher-level services for the tasks commonly performed with peeks and pokes on micros, and real languages tend not to encourage low-level memory groveling, a question like "How do I do a peek in C?"
is diagnostic of the :ref:`newbie`\.
(Of course, OS kernels often have to do exactly this; a real kernel hacker would unhesitatingly, if unportably, assign an absolute address to a pointer variable and indirect through it.)

