# Retained specification text (collector assembly)

> This consumer Markdown assembles the explicitly retained originals in declared order. Source labels, line anchors and local href rewrites are collector additions; HTML is represented as structural text with ordered table cells and preserved code, without running source scripts.

> Collector representation: declared cell spans are annotations, not an expanded table grid; code br line breaks and NBSP are retained, and image-label whitespace is normalized without dropping label words.

Original HTML: [specification.html](../source/specification.html#L1-L365).

> Collector content boundary: only the article selected by "article#mainContent" is represented below. Original-line ranges are enclosing provenance bounds; the final range may extend to HTML entity EOF and does not imply that every line was converted.

<a id="specification-L1"></a>

<a id="specification-L85"></a>
<a id="specification-mainContent"></a>


 # Schemas

<a id="specification-L87"></a>
## Organization of Schemas
 The schemas are a set of 'types', each associated with a set of properties. The types are arranged in a hierarchy.
 The vocabulary currently consists of 826 Types, 1540 Properties 19 Datatypes, 96 Enumerations and 544 Enumeration members.
 
Browse the full hierarchy in HTML: 

 

- [One page per type](https://schema.org/Thing)

 

- [Full list of types, shown on one page](https://schema.org/docs/full.html)

 

   


 Look up a term using the TermFinder: 
<a id="specification-termfindwrap"></a>


 
<a id="specification-termfindprompt"></a>


 
<a id="specification-termfind"></a>
 

 
<a id="specification-suggestionwrap"></a>


 
<a id="specification-suggestions"></a>




 

 

 

 
Or you can jump directly to a commonly used type: 

 

- Creative works: [CreativeWork](https://schema.org/CreativeWork), [Book](https://schema.org/Book), [Movie](https://schema.org/Movie), [MusicRecording](https://schema.org/MusicRecording), [Recipe](https://schema.org/Recipe), [TVSeries](https://schema.org/TVSeries) ...

 

- Embedded non-text objects: [AudioObject](https://schema.org/AudioObject), [ImageObject](https://schema.org/ImageObject), [VideoObject](https://schema.org/VideoObject)

 

-  [Event](https://schema.org/Event)

 

- [Health and medical types](https://schema.org/docs/meddocs.html): notes on the health and medical types under [MedicalEntity](https://schema.org/MedicalEntity).

 

-  [Organization](https://schema.org/Organization)

 

-  [Person](https://schema.org/Person)

 

-  [Place](https://schema.org/Place), [LocalBusiness](https://schema.org/LocalBusiness), [Restaurant](https://schema.org/Restaurant) ...

 

-  [Product](https://schema.org/Product), [Offer](https://schema.org/Offer), [AggregateOffer](https://schema.org/AggregateOffer)

 

-  [Review](https://schema.org/Review), [AggregateRating](https://schema.org/AggregateRating)

 

-  [Action](https://schema.org/Action)

 

 
See also the [releases](https://schema.org/docs/releases.html) page for recent updates and project history.
 
 We also have a small set of [primitive data types](https://schema.org/DataType) for numbers, text, etc. More details about the data model, etc. are available [here](https://schema.org/docs/datamodel.html). 
 
Developer information / Download Machine Readable files (RDF, JSON-LD, etc): 

 

- [Schema.org for Developers](https://schema.org/docs/developers.html)

<a id="specification-L273"></a>
<a id="specification-ext"></a>
## Extensions
 

As schema.org has grown, we have explored various mechanisms for [community extension](https://schema.org/docs/extension.html) as a way of adding more detailed descriptive vocabulary that builds on the schema.org core. Some areas of Schema.org were developed as "named extensions", and have dedicated entry pages. We previously called these "hosted" extensions, but they are best considered simply as views into a single collection of schema definitions.

<a id="specification-L284"></a>
<a id="specification-hosted"></a>
### Hosted Sections
 

 For example, via the [auto](https://schema.org/docs/auto.home.html) section there is a property for [emissionsCO2](https://schema.org/emissionsCO2), and via the [bib](https://schema.org/docs/bib.home.html) section we have a property [publisherImprint](https://schema.org/publisherImprint). However, from the perspective of a publisher, these are simply schema.org properties. 

 

We have a few of these sections:

 

 

- [auto](https://schema.org/docs/auto.home.html)

 

- [bib](https://schema.org/docs/bib.home.html)

 

- [health-lifesci](https://schema.org/docs/health-lifesci.home.html)

 

- [meta](https://schema.org/docs/meta.home.html)

 

- [pending](https://schema.org/docs/pending.home.html)

 

 

Note: the 'pending' and 'meta' hosted sections are part of schema.org's schema development process.

 
<a id="specification-ext_pending"></a>


 We use the '[pending](https://schema.org/docs/pending.home.html)' section as a staging area for new schema.org terms that are under discussion and review. Implementors and publishers are cautioned that terms in the [pending](https://schema.org/docs/pending.home.html) section may lack consensus and that terminology and definitions could still change significantly after community and [steering group](https://schema.org/docs/about.html#cgsg) review. Consumers of schema.org data who encourage use of such terms are strongly encouraged to update implementations and documentation to track any evolving changes, and to share early implementation feedback with the [wider community](http://www.w3.org/community/schemaorg). 

 
<a id="specification-ext_meta"></a>


 The '[meta](https://schema.org/docs/meta.home.html)' section is primarily for vocabulary used internally within schema.org to support technical definitions and schema.org site functionality. These terms are not intended for general usage in the public Web. 

 
<a id="specification-attic"></a>


[Attic](https://schema.org/docs/attic.home.html) is a special area where terms are archived when deprecated from the core and other sections, or removed from [pending](https://schema.org/docs/pending.home.html) as not accepted into the full vocabulary. References to terms in the attic area are not normally displayed unless accessed via the term identifier or via the home page. Implementors and data publishers are cautioned not to use terms in the attic area. 

 

 Unlike other core and section terms, these areas may be updated at any time without the need for a full [release](https://schema.org/docs/releases.html).

<a id="specification-L324"></a>
<a id="specification-extext"></a>
### External Extensions
 

The schema.org [steering group](https://schema.org/docs/about.html#cgsg) does not officially approve external extensions - they are fully independent. We list here some notable extensions that extend schema.org in interesting and useful ways.

 

 

- [GS1 Web Vocabulary](http://gs1.org/voc/) ([blog post](https://blog-schema.org/2016/02/22/gs1-web-vocabulary-welcoming-the-first-schema-org-external-extension/))

 

- [Croissant](https://mlcommons.org/working-groups/data/croissant/) is an open community-built standardized metadata vocabulary for ML datasets.


<!-- materialization-redistribution-notice -->
## Redistribution notice

This document includes material copied from or derived from "Schemas", published by Schema.org at https://schema.org/docs/schemas.html. The Schema.org Terms identify Google, Inc., Yahoo, Inc., Microsoft Corporation, and Yandex collectively as the "Sponsors" and license the Sponsors' copyrights under Creative Commons Attribution-ShareAlike 3.0 Unported; FAQ #18 applies those terms to supporting documentation. Licensed under CC BY-SA 3.0, https://creativecommons.org/licenses/by-sa/3.0/. This Markdown adaptation and its selector excerpts are distributed under CC BY-SA 3.0. No endorsement by Schema.org, the Sponsors, GS1, or MLCommons is implied. 本原响应实际嵌入Schema.org网站模板另按Apache-2.0，不将软件重许可为BY-SA，也不统授未下载的analytics.js/jQuery、外链GS1/Croissant或第三方材料，不暗示背书。

Changes: 同一HTTP响应4500B gzip wire原样保存，机械gzip解码所得12007B entity原字节保留；不是第二GET/replay自动解码覆盖。派生DOM仅消费唯一article#mainContent，保留unwrapped作者定义/dated数量、层次、href、代码和warning。结构Markdown、空白连续化、链接解析、源行锚点/sidecar与边界说明属于collector-derived format conversion，不是raw quotation；保守source bounds可至entity EOF但article外development/banner/footer不进入正文。TermFinder静态UI不作事实evidence、不执行脚本/取交互结果；文档Markdown/selector改编按BY-SA3 SA，模板不重许可。新normalized EOF附唯一归属/范围/修改块和NOTICE；旧root doc/34selectors不改，旧NOTICE复制history，全旧M/C/R保全。

Scope: 仅本次https://schema.org/docs/schemas.html单页dated-response-2026-09-17T14:20:15Z的4500B gzip wire/12007B解码entity内作者文档/示例（CC-BY-SA-3.0）及实际网站模板（Apache-2.0），并覆盖声明article结构Markdown/新sidecar；AND分范围履约不是OR，文档改编/selector遵守SA，不重许可Apache模板或其他集合作品。旧f62a658…的2982B正文/34selectors和text-only grant另留完整历史。未下载的analytics.js/jQuery/CSS/favicon、交互结果、type/property/release/download页、GS1/Croissant原作/代码/数据、商标及超出适用法条授予范围的专利/隐私权不准入。本页数量/development/V30.1只作dated状态；不是完整Vocabulary/release或部署commit，原UID边界unresolved，partial/full_text不等于complete/trusted。

Full license and original rights links: [NOTICE.md](../NOTICE.md).
