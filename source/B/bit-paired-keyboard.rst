.. _bit-paired-keyboard:

============================================================
bit-paired keyboard
============================================================

n\.,obs\.

(alt.
: bit-shift keyboard) A non-standard keyboard layout that seems to have originated with the Teletype ASR-33 and remained common for several years on early computer equipment.
The ASR-33 was a mechanical device (see :ref:`EOU`\), so the only way to generate the character codes from keystrokes was by some physical linkage.
The design of the ASR-33 assigned each character key a basic pattern that could be modified by flipping bits if the SHIFT or the CTRL key was pressed.
In order to avoid making the thing even more of a kluge than it already was, the design had to group characters that shared the same basic bit pattern on one key.

Looking at the ASCII chart, we find:

.. code-block:: none


   high  low bits
   bits  0000 0001 0010 0011 0100 0101 0110 0111 1000 1001
    010        !    "    #    $    %    &    '    (    )
    011   0    1    2    3    4    5    6    7    8    9

This is why the characters !
"#$%&'() appear where they do on a Teletype (thankfully, they didn't use shift-0 for space).
The Teletype Model 33 was actually designed before ASCII existed, and was originally intended to use a code that contained these two rows:

.. code-block:: none


         low bits
   high  0000  0010  0100  0110  1000  1010  1100  1110
   bits     0001  0011  0101  0111  1001  1011  1101  1111
     10   )  ! bel #  $  % wru &  *  (  "  :  ?  _  ,   .
     11   0  1  2  3  4  5  6  7  8  9  '  ;  /  - esc del

The result would have been something closer to a normal keyboard.
But as it happened, Teletype had to use a lot of persuasion just to keep ASCII, and the Model 33 keyboard, from looking like this instead:

.. code-block:: none


             !  "  ?  $  '  &  -  (  )  ;  :  *  /  ,  .
          0  1  2  3  4  5  6  7  8  9  +  ~  <  >  ×  |

Teletype's was *not* the weirdest variant of the :ref:`QWERTY` layout widely seen, by the way; that prize should probably go to one of several (differing) arrangements on IBM's even clunkier 026 and 029 card punches.

When electronic terminals became popular, in the early 1970s, there was no agreement in the industry over how the keyboards should be laid out.
Some vendors opted to emulate the Teletype keyboard, while others used the flexibility of electronic circuitry to make their product look like an office typewriter.
Either choice was supported by the ANSI computer keyboard standard, X4.14-1971, which referred to the alternatives as "logical bit pairing" and "typewriter pairing".
These alternatives became known as bit-paired and typewriter-paired keyboards.
To a hacker, the bit-paired keyboard seemed far more logical — and because most hackers in those days had never learned to touch-type, there was little pressure from the pioneering users to adapt keyboards to the typewriter standard.

The doom of the bit-paired keyboard was the large-scale introduction of the computer terminal into the normal office environment, where out-and-out technophobes were expected to use the equipment.
The typewriter-paired standard became universal, X4.14 was superseded by X4.23-1982, bit-paired hardware was quickly junked or relegated to dusty corners, and both terms passed into disuse.

However, in countries without a long history of touch typing, the argument against the bit-paired keyboard layout was weak or nonexistent.
As a result, the standard Japanese keyboard, used on PCs, Unix boxen etc.
still has all of the !
"#$%&'() characters above the numbers in the ASR-33 layout.

