.. _meaning-of-hack:

============================================================
The Meaning of ‘Hack’
============================================================

"The word :ref:`hack` doesn't really have 69 different meanings", according to MIT hacker Phil Agre.
"In fact, :ref:`hack` has only one meaning, an extremely subtle and profound one which defies articulation.
Which connotation is implied by a given use of the word depends in similarly profound ways on the context.
Similar remarks apply to a couple of other hacker words, most notably :ref:`random`\."

Hacking might be characterized as ‘an appropriate application of ingenuity’.
Whether the result is a quick-and-dirty patchwork job or a carefully crafted work of art, you have to admire the cleverness that went into it.

An important secondary meaning of :ref:`hack` is ‘a creative practical joke’.
This kind of hack is easier to explain to non-hackers than the programming kind.
Of course, some hacks have both natures; see the lexicon entries for :ref:`pseudo` and :ref:`kgbvax`\.
But here are some examples of pure practical jokes that illustrate the hacking spirit:

.. code-block:: none


   In 1961, students from Caltech (California Institute of Technology, in
   Pasadena) hacked the Rose Bowl football game.  One student posed as a reporter
   and ‘interviewed’ the director of the University of Washington
   card stunts (such stunts involve people in the stands who hold up colored
   cards to make pictures).  The reporter learned exactly how the stunts were
   operated, and also that the director would be out to dinner later.

   While the director was eating, the students (who called themselves the
   ‘Fiendish Fourteen’) picked a lock and stole a blank direction
   sheet for the card stunts.  They then had a printer run off 2300 copies of the
   blank.  The next day they picked the lock again and stole the master plans for
   the stunts — large sheets of graph paper colored in with the stunt
   pictures.  Using these as a guide, they made new instructions for three of the
   stunts on the duplicated blanks.  Finally, they broke in once more, replacing
   the stolen master plans and substituting the stack of diddled instruction
   sheets for the original set.

   The result was that three of the pictures were totally different.
   Instead of ‘WASHINGTON’, the word ‘CALTECH’ was
   flashed.  Another stunt showed the word ‘HUSKIES’, the Washington
   nickname, but spelled it backwards.  And what was supposed to have been a
   picture of a husky instead showed a beaver.  (Both Caltech and MIT use the
   beaver — nature's engineer — as a mascot.)

   After the game, the Washington faculty athletic representative said:
   Some thought it ingenious; others were indignant. The
   Washington student body president remarked: No hard feelings, but at
   the time it was unbelievable.  We were amazed.

This is now considered a classic hack, particularly because revising the direction sheets constituted a form of programming.

Here is another classic hack:

.. code-block:: none


   On November 20, 1982, MIT hacked the Harvard-Yale football game.  Just
   after Harvard's second touchdown against Yale, in the first quarter, a small
   black ball popped up out of the ground at the 40-yard line, and grew bigger,
   and bigger, and bigger.  The letters ‘MIT’ appeared all over the
   ball.  As the players and officials stood around gawking, the ball grew to six
   feet in diameter and then burst with a bang and a cloud of white
   smoke.

   The Boston Globe later reported: If you
   want to know the truth, MIT won The Game.

   The prank had taken weeks of careful planning by members of MIT's Delta
   Kappa Epsilon fraternity.  The device consisted of a weather balloon, a
   hydraulic ram powered by Freon gas to lift it out of the ground, and a
   vacuum-cleaner motor to inflate it.  They made eight separate expeditions to
   Harvard Stadium between 1 and 5 AM, locating an unused 110-volt circuit in the
   stadium and running buried wires from the stadium circuit to the 40-yard line,
   where they buried the balloon device.  When the time came to activate the
   device, two fraternity members had merely to flip a circuit breaker and push a
   plug into an outlet.

   This stunt had all the earmarks of a perfect hack: surprise, publicity,
   the ingenious use of technology, safety, and harmlessness.  The use of manual
   control allowed the prank to be timed so as not to disrupt the game (it was
   set off between plays, so the outcome of the game would not be unduly
   affected).  The perpetrators had even thoughtfully attached a note to the
   balloon explaining that the device was not dangerous and contained no
   explosives.

   Harvard president Derek Bok commented: They have an awful lot of
   clever people down there at MIT, and they did it again. President Paul
   E. Gray of MIT said: There is absolutely no truth to the rumor that I
   had anything to do with it, but I wish there were.

The hacks above are verifiable history; they can be proved to have happened.
Many other classic-hack stories from MIT and elsewhere, though retold as history, have the characteristics of what Jan Brunvand has called ‘urban folklore’ (see :ref:`FOAF`\).
Perhaps the best known of these is the legend of the infamous trolley-car hack, an alleged incident in which engineering students are said to have welded a trolley car to its tracks with thermite.
Numerous versions of this have been recorded from the 1940s to the present, most set at MIT but at least one very detailed version set at CMU.

Brian Leibowitz has researched MIT hacks both real and mythical extensively; the interested reader is referred to his delightful pictorial compendium *The Journal of the Institute for Hacks, Tomfoolery, andPranks* (MIT Museum, 1990; ISBN 0-917027-03-5).
The Institute has a World Wide Web page at `http://hacks.mit.edu/Hacks/Gallery.html <http://hacks.mit.edu/Hacks/Gallery.html>`_.
There is a sequel entitled *Is This The Way To Baker House?*\.
The Caltech Alumni Association has published two similar books titled *Legends of Caltech* and *More Legends ofCaltech*\.

Here is a story about one of the classic computer hacks:

.. code-block:: none


   Back in the mid-1970s, several of the system support staff at Motorola
   discovered a relatively simple way to crack system security on the Xerox CP-V
   timesharing system.  Through a simple programming strategy, it was possible
   for a user program to trick the system into running a portion of the program
   in ‘master mode’ (supervisor state), in which memory protection
   does not apply.  The program could then poke a large value into its
   ‘privilege level’ byte (normally write-protected) and could then
   proceed to bypass all levels of security within the file-management system,
   patch the system monitor, and do numerous other interesting things.  In short,
   the barn door was wide open.

   Motorola quite properly reported this problem to Xerox via an official
   ‘level 1 SIDR’ (a bug report with an intended urgency of
   ‘needs to be fixed yesterday’).  Because the text of each SIDR was
   entered into a database that could be viewed by quite a number of people,
   Motorola followed the approved procedure: they simply reported the problem as
   ‘Security SIDR’, and attached all of the necessary documentation,
   ways-to-reproduce, etc.

   The CP-V people at Xerox sat on their thumbs; they either didn't realize
   the severity of the problem, or didn't assign the necessary
   operating-system-staff resources to develop and distribute an official
   patch.

   Months passed.  The Motorola guys pestered their Xerox field-support
   rep, to no avail.  Finally they decided to take direct action, to demonstrate
   to Xerox management just how easily the system could be cracked and just how
   thoroughly the security safeguards could be subverted.

   They dug around in the operating-system listings and devised a
   thoroughly devilish set of patches.  These patches were then incorporated into
   a pair of programs called ‘Robin Hood’ and ‘Friar
   Tuck’.  Robin Hood and Friar Tuck were designed to run as ‘ghost
   jobs’ (daemons, in Unix terminology); they would use the existing
   loophole to subvert system security, install the necessary patches, and then
   keep an eye on one another's statuses in order to keep the system operator (in
   effect, the superuser) from aborting them.

   One fine day, the system operator on the main CP-V software development
   system in El Segundo was surprised by a number of unusual phenomena.  These
   included the following:

   Tape drives would rewind and dismount their tapes in the middle of a
   job.

   Disk drives would seek back and forth so rapidly that they would attempt
   to walk across the floor (see walking drives).

   The card-punch output device would occasionally start up of itself and
   punch a ‘lace card’ (card with all positions punched).  These
   would usually jam in the punch.

   The console would print snide and insulting messages from Robin Hood
   to Friar Tuck, or vice versa.

   The Xerox card reader had two output stackers; it could be instructed
   to stack into A, stack into B, or stack into A (unless a card was
   unreadable, in which case the bad card was placed into stacker B).  One
   of the patches installed by the ghosts added some code to the
   card-reader driver... after reading a card, it would flip over to
   the opposite stacker.  As a result, card decks would divide themselves
   in half when they were read, leaving the operator to recollate them
   manually.

   Naturally, the operator called in the operating-system developers.  They
   found the bandit ghost jobs running, and killed them... and were once
   again surprised.  When Robin Hood was gunned, the following sequence of events
   took place:

   !X id1

   id1: Friar Tuck... I am under attack!  Pray save me!
   id1: Off (aborted)

   id2: Fear not, friend Robin!  I shall rout the Sheriff
        of Nottingham's men!

   id1: Thank you, my good fellow!

   Each ghost-job would detect the fact that the other had been killed, and
   would start a new copy of the recently slain program within a few
   milliseconds.  The only way to kill both ghosts was to kill them
   simultaneously (very difficult) or to deliberately crash the system.

   Finally, the system programmers did the latter — only to find that
   the bandits appeared once again when the system rebooted!  It turned out that
   these two programs had patched the boot-time OS image (the kernel file, in
   Unix terms) and had added themselves to the list of programs that were to be
   started at boot time (this is similar to the way Windows viruses
   propagate).

   The Robin Hood and Friar Tuck ghosts were finally eradicated when the
   system staff rebooted the system from a clean boot-tape and reinstalled the
   monitor.  Not long thereafter, Xerox released a patch for this problem.

   It is alleged that Xerox filed a complaint with Motorola's management
   about the merry-prankster actions of the two employees in question.  It is not
   recorded that any serious disciplinary action was taken against either of
   them.

Finally, here is a wonderful hack story for the new millennium:

1990's addition to the hallowed tradition of April Fool RFCs was RFC 1149, *A Standard for the Transmission of IP Datagrams on AvianCarriers*\.
This sketched a method for transmitting IP packets via carrier pigeons.

Eleven years later, on 28 April 2001, the Bergen Linux User's Group successfully demonstrated CPIP (Carrier Pigeon IP) between two Linux machines running on opposite sides of a small mountain in Bergen, Norway.
Their network stack used printers to hex-dump packets onto paper, pigeons to transport the paper, and OCR software to read the dumps at the other end and feed them to the receiving machine's network layer.

Here is the actual log of the ping command they successfully executed.
Note the exceptional packet times.

.. code-block:: none


   Script started on Sat Apr 28 11:24:09 2001
   vegard@gyversalen:~$ /sbin/ifconfig tun0
   tun0      Link encap:Point-to-Point Protocol
             inet addr:10.0.3.2  P-t-P:10.0.3.1  Mask:255.255.255.255
             UP POINTOPOINT RUNNING NOARP MULTICAST  MTU:150  Metric:1
             RX packets:1 errors:0 dropped:0 overruns:0 frame:0
             TX packets:2 errors:0 dropped:0 overruns:0 carrier:0
             collisions:0
             RX bytes:88 (88.0 b)  TX bytes:168 (168.0 b)

   vegard@gyversalen:~$ ping -i 450 10.0.3.1
   PING 10.0.3.1 (10.0.3.1): 56 data bytes
   64 bytes from 10.0.3.1: icmp_seq=0 ttl=255 time=6165731.1 ms
   64 bytes from 10.0.3.1: icmp_seq=4 ttl=255 time=3211900.8 ms
   64 bytes from 10.0.3.1: icmp_seq=2 ttl=255 time=5124922.8 ms
   64 bytes from 10.0.3.1: icmp_seq=1 ttl=255 time=6388671.9 ms

   — 10.0.3.1 ping statistics —
   9 packets transmitted, 4 packets received, 55% packet loss
   round-trip min/avg/max = 3211900.8/5222806.6/6388671.9 ms
   vegard@gyversalen:~$ exit

   Script done on Sat Apr 28 14:14:28 2001

A web page documenting the event, with pictures, is at `http://www.blug.linux.no/rfc1149/ <http://www.blug.linux.no/rfc1149/>`_.
In the finest Internet tradition, all software involved was open-source; the custom parts are available for download from the site.

While all acknowledged the magnitude of this achievement, some debate ensued over whether BLUG's implementation was properly conformant to the RFC.
It seems they had not used the duct tape specified in 1149 to attach messages to pigeon legs, but instead employed other methods less objectionable to the pigeons.
The debate was properly resolved when it was pointed out that the duct-tape specification was not prefixed by a MUST, and was thus a recommendation rather than a requirement.

The perpetrators finished their preliminary writeup in this wise: "Now, we're waiting for someone to write other implementations, so that we can do interoperability tests, and maybe we finally can get the RFC into the standards track... ".

The logical next step should be an implementation of RFC2549.

