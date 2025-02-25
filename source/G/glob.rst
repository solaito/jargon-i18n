.. _glob:

============================================================
glob
============================================================

/glob/, not, /glohb/, v\.,n\.

[Unix; common] To expand special characters in a wildcarded name, or the act of so doing (the action is also called globbing).
The Unix conventions for filename wildcarding have become sufficiently pervasive that many hackers use some of them in written English, especially in email or news on technical topics.
Those commonly encountered include the following:

.. list-table::

   * - \*
     - wildcard for any string (see also :ref:`UN-asterisk-X`\)
   * - ?
     - wildcard for any single character (generally read this way only at the beginning or in the middle of a word)
   * - []
     - delimits a wildcard matching any of the enclosed characters
   * - {}
     - alternation of comma-separated alternatives; thus, ‘foo{baz,qux}’ would be read as ‘foobaz’ or ‘fooqux’

Some examples: "He said his name was [KC]arl" (expresses ambiguity).
"I don't read talk.politics.\*" (any of the talk.politics subgroups on :ref:`Usenet`\).
Other examples are given under the entry for :ref:`X`\.
Note that glob patterns are similar, but not identical, to those used in :ref:`regexp`\s.

Historical note: The jargon usage derives from :code:`glob`\, the name of a subprogram that expanded wildcards in archaic pre-Bourne versions of the Unix shell.

