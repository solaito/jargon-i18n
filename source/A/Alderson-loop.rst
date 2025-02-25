.. _Alderson-loop:

============================================================
Alderson loop
============================================================

n\.

[Intel] A special version of an :ref:`infinite-loop` where there is an exit condition available, but inaccessible in the current implementation of the code.
Typically this is created while debugging user interface code.
An example would be when there is a menu stating, "Select 1-3 or 9 to quit" and 9 is not allowed by the function that takes the selection from the user.

This term received its name from a programmer who had coded a modal message box in MSAccess with no Ok or Cancel buttons, thereby disabling the entire program whenever the box came up.
The message box had the proper code for dismissal and even was set up so that when the non-existent Ok button was pressed the proper code would be called.

