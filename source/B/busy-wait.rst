.. _busy-wait:

============================================================
busy-wait
============================================================

vi\.

Used of human behavior, conveys that the subject is busy waiting for someone or something, intends to move instantly as soon as it shows up, and thus cannot do anything else at the moment.
"Can't talk now, I'm busy-waiting till Bill gets off the phone."

Technically, busy-wait means to wait on an event by :ref:`spin`\ning through a tight or timed-delay loop that polls for the event on each pass, as opposed to setting up an interrupt handler and continuing execution on another part of the task.
In applications this is a wasteful technique, and best avoided on timesharing systems where a busy-waiting program may :ref:`hog` the processor.
However, it is often unavoidable in kernel programming.
In the Linux world, kernel busy-waits are usually referred to as spinlocks.

