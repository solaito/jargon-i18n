.. _chain:

============================================================
chain
============================================================

1. vi\.
   [orig.
   from BASIC's :code:`CHAIN` statement] To hand off execution to a child or successor without going through the :ref:`OS` command interpreter that invoked it.
   The state of the parent program is lost and there is no returning to it.
   Though this facility used to be common on memory-limited micros and is still widely supported for backward compatibility, the jargon usage is semi-obsolescent; in particular, most Unix programmers will think of this as an :ref:`exec`\.
   Oppose the more modern subshell.

2. n\.
   A series of linked data areas within an operating system or application.
   Chain rattling is the process of repeatedly running through the linked data areas searching for one which is of interest to the executing program.
   The implication is that there is a very large number of links on the chain.

