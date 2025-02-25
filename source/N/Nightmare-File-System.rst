.. _Nightmare-File-System:

============================================================
Nightmare File System
============================================================

n\.

Pejorative hackerism for Sun's Network File System (NFS).
In any nontrivial network of Suns where there is a lot of NFS cross-mounting, when one Sun goes down, the others often freeze up.
Some machine tries to access the down one, and (getting no response) repeats indefinitely.
This causes it to appear dead to some messages (what is actually happening is that it is locked up in what should have been a brief excursion to a higher :ref:`spl` level).
Then another machine tries to reach either the down machine or the pseudo-down machine, and itself becomes pseudo-down.
The first machine to discover the down one is now trying both to access the down one and to respond to the pseudo-down one, so it is even harder to reach.
This situation snowballs very quickly, and soon the entire network of machines is frozen — worst of all, the user can't even abort the file access that started the problem!
Many of NFS's problems are excused by partisans as being an inevitable result of its statelessness, which is held to be a great feature (critics, of course, call it a great :ref:`misfeature`\).
(ITS partisans are apt to cite this as proof of Unix's alleged bogosity; ITS had a working NFS-like shared file system with none of these problems in the early 1970s.)
See also :ref:`broadcast-storm`\.

