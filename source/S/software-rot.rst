.. _software-rot:

============================================================
software rot
============================================================

n\.

Term used to describe the tendency of software that has not been used in a while to :ref:`lose`\; such failure may be semi-humorously ascribed to :ref:`bit-rot`\.
More commonly, software rot strikes when a program's assumptions become out of date.
If the design was insufficiently :ref:`robust`\, this may cause it to fail in mysterious ways.
Syn.
code rot.
See also :ref:`link-rot`\.

For example, owing to endemic shortsightedness in the design of COBOL programs, a good number of them succumbed to software rot when their 2-digit year counters underwent :ref:`wrap-around` at the beginning of the year 2000.
Actually, related lossages often afflict centenarians who have to deal with computer software designed by unimaginative clods.
One such incident became the focus of a minor public flap in 1990, when a gentleman born in 1889 applied for a driver's license renewal in Raleigh, North Carolina.
The new system refused to issue the card, probably because with 2-digit years the ages 101 and 1 cannot be distinguished.

Historical note: Software rot in an even funnier sense than the mythical one was a real problem on early research computers (e.g., the R1; see :ref:`grind-crank`\).
If a program that depended on a peculiar instruction hadn't been run in quite a while, the user might discover that the opcodes no longer did the same things they once did.
("Hey, so-and-so needs an instruction to do such-and-such.
We can :ref:`snarf` this opcode, right?
No one uses it.")
Another classic example of this sprang from the time an MIT hacker found a simple way to double the speed of the unconditional jump instruction on a PDP-6, so he patched the hardware.
Unfortunately, this broke some fragile timing software in a music-playing program, throwing its output out of tune.
This was fixed by adding a defensive initialization routine to compare the speed of a timing loop with the real-time clock; in other words, it figured out how fast the PDP-6 was that day, and corrected appropriately.

Compare :ref:`bit-rot`\.

