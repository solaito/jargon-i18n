.. _Postels-Prescription:

============================================================
Postel's Prescription
============================================================

[proposed] Several of the key Internet :ref:`RFC`\s, especially 1122 and 791 contain a piece of advice due to Jon Postel, which is most often stated as:

.. code-block:: none


      Be liberal in what you accept, and conservative in what you
      send.

That is, a well-engineered implementation of any of the Internet protocols should be willing to deal with marginal and imperfectly-formed inputs, but should not assume that the program on the other end (that is, the program dealing with the well-engineered implementation's output) will be anything other than rigid and inflexible, and perhaps even incomplete or downright buggy.

This property is valuable because a network of programs adhering to it will be much more robust in the presence of any uncertainties in the protocol specifications, or any individual implementor's failure to understand those specifications perfectly.
Though the policy does tend to accommodate broken implementations it is held to more important to get the communication flowing than to immediately (but terminally) diagnose the broken implementations at the expense of the people trying to use them.

The principle is a well-known one in the design of programs that handle Internet wire protocols, especially network relays and servers, and it is regularly applied by extension in any situation where two or more separately-implemented pieces of software are supposed to interoperate even though the various implementors have never talked to each other and have absolutely nothing whatsoever in common other than having all read the same protocol specification.
The principle travels under several different names, including "the Internet credo", "the IETF maxim", "the Internet Engineering Principle", and "the liberal/conservative rule"; the [proposed] term "Postel' Prescription" is a tribute to its inventor, the first RFC editor and (until his untimely death) probably the single most respected individual in the Internet engineering community.

