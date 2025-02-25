.. _register-dancing:

============================================================
register dancing
============================================================

n\.

Many older processor architectures suffer from a serious shortage of general-purpose registers.
This is especially a problem for compiler-writers, because their generated code needs places to store temporaries for things like intermediate values in expression evaluation.
Some designs with this problem, like the Intel 80x86, do have a handful of special-purpose registers that can be pressed into service, providing suitable care is taken to avoid unpleasant side effects on the state of the processor: while the special-purpose register is being used to hold an intermediate value, a delicate minuet is required in which the previous value of the register is saved and then restored just before the official function (and value) of the special-purpose register is again needed.

