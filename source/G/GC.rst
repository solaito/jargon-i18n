.. _GC:

============================================================
GC
============================================================

/G·C/

[from LISP terminology; Garbage Collect]

1. vt\.
   To clean up and throw away useless things.
   "I think I'll GC the top of my desk today."

2. vt\.
   To recycle, reclaim, or put to another use.

3. n\.
   An instantiation of the garbage collector process.

Garbage collection is computer-science techspeak for a particular class of strategies for dynamically but transparently reallocating computer memory (i.e., without requiring explicit allocation and deallocation by higher-level software).
One such strategy involves periodically scanning all the data in memory and determining what is no longer accessible; useless data items are then discarded so that the memory they occupy can be recycled and used for another purpose.
Implementations of the LISP language usually use garbage collection.

In jargon, the full phrase is sometimes heard but the :ref:`abbrev` GC is more frequently used because it is shorter.
Note that there is an ambiguity in usage that has to be resolved by context: "I'm going to garbage-collect my desk" usually means to clean out the drawers, but it could also mean to throw away or recycle the desk itself.

