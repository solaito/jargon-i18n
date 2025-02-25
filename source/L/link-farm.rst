.. _link-farm:

============================================================
link farm
============================================================

n\.

[Unix] A directory tree that contains many links to files in a master directory tree of files.
Link farms save space when one is maintaining several nearly identical copies of the same source tree — for example, when the only difference is architecture-dependent object files.
"Let's freeze the source and then rebuild the FROBOZZ-3 and FROBOZZ-4 link farms."
Link farms may also be used to get around restrictions on the number of :code:`-I` (include-file directory) arguments on older C preprocessors.
However, they can also get completely out of hand, becoming the filesystem equivalent of :ref:`spaghetti-code`\.
See also :ref:`farm`\.

