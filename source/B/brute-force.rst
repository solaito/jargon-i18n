.. _brute-force:

============================================================
brute force
============================================================

adj\.

Describes a primitive programming style, one in which the programmer relies on the computer's processing power instead of using his or her own intelligence to simplify the problem, often ignoring problems of scale and applying naive methods suited to small problems directly to large ones.
The term can also be used in reference to programming style: brute-force programs are written in a heavyhanded, tedious way, full of repetition and devoid of any elegance or useful abstraction (see also :ref:`brute-force-and-ignorance`\).

The :ref:`canonical` example of a brute-force algorithm is associated with the ‘traveling salesman problem’ (TSP), a classical :ref:`NP-`\hard problem: Suppose a person is in, say, Boston, and wishes to drive to ``N`` other cities.
In what order should the cities be visited in order to minimize the distance travelled?
The brute-force method is to simply generate all possible routes and compare the distances; while guaranteed to work and simple to implement, this algorithm is clearly very stupid in that it considers even obviously absurd routes (like going from Boston to Houston via San Francisco and New York, in that order).
For very small ``N`` it works well, but it rapidly becomes absurdly inefficient when ``N`` increases (for ``N = 15``\, there are already 1,307,674,368,000 possible routes to consider, and for ``N = 1000`` — well, see :ref:`bignum`\).
Sometimes, unfortunately, there is no better general solution than brute force.
See also :ref:`NP-` and :ref:`rubber-hose-cryptanalysis`\.

A more simple-minded example of brute-force programming is finding the smallest number in a large list by first using an existing program to sort the list in ascending order, and then picking the first number off the front.

Whether brute-force programming should actually be considered stupid or not depends on the context; if the problem is not terribly big, the extra CPU time spent on a brute-force solution may cost less than the programmer time it would take to develop a more ‘intelligent’ algorithm.
Additionally, a more intelligent algorithm may imply more long-term complexity cost and bug-chasing than are justified by the speed improvement.

Ken Thompson, co-inventor of Unix, is reported to have uttered the epigram "When in doubt, use brute force".
He probably intended this as a :ref:`ha-ha-only-serious`\, but the original Unix kernel's preference for simple, robust, and portable algorithms over :ref:`brittle` ‘smart’ ones does seem to have been a significant factor in the success of that OS.
Like so many other tradeoffs in software design, the choice between brute force and complex, finely-tuned cleverness is often a difficult one that requires both engineering savvy and delicate esthetic judgment.

