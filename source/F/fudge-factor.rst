.. _fudge-factor:

============================================================
fudge factor
============================================================

n\.

[common] A value or parameter that is varied in an ad hoc way to produce the desired result.
The terms tolerance and :ref:`slop` are also used, though these usually indicate a one-sided leeway, such as a buffer that is made larger than necessary because one isn't sure exactly how large it needs to be, and it is better to waste a little space than to lose completely for not having enough.
A fudge factor, on the other hand, can often be tweaked in more than one direction.
A good example is the fuzz typically allowed in floating-point calculations: two numbers being compared for equality must be allowed to differ by a small amount; if that amount is too small, a computation may never terminate, while if it is too large, results will be needlessly inaccurate.
Fudge factors are frequently adjusted incorrectly by programmers who don't fully understand their import.
See also :ref:`coefficient-of-X`\.

