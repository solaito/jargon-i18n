.. _email-style:

============================================================
Email Quotes and Inclusion Conventions
============================================================

One area where conventions for on-line writing are still in some flux is the marking of included material from earlier messages — what would be called ‘block quotations’ in ordinary English.
From the usual typographic convention employed for these (smaller font at an extra indent), there derived a practice of included text being indented by one ASCII TAB (0001001) character, which under Unix and many other environments gives the appearance of an 8-space indent.

Early mail and netnews readers had no facility for including messages this way, so people had to paste in copy manually.
BSD :manpage:`Mail(1)` was the first message agent to support inclusion, and early Usenetters emulated its style.
But the TAB character tended to push included text too far to the right (especially in multiply nested inclusions), leading to ugly wraparounds.
After a brief period of confusion (during which an inclusion leader consisting of three or four spaces became established in EMACS and a few mailers), the use of leading ``>`` or ``>MARKER_REPLACE_WHITE_SPACE`` became standard, perhaps owing to its use in :manpage:`ed(1)` to display tabs (alternatively, it may derive from the ``>`` that some early Unix mailers used to quote lines starting with "From" in text, so they wouldn't look like the beginnings of new message headers).
Inclusions within inclusions keep their ``>`` leaders, so the ‘nesting level' of a quotation is visually apparent.

The practice of including text from the parent article when posting a followup helped solve what had been a major nuisance on Usenet: the fact that articles do not arrive at different sites in the same order.
Careless posters used to post articles that would begin with, or even consist entirely of, "No, that's wrong" or "I agree" or the like.
It was hard to see who was responding to what.
Consequently, around 1984, new news-posting software evolved a facility to automatically include the text of a previous article, marked with “> ” or whatever the poster chose.
The poster was expected to delete all but the relevant lines.
The result has been that, now, careless posters post articles containing the *entire* text of a preceding article, *followed* only by "No, that's wrong" or "I agree".

Many people feel that this cure is worse than the original disease, and there soon appeared newsreader software designed to let the reader skip over included text if desired.
Today, some posting software rejects articles containing too high a proportion of lines beginning with ‘>' — but this too has led to undesirable workarounds, such as the deliberate inclusion of zero-content filler lines which aren't quoted and thus pull the message below the rejection threshold.

Inclusion practice is still evolving, and disputes over the ‘correct’ inclusion style occasionally lead to :ref:`holy-wars`\.

Most netters view an inclusion as a promise that comment on it will immediately follow.
The preferred, conversational style looks like this,

.. code-block:: none


        > relevant excerpt 1
        response to excerpt
        > relevant excerpt 2
        response to excerpt
        > relevant excerpt 3
        response to excerpt

or for short messages like this:

.. code-block:: none


        > entire message
        response to message

Thanks to poor design of some PC-based mail agents (notably Microsoft Outlook and Outlook Express), one will occasionally see the entire quoted message *after* the response, like this

.. code-block:: none


        response to message
        > entire message

but this practice is strongly deprecated.

Though ``>`` remains the standard inclusion leader, ``|`` is occasionally used for extended quotations where original variations in indentation are being retained (one mailer even combines these and uses ``|>``\).
One also sees different styles of quoting a number of authors in the same message: one (deprecated because it loses information) uses a leader of ``>MARKER_REPLACE_WHITE_SPACE`` for everyone, another (the most common) is ``> > > >``\, ``> > >MARKER_REPLACE_WHITE_SPACE``\, etc.
(or ``>>>>MARKER_REPLACE_WHITE_SPACE``\, ``>>>``\, etc., depending on line length and nesting depth) reflecting the original order of messages, and yet another is to use a different citation leader for each author, say ``>MARKER_REPLACE_WHITE_SPACE``\, ``:MARKER_REPLACE_WHITE_SPACE``\, ``|``\, ``\@`` (preserving nesting so that the inclusion order of messages is still apparent, or tagging the inclusions with authors' names).
Yet *another* style is to use each poster's initials (or login name) as a citation leader for that poster.

Occasionally one sees a ``#MARKER_REPLACE_WHITE_SPACE`` leader used for quotations from authoritative sources such as standards documents; the intended allusion is to the root prompt (the special Unix command prompt issued when one is running as the privileged super-user).

