.. _fork-bomb:

============================================================
fork bomb
============================================================

n\.

[Unix] A particular species of :ref:`wabbit` that can be written in one line of C (:code:`main() {for(;;)fork();`\}) or shell (:code:`$0 & $0 &`\) on any Unix system, or occasionally created by an egregious coding bug.
A fork bomb process ‘explodes’ by recursively spawning copies of itself (using the Unix system call :manpage:`fork(2)`\).
Eventually it eats all the process table entries and effectively wedges the system.
Fortunately, fork bombs are relatively easy to spot and kill, so creating one deliberately seldom accomplishes more than to bring the just wrath of the gods down upon the perpetrator.
Also called a fork bunny.
See also :ref:`logic-bomb`\.

