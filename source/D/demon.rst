.. _demon:

============================================================
demon
============================================================

n\.

1.
   Often used equivalently to :ref:`daemon` — especially in the :ref:`Unix` world, where the latter spelling and pronunciation is considered mildly archaic.

2.
   [MIT; now probably obsolete] A portion of a program that is not invoked explicitly, but that lies dormant waiting for some condition(s) to occur.
   See :ref:`daemon`\.
   The distinction is that demons are usually processes within a program, while daemons are usually programs running on an operating system.

Demons in sense 2 are particularly common in AI programs.
For example, a knowledge-manipulation program might implement inference rules as demons.
Whenever a new piece of knowledge was added, various demons would activate (which demons depends on the particular piece of data) and would create additional pieces of knowledge by applying their respective inference rules to the original piece.
These new pieces could in turn activate more demons as the inferences filtered down through chains of logic.
Meanwhile, the main program could continue with whatever its primary task was.

