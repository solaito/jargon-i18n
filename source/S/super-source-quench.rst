.. _super-source-quench:

============================================================
super source quench
============================================================

n\.

A special packet designed to shut up an Internet host.
The Internet Protocol (IP) has a control message called Source Quench that asks a host to transmit more slowly on a particular connection to avoid congestion.
It also has a Redirect control message intended to instruct a host to send certain packets to a different local router.
A "super source quench" is actually a redirect control packet, forged to look like it came from a local router, that instructs a host to send all packets to its own local loopback address.
This will effectively tie many Internet hosts up in knots.
Compare :ref:`Godzillagram`\, :ref:`breath-of-life-packet`\.

