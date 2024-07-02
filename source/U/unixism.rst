.. _unixism:

============================================================
unixism
============================================================

n\.

A piece of code or a coding technique that depends on the protected multi-tasking environment with relatively low process-spawn overhead that exists on virtual-memory Unix systems.
Common :ref:`unixism`\s include: gratuitous use of :manpage:`fork(2)`\; the assumption that certain undocumented but well-known features of Unix libraries such as :manpage:`stdio(3)` are supported elsewhere; reliance on :ref:`obscure` side-effects of system calls (use of :manpage:`sleep(2)` with a 0 argument to clue the scheduler that you're willing to give up your time-slice, for example); the assumption that freshly allocated memory is zeroed; and the assumption that fragmentation problems won't arise from never :manpage:`free()`\ing memory.
Compare :ref:`vaxocentrism`\; see also :ref:`New-Jersey`\.

