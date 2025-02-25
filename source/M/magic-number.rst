.. _magic-number:

============================================================
magic number
============================================================

n\.

[Unix/C; common]

1.
   In source code, some non-obvious constant whose value is significant to the operation of a program and that is inserted inconspicuously in-line ( :ref:`hardcoded`\), rather than expanded in by a symbol set by a commented :code:`#define`\.
   Magic numbers in this sense are bad style.

2.
   A number that encodes critical information used in an algorithm in some opaque way.
   The classic examples of these are the numbers used in hash or CRC functions, or the coefficients in a linear congruential generator for pseudo-random numbers.
   This sense actually predates and was ancestral to the more common sense

3.
   Special data located at the beginning of a binary data file to indicate its type to a utility.
   Under Unix, the system and various applications programs (especially the linker) distinguish between types of executable file by looking for a magic number.
   Once upon a time, these magic numbers were :ref:`PDP-11` branch instructions that skipped over header data to the start of executable code; 0407, for example, was octal for ‘branch 16 bytes relative’.
   Many other kinds of files now have magic numbers somewhere; some magic numbers are, in fact, strings, like the ``!<arch>`` at the beginning of a Unix archive file or the ``%!`` leading PostScript files.
   Nowadays only a :ref:`wizard` knows the spells to create magic numbers.
   How do you choose a fresh magic number of your own?
   Simple — you pick one at random.
   See?
   It's magic!

4.
   An input that leads to a computational boundary condition, where algorithm behavior becomes discontinuous.
   Numeric overflows (particularly with signed data types) and run-time errors (divide by zero, stack overflows) are indications of magic numbers.
   The Y2K scare was probably the most notorious magic number non-incident.

*The* magic number, on the other hand, is ``7±2``\.
See *The magical number seven, plus or minus two: some limits on our capacity for processing information* by George Miller, in the *Psychological Review* 63:81-97 (1956).
This classic paper established the number of distinct items (such as numeric digits) that humans can hold in short-term memory.
Among other things, this strongly influenced the interface design of the phone system.

