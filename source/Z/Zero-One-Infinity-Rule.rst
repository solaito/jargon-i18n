.. _Zero-One-Infinity-Rule:

============================================================
Zero-One-Infinity Rule
============================================================

prov\.

"Allow none of :ref:`foo`\, one of :ref:`foo`\, or any number of :ref:`foo`\."
A rule of thumb for software design, which instructs one to not place :ref:`random` limits on the number of instances of a given entity (such as: windows in a window system, letters in an OS's filenames, etc.).
Specifically, one should either disallow the entity entirely, allow exactly one instance (an "exception"), or allow as many as the user wants — address space and memory permitting.

The logic behind this rule is that there are often situations where it makes clear sense to allow one of something instead of none.
However, if one decides to go further and allow N (for N > 1), then why not N+1?
And if N+1, then why not N+2, and so on?
Once above 1, there's no excuse not to allow any N; hence, :ref:`infinity`\.

Many hackers recall in this connection Isaac Asimov's SF novel *The Gods Themselves* in which a character announces that the number 2 is impossible — if you're going to believe in more than one universe, you might as well believe in an infinite number of them.

