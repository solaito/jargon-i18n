.. _arena:

============================================================
arena
============================================================

n\.

[common; Unix] The area of memory attached to a process by :manpage:`brk(2)` and :manpage:`sbrk(2)` and used by :manpage:`malloc(3)` as dynamic storage.
So named from a :code:`malloc: corrupt arena` message emitted when some early versions detected an impossible value in the free block list.
See :ref:`overrun-screw`\, :ref:`aliasing-bug`\, :ref:`memory-leak`\, :ref:`memory-smash`\, :ref:`smash-the-stack`\.

