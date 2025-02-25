.. _spamblock:

============================================================
spamblock
============================================================

/spam´blok/, n\.

[poss.
by analogy to sunblock] Text inserted in an email address to render it invalid and thus useless to spammers.
For example, the address <jrandom@hacker.org> might be transformed to <jrandom@NOSPAM.hacker.org>.
Adding spamblock to an address is often referred to as munging it (see :ref:`munge`\).
This evasion tactic depends on the fact that most spammers collect names with some sort of :ref:`address-harvester` on volumes too high to de-mung by hand, but individual humans reading an email message can readily spot and remove a spamblock in the From address.

Note: This is not actually a very effective tactic, and may already be passing out of use in early 1999 after about two years of life.
In both mail and news, it's essentially impossible to keep a smart address harvester from mining out the addresses in the message header and trace lines.
Therefore the only people who can be protected are third parties mentioned by email address in the message — not a common enough case to interest spammers.

