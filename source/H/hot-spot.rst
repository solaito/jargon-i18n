.. _hot-spot:

============================================================
hot spot
============================================================

n\.

1.
   [primarily used by C/Unix programmers, but spreading] It is received wisdom that in most programs, less than 10% of the code eats 90% of the execution time; if one were to graph instruction visits versus code addresses, one would typically see a few huge spikes amidst a lot of low-level noise.
   Such spikes are called hot spots and are good candidates for heavy optimization or :ref:`hand-hacking`\.
   The term is especially used of tight loops and recursions in the code's central algorithm, as opposed to (say) initial set-up costs or large but infrequent I/O operations.
   See :ref:`tune`\, :ref:`hand-hacking`\.

2.
   The active location of a cursor on a bit-map display.
   "Put the mouse's hot spot on the ‘ON’ widget and click the left button."

3.
   A screen region that is sensitive to mouse gestures, which trigger some action.
   World Wide Web pages now provide the :ref:`canonical` examples; WWW browsers present hypertext links as hot spots which, when clicked on, point the browser at another document (these are specifically called :ref:`hotlink`\s).

4.
   In a massively parallel computer with shared memory, the one location that all 10,000 processors are trying to read or write at once (perhaps because they are all doing a :ref:`busy-wait` on the same lock).

5.
   More generally, any place in a hardware design that turns into a performance bottleneck due to resource contention.

