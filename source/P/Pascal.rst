.. _Pascal:

============================================================
Pascal
============================================================

n\.

An Algol-descended language designed by Niklaus Wirth on the CDC 6600 around 1967--68 as an instructional tool for elementary programming.
This language, designed primarily to keep students from shooting themselves in the foot and thus extremely restrictive from a general-purpose-programming point of view, was later promoted as a general-purpose tool and, in fact, became the ancestor of a large family of languages including Modula-2 and Ada (see also :ref:`bondage-and-discipline-language`\).
The hackish point of view on Pascal was probably best summed up by a devastating (and, in its deadpan way, screamingly funny) 1981 paper by Brian Kernighan (of :ref:`K-ampersand-R` fame) entitled *Why Pascal is Not My Favorite Programming Language*\, which was turned down by the technical journals but circulated widely via photocopies.
It was eventually published in *Comparing and Assessing Programming Languages*\, edited by Alan Feuer and Narain Gehani (Prentice-Hall, 1984).
Part of his discussion is worth repeating here, because its criticisms are still apposite to Pascal itself after many years of improvement and could also stand as an indictment of many other bondage-and-discipline languages.
(The entire essay is available at `http://www.lysator.liu.se/c/bwk-on-pascal.html <http://www.lysator.liu.se/c/bwk-on-pascal.html>`_.)
At the end of a summary of the case against Pascal, Kernighan wrote:

.. code-block:: none


   9. There is no escape

   This last point is perhaps the most important.  The language is
   inadequate but circumscribed, because there is no way to escape its
   limitations.  There are no casts to disable the type-checking when necessary.
   There is no way to replace the defective run-time environment with a sensible
   one, unless one controls the compiler that defines the standard
   procedures.  The language is closed.

   People who use Pascal for serious programming fall into a fatal trap.
   Because the language is impotent, it must be extended.  But each group extends
   Pascal in its own direction, to make it look like whatever language they
   really want.  Extensions for separate compilation, FORTRAN-like COMMON, string
   data types, internal static variables, initialization, octal numbers, bit
   operators, etc., all add to the utility of the language for one group but
   destroy its portability to others.

   I feel that it is a mistake to use Pascal for anything much beyond its
   original target.  In its pure form, Pascal is a toy language, suitable for
   teaching but not for real programming.

Pascal has since been entirely displaced (mainly by :ref:`C`\) from the niches it had acquired in serious applications and systems programming, and from its role as a teaching language by Java.

