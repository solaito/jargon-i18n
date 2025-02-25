.. _hole:

============================================================
hole
============================================================

n\.

A region in an otherwise :ref:`flat` entity which is not actually present.
For example, some Unix filesystems can store large files with holes so that unused regions of the file are never actually stored on disk.
(In techspeak, these are referred to as ‘sparse’ files.)
As another example, the region of memory in IBM PCs reserved for memory-mapped I/O devices which may not actually be present is called ‘the I/O hole’, since memory-management systems must skip over this area when filling user requests for memory.

