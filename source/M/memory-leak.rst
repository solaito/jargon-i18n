.. _memory-leak:

============================================================
memory leak
============================================================

n\.

An error in a program's dynamic-store allocation logic that causes it to fail to reclaim discarded memory, leading to eventual collapse due to memory exhaustion.
Also (esp.
at CMU) called :ref:`core-leak`\.
These problems were severe on older machines with small, fixed-size address spaces, and special "leak detection" tools were commonly written to root them out.
With the advent of virtual memory, it is unfortunately easier to be sloppy about wasting a bit of memory (although when you run out of memory on a VM machine, it means you've got a *real* leak!).
See :ref:`aliasing-bug`\, :ref:`fandango-on-core`\, :ref:`smash-the-stack`\, :ref:`precedence-lossage`\, :ref:`overrun-screw`\, :ref:`leaky-heap`\, :ref:`leak`\.

