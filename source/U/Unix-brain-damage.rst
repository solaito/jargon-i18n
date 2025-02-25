.. _Unix-brain-damage:

============================================================
Unix brain damage
============================================================

n\.

Something that has to be done to break a network program (typically a mailer) on a non-Unix system so that it will interoperate with Unix systems.
The hack may qualify as Unix brain damage if the program conforms to published standards and the Unix program in question does not.
Unix brain damage happens because it is much easier for other (minority) systems to change their ways to match non-conforming behavior than it is to change all the hundreds of thousands of Unix systems out there.

An example of Unix brain damage is a :ref:`kluge` in a mail server to recognize bare line feed (the Unix newline) as an equivalent form to the Internet standard newline, which is a carriage return followed by a line feed.
Such things can make even a hardened :ref:`jock` weep.

