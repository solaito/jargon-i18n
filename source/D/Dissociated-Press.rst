.. _Dissociated-Press:

============================================================
Dissociated Press
============================================================

n\.

[play on ‘Associated Press’; perhaps inspired by a reference in the 1950 Bugs Bunny cartoon *What's Up, Doc?*\] An algorithm for transforming any text into potentially humorous garbage even more efficiently than by passing it through a :ref:`marketroid`\.
The algorithm starts by printing any ``N`` consecutive words (or letters) in the text.
Then at every step it searches for any random occurrence in the original text of the last ``N`` words (or letters) already printed and then prints the next word or letter.
:ref:`EMACS` has a handy command for this.
Here is a short example of word-based Dissociated Press applied to an earlier version of this Jargon File:

.. code-block:: none


   wart: n. A small, crocky
   feature that sticks out of an array (C has no checks
   for this).  This is relatively benign and easy to spot if the phrase is bent
   so as to be not worth paying attention to the medium in question.

Here is a short example of letter-based Dissociated Press applied to the same source:

.. code-block:: none

    window sysIWYG: n. A bit was named aften /bee´t@/ prefer to use the other
   guy's re, especially in every cast a chuckle on neithout getting into useful
   informash speech makes removing a featuring a move or usage actual
   abstractionsidered interj. Indeed spectace

A hackish idle pastime is to apply letter-based Dissociated Press to a random body of text and :ref:`vgrep` the output in hopes of finding an interesting new word.
(In the preceding example, ‘window sysIWYG’ and ‘informash’ show some promise.)
Iterated applications of Dissociated Press usually yield better results.
Similar techniques called travesty generators have been employed with considerable satirical effect to the utterances of Usenet flamers; see :ref:`pseudo`\.

