.. _DWIM:

============================================================
DWIM
============================================================

/dwim/

[acronym, ‘Do What I Mean’]

1. adj.
   Able to guess, sometimes even correctly, the result intended when bogus input was provided.

2. n\.
   obs.
   The BBNLISP/INTERLISP function that attempted to accomplish this feat by correcting many of the more common errors.
   See :ref:`hairy`\.

3.
   Occasionally, an interjection hurled at a balky computer, esp.
   when one senses one might be tripping over legalisms (see :ref:`legalese`\).

4.
   Of a person, someone whose directions are incomprehensible and vague, but who nevertheless has the expectation that you will solve the problem using the specific method he/she has in mind.

Warren Teitelman originally wrote DWIM to fix his typos and spelling errors, so it was somewhat idiosyncratic to his style, and would often make hash of anyone else's typos if they were stylistically different.
Some victims of DWIM thus claimed that the acronym stood for ‘Damn Warren’s Infernal Machine!
'.

In one notorious incident, Warren added a DWIM feature to the command interpreter used at Xerox PARC.
One day another hacker there typed :code:`delete \*$` to free up some disk space.
(The editor there named backup files by appending :code:`$` to the original file name, so he was trying to delete any backup files left over from old editing sessions.)
It happened that there weren't any editor backup files, so DWIM helpfully reported :code:`\*$ not found, assuming you meant 'delete \*'.` It then started to delete all the files on the disk!
The hacker managed to stop it with a :ref:`Vulcan-nerve-pinch` after only a half dozen or so files were lost.

The disgruntled victim later said he had been sorely tempted to go to Warren's office, tie Warren down in his chair in front of his workstation, and then type :code:`delete \*$` twice.

DWIM is often suggested in jest as a desired feature for a complex program; it is also occasionally described as the single instruction the ideal computer would have.
Back when proofs of program correctness were in vogue, there were also jokes about DWIMC (Do What I Mean, Correctly).
A related term, more often seen as a verb, is DTRT (Do The Right Thing); see :ref:`Right-Thing`\.

