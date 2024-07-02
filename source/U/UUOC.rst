.. _UUOC:

============================================================
UUOC
============================================================

[from the comp.unix.shell group on Usenet] Stands for Useless Use of cat; the reference is to the Unix command :manpage:`cat(1)`\, not the feline animal.
As received wisdom on comp.unix.shell observes, "The purpose of cat is to concatenate (or ‘catenate’) files.
If it's only one file, concatenating it with nothing at all is a waste of time, and costs you a process."
Nevertheless one sees people doing

.. code-block:: none


   cat file | some_command and its args ...

instead of the equivalent and cheaper

.. code-block:: none


   <file some_command and its args ...

or (equivalently and more classically)

.. code-block:: none


   some_command and its args ... <file

Since 1995, occasional awards for UUOC have been given out, usually by Perl luminary Randal L. Schwartz.
There is a `web page <http://www.ling.helsinki.fi/~reriksso/unix/award.html>`_\  devoted to this and other similar awards.

