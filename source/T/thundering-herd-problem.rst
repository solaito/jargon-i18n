.. _thundering-herd-problem:

============================================================
thundering herd problem
============================================================

Scheduler thrashing.
This can happen under Unix when you have a number of processes that are waiting on a single event.
When that event (a connection to the web server, say) happens, every process which could possibly handle the event is awakened.
In the end, only one of those processes will actually be able to do the work, but, in the meantime, all the others wake up and contend for CPU time before being put back to sleep.
Thus the system thrashes briefly while a herd of processes thunders through.
If this starts to happen many times per second, the performance impact can be significant.

