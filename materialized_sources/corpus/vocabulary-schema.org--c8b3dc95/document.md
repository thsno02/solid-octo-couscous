# Schemas


## Organization of Schemas

One page per type

Full list of types, shown on one page

Creative works: CreativeWork , Book , Movie , MusicRecording , Recipe , TVSeries ...

Embedded non-text objects: AudioObject , ImageObject , VideoObject

Event

Health and medical types : notes on the health and medical types under MedicalEntity .

Organization

Person

Place , LocalBusiness , Restaurant ...

Product , Offer , AggregateOffer

Review , AggregateRating

Action

Schema.org for Developers


## Extensions

As schema.org has grown, we have explored various mechanisms for community extension as
   a way of adding more detailed descriptive vocabulary that builds on the schema.org core. Some areas of Schema.org were
   developed as "named extensions", and have dedicated entry pages. We previously called these "hosted" extensions, but
   they are best considered simply as views into a single collection of schema definitions.


### Hosted Sections

For example, via the auto section there is a property for emissionsCO2 ,
and via the bib section we have a property publisherImprint .
However, from the perspective of a publisher, these are simply schema.org properties.

We have a few of these sections:

auto

bib

health-lifesci

meta

pending

Note : the 'pending' and 'meta' hosted sections are part of schema.org's schema development process.

We use the ' pending ' section as a staging area for new schema.org terms that are under discussion and review.
  Implementors and publishers are cautioned that terms in the pending section
  may lack consensus and that terminology and definitions could still change significantly after community and steering group review.
  Consumers of schema.org data who encourage use of such terms are strongly encouraged to update implementations and documentation to track any evolving changes, and to share early implementation feedback with the wider community .

The ' meta ' section is primarily for vocabulary used internally within schema.org to support technical definitions and
schema.org site functionality. These terms are not intended for general usage in the public Web.

Attic is a special area where terms are archived when deprecated from the core and other sections, or removed from pending as not accepted into the full vocabulary. References to terms in the attic area are not normally displayed unless accessed via the term identifier or via the  home page. Implementors and data publishers are cautioned not to use terms in the attic area.

Unlike other core and section terms, these areas may be updated at any time without the need for a full release .


### External Extensions

The schema.org steering group does not officially approve external extensions - they are fully independent.
  We list here some notable extensions that extend schema.org in interesting and useful ways.

GS1 Web Vocabulary ( blog post )

Croissant is an open community-built standardized metadata vocabulary for ML datasets.
