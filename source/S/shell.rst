.. _shell:

============================================================
shell
============================================================

n\.

[orig.
:ref:`Multics` techspeak, widely propagated via Unix]

1.
   [techspeak] The command interpreter used to pass commands to an operating system; so called because it is the part of the operating system that interfaces with the outside world.

2.
   More generally, any interface program that mediates access to a special resource or :ref:`server` for convenience, efficiency, or security reasons; for this meaning, the usage is usually a shell around whatever.
   This sort of program is also called a wrapper.

3.
   A skeleton program, created by hand or by another program (like, say, a parser generator), which provides the necessary :ref:`incantation`\s to set up some task and the control flow to drive it (the term :ref:`driver` is sometimes used synonymously).
   The user is meant to fill in whatever code is needed to get real work done.
   This usage is common in the AI and Microsoft Windows worlds, and confuses Unix hackers.

Historical note: Apparently, the original Multics shell (sense 1) was so called because it was a shell (sense 3); it ran user programs not by starting up separate processes, but by dynamically linking the programs into its own code, calling them as subroutines, and then dynamically de-linking them on return.
The VMS command interpreter still does something very like this.

