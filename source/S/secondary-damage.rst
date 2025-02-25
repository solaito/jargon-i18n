.. _secondary-damage:

============================================================
secondary damage
============================================================

n\.

When a fatal error occurs (esp.
a :ref:`segfault`\) the immediate cause may be that a pointer has been trashed due to a previous :ref:`fandango-on-core`\.
However, this fandango may have been due to an *earlier* fandango, so no amount of analysis will reveal (directly) how the damage occurred.
"The data structure was clobbered, but it was secondary damage."
By extension, the corruption resulting from ``N`` cascaded fandangoes on core is ‘``N``\th-level damage’.
There is at least one case on record in which 17 hours of :ref:`grovel`\ling with :code:`adb` actually dug up the underlying bug behind an instance of seventh-level damage!
The hacker who accomplished this near-superhuman feat was presented with an award by his fellows.

