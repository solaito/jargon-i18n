.. _security-through-obscurity:

============================================================
security through obscurity
============================================================

(alt.
: security by obscurity) A term applied by hackers to most OS vendors' favorite way of coping with security holes — namely, ignoring them, documenting neither any known holes nor the underlying security algorithms, trusting that nobody will find out about them and that people who do find out about them won't exploit them.
This "strategy" never works for long and occasionally sets the world up for debacles like the :ref:`RTM` worm of 1988 (see :ref:`Great-Worm`\), but once the brief moments of panic created by such events subside most vendors are all too willing to turn over and go back to sleep.
After all, actually fixing the bugs would siphon off the resources needed to implement the next user-interface frill on marketing's wish list — and besides, if they started fixing security bugs customers might begin to *expect* it and imagine that their warranties of merchantability gave them some sort of *right* to a system with fewer holes in it than a shotgunned Swiss cheese, and *then* where would we be?

Historical note: There are conflicting stories about the origin of this term.
It has been claimed that it was first used in the Usenet newsgroup :samp:`comp.sys.apollo` during a campaign to get HP/Apollo to fix security problems in its Unix- :ref:`clone` Aegis/DomainOS (they didn't change a thing).
:ref:`ITS` fans, on the other hand, say it was coined years earlier in opposition to the incredibly paranoid :ref:`Multics` people down the hall, for whom security was everything.
In the ITS culture it referred to (1) the fact that by the time a tourist figured out how to make trouble he'd generally gotten over the urge to make it, because he felt part of the community; and (2) (self-mockingly) the poor coverage of the documentation and obscurity of many commands.
One instance of *deliberate* security through obscurity is recorded; the command to allow patching the running ITS system (escape escape control-R) echoed as $$^D.
If you actually typed alt alt ^D, that set a flag that would prevent patching the system even if you later got it right.

