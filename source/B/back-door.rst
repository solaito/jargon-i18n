.. _back-door:

============================================================
back door
============================================================

n\.

[common] A hole in the security of a system deliberately left in place by designers or maintainers.
The motivation for such holes is not always sinister; some operating systems, for example, come out of the box with privileged accounts intended for use by field service technicians or the vendor's maintenance programmers.
Syn.
:ref:`trap-door`\; may also be called a wormhole.
See also :ref:`iron-box`\, :ref:`cracker`\, :ref:`worm`\, :ref:`logic-bomb`\.

Historically, back doors have often lurked in systems longer than anyone expected or planned, and a few have become widely known.
Ken Thompson's 1983 Turing Award lecture to the ACM admitted the existence of a back door in early Unix versions that may have qualified as the most fiendishly clever security hack of all time.
In this scheme, the C compiler contained code that would recognize when the login command was being recompiled and insert some code recognizing a password chosen by Thompson, giving him entry to the system whether or not an account had been created for him.

Normally such a back door could be removed by removing it from the source code for the compiler and recompiling the compiler.
But to recompile the compiler, you have to *use* the compiler — so Thompson also arranged that the compiler would *recognize when it was compiling a version of itself*\, and insert into the recompiled compiler the code to insert into the recompiled login the code to allow Thompson entry — and, of course, the code to recognize itself and do the whole thing again the next time around!
And having done this once, he was then able to recompile the compiler from the original sources; the hack perpetuated itself invisibly, leaving the back door in place and active but with no trace in the sources.

The Turing lecture that reported this truly moby hack was later published as "Reflections on Trusting Trust", *Communications of the ACM 27*\, 8 (August 1984), pp.
761--763 (text available at `http://www.acm.org/classics/ <http://www.acm.org/classics/sep95/>`_).
Ken Thompson has since confirmed that this hack was implemented and that the Trojan Horse code did appear in the login binary of a Unix Support group machine.
Ken says the crocked compiler was never distributed.
Your editor has heard two separate reports that suggest that the crocked login did make it out of Bell Labs, notably to BBN, and that it enabled at least one late-night login across the network by someone using the login name "kt".

