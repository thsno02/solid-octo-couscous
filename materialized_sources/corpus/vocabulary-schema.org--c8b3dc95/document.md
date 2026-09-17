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


<!-- materialization-redistribution-notice -->
## Redistribution notice

This document includes material copied from or derived from "Schemas", published by Schema.org at https://schema.org/docs/schemas.html. The Schema.org Terms identify Google, Inc., Yahoo, Inc., Microsoft Corporation, and Yandex collectively as the "Sponsors" and license the Sponsors' copyrights under Creative Commons Attribution-ShareAlike 3.0 Unported; FAQ #18 applies those terms to supporting documentation. Licensed under CC BY-SA 3.0, https://creativecommons.org/licenses/by-sa/3.0/. This Markdown adaptation and its selector excerpts are distributed under CC BY-SA 3.0. No endorsement by Schema.org, the Sponsors, GS1, or MLCommons is implied.

Changes: Converted the retained 12,007-byte HTML response into a 2,982-byte pre-notice Markdown adaptation by selecting h1-h4, p, li, and pre blocks; navigation, scripts, styles, forms, SVG/canvas, the footer/version/Terms link, hyperlink targets, raw markup, and some unwrapped page text were omitted or normalized; 34 selector excerpts were generated. The redistribution notice and attribution footer were added after conversion.

Scope: 仅覆盖 source_revision 所指固定快照中、许可附注前的 2,982-byte Markdown 改编及其 34 个 selector 摘录，二者均按 CC BY-SA 3.0 分发。原页面仅以名称和简短说明提及 GS1 Web Vocabulary 与 Croissant；胶囊未保存其外链页面、规范、代码、媒体或标识。Schema.org 网站软件（另按 Apache-2.0 提供）、商标、专利、隐私/形象权及权利人无权许可的第三方材料不在此包装的授权范围。 将本作品纳入仓库集合（Collection）并不重新许可集合中的其他独立作品；后续引用、摘录、转换或派生 内容仍须按实际使用方式分别核验，构成改编（Adaptation）时须满足 CC BY-SA 3.0 的 ShareAlike（SA）义务。

Full license and original rights links: [NOTICE.md](NOTICE.md).
