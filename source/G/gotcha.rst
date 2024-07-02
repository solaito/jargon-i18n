.. _gotcha:

============================================================
gotcha
============================================================

n\.

A :ref:`misfeature` of a system, especially a programming language or environment, that tends to breed bugs or mistakes because it is both enticingly easy to invoke and completely unexpected and/or unreasonable in its outcome.
For example, a classic gotcha in :ref:`C` is the fact that :code:`if (a=b) {code;`\} is syntactically valid and sometimes even correct.
It puts the value of :code:`b` into :code:`a` and then executes :code:`code` if :code:`a` is non-zero.
What the programmer probably meant was :code:`if (a==b) {code;`\}, which executes :code:`code` if :code:`a` and :code:`b` are equal.

