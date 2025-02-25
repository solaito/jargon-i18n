.. _death-code:

============================================================
death code
============================================================

n\.

A routine whose job is to set everything in the computer — registers, memory, flags, everything — to zero, including that portion of memory where it is running; its last act is to :ref:`stomp-on` its own "store zero" instruction.
Death code isn't very useful, but writing it is an interesting hacking challenge on architectures where the instruction set makes it possible, such as the PDP-8 (it has also been done on the DG Nova).

Perhaps the ultimate death code is on the TI 990 series, where all registers are actually in RAM, and the instruction "store immediate 0" has the opcode "0".
The PC will immediately wrap around core as many times as it can until a user hits HALT.
Any empty memory location is death code.
Worse, the manufacturer recommended use of this instruction in startup code (which would be in ROM and therefore survive).

