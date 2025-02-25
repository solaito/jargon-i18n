.. _snap:

============================================================
snap
============================================================

v\.

To replace a pointer to a pointer with a direct pointer; to replace an old address with the forwarding address found there.
If you telephone the main number for an institution and ask for a particular person by name, the operator may tell you that person's extension before connecting you, in the hopes that you will snap your pointer and dial direct next time.
The underlying metaphor may be that of a rubber band stretched through a number of intermediate points; if you remove all the thumbtacks in the middle, it snaps into a straight line from first to last.
See :ref:`chase-pointers`\.

Often, the behavior of a :ref:`trampoline` is to perform an error check once and then snap the pointer that invoked it so as henceforth to bypass the trampoline (and its one-shot error check).
In this context one also speaks of snapping links.
For example, in a LISP implementation, a function interface trampoline might check to make sure that the caller is passing the correct number of arguments; if it is, and if the caller and the callee are both compiled, then snapping the link allows that particular path to use a direct procedure-call instruction with no further overhead.

