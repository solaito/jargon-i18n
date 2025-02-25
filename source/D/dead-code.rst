.. _dead-code:

============================================================
dead code
============================================================

n\.

Routines that can never be accessed because all calls to them have been removed, or code that cannot be reached because it is guarded by a control structure that provably must always transfer control somewhere else.
The presence of dead code may reveal either logical errors due to alterations in the program or significant changes in the assumptions and environment of the program (see also :ref:`software-rot`\); a good compiler should report dead code so a maintainer can think about what it means.
(Sometimes it simply means that an *extremely* defensive programmer has inserted :ref:`can-t-happen` tests which really can't happen — yet.)
Syn.
:ref:`grunge`\.
See also :ref:`dead`\, and :ref:`The Story of Mel'<story-of-mel>`\.

