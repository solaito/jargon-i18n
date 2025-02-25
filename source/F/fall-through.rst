.. _fall-through:

============================================================
fall through
============================================================

v\.

(n. fallthrough, var.
: fall-through)

1.
   To exit a loop by exhaustion, i.e., by having fulfilled its exit condition rather than via a break or exception condition that exits from the middle of it.
   This usage appears to be *really* old, dating from the 1940s and 1950s.

2.
   To fail a test that would have passed control to a subroutine or some other distant portion of code.

3.
   In C, ‘fall-through’ occurs when the flow of execution in a switch statement reaches a :code:`case` label other than by jumping there from the switch header, passing a point where one would normally expect to find a :code:`break`\.
   A trivial example:

.. code-block:: none


   switch (color)
   {
   case GREEN:
      do_green();
      break;
   case PINK:
      do_pink();
      /* FALL THROUGH */
   case RED:
      do_red();
      break;
   default:
      do_blue();
      break;
   }

The variant spelling /\* FALL THRU \*/ is also common.

The effect of the above code is to :manpage:`do_green()` when color is :code:`GREEN`\, :manpage:`do_red()` when color is :code:`RED`\, :manpage:`do_blue()` on any other color other than :code:`PINK`\, and (and this is the important part) :manpage:`do_pink()` *and then* :manpage:`do_red()` when color is :code:`PINK`\.
Fall-through is :ref:`considered-harmful` by some, though there are contexts (such as the coding of state machines) in which it is natural; it is generally considered good practice to include a comment highlighting the fall-through where one would normally expect a break.
See also :ref:`Duffs-device`\.

