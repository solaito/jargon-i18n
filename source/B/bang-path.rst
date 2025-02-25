.. _bang-path:

============================================================
bang path
============================================================

n\.

[now historical] An old-style UUCP electronic-mail address specifying hops to get from some assumed-reachable location to the addressee, so called because each :ref:`hop` is signified by a :ref:`bang` sign.
Thus, for example, the path :samp:`...!bigsite!foovax!barbox!me` directs people to route their mail to machine :samp:`bigsite` (presumably a well-known location accessible to everybody) and from there through the machine :samp:`foovax` to the account of user :samp:`me` on :samp:`barbox`\.

In the bad old days of not so long ago, before autorouting mailers and Internet became commonplace, people often published compound bang addresses using the { } convention (see :ref:`glob`\) to give paths from *several* big machines, in the hopes that one's correspondent might be able to get mail to one of them reliably (example: :samp:`...!
{seismo, ut-sally, ihnp4`\!rice!beta!gamma!me}).
Bang paths of 8 to 10 hops were not uncommon.
Late-night dial-up UUCP links would cause week-long transmission times.
Bang paths were often selected by both transmission time and reliability, as messages would not infrequently get lost.
See :ref:`the-network` and :ref:`sitename`\.

