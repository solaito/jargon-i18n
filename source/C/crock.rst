.. _crock:

============================================================
crock
============================================================

n\.

[from the American scatologism crock of shit]

1.
   An awkward feature or programming technique that ought to be made cleaner.
   For example, using small integers to represent error codes without the program interpreting them to the user (as in, for example, Unix :manpage:`make(1)`\, which returns code 139 for a process that dies due to :ref:`segfault`\).

2.
   A technique that works acceptably, but which is quite prone to failure if disturbed in the least.
   For example, a too-clever programmer might write an assembler which mapped instruction mnemonics to numeric opcodes algorithmically, a trick which depends far too intimately on the particular bit patterns of the opcodes.
   (For another example of programming with a dependence on actual opcode values, see :ref:`The Story of Mel'<story-of-mel>` in Appendix A.)
   Many crocks have a tightly woven, almost completely unmodifiable structure.
   See :ref:`kluge`\, :ref:`brittle`\.
   The adjectives crockish and crocky, and the nouns crockishness and crockitude, are also used.

