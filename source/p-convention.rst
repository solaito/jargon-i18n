.. _p-convention:

============================================================
The -P Convention
============================================================

Turning a word into a question by appending the syllable ‘P’; from the LISP convention of appending the letter ‘P’ to denote a predicate (a boolean-valued function).
The question should expect a yes/no answer, though it needn't.
(See :ref:`T` and :ref:`NIL`\.)

.. code-block:: none


       At dinnertime:
             Q: Foodp?
             A: Yeah, I'm pretty hungry. or T!

       At any time:
             Q: State-of-the-world-P?
             A: (Straight) I'm about to go home.
             A: (Humorous) Yes, the world has a state.

       On the phone to Florida:
             Q: State-p Florida?
             A: Been reading JARGON.TXT again, eh?

[Once, when we were at a Chinese restaurant, Bill Gosper wanted to know whether someone would like to share with him a two-person-sized bowl of soup.
His inquiry was: "Split-p soup?"
— GLS]

