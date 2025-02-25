.. _breath-of-life-packet:

============================================================
breath-of-life packet
============================================================

n\.

[XEROX PARC] An Ethernet packet that contains bootstrap (see :ref:`boot`\) code, periodically sent out from a working computer to infuse the ‘breath of life’ into any computer on the network that has happened to crash.
Machines depending on such packets have sufficient hardware or firmware code to wait for (or request) such a packet during the reboot process.
See also :ref:`dickless-workstation`\.

The notional kiss-of-death packet, with a function complementary to that of a breath-of-life packet, is recommended for dealing with hosts that consume too many network resources.
Though ‘kiss-of-death packet’ is usually used in jest, there is at least one documented instance of an Internet subnet with limited address-table slots in a gateway machine in which such packets were routinely used to compete for slots, rather like Christmas shoppers competing for scarce parking spaces.

