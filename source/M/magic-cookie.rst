.. _magic-cookie:

============================================================
magic cookie
============================================================

n\.

[Unix; common]

1.
   Something passed between routines or programs that enables the receiver to perform some operation; a capability ticket or opaque identifier.
   Especially used of small data objects that contain data encoded in a strange or intrinsically machine-dependent way.
   E.g., on non-Unix OSes with a non-byte-stream model of files, the result of :manpage:`ftell(3)` may be a magic cookie rather than a byte offset; it can be passed to :manpage:`fseek(3)`\, but not operated on in any meaningful way.
   The phrase it hands you a magic cookie means it returns a result whose contents are not defined but which can be passed back to the same or some other program later.

2.
   An in-band code for changing graphic rendition (e.g., inverse video or underlining) or performing other control functions (see also :ref:`cookie`\).
   Some older terminals would leave a blank on the screen corresponding to mode-change magic cookies; this was also called a :ref:`glitch` (or occasionally a turd; compare :ref:`mouse-droppings`\).
   See also :ref:`cookie`\.

