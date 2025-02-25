.. _network-meltdown:

============================================================
network meltdown
============================================================

n\.

A state of complete network overload; the network equivalent of :ref:`thrash`\ing.
This may be induced by a :ref:`Chernobyl-packet`\.
See also :ref:`broadcast-storm`\, :ref:`kamikaze-packet`\.

Network meltdown is often a result of network designs that are optimized for a steady state of moderate load and don't cope well with the very jagged, bursty usage patterns of the real world.
One amusing instance of this is triggered by the popular and very bloody shoot-'em-up game *Doom* on the PC.
When used in multiplayer mode over a network, the game uses broadcast packets to inform other machines when bullets are fired.
This causes problems with weapons like the chain gun which fire rapidly — it can blast the network into a meltdown state just as easily as it shreds opposing monsters.

