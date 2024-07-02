.. _COME-FROM:

============================================================
COME FROM
============================================================

n\.

A semi-mythical language construct dual to the ‘go to’; :code:`COME FROM` <label> would cause the referenced label to act as a sort of trapdoor, so that if the program ever reached it control would quietly and :ref:`automagically` be transferred to the statement following the :code:`COME FROM`\.
:code:`COME FROM` was first proposed in R. Lawrence Clark's *A Linguistic Contribution to GOTO-less programming*\, which appeared in a 1973 :ref:`Datamation` issue (and was reprinted in the April 1984 issue of *Communications of the ACM*\).
This parodied the then-raging ‘structured programming’ :ref:`holy-wars` (see :ref:`considered-harmful`\).
Mythically, some variants are the assigned COME FROM and the computed COME FROM (parodying some nasty control constructs in FORTRAN and some extended BASICs).
Of course, multi-tasking (or non-determinism) could be implemented by having more than one :code:`COME FROM` statement coming from the same label.

In some ways the FORTRAN :code:`DO` looks like a :code:`COME FROM` statement.
After the terminating statement number/:code:`CONTINUE` is reached, control continues at the statement following the DO.
Some generous FORTRANs would allow arbitrary statements (other than :code:`CONTINUE`\) for the statement, leading to examples like:

.. code-block:: none


         DO 10 I=1,LIMIT
   C imagine many lines of code here, leaving the
   C original DO statement lost in the spaghetti...
         WRITE(6,10) I,FROB(I)
    10   FORMAT(1X,I5,G10.4)

in which the trapdoor is just after the statement labeled 10.
(This is particularly surprising because the label doesn't appear to have anything to do with the flow of control at all!)
While sufficiently astonishing to the unsuspecting reader, this form of :code:`COME FROM` statement isn't completely general.
After all, control will eventually pass to the following statement.
The implementation of the general form was left to Univac FORTRAN, ca.
1975 (though a roughly similar feature existed on the IBM 7040 ten years earlier).
The statement :code:`AT 100` would perform a :code:`COME FROM 100`\.
It was intended strictly as a debugging aid, with dire consequences promised to anyone so deranged as to use it in production code.
More horrible things had already been perpetrated in production languages, however; doubters need only contemplate the :code:`ALTER` verb in :ref:`COBOL`\.
:code:`COME FROM` was supported under its own name for the first time 15 years later, in C-INTERCAL (see :ref:`INTERCAL`\, :ref:`retrocomputing`\); knowledgeable observers are still reeling from the shock.

