.. _boot:

============================================================
boot
============================================================

v\.,n\.

[techspeak; from ‘by one's bootstraps’] To load and initialize the operating system on a machine.
This usage is no longer jargon (having passed into techspeak) but has given rise to some derivatives that are still jargon.

The derivative reboot implies that the machine hasn't been down for long, or that the boot is a :ref:`bounce` (sense 4) intended to clear some state of :ref:`wedgitude`\.
This is sometimes used of human thought processes, as in the following exchange: "You've lost me."
"OK, reboot.
Here's the theory...."

This term is also found in the variants cold boot (from power-off condition) and warm boot (with the CPU and all devices already powered up, as after a hardware reset or software crash).

Another variant: soft boot, reinitialization of only part of a system, under control of other software still running: "If you're running the :ref:`mess-dos` emulator, control-alt-insert will cause a soft-boot of the emulator, while leaving the rest of the system running."

Opposed to this there is hard boot, which connotes hostility towards or frustration with the machine being booted: "I'll have to hard-boot this losing Sun."
"I recommend booting it hard."
One often hard-boots by performing a :ref:`power-cycle`\.

Historical note: this term derives from bootstrap loader, a short program that was read in from cards or paper tape, or toggled in from the front panel switches.
This program was always very short (great efforts were expended on making it short in order to minimize the labor and chance of error involved in toggling it in), but was just smart enough to read in a slightly more complex program (usually from a card or paper tape reader), to which it handed control; this program in turn was smart enough to read the application or operating system from a magnetic tape drive or disk drive.
Thus, in successive steps, the computer ‘pulled itself up by its bootstraps’ to a useful operating state.
Nowadays the bootstrap is usually found in ROM or EPROM, and reads the first stage in from a fixed location on the disk, called the ‘boot block’.
When this program gains control, it is powerful enough to load the actual OS and hand control over to it.

