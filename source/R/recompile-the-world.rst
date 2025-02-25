.. _recompile-the-world:

============================================================
recompile the world
============================================================

The surprisingly large amount of work that needs to be done as the result of any small but globally visible program change.
"The world" may mean the entirety of some huge program, or may in theory refer to every program of a certain class in the entire known universe.
For instance, "Add one #define to stdio.h, and you have to recompile the world."
This means that any minor change to the standard-I/O header file theoretically mandates recompiling every C program in existence, even if only to verify that the change didn't screw something else up.
In practice, you may not actually have to recompile the world, but the implication is that some human cleverness is required to figure out what parts can be safely left out.

