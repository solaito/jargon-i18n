.. _vaxocentrism:

============================================================
vaxocentrism
============================================================

/vak\`soh·sen´trizm/, n\.

[analogy with ‘ethnocentrism’] A notional disease said to afflict C programmers who persist in coding according to certain assumptions that are valid (esp.
under Unix) on :ref:`VAXen` but false elsewhere.
Among these are:

- The assumption that dereferencing a null pointer is safe because it is all bits 0, and location 0 is readable and 0.
  Problem: this may instead cause an illegal-address trap on non-VAXen, and even on VAXen under OSes other than BSD Unix.
  Usually this is an implicit assumption of sloppy code (forgetting to check the pointer before using it), rather than deliberate exploitation of a misfeature.

- The assumption that characters are signed.

- The assumption that a pointer to any one type can freely be cast into a pointer to any other type.
  A stronger form of this is the assumption that all pointers are the same size and format, which means you don't have to worry about getting the casts or types correct in calls.
  Problem: this fails on word-oriented machines or others with multiple pointer formats.

- The assumption that the parameters of a routine are stored in memory, on a stack, contiguously, and in strictly ascending or descending order.
  Problem: this fails on many RISC architectures.

- The assumption that pointer and integer types are the same size, and that pointers can be stuffed into integer variables (and vice-versa) and drawn back out without being truncated or mangled.
  Problem: this fails on segmented architectures or word-oriented machines with funny pointer formats.

- The assumption that a data type of any size may begin at any byte address in memory (for example, that you can freely construct and dereference a pointer to a word- or greater-sized object at an odd char address).
  Problem: this fails on many (esp.
  RISC) architectures better optimized for :ref:`HLL` execution speed, and can cause an illegal address fault or bus error.

- The (related) assumption that there is no padding at the end of types and that in an array you can thus step right from the last byte of a previous component to the first byte of the next one.
  This is not only machine- but compiler-dependent.

- The assumption that memory address space is globally flat and that the array reference :code:`foo[-1]` is necessarily valid.
  Problem: this fails at 0, or other places on segment-addressed machines like Intel chips (yes, segmentation is universally considered a :ref:`brain-damaged` way to design machines (see :ref:`moby`\), but that is a separate issue).

- The assumption that objects can be arbitrarily large with no special considerations.
  Problem: this fails on segmented architectures and under non-virtual-addressing environments.

- The assumption that the stack can be as large as memory.
  Problem: this fails on segmented architectures or almost anything else without virtual addressing and a paged stack.

- The assumption that bits and addressable units within an object are ordered in the same way and that this order is a constant of nature.
  Problem: this fails on :ref:`big-endian` machines.

- The assumption that it is meaningful to compare pointers to different objects not located within the same array, or to objects of different types.
  Problem: the former fails on segmented architectures, the latter on word-oriented machines or others with multiple pointer formats.

- The assumption that an int is 32 bits, or (nearly equivalently) the assumption that :code:`sizeof(int) ==sizeof(long)`\.
  Problem: this fails on :ref:`PDP-11`\s, 286-based systems and even on 386 and 68000 systems under some compilers (and on 64-bit systems like the Alpha, of course).

- The assumption that :code:`argv[]` is writable.
  Problem: this fails in many embedded-systems C environments and even under a few flavors of Unix.

Note that a programmer can validly be accused of vaxocentrism even if he or she has never seen a :ref:`VAX`\.
Some of these assumptions (esp.
2--5) were valid on the :ref:`PDP-11`\, the original C machine, and became endemic years before the VAX.
The terms vaxocentricity and all-the-world's-a-VAX syndrome have been used synonymously.

