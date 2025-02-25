.. _timesharing:

============================================================
timesharing
============================================================

[now primarily historical] Timesharing is the technique of scheduling a computer's time so that they are shared across multiple tasks and multiple users, with each user having the illusion that his or her computation is going on continuously.
John McCarthy, the inventor of :ref:`LISP`\, first `imagined this technique <http://www-formal.stanford.edu/jmc/history/timesharing/timesharing.html>`_\  in the late 1950s.
The first timesharing operating systems, BBN's "Little Hospital" and :ref:`CTSS`\, were deplayed in 1962-63.
The early hacker culture of the 1960s and 1970s grew up around the first generation of relatively cheap timesharing computers, notably the :ref:`DEC` 10, 11, and :ref:`VAX` lines.
But these were only cheap in a relative sense; though quite a bit less powerful than today's personal computers, they had to be shared by dozens or even hundreds of people each.
The early hacker comunities nucleated around places where it was relatively easy to get access to a timesharing account.

Nowadays, communications bandwidth is usually the most important constraint on what you can do with your computer.
Not so back then; timesharing machines were often loaded to capacity, and it was not uncommon for everyone's work to grind to a halt while the machine scheduler thrashed, trying to figure out what to do next.
Early hacker slang was replete with terms like cycle crunch and cycle drought for describing the consequences of too few instructions-per-second spread among too many users.
As GLS has noted, this sort of problem influenced the tendency of many hackers to work odd schedules.

One reason this is worth noting here is to make the point that the earliest hacker communities were physical, not distributed via networks; they consisted of hackers who shared a machine and therefore had to deal with many of the same problems with respect to it.
A system crash could idle dozens of eager programmers, all sitting in the same terminal room and with little to do but talk with each other until normal operation resumed.

Timesharing moved from being the luxury of a few large universities runing semi-experimental operating systems to being more generally available about 1975-76.
Hackers in search of more cycles and more control over their programming environment began to migrate off timesharing machines and onto what are now called workstations around 1983.
It took another ten years, the development of powerful 32-bit personal micros, the :ref:`Great-Internet-Explosion` before the migration was complete.
It is no coincidence that the last stages of this migration coincided with the development of the first open-source operating systems.

