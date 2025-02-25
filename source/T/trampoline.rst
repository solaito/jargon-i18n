.. _trampoline:

============================================================
trampoline
============================================================

n\.

An incredibly :ref:`hairy` technique, found in some :ref:`HLL` and program-overlay implementations (e.g., on the Macintosh), that involves on-the-fly generation of small executable (and, likely as not, self-modifying) code objects to do indirection between code sections.
Under BSD and possibly in other Unixes, trampoline code is used to transfer control from the kernel back to user mode when a signal (which has had a handler installed) is sent to a process.
These pieces of :ref:`live-data` are called trampolines.
Trampolines are notoriously difficult to understand in action; in fact, it is said by those who use this term that the trampoline that doesn't bend your brain is not the true trampoline.
See also :ref:`snap`\.

