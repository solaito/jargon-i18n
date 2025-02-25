.. _daemon:

============================================================
daemon
============================================================

/day´mn/, /dee´mn/, n\.

[from Maxwell's Demon, later incorrectly retronymed as ‘Disk And Execution MONitor’] A program that is not invoked explicitly, but lies dormant waiting for some condition(s) to occur.
The idea is that the perpetrator of the condition need not be aware that a daemon is lurking (though often a program will commit an action only because it knows that it will implicitly invoke a daemon).
For example, under :ref:`ITS`\, writing a file on the LPT spooler's directory would invoke the spooling daemon, which would then print the file.
The advantage is that programs wanting (in this example) files printed need neither compete for access to nor understand any idiosyncrasies of the LPT.
They simply enter their implicit requests and let the daemon decide what to do with them.
Daemons are usually spawned automatically by the system, and may either live forever or be regenerated at intervals.

Daemon and :ref:`demon` are often used interchangeably, but seem to have distinct connotations.
The term daemon was introduced to computing by :ref:`CTSS` people (who pronounced it /dee´mon/) and used it to refer to what ITS called a :ref:`dragon`\; the prototype was a program called DAEMON that automatically made tape backups of the file system.
Although the meaning and the pronunciation have drifted, we think this glossary reflects current (2003) usage.

