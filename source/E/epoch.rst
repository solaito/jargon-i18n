.. _epoch:

============================================================
epoch
============================================================

n\.

[Unix: prob.
: from astronomical timekeeping] The time and date corresponding to 0 in an operating system's clock and timestamp values.
Under most Unix versions the epoch is 00:00:00 GMT, January 1, 1970; under VMS, it's 00:00:00 of November 17, 1858 (base date of the U.S.
Naval Observatory's ephemerides); on a Macintosh, it's the midnight beginning January 1 1904.
System time is measured in seconds or :ref:`tick`\s past the epoch.
Weird problems may ensue when the clock wraps around (see :ref:`wrap-around`\), which is not necessarily a rare event; on systems counting 10 ticks per second, a signed 32-bit count of ticks is good only for 6.8 years.
The 1-tick-per-second clock of Unix is good only until January 18, 2038, assuming at least some software continues to consider it signed and that word lengths don't increase by then.
See also :ref:`wall-time`\.
Microsoft Windows, on the other hand, has an epoch problem every 49.7 days — but this is seldom noticed as Windows is almost incapable of staying up continuously for that long.

