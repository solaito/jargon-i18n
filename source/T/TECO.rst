.. _TECO:

============================================================
TECO
============================================================

/tee´koh/, n\.,v\.
obs\.

1.
   [originally an acronym for ‘[paper] Tape Editor and COrrector’; later, ‘Text Editor and COrrector’] n. A text editor developed at MIT and modified by just about everybody.
   With all the dialects included, TECO may have been the most prolific editor in use before :ref:`EMACS`\, to which it was directly ancestral.
   Noted for its powerful programming-language-like features and its unspeakably :ref:`hairy` syntax.
   It is literally the case that every string of characters is a valid TECO program (though probably not a useful one); one common game used to be mentally working out what the TECO commands corresponding to human names did.

2. vt\.
   Originally, to edit using the TECO editor in one of its infinite variations (see below).

3. vt.,obs.
   To edit even when TECO is *not* the editor being used!
   This usage is rare and now primarily historical.

As an example of TECO's obscurity, here is a TECO program that takes a list of names such as:

.. code-block:: none


   Loser, J. Random
   Quux, The Great
   Dick, Moby

sorts them alphabetically according to surname, and then puts the surname last, removing the comma, to produce the following:

.. code-block:: none


   Moby Dick
   J. Random Loser
   The Great Quux

The program is

.. code-block:: none


   [1 J^P$L$$
   J <.-Z; .,(S,$ -D .)FX1 @F^B $K :L I $ G1 L>$$

(where ^B means ‘Control-B’ (ASCII 0000010) and $ is actually an :ref:`alt` or escape (ASCII 0011011) character).

In fact, this very program was used to produce the second, sorted list from the first list.
The first hack at it had a :ref:`bug`\: GLS (the author) had accidentally omitted the :code:`\@` in front of :code:`F^B`\, which as anyone can see is clearly the :ref:`Wrong-Thing`\.
It worked fine the second time.
There is no space to describe all the features of TECO, but it may be of interest that :code:`^P` means ‘sort’ and :code:`J<.-Z; ... L>` is an idiomatic series of commands for ‘do once for every line’.

In mid-1991, TECO is pretty much one with the dust of history, having been replaced in the affections of hackerdom by :ref:`EMACS`\.
Descendants of an early (and somewhat lobotomized) version adopted by DEC can still be found lurking on VMS and a couple of crufty :ref:`PDP-11` operating systems, however, and ports of the more advanced MIT versions remain the focus of some antiquarian interest.
See also :ref:`retrocomputing`\, :ref:`write-only-language`\.

