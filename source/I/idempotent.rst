.. _idempotent:

============================================================
idempotent
============================================================

adj\.

[from mathematical techspeak] Acting as if used only once, even if used multiple times.
This term is often used with respect to :ref:`C` header files, which contain common definitions and declarations to be included by several source files.
If a header file is ever included twice during the same compilation (perhaps due to nested #include files), compilation errors can result unless the header file has protected itself against multiple inclusion; a header file so protected is said to be idempotent.
The term can also be used to describe an initialization subroutine that is arranged to perform some critical action exactly once, even if the routine is called several times.

