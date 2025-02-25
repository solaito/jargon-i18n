.. _moby:

============================================================
moby
============================================================

/moh´bee/

[MIT: seems to have been in use among model railroad fans years ago.
Derived from Melville's *Moby Dick* (some say from ‘Moby Pickle’).
Now common.]

1. adj.
   Large, immense, complex, impressive.
   "A Saturn V rocket is a truly moby frob."
   "Some MIT undergrads pulled off a moby hack at the Harvard-Yale game."
   (See :ref:`Appendix A<appendixa>` for discussion.)

2. n\.
   obs.
   The maximum address space of a machine (see below).
   For a 680[234]0 or :ref:`VAX` or most modern 32-bit architectures, it is 4,294,967,296 8-bit bytes (4 gigabytes).

3.
   A title of address (never of third-person reference), usually used to show admiration, respect, and/or friendliness to a competent hacker.
   "Greetings, moby Dave.
   How's that address-book thing for the Mac going?"

4. adj.
   In backgammon, doubles on the dice, as in moby sixes, moby ones, etc.
   Compare this with :ref:`bignum` (sense 3): double sixes are both bignums and moby sixes, but moby ones are not bignums (the use of moby to describe double ones is sarcastic).
   Standard emphatic forms: Moby foo, moby win, moby loss.
   Foby moo: a spoonerism due to Richard Greenblatt.

5.
   The largest available unit of something which is available in discrete increments.
   Thus, ordering a "moby Coke" at the local fast-food joint is not just a request for a large Coke, it's an explicit request for the largest size they sell.

This term entered hackerdom with the Fabritek 256K memory added to the MIT AI PDP-6 machine, which was considered unimaginably huge when it was installed in the 1960s (at a time when a more typical memory size for a timesharing system was 72 kilobytes).
Thus, a moby is classically 256K 36-bit words, the size of a PDP-6 or PDP-10 moby.
Back when address registers were narrow the term was more generally useful, because when a computer had virtual memory mapping, it might actually have more physical memory attached to it than any one program could access directly.
One could then say "This computer has 6 mobies" meaning that the ratio of physical memory to address space is 6, without having to say specifically how much memory there actually is.
That in turn implied that the computer could timeshare six ‘full-sized’ programs without having to swap programs between memory and disk.

Nowadays the low cost of processor logic means that address spaces are usually larger than the most physical memory you can cram onto a machine, so most systems have much *less* than one theoretical ‘native’ moby of :ref:`core`\.
Also, more modern memory-management techniques (esp.
paging) make the ‘moby count’ less significant.
However, there is one series of widely-used chips for which the term could stand to be revived — the Intel 8088 and 80286 with their incredibly :ref:`brain-damaged` segmented-memory designs.
On these, a moby would be the 1-megabyte address span of a segment/offset pair (by coincidence, a PDP-10 moby was exactly 1 megabyte of 9-bit bytes).

