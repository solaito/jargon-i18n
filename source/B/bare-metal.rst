.. _bare-metal:

============================================================
bare metal
============================================================

n\.

1.
   [common] New computer hardware, unadorned with such snares and delusions as an :ref:`operating-system`\, an :ref:`HLL`\, or even assembler.
   Commonly used in the phrase programming on the bare metal, which refers to the arduous work of :ref:`bit-bashing` needed to create these basic tools for a new machine.
   Real bare-metal programming involves things like building boot proms and BIOS chips, implementing basic monitors used to test device drivers, and writing the assemblers that will be used to write the compiler back ends that will give the new machine a real development environment.

2.
   "Programming on the bare metal" is also used to describe a style of :ref:`hand-hacking` that relies on bit-level peculiarities of a particular hardware design, esp.
   tricks for speed and space optimization that rely on crocks such as overlapping instructions (or, as in the famous case described in :ref:`The Story of Mel'<story-of-mel>` (in Appendix A), interleaving of opcodes on a magnetic drum to minimize fetch delays due to the device's rotational latency).
   This sort of thing has become rare as the relative costs of programming time and machine resources have changed, but is still found in heavily constrained environments such as industrial embedded systems.
   See :ref:`Real-Programmer`\.

