.. _Whorfian-mind-lock:

============================================================
Whorfian mind-lock
============================================================

[from the Lojban-language list] Software designs are often restricted in unavoidable ways by the capacities of the operating system or hardware they have to work with.
Sometimes they are restricted in avoidable ways by mental habits a developer has picked up from a particular language or environment (perhaps a now-obsolete one) and never discarded.
When a design develops complications that are the result of a mental habit that is no longer adaptive, the developer has succumbed to Whorfian mind-lock.
The design itself has been ‘whorfed’.

For example, some Unix designs are whorfed by the assumption that directory searches are linear and expensive for large directories; therefore directories must be kept small.
Another common way to succumb to Whorfian mind-lock is to do serial processing with a small working set rather than slurping an entire file or data structure into memory; the hidden assumption here is that not much core is available and virtual memory works poorly if at all.
Detecting Whorfian mind-lock is important, because it tends to introduce unnecessary complexity and bugs.

