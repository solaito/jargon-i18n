.. _bit-bang:

============================================================
bit bang
============================================================

n\.

Transmission of data on a serial line, when accomplished by rapidly tweaking a single output bit, in software, at the appropriate times.
The technique is a simple loop with eight OUT and SHIFT instruction pairs for each byte.
Input is more interesting.
And full duplex (doing input and output at the same time) is one way to separate the real hackers from the :ref:`wannabee`\s.

Bit bang was used on certain early models of Prime computers, presumably when UARTs were too expensive, and on archaic Z80 micros with a Zilog PIO but no SIO.
In an interesting instance of the :ref:`cycle-of-reincarnation`\, this technique returned to use in the early 1990s on some RISC architectures because it consumes such an infinitesimal part of the processor that it actually makes sense not to have a UART.
Compare :ref:`cycle-of-reincarnation`\.
Nowadays it's used to describe I2C, a serial protocol for monitoring motherboard hardware.

