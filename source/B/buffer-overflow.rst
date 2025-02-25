.. _buffer-overflow:

============================================================
buffer overflow
============================================================

n\.

What happens when you try to stuff more data into a buffer (holding area) than it can handle.
This problem is commonly exploited by :ref:`cracker`\s to get arbitrary commands executed by a program running with root permissions.
This may be due to a mismatch in the processing rates of the producing and consuming processes (see :ref:`overrun` and :ref:`firehose-syndrome`\), or because the buffer is simply too small to hold all the data that must accumulate before a piece of it can be processed.
For example, in a text-processing tool that :ref:`crunch`\es a line at a time, a short line buffer can result in :ref:`lossage` as input from a long line overflows the buffer and trashes data beyond it.
Good defensive programming would check for overflow on each character and stop accepting data when the buffer is full up.
The term is used of and by humans in a metaphorical sense.
"What time did I agree to meet you?
My buffer must have overflowed."
Or "If I answer that phone my buffer is going to overflow."
See also :ref:`spam`\, :ref:`overrun-screw`\.

