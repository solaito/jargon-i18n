.. _can-t-happen:

============================================================
can't happen
============================================================

The traditional program comment for code executed under a condition that should never be true, for example a file size computed as negative.
Often, such a condition being true indicates data corruption or a faulty algorithm; it is almost always handled by emitting a fatal error message and terminating or crashing, since there is little else that can be done.
Some case variant of "can't happen" is also often the text emitted if the ‘impossible’ error actually happens!
Although "can't happen" events are genuinely infrequent in production code, programmers wise enough to check for them habitually are often surprised at how frequently they are triggered during development and how many headaches checking for them turns out to head off.
See also :ref:`firewall-code` (sense 2).

