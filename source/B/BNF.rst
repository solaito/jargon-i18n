.. _BNF:

============================================================
BNF
============================================================

/B·N·F/, n\.

1.
   [techspeak] Acronym for Backus Normal Form (later retronymed to Backus-Naur Form because BNF was not in fact a normal form), a metasyntactic notation used to specify the syntax of programming languages, command sets, and the like.
   Widely used for language descriptions but seldom documented anywhere, so that it must usually be learned by osmosis from other hackers.
   Consider this BNF for a U.S. postal address:

.. code-block:: none


    <postal-address> ::= <name-part> <street-address> <zip-part>

    <personal-part> ::= <name> | <initial> "."

    <name-part> ::= <personal-part> <last-name> [<jr-part>] <EOL>
                  | <personal-part> <name-part>

    <street-address> ::= [<apt>] <house-num> <street-name> <EOL>

    <zip-part> ::= <town-name> "," <state-code> <ZIP-code> <EOL>

This translates into English as: "A postal-address consists of a name-part, followed by a street-address part, followed by a zip-code part.
A personal-part consists of either a first name or an initial followed by a dot.
A name-part consists of either: a personal-part followed by a last name followed by an optional jr-part (Jr., Sr., or dynastic number) and end-of-line, or a personal part followed by a name part (this rule illustrates the use of recursion in BNFs, covering the case of people who use multiple first and middle names and/or initials).
A street address consists of an optional apartment specifier, followed by a street number, followed by a street name.
A zip-part consists of a town-name, followed by a comma, followed by a state code, followed by a ZIP-code followed by an end-of-line."
Note that many things (such as the format of a personal-part, apartment specifier, or ZIP-code) are left unspecified.
These are presumed to be obvious from context or detailed somewhere nearby.
See also :ref:`parse`\.

2.
   Any of a number of variants and extensions of BNF proper, possibly containing some or all of the :ref:`regexp` wildcards such as :code:`\*` or :code:`+`\.
   In fact the example above isn't the pure form invented for the Algol-60 report; it uses :code:`[]`\, which was introduced a few years later in IBM's PL/I definition but is now universally recognized.

3.
   In :ref:`science-fiction-fandom`\, a ‘Big-Name Fan’ (someone famous or notorious).
   Years ago a fan started handing out black-on-green BNF buttons at SF conventions; this confused the hacker contingent terribly.

