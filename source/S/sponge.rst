.. _sponge:

============================================================
sponge
============================================================

n\.

[Unix] A special case of a :ref:`filter` that reads its entire input before writing any output; the canonical example is a sort utility.
Unlike most filters, a sponge can conveniently overwrite the input file with the output data stream.
If a file system has versioning (as ITS did and VMS does now) the sponge/filter distinction loses its usefulness, because directing filter output would just write a new version.
See also :ref:`slurp`\.

