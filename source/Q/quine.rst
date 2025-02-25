.. _quine:

============================================================
quine
============================================================

/kwi:n/, n\.

[from the name of the logician Willard van Orman Quine, via Douglas Hofstadter] A program that generates a copy of its own source text as its complete output.
Devising the shortest possible quine in some given programming language is a common hackish amusement.
(We ignore some variants of BASIC in which a program consisting of a single empty string literal reproduces itself trivially.)
Here is one classic quine:

.. code-block:: none


   ((lambda (x)
     (list x (list (quote quote) x)))
    (quote
       (lambda (x)
         (list x (list (quote quote) x)))))

This one works in LISP or Scheme.
It's relatively easy to write quines in other languages such as Postscript which readily handle programs as data; much harder (and thus more challenging!)
in languages like C which do not.
Here is a classic C quine for ASCII machines:

.. code-block:: none


   char*f="char*f=%c%s%c;main()
   {printf(f,34,f,34,10);}%c";
   main(){printf(f,34,f,34,10);}

For excruciatingly exact quinishness, remove the interior line breaks.
Here is another elegant quine in ANSI C:

.. code-block:: none


   #define q(k)main(){return!puts(#k"\nq("#k")");}
   q(#define q(k)main(){return!puts(#k"\nq("#k")");})

Some infamous :ref:`Obfuscated-C-Contest` entries have been quines that reproduced in exotic ways.
There is an amusing `Quine Home Page <http://www.nyx.org/~gthompso/quine.htm>`_.

