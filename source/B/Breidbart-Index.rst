.. _Breidbart-Index:

============================================================
Breidbart Index
============================================================

/bri:d´bart ind\@ks/

A measurement of the severity of spam invented by long-time hacker Seth Breidbart, used for programming cancelbots.
The Breidbart Index takes into account the fact that excessive multi-posting :ref:`EMP` is worse than excessive cross-posting :ref:`ECP`\.
The Breidbart Index is computed as follows: For each article in a spam, take the square-root of the number of newsgroups to which the article is posted.
The Breidbart Index is the sum of the square roots of all of the posts in the spam.
For example, one article posted to nine newsgroups and again to sixteen would have BI = sqrt(9) + sqrt(16) = 7.
It is generally agreed that a spam is cancelable if the Breidbart Index exceeds 20.

The Breidbart Index accumulates over a 45-day window.
Ten articles yesterday and ten articles today and ten articles tomorrow add up to a 30-article spam.
Spam fighters will often reset the count if you can convince them that the spam was accidental and/or you have seen the error of your ways and won't repeat it.
Breidbart Index can accumulate over multiple authors.
For example, the "Make Money Fast" pyramid scheme exceeded a BI of 20 a long time ago, and is now considered "cancel on sight".

