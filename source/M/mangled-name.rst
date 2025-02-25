.. _mangled-name:

============================================================
mangled name
============================================================

n\.

A name, appearing in a C++ object file, that is a coded representation of the object declaration as it appears in the source.
Mangled names are used because C++ allows multiple objects to have the same name, as long as they are distinguishable in some other way, such as by having different parameter types.
Thus, the internal name must have that additional information embedded in it, using the limited character set allowed by most linkers.
For instance, one popular compiler encodes the standard library function declaration "memchr(const void\*,int,unsigned int)" as "\@memchr$qpxviui".

