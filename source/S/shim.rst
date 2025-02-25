.. _shim:

============================================================
shim
============================================================

n\.

1.
   A small piece of data inserted in order to achieve a desired memory alignment or other addressing property.
   For example, the :ref:`PDP-11` Unix linker, in split I&D (instructions and data) mode, inserts a two-byte shim at location 0 in data space so that no data object will have an address of 0 (and be confused with the C null pointer).
   See also :ref:`loose-bytes`\.

2.
   A type of small transparent image inserted into HTML documents by certain WYSIWYG HTML editors, used to set the spacing of elements meant to have a fixed positioning within a TABLE or DIVision.
   Hackers who work on the HTML code of such pages afterwards invariably curse these for their crocky dependence on the particular spacing of original image file, the editor that generated them, and the version of the browser used to view them.
   Worse, they are a poorly designed :ref:`kludge` which the advent of Cascading Style Sheets makes wholly unnecessary; Any fool can plainly see that use of borders, layers and positioned elements is the Right Thing (or would be if adequate support for CSS were more common).

