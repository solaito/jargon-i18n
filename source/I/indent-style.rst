.. _indent-style:

============================================================
indent style
============================================================

n\.

[C, C++, and Java programmers] The rules one uses to indent code in a readable fashion.
There are four major C indent styles, described below; all have the aim of making it easier for the reader to visually track the scope of control constructs.
They have been inherited by C++ and Java, which have C-like syntaxes.
The significant variable is the placement of ``{`` and ``}`` with respect to the statement(s) they enclose and to the guard or controlling statement (:code:`if`\, :code:`else`\, :code:`for`\, :code:`while`\, or :code:`do`\) on the block, if any.

K&R style — Named after Kernighan & Ritchie, because the examples in :ref:`K-ampersand-R` are formatted this way.
Also called kernel style because the Unix kernel is written in it, and the ‘One True Brace Style’ (abbrev.
1TBS) by its partisans.
In C code, the body is typically indented by eight spaces (or one tab) per level, as shown here.
Four spaces are occasionally seen in C, but in C++ and Java four tends to be the rule rather than the exception.

.. code-block:: none


   if (<cond>) {
           <body>
   }

Allman style — Named for Eric Allman, a Berkeley hacker who wrote a lot of the BSD utilities in it (it is sometimes called BSD style).
Resembles normal indent style in Pascal and Algol.
It is the only style other than K&R in widespread use among Java programmers.
Basic indent per level shown here is eight spaces, but four (or sometimes three) spaces are generally preferred by C++ and Java programmers.

.. code-block:: none


   if (<cond>)
   {
           <body>
   }

Whitesmiths style — popularized by the examples that came with Whitesmiths C, an early commercial C compiler.
Basic indent per level shown here is eight spaces, but four spaces are occasionally seen.

.. code-block:: none


   if (<cond>)
           {
           <body>
           }

GNU style — Used throughout GNU EMACS and the Free Software Foundation code, and just about nowhere else.
Indents are always four spaces per level, with :code:`{` and :code:`}` halfway between the outer and inner indent levels.

.. code-block:: none


   if (<cond>)
     {
       <body>
     }

Surveys have shown the Allman and Whitesmiths styles to be the most common, with about equal mind shares.
K&R/1TBS used to be nearly universal, but is now much less common in C (the opening brace tends to get lost against the right paren of the guard part in an :code:`if` or :code:`while`\, which is a :ref:`Bad-Thing`\).
Defenders of 1TBS argue that any putative gain in readability is less important than their style's relative economy with vertical space, which enables one to see more code on one's screen at once.
The Java Language Specification legislates not only the capitalization of identifiers, but where nouns, adjectives, and verbs should be in method, class, interface, and variable names (section 6.8).
While the specification stops short of also standardizing on a bracing style, all source code originating from Sun Laboratories uses the K&R style.
This has set a precedent for Java programmers, which most follow.

Doubtless these issues will continue to be the subject of :ref:`holy-wars`\.

