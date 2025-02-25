.. _thunk:

============================================================
thunk
============================================================

/thuhnk/, n\.

1.
   [obs.
   ]"A piece of coding which provides an address:", according to P. Z. Ingerman, who invented thunks in 1961 as a way of binding actual parameters to their formal definitions in Algol-60 procedure calls.
   If a procedure is called with an expression in the place of a formal parameter, the compiler generates a thunk which computes the expression and leaves the address of the result in some standard location.

2.
   Later generalized into: an expression, frozen together with its environment, for later evaluation if and when needed (similar to what in techspeak is called a closure).
   The process of unfreezing these thunks is called forcing.

3.
   A :ref:`stubroutine`\, in an overlay programming environment, that loads and jumps to the correct overlay.
   Compare :ref:`trampoline`\.

4.
   Microsoft and IBM have both defined, in their Intel-based systems, a "16-bit environment" (with bletcherous segment registers and 64K address limits) and a "32-bit environment" (with flat addressing and semi-real memory management).
   The two environments can both be running on the same computer and OS (thanks to what is called, in the Microsoft world, WOW which stands for Windows On Windows).
   MS and IBM have both decided that the process of getting from 16- to 32-bit and vice versa is called a "thunk"; for Windows 95, there is even a tool THUNK.EXE called a "thunk compiler".

5.
   A person or activity scheduled in a thunklike manner.
   "It occurred to me the other day that I am rather accurately modeled by a thunk — I frequently need to be forced to completion.
   :" — paraphrased from a :ref:`plan-file`\.

Historical note: There are a couple of onomatopoeic myths circulating about the origin of this term.
The most common is that it is the sound made by data hitting the stack; another holds that the sound is that of the data hitting an accumulator.
Yet another suggests that it is the sound of the expression being unfrozen at argument-evaluation time.
In fact, according to the inventors, it was coined after they realized (in the wee hours after hours of discussion) that the type of an argument in Algol-60 could be figured out in advance with a little compile-time thought, simplifying the evaluation machinery.
In other words, it had ‘already been thought of’; thus it was christened a thunk, which is "the past tense of ‘think’ at two in the morning".

