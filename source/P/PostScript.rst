.. _PostScript:

============================================================
PostScript
============================================================

n\.

A page description language, based on work originally done by John Gaffney at Evans and Sutherland in 1976, evolving through ‘JaM’ (‘John and Martin’, Martin Newell) at :ref:`XEROX-PARC`\, and finally implemented in its current form by John Warnock et al.
after he and Chuck Geschke founded Adobe Systems Incorporated in 1982.
PostScript gets its leverage by using a full programming language, rather than a series of low-level escape sequences, to describe an image to be printed on a laser printer or other output device (in this it parallels :ref:`EMACS`\, which exploited a similar insight about editing tasks).
It is also noteworthy for implementing on-the fly rasterization, from Bezier curve descriptions, of high-quality fonts at low (e.g.
300 dpi) resolution (it was formerly believed that hand-tuned bitmap fonts were required for this task).
Hackers consider PostScript to be among the most elegant hacks of all time, and the combination of technical merits and widespread availability has made PostScript the language of choice for graphical output.

