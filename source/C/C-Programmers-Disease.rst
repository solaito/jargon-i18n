.. _C-Programmers-Disease:

============================================================
C Programmer's Disease
============================================================

n\.

The tendency of the undisciplined C programmer to set arbitrary but supposedly generous static limits on table sizes (defined, if you're lucky, by constants in header files) rather than taking the trouble to do proper dynamic storage allocation.
If an application user later needs to put 68 elements into a table of size 50, the afflicted programmer reasons that he or she can easily reset the table size to 68 (or even as much as 70, to allow for future expansion) and recompile.
This gives the programmer the comfortable feeling of having made the effort to satisfy the user's (unreasonable) demands, and often affords the user multiple opportunities to explore the marvelous consequences of :ref:`fandango-on-core`\.
In severe cases of the disease, the programmer cannot comprehend why each fix of this kind seems only to further disgruntle the user.

