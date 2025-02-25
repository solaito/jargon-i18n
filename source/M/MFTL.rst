.. _MFTL:

============================================================
MFTL
============================================================

/M·F·T·L/

[abbreviation: ‘My Favorite Toy Language’]

1. adj.
   Describes a talk on a programming language design that is heavy on the syntax (with lots of BNF), sometimes even talks about semantics (e.g., type systems), but rarely, if ever, has any content (see :ref:`content-free`\).
   More broadly applied to talks — even when the topic is not a programming language — in which the subject matter is gone into in unnecessary and meticulous detail at the sacrifice of any conceptual content.
   "Well, it was a typical MFTL talk".

2. n\.
   Describes a language about which the developers are passionate (often to the point of proselytic zeal) but no one else cares about.
   Applied to the language by those outside the originating group.
   "He cornered me about type resolution in his MFTL."

The first great goal in the mind of the designer of an MFTL is usually to write a compiler for it, then bootstrap the design away from contamination by lesser languages by writing a compiler for it in itself.
Thus, the standard put-down question at an MFTL talk is "Has it been used for anything besides its own compiler?"
On the other hand, a (compiled) language that cannot even be used to write its own compiler is beneath contempt.
(The qualification has become necessary because of the increasing popularity of interpreted languages like :ref:`Perl` and :ref:`Python`\.)
See :ref:`break-even-point`\.
(On a related note, Doug McIlroy once proposed a test of the generality and utility of a language and the operating system under which it is compiled: "Is the output of a FORTRAN program acceptable as input to the FORTRAN compiler?"
In other words, can you write programs that write programs?
(See :ref:`toolsmith`\.)
Alarming numbers of (language, OS) pairs fail this test, particularly when the language is FORTRAN; aficionados are quick to point out that :ref:`Unix` (even using FORTRAN) passes it handily.
That the test could ever be failed is only surprising to those who have had the good fortune to have worked only under modern systems which lack OS-supported and -imposed "file types".)

