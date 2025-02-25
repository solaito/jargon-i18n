.. _ping:

============================================================
ping
============================================================

[from the submariners' term for a sonar pulse]

1. n\.
   Slang term for a small network message (ICMP ECHO) sent by a computer to check for the presence and alertness of another.
   The Unix command :manpage:`ping(8)` can be used to do this manually (note that :manpage:`ping(8)`\'s author denies the widespread folk etymology that the name was ever intended as an acronym for ‘Packet INternet Groper’).
   Occasionally used as a phone greeting.
   See :ref:`ACK`\, also :ref:`ENQ`\.

2. vt\.
   To verify the presence of.

3. vt\.
   To get the attention of.

4. vt\.
   To send a message to all members of a :ref:`mailing-list` requesting an :ref:`ACK` (in order to verify that everybody's addresses are reachable).
   "We haven't heard much of anything from Geoff, but he did respond with an ACK both times I pinged jargon-friends."

5. n\.
   A quantum packet of happiness.
   People who are very happy tend to exude pings; furthermore, one can intentionally create pings and aim them at a needy party (e.g., a depressed person).
   This sense of ping may appear as an exclamation; "Ping!"
   (I'm happy; I am emitting a quantum of happiness; I have been struck by a quantum of happiness).
   The form "pingfulness", which is used to describe people who exude pings, also occurs.
   (In the standard abuse of language, "pingfulness" can also be used as an exclamation, in which case it's a much stronger exclamation than just "ping"!).
   Oppose :ref:`blargh`\.

The funniest use of ‘ping’ to date was `described <http://groups.google.com/groups?selm=1991Jan23.211609.877%40news.cs.indiana.edu>`_\  in January 1991 by Steve Hayman on the Usenet group :samp:`comp.sys.next`\.
He was trying to isolate a faulty cable segment on a TCP/IP Ethernet hooked up to a NeXT machine, and got tired of having to run back to his console after each cabling tweak to see if the ping packets were getting through.
So he used the sound-recording feature on the NeXT, then wrote a script that repeatedly invoked :manpage:`ping(8)`\, listened for an echo, and played back the recording on each returned packet.
Result?
A program that caused the machine to repeat, over and over, "Ping ... ping ... ping ..." as long as the network was up.
He turned the volume to maximum, ferreted through the building with one ear cocked, and found a faulty tee connector in no time.

