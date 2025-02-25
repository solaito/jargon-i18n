.. _fencepost-error:

============================================================
fencepost error
============================================================

n\.

1.
   [common] A problem with the discrete equivalent of a boundary condition, often exhibited in programs by iterative loops.
   From the following problem: "If you build a fence 100 feet long with posts 10 feet apart, how many posts do you need?"
   (Either 9 or 11 is a better answer than the obvious 10.)
   For example, suppose you have a long list or array of items, and want to process items ``m`` through ``n``\; how many items are there?
   The obvious answer is ``n - m``\, but that is off by one; the right answer is ``n - m + 1``\.
   A program that used the ‘obvious’ formula would have a fencepost error in it.
   See also :ref:`zeroth` and :ref:`off-by-one-error`\, and note that not all off-by-one errors are fencepost errors.
   The game of Musical Chairs involves a catastrophic off-by-one error where ``N`` people try to sit in ``N - 1`` chairs, but it's not a fencepost error.
   Fencepost errors come from counting things rather than the spaces between them, or vice versa, or by neglecting to consider whether one should count one or both ends of a row.

2.
   [rare] An error induced by unexpected regularities in input values, which can (for instance) completely thwart a theoretically efficient binary tree or hash table implementation.
   (The error here involves the difference between expected and worst case behaviors of an algorithm.)

