.. _sharchive:

============================================================
sharchive
============================================================

/shar´ki:v/, n\.

[Unix and Usenet; from /bin/sh archive] A :ref:`flatten`\ed representation of a set of one or more files, with the unique property that it can be unflattened (the original files restored) by feeding it through a standard Unix shell; thus, a sharchive can be distributed to anyone running Unix, and no special unpacking software is required.
Sharchives are also intriguing in that they are typically created by shell scripts; the script that produces sharchives is thus a script which produces self-unpacking scripts, which may themselves contain scripts.
Sharchives are also commonly referred to as ‘shar files’ after the name of the most common program for generating them.

The downsides of sharchives are that they are an ideal venue for :ref:`Trojan-horse` attacks and that, for recipients not running Unix, no simple un-sharchiving program is possible; sharchives can and do make use of arbitrarily-powerful shell features.
For these reasons, this technique has largely fallen out of use since the mid-1990s.

