.. _screaming-tty:

============================================================
screaming tty
============================================================

n\.

[Unix] A terminal line which spews an infinite number of random characters at the operating system.
This can happen if the terminal is either disconnected or connected to a powered-off terminal but still enabled for login; misconfiguration, misimplementation, or simple bad luck can start such a terminal screaming.
A screaming tty or two can seriously degrade the performance of a vanilla Unix system; the arriving "characters" are treated as userid/password pairs and tested as such.
The Unix password encryption algorithm is designed to be computationally intensive in order to foil brute-force crack attacks, so although none of the logins succeeds; the overhead of rejecting them all can be substantial.

