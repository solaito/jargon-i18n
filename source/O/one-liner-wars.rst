.. _one-liner-wars:

============================================================
one-liner wars
============================================================

n\.

A game popular among hackers who code in the language APL (see :ref:`write-only-language` and :ref:`line-noise`\).
The objective is to see who can code the most interesting and/or useful routine in one line of operators chosen from APL's exceedingly :ref:`hairy` primitive set.
A similar amusement was practiced among :ref:`TECO` hackers and is now popular among :ref:`Perl` aficionados.

Ken Iverson, the inventor of APL, has been credited with a one-liner that, given a number ``N``\, produces a list of the prime numbers from 1 to ``N`` inclusive.
It looks like this:

.. code-block:: none


    	(2=0+.=T∅.|T)/T←ιN

Here's a :ref:`Perl` program that prints primes:

.. code-block:: none


           perl -wle '(1 x $_) !~ /^(11+)\1+$/ && print while ++ $_'

In the Perl world this game is sometimes called Perl Golf because the player with the fewest (key)strokes wins.

