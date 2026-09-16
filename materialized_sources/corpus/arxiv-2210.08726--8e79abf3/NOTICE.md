# RARR v3：分组件归属、许可及未决短引声明（Component notice）

本声明仅对应固定 arXiv 2210.08726v3，https://arxiv.org/abs/2210.08726v3；source revision 为 sha256:7cc1715f63dfe9bdf62eeb456a02965794f4c8defd60291dbc406555bd1c4c70。ACL 出版的作者表达许可、模板表达许可、BST 原始许可、独立 Wiki 节选和未决研究短引分别记录，不能互相替代，也不是整库重许可。本轮完成条款包装，不放行尚未闭合的公开持久分发（public persistent redistribution）。

## 归属、来源与修改（Attribution, sources and changes）

Paper attribution: Luyu Gao, Zhuyun Dai, Panupong Pasupat, Anthony Chen, Arun Tejasvi Chaganty, Yicheng Fan, Vincent Y. Zhao, Ni Lao, Hongrae Lee, Da-Cheng Juan and Kelvin Guu, "RARR: Researching and Revising What Language Models Say, Using Language Models" (ACL 2023), https://aclanthology.org/2023.acl-long.910/, DOI https://doi.org/10.18653/v1/2023.acl-long.910. The retained fixed arXiv v3 https://arxiv.org/abs/2210.08726v3 corresponds to the ACL-published main text and appendices A-E. Copyright ©2023 Association for Computational Linguistics. Author/ACL-licensable paper expression is under Creative Commons Attribution 4.0 International, https://creativecommons.org/licenses/by/4.0/; publisher policy https://aclanthology.org/faq/copyright/. This is the ACL publication license path, not a public sublicense from arXiv's non-exclusive distribution terms, and excludes independently sourced third-party expression.

EMNLP template attribution: Houda Bouamor, Juan Pino and Kalika Bali, "Instructions for EMNLP 2023 Proceedings", https://www.overleaf.com/latex/templates/instructions-for-emnlp-2023-proceedings/scyjxmtnrskr, CC BY 4.0, https://creativecommons.org/licenses/by/4.0/. Official style page: https://2023.emnlp.org/calls/style-and-formatting/; source ZIP: https://2023.emnlp.org/downloads/emnlp2023-latex.zip. Retained acl2023.sty corresponds to the official emnlp2023.sty expression except the existing EMNLP-to-ACL conference and anonymous-submission labels at lines 27 and 150. These existing label changes are retained; the repository did not make them. The BST's independent LPPL terms are not replaced by CC BY.

BST attribution: acl_natbib.bst is retained unchanged with its original header and "% urlbst" modification marks. Copyright 1994-2002 Patrick W Daly; compling.bst created by Ron Artstein (2005-08-22); ACL changes credited to Dan Gildea (2017-06-08, 2019-04-12) and Shay Cohen (2018-02-16); generated urlbst changes Copyright 2002-2023 Norman Gray. The file permits LPPL version 1 or any later version; this package selects LPPL 1.3c, https://www.latex-project.org/lppl/lppl-1-3c.txt. Correspondence: https://2023.emnlp.org/downloads/emnlp2023-latex.zip and https://github.com/acl-org/acl-style-files/blob/4c318538c99ce2d91201a3b43cfc12ef513e374b/acl_natbib.bst; urlbst LPPL source: https://ctan.org/tex-archive/biblio/bibtex/contrib/urlbst. No urlbst script is retained; no Current Maintainer or endorsement is claimed.

Wikipedia contributors, "Havel–Hakimi algorithm", https://en.wikipedia.org/wiki/Havel%E2%80%93Hakimi_algorithm — fig_prompts.tex lines 86, 149, 265 and 323.

Wikipedia contributors, "If She Knew What She Wants", https://en.wikipedia.org/wiki/If_She_Knew_What_She_Wants — fig_interesting_examples.tex line 8.

Wikipedia contributors, "Back to God", https://en.wikipedia.org/wiki/Back_to_God — 7a_human_eval.tex line 109.

Wikipedia contributors, "2017 NCAA Division I women's basketball tournament", https://en.wikipedia.org/wiki/2017_NCAA_Division_I_women%27s_basketball_tournament — 7a_human_eval.tex line 134 only; lines 119 and 132 are separate news expressions.

Wikipedia contributors, "The Addams Family (1973 TV series)", https://en.wikipedia.org/wiki/The_Addams_Family_(1973_TV_series) — 7a_human_eval.tex line 164 only; the 1964-1966 passage at line 166 is not attributed to this page.

Wikipedia contributors, "Sagrada Família", https://en.wikipedia.org/wiki/Sagrada_Fam%C3%ADlia — 7a_human_eval.tex lines 181-182.

The listed Wikipedia expressions, existing adaptations and corresponding selector excerpts are shared independently under CC BY-SA 4.0, https://creativecommons.org/licenses/by-sa/4.0/. Corresponding current expressions and page license notices were checked; no whole-article byte identity, original collection date or exact historical page revision is claimed. Historical adaptation path: https://meta.wikimedia.org/wiki/Terms_of_use/Creative_Commons_4.0/Legal_note; reuse terms: https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use.

MarioWiki contributors, "F.L.U.D.D.", https://www.mariowiki.com/F.L.U.D.D. — fig_prompts.tex line 279, the retained 48-word introduction and corresponding selector excerpt, CC BY-SA 3.0 Unported, https://creativecommons.org/licenses/by-sa/3.0/. The official policy https://www.mariowiki.com/MarioWiki:Copyrights identifies contributions before 2026-02-27 as BY-SA 3.0; this package selects that path, not a retroactive 4.0 claim. Existing excerpting, formatting and name variants are retained. This covers Wiki-authored text, not Nintendo images or game materials.

Other research quotations are not relicensed: Tyler Santora, Live Science (2021-09-18), https://www.livescience.com/breathing-nose-sides, the approximately 47-word nasal-cycle excerpt in fig_prompts.tex and fig_example_prompts.tex line 20; PA Media, The Guardian (2021-01-09), https://www.theguardian.com/uk-news/2021/jan/09/kelvin-hopkins-quits-labour-before-conclusion-of-sexual-harassment-inquiry, approximately the first 47 words at fig_prompts.tex line 98, excluding the following model phrase "This agrees"; NPR, "Accuracy", https://www.npr.org/about-npr/688139552/accuracy, the approximately 18-word ellipsis quotation in 7a_human_eval.tex line 147. Other original collection URLs not supplied in the retained source are identified as quotations as reproduced in Gao et al., RARR (ACL 2023), not as authorized or original model output.

Changes: 本次包装不修改全部33个实存 source 文件、normalized/document.tex、原115,974-byte normalized/document.txt 正文前缀、101个 selectors 或 files.jsonl。既有 TeX-to-plain-text 提取已展开 include、减少宏/注释/格式；论文既有摘录、转述、遗漏、模型条件表达和名称变体保持不变，不虚构其修改者。acl2023.sty 既有两处 EMNLP→ACL 标签差异保留；acl_natbib.bst 及原许可头注原样保留。只追加此归属、分组件范围、修改及未决短引声明，并写入对应 NOTICE；不伪造原始获取日、oldid 或历史 retrieval。

Scope: 许可按组件（component）限定：固定v3作者/ACL可许可的主文及附录A–E表达与所列模板表达适用CC BY4；原样BST独立选择LPPL1.3c；六个明确列出的Wikipedia页面表达/既有改写及selector节选独立BY-SA4；MarioWiki FLUDD文字及selector节选独立BY-SA3，不把ShareAlike扩张到独立论文或整个repo。其他研究样例不被BY4重许可。公开发布仍阻断（publication block）：Little House约41词宣传可能为原作品核心且原URL未保留；Social Work、Stanford、Lexington、Phoenix Mills/Market City、2010募款歌句、旅游33词、部分domain-only与Reading/电视史/体育样例的原出处或分发依据未闭合。只记录有限研究/批评目的、事实性已发表材料、短片段及非替代性可能支持美国情境合理使用（fair use）的因素；fig_prompts的11个独立证据表达在28行重复也计入使用量，不设字数安全港、不宣称司法结论、权利人授权或用户已接受风险。旅游7a_human_eval.tex第184行的33词第三方表达与第185行作者17词方法推论分开；募款歌句未核为候选Wikipedia页面来源；不把相邻Wiki归属扩至新闻句或1964–1966电视史。未授权省略媒体、外链全文、程序/模型/数据包、商标、专利或Nintendo材料；包装声明条款与具体未决范围，本身不是发布批准。

## 研究短引的有限情境与具体未决范围（Research quotation context and unresolved scope）

- `fig_prompts.tex` 共11个独立短证据表达、28行重复展示，每个约23–51词，用于 agreement/revision 模型条件。上述已经独立归属的 Wiki 表达不并入论文 BY4；其余片段也不因位于已许可论文或模型输出中而自动原创或获得授权。
- Little House 约41词宣传、Social Work 约35词历史、Stanford 约30词介绍、Lexington 约23词事实、Phoenix Mills 约42词历史、Phoenix Market City 约40词、2010募款歌句及旅游约33词的原始 collection URL 未保留。诚实归属为 “quoted as reproduced in Gao et al., RARR (ACL 2023), prompt figure / human-evaluation Appendix C; original collection URL not supplied in retained source”。不伪填作者、许可、原始获取日或 URL。募款歌句在 `fig_prompts.tex` 92/155/272/330 的 https://en.wikipedia.org/wiki/(I%27ve_Had)_The_Time_of_My_Life 仅为未匹配该句的候选页，不列为已核 BY-SA 来源。
- `fig_interesting_examples.tex` 13/19/25/33 已存 Britannica / SecondHandSongs / MeTV / Refinery29 标签；保留其短事实、作品 metadata 和节目 tagline 的现有归属与研究上下文，不把它们认成歌词或 ACL 许可表达。`fig_compare_outputs.tex` 32–35 的中央薪酬委员会短事实、`7a_human_eval.tex` 119/132 体育赛果、166 电视史、227/229 Reading 模型比较及部分 domain-only 出处仍按论文中所呈现的研究样例记录，分发依据未闭合。旅游184行两句第三方摘录约33词，185行另为作者17词方法推论，不能混算为旅游引用。
- 美国版权局四因素说明 https://www.copyright.gov/fair-use/ 为有限情境依据：研究/批评的新目的、事实性已发表材料、每件短片段而非整文、未构成完整新闻/旅游/小说/歌词替代品；重复28行也属于使用量因素。Little House 宣传可能是原宣传的核心，短词数不是安全港，市场影响与原出处仍有不确定性。这是潜在美国情境合理使用（fair use）的因素记录，不是公众许可证、司法结论或用户已接受风险的声明，不能套用到一般外部全文。
- 公开发布仍 block，具体剩余条件是上述宣传核心风险及未知出处/分发依据，而不是新建“每句事实必须取授权”的一般要求。没有声称 GraphRAG 个案等于本项目全库风险政策，也不宣称权利人已授权。

各 CC 组件的现有摘录、转述和格式/名称变化已如上注明；归属和 ShareAlike 仅限这些组件及对应 selector 摘录，不覆盖独立作者表达、整个论文或 repo。没有额外限制或技术措施，也不暗示任何被归属个人或组织背书。已省略的8个非文字媒体成员仍不入许可范围。

## A. Creative Commons Attribution 4.0 International（CC BY 4.0）

仅适用于作者/ACL 有权许可的论文主文及附录表达与所列模板表达；独立第三方组件和短引不受此许可覆盖。
官方法条：https://creativecommons.org/licenses/by/4.0/legalcode.en

```text
Attribution 4.0 International

=======================================================================

Creative Commons Corporation ("Creative Commons") is not a law firm and
does not provide legal services or legal advice. Distribution of
Creative Commons public licenses does not create a lawyer-client or
other relationship. Creative Commons makes its licenses and related
information available on an "as-is" basis. Creative Commons gives no
warranties regarding its licenses, any material licensed under their
terms and conditions, or any related information. Creative Commons
disclaims all liability for damages resulting from their use to the
fullest extent possible.

Using Creative Commons Public Licenses

Creative Commons public licenses provide a standard set of terms and
conditions that creators and other rights holders may use to share
original works of authorship and other material subject to copyright
and certain other rights specified in the public license below. The
following considerations are for informational purposes only, are not
exhaustive, and do not form part of our licenses.

     Considerations for licensors: Our public licenses are
     intended for use by those authorized to give the public
     permission to use material in ways otherwise restricted by
     copyright and certain other rights. Our licenses are
     irrevocable. Licensors should read and understand the terms
     and conditions of the license they choose before applying it.
     Licensors should also secure all rights necessary before
     applying our licenses so that the public can reuse the
     material as expected. Licensors should clearly mark any
     material not subject to the license. This includes other CC-
     licensed material, or material used under an exception or
     limitation to copyright. More considerations for licensors:
    wiki.creativecommons.org/Considerations_for_licensors

     Considerations for the public: By using one of our public
     licenses, a licensor grants the public permission to use the
     licensed material under specified terms and conditions. If
     the licensor's permission is not necessary for any reason--for
     example, because of any applicable exception or limitation to
     copyright--then that use is not regulated by the license. Our
     licenses grant only permissions under copyright and certain
     other rights that a licensor has authority to grant. Use of
     the licensed material may still be restricted for other
     reasons, including because others have copyright or other
     rights in the material. A licensor may make special requests,
     such as asking that all changes be marked or described.
     Although not required by our licenses, you are encouraged to
     respect those requests where reasonable. More considerations
     for the public:
    wiki.creativecommons.org/Considerations_for_licensees

=======================================================================

Creative Commons Attribution 4.0 International Public License

By exercising the Licensed Rights (defined below), You accept and agree
to be bound by the terms and conditions of this Creative Commons
Attribution 4.0 International Public License ("Public License"). To the
extent this Public License may be interpreted as a contract, You are
granted the Licensed Rights in consideration of Your acceptance of
these terms and conditions, and the Licensor grants You such rights in
consideration of benefits the Licensor receives from making the
Licensed Material available under these terms and conditions.


Section 1 -- Definitions.

  a. Adapted Material means material subject to Copyright and Similar
     Rights that is derived from or based upon the Licensed Material
     and in which the Licensed Material is translated, altered,
     arranged, transformed, or otherwise modified in a manner requiring
     permission under the Copyright and Similar Rights held by the
     Licensor. For purposes of this Public License, where the Licensed
     Material is a musical work, performance, or sound recording,
     Adapted Material is always produced where the Licensed Material is
     synched in timed relation with a moving image.

  b. Adapter's License means the license You apply to Your Copyright
     and Similar Rights in Your contributions to Adapted Material in
     accordance with the terms and conditions of this Public License.

  c. Copyright and Similar Rights means copyright and/or similar rights
     closely related to copyright including, without limitation,
     performance, broadcast, sound recording, and Sui Generis Database
     Rights, without regard to how the rights are labeled or
     categorized. For purposes of this Public License, the rights
     specified in Section 2(b)(1)-(2) are not Copyright and Similar
     Rights.

  d. Effective Technological Measures means those measures that, in the
     absence of proper authority, may not be circumvented under laws
     fulfilling obligations under Article 11 of the WIPO Copyright
     Treaty adopted on December 20, 1996, and/or similar international
     agreements.

  e. Exceptions and Limitations means fair use, fair dealing, and/or
     any other exception or limitation to Copyright and Similar Rights
     that applies to Your use of the Licensed Material.

  f. Licensed Material means the artistic or literary work, database,
     or other material to which the Licensor applied this Public
     License.

  g. Licensed Rights means the rights granted to You subject to the
     terms and conditions of this Public License, which are limited to
     all Copyright and Similar Rights that apply to Your use of the
     Licensed Material and that the Licensor has authority to license.

  h. Licensor means the individual(s) or entity(ies) granting rights
     under this Public License.

  i. Share means to provide material to the public by any means or
     process that requires permission under the Licensed Rights, such
     as reproduction, public display, public performance, distribution,
     dissemination, communication, or importation, and to make material
     available to the public including in ways that members of the
     public may access the material from a place and at a time
     individually chosen by them.

  j. Sui Generis Database Rights means rights other than copyright
     resulting from Directive 96/9/EC of the European Parliament and of
     the Council of 11 March 1996 on the legal protection of databases,
     as amended and/or succeeded, as well as other essentially
     equivalent rights anywhere in the world.

  k. You means the individual or entity exercising the Licensed Rights
     under this Public License. Your has a corresponding meaning.


Section 2 -- Scope.

  a. License grant.

       1. Subject to the terms and conditions of this Public License,
          the Licensor hereby grants You a worldwide, royalty-free,
          non-sublicensable, non-exclusive, irrevocable license to
          exercise the Licensed Rights in the Licensed Material to:

            a. reproduce and Share the Licensed Material, in whole or
               in part; and

            b. produce, reproduce, and Share Adapted Material.

       2. Exceptions and Limitations. For the avoidance of doubt, where
          Exceptions and Limitations apply to Your use, this Public
          License does not apply, and You do not need to comply with
          its terms and conditions.

       3. Term. The term of this Public License is specified in Section
          6(a).

       4. Media and formats; technical modifications allowed. The
          Licensor authorizes You to exercise the Licensed Rights in
          all media and formats whether now known or hereafter created,
          and to make technical modifications necessary to do so. The
          Licensor waives and/or agrees not to assert any right or
          authority to forbid You from making technical modifications
          necessary to exercise the Licensed Rights, including
          technical modifications necessary to circumvent Effective
          Technological Measures. For purposes of this Public License,
          simply making modifications authorized by this Section 2(a)
          (4) never produces Adapted Material.

       5. Downstream recipients.

            a. Offer from the Licensor -- Licensed Material. Every
               recipient of the Licensed Material automatically
               receives an offer from the Licensor to exercise the
               Licensed Rights under the terms and conditions of this
               Public License.

            b. No downstream restrictions. You may not offer or impose
               any additional or different terms or conditions on, or
               apply any Effective Technological Measures to, the
               Licensed Material if doing so restricts exercise of the
               Licensed Rights by any recipient of the Licensed
               Material.

       6. No endorsement. Nothing in this Public License constitutes or
          may be construed as permission to assert or imply that You
          are, or that Your use of the Licensed Material is, connected
          with, or sponsored, endorsed, or granted official status by,
          the Licensor or others designated to receive attribution as
          provided in Section 3(a)(1)(A)(i).

  b. Other rights.

       1. Moral rights, such as the right of integrity, are not
          licensed under this Public License, nor are publicity,
          privacy, and/or other similar personality rights; however, to
          the extent possible, the Licensor waives and/or agrees not to
          assert any such rights held by the Licensor to the limited
          extent necessary to allow You to exercise the Licensed
          Rights, but not otherwise.

       2. Patent and trademark rights are not licensed under this
          Public License.

       3. To the extent possible, the Licensor waives any right to
          collect royalties from You for the exercise of the Licensed
          Rights, whether directly or through a collecting society
          under any voluntary or waivable statutory or compulsory
          licensing scheme. In all other cases the Licensor expressly
          reserves any right to collect such royalties.


Section 3 -- License Conditions.

Your exercise of the Licensed Rights is expressly made subject to the
following conditions.

  a. Attribution.

       1. If You Share the Licensed Material (including in modified
          form), You must:

            a. retain the following if it is supplied by the Licensor
               with the Licensed Material:

                 i. identification of the creator(s) of the Licensed
                    Material and any others designated to receive
                    attribution, in any reasonable manner requested by
                    the Licensor (including by pseudonym if
                    designated);

                ii. a copyright notice;

               iii. a notice that refers to this Public License;

                iv. a notice that refers to the disclaimer of
                    warranties;

                 v. a URI or hyperlink to the Licensed Material to the
                    extent reasonably practicable;

            b. indicate if You modified the Licensed Material and
               retain an indication of any previous modifications; and

            c. indicate the Licensed Material is licensed under this
               Public License, and include the text of, or the URI or
               hyperlink to, this Public License.

       2. You may satisfy the conditions in Section 3(a)(1) in any
          reasonable manner based on the medium, means, and context in
          which You Share the Licensed Material. For example, it may be
          reasonable to satisfy the conditions by providing a URI or
          hyperlink to a resource that includes the required
          information.

       3. If requested by the Licensor, You must remove any of the
          information required by Section 3(a)(1)(A) to the extent
          reasonably practicable.

       4. If You Share Adapted Material You produce, the Adapter's
          License You apply must not prevent recipients of the Adapted
          Material from complying with this Public License.


Section 4 -- Sui Generis Database Rights.

Where the Licensed Rights include Sui Generis Database Rights that
apply to Your use of the Licensed Material:

  a. for the avoidance of doubt, Section 2(a)(1) grants You the right
     to extract, reuse, reproduce, and Share all or a substantial
     portion of the contents of the database;

  b. if You include all or a substantial portion of the database
     contents in a database in which You have Sui Generis Database
     Rights, then the database in which You have Sui Generis Database
     Rights (but not its individual contents) is Adapted Material; and

  c. You must comply with the conditions in Section 3(a) if You Share
     all or a substantial portion of the contents of the database.

For the avoidance of doubt, this Section 4 supplements and does not
replace Your obligations under this Public License where the Licensed
Rights include other Copyright and Similar Rights.


Section 5 -- Disclaimer of Warranties and Limitation of Liability.

  a. UNLESS OTHERWISE SEPARATELY UNDERTAKEN BY THE LICENSOR, TO THE
     EXTENT POSSIBLE, THE LICENSOR OFFERS THE LICENSED MATERIAL AS-IS
     AND AS-AVAILABLE, AND MAKES NO REPRESENTATIONS OR WARRANTIES OF
     ANY KIND CONCERNING THE LICENSED MATERIAL, WHETHER EXPRESS,
     IMPLIED, STATUTORY, OR OTHER. THIS INCLUDES, WITHOUT LIMITATION,
     WARRANTIES OF TITLE, MERCHANTABILITY, FITNESS FOR A PARTICULAR
     PURPOSE, NON-INFRINGEMENT, ABSENCE OF LATENT OR OTHER DEFECTS,
     ACCURACY, OR THE PRESENCE OR ABSENCE OF ERRORS, WHETHER OR NOT
     KNOWN OR DISCOVERABLE. WHERE DISCLAIMERS OF WARRANTIES ARE NOT
     ALLOWED IN FULL OR IN PART, THIS DISCLAIMER MAY NOT APPLY TO YOU.

  b. TO THE EXTENT POSSIBLE, IN NO EVENT WILL THE LICENSOR BE LIABLE
     TO YOU ON ANY LEGAL THEORY (INCLUDING, WITHOUT LIMITATION,
     NEGLIGENCE) OR OTHERWISE FOR ANY DIRECT, SPECIAL, INDIRECT,
     INCIDENTAL, CONSEQUENTIAL, PUNITIVE, EXEMPLARY, OR OTHER LOSSES,
     COSTS, EXPENSES, OR DAMAGES ARISING OUT OF THIS PUBLIC LICENSE OR
     USE OF THE LICENSED MATERIAL, EVEN IF THE LICENSOR HAS BEEN
     ADVISED OF THE POSSIBILITY OF SUCH LOSSES, COSTS, EXPENSES, OR
     DAMAGES. WHERE A LIMITATION OF LIABILITY IS NOT ALLOWED IN FULL OR
     IN PART, THIS LIMITATION MAY NOT APPLY TO YOU.

  c. The disclaimer of warranties and limitation of liability provided
     above shall be interpreted in a manner that, to the extent
     possible, most closely approximates an absolute disclaimer and
     waiver of all liability.


Section 6 -- Term and Termination.

  a. This Public License applies for the term of the Copyright and
     Similar Rights licensed here. However, if You fail to comply with
     this Public License, then Your rights under this Public License
     terminate automatically.

  b. Where Your right to use the Licensed Material has terminated under
     Section 6(a), it reinstates:

       1. automatically as of the date the violation is cured, provided
          it is cured within 30 days of Your discovery of the
          violation; or

       2. upon express reinstatement by the Licensor.

     For the avoidance of doubt, this Section 6(b) does not affect any
     right the Licensor may have to seek remedies for Your violations
     of this Public License.

  c. For the avoidance of doubt, the Licensor may also offer the
     Licensed Material under separate terms or conditions or stop
     distributing the Licensed Material at any time; however, doing so
     will not terminate this Public License.

  d. Sections 1, 5, 6, 7, and 8 survive termination of this Public
     License.


Section 7 -- Other Terms and Conditions.

  a. The Licensor shall not be bound by any additional or different
     terms or conditions communicated by You unless expressly agreed.

  b. Any arrangements, understandings, or agreements regarding the
     Licensed Material not stated herein are separate from and
     independent of the terms and conditions of this Public License.


Section 8 -- Interpretation.

  a. For the avoidance of doubt, this Public License does not, and
     shall not be interpreted to, reduce, limit, restrict, or impose
     conditions on any use of the Licensed Material that could lawfully
     be made without permission under this Public License.

  b. To the extent possible, if any provision of this Public License is
     deemed unenforceable, it shall be automatically reformed to the
     minimum extent necessary to make it enforceable. If the provision
     cannot be reformed, it shall be severed from this Public License
     without affecting the enforceability of the remaining terms and
     conditions.

  c. No term or condition of this Public License will be waived and no
     failure to comply consented to unless expressly agreed to by the
     Licensor.

  d. Nothing in this Public License constitutes or may be interpreted
     as a limitation upon, or waiver of, any privileges and immunities
     that apply to the Licensor or You, including from the legal
     processes of any jurisdiction or authority.


=======================================================================

Creative Commons is not a party to its public
licenses. Notwithstanding, Creative Commons may elect to apply one of
its public licenses to material it publishes and in those instances
will be considered the “Licensor.” The text of the Creative Commons
public licenses is dedicated to the public domain under the CC0 Public
Domain Dedication. Except for the limited purpose of indicating that
material is shared under a Creative Commons public license or as
otherwise permitted by the Creative Commons policies published at
creativecommons.org/policies, Creative Commons does not authorize the
use of the trademark "Creative Commons" or any other trademark or logo
of Creative Commons without its prior written consent including,
without limitation, in connection with any unauthorized modifications
to any of its public licenses or any other arrangements,
understandings, or agreements concerning use of licensed material. For
the avoidance of doubt, this paragraph does not form part of the
public licenses.

Creative Commons may be contacted at creativecommons.org.

```

## B. Creative Commons Attribution-ShareAlike 4.0 International（CC BY-SA 4.0）

仅适用于明确列出的六个 Wikipedia 页面对应表达、既有改写及 selector 节选；不扩展到未核实的相邻新闻/电视史或候选募款歌曲句。
官方法条：https://creativecommons.org/licenses/by-sa/4.0/legalcode.en

```text
Attribution-ShareAlike 4.0 International

=======================================================================

Creative Commons Corporation ("Creative Commons") is not a law firm and
does not provide legal services or legal advice. Distribution of
Creative Commons public licenses does not create a lawyer-client or
other relationship. Creative Commons makes its licenses and related
information available on an "as-is" basis. Creative Commons gives no
warranties regarding its licenses, any material licensed under their
terms and conditions, or any related information. Creative Commons
disclaims all liability for damages resulting from their use to the
fullest extent possible.

Using Creative Commons Public Licenses

Creative Commons public licenses provide a standard set of terms and
conditions that creators and other rights holders may use to share
original works of authorship and other material subject to copyright
and certain other rights specified in the public license below. The
following considerations are for informational purposes only, are not
exhaustive, and do not form part of our licenses.

     Considerations for licensors: Our public licenses are
     intended for use by those authorized to give the public
     permission to use material in ways otherwise restricted by
     copyright and certain other rights. Our licenses are
     irrevocable. Licensors should read and understand the terms
     and conditions of the license they choose before applying it.
     Licensors should also secure all rights necessary before
     applying our licenses so that the public can reuse the
     material as expected. Licensors should clearly mark any
     material not subject to the license. This includes other CC-
     licensed material, or material used under an exception or
     limitation to copyright. More considerations for licensors:
    wiki.creativecommons.org/Considerations_for_licensors

     Considerations for the public: By using one of our public
     licenses, a licensor grants the public permission to use the
     licensed material under specified terms and conditions. If
     the licensor's permission is not necessary for any reason--for
     example, because of any applicable exception or limitation to
     copyright--then that use is not regulated by the license. Our
     licenses grant only permissions under copyright and certain
     other rights that a licensor has authority to grant. Use of
     the licensed material may still be restricted for other
     reasons, including because others have copyright or other
     rights in the material. A licensor may make special requests,
     such as asking that all changes be marked or described.
     Although not required by our licenses, you are encouraged to
     respect those requests where reasonable. More considerations
     for the public:
    wiki.creativecommons.org/Considerations_for_licensees

=======================================================================

Creative Commons Attribution-ShareAlike 4.0 International Public
License

By exercising the Licensed Rights (defined below), You accept and agree
to be bound by the terms and conditions of this Creative Commons
Attribution-ShareAlike 4.0 International Public License ("Public
License"). To the extent this Public License may be interpreted as a
contract, You are granted the Licensed Rights in consideration of Your
acceptance of these terms and conditions, and the Licensor grants You
such rights in consideration of benefits the Licensor receives from
making the Licensed Material available under these terms and
conditions.


Section 1 -- Definitions.

  a. Adapted Material means material subject to Copyright and Similar
     Rights that is derived from or based upon the Licensed Material
     and in which the Licensed Material is translated, altered,
     arranged, transformed, or otherwise modified in a manner requiring
     permission under the Copyright and Similar Rights held by the
     Licensor. For purposes of this Public License, where the Licensed
     Material is a musical work, performance, or sound recording,
     Adapted Material is always produced where the Licensed Material is
     synched in timed relation with a moving image.

  b. Adapter's License means the license You apply to Your Copyright
     and Similar Rights in Your contributions to Adapted Material in
     accordance with the terms and conditions of this Public License.

  c. BY-SA Compatible License means a license listed at
     creativecommons.org/compatiblelicenses, approved by Creative
     Commons as essentially the equivalent of this Public License.

  d. Copyright and Similar Rights means copyright and/or similar rights
     closely related to copyright including, without limitation,
     performance, broadcast, sound recording, and Sui Generis Database
     Rights, without regard to how the rights are labeled or
     categorized. For purposes of this Public License, the rights
     specified in Section 2(b)(1)-(2) are not Copyright and Similar
     Rights.

  e. Effective Technological Measures means those measures that, in the
     absence of proper authority, may not be circumvented under laws
     fulfilling obligations under Article 11 of the WIPO Copyright
     Treaty adopted on December 20, 1996, and/or similar international
     agreements.

  f. Exceptions and Limitations means fair use, fair dealing, and/or
     any other exception or limitation to Copyright and Similar Rights
     that applies to Your use of the Licensed Material.

  g. License Elements means the license attributes listed in the name
     of a Creative Commons Public License. The License Elements of this
     Public License are Attribution and ShareAlike.

  h. Licensed Material means the artistic or literary work, database,
     or other material to which the Licensor applied this Public
     License.

  i. Licensed Rights means the rights granted to You subject to the
     terms and conditions of this Public License, which are limited to
     all Copyright and Similar Rights that apply to Your use of the
     Licensed Material and that the Licensor has authority to license.

  j. Licensor means the individual(s) or entity(ies) granting rights
     under this Public License.

  k. Share means to provide material to the public by any means or
     process that requires permission under the Licensed Rights, such
     as reproduction, public display, public performance, distribution,
     dissemination, communication, or importation, and to make material
     available to the public including in ways that members of the
     public may access the material from a place and at a time
     individually chosen by them.

  l. Sui Generis Database Rights means rights other than copyright
     resulting from Directive 96/9/EC of the European Parliament and of
     the Council of 11 March 1996 on the legal protection of databases,
     as amended and/or succeeded, as well as other essentially
     equivalent rights anywhere in the world.

  m. You means the individual or entity exercising the Licensed Rights
     under this Public License. Your has a corresponding meaning.


Section 2 -- Scope.

  a. License grant.

       1. Subject to the terms and conditions of this Public License,
          the Licensor hereby grants You a worldwide, royalty-free,
          non-sublicensable, non-exclusive, irrevocable license to
          exercise the Licensed Rights in the Licensed Material to:

            a. reproduce and Share the Licensed Material, in whole or
               in part; and

            b. produce, reproduce, and Share Adapted Material.

       2. Exceptions and Limitations. For the avoidance of doubt, where
          Exceptions and Limitations apply to Your use, this Public
          License does not apply, and You do not need to comply with
          its terms and conditions.

       3. Term. The term of this Public License is specified in Section
          6(a).

       4. Media and formats; technical modifications allowed. The
          Licensor authorizes You to exercise the Licensed Rights in
          all media and formats whether now known or hereafter created,
          and to make technical modifications necessary to do so. The
          Licensor waives and/or agrees not to assert any right or
          authority to forbid You from making technical modifications
          necessary to exercise the Licensed Rights, including
          technical modifications necessary to circumvent Effective
          Technological Measures. For purposes of this Public License,
          simply making modifications authorized by this Section 2(a)
          (4) never produces Adapted Material.

       5. Downstream recipients.

            a. Offer from the Licensor -- Licensed Material. Every
               recipient of the Licensed Material automatically
               receives an offer from the Licensor to exercise the
               Licensed Rights under the terms and conditions of this
               Public License.

            b. Additional offer from the Licensor -- Adapted Material.
               Every recipient of Adapted Material from You
               automatically receives an offer from the Licensor to
               exercise the Licensed Rights in the Adapted Material
               under the conditions of the Adapter's License You apply.

            c. No downstream restrictions. You may not offer or impose
               any additional or different terms or conditions on, or
               apply any Effective Technological Measures to, the
               Licensed Material if doing so restricts exercise of the
               Licensed Rights by any recipient of the Licensed
               Material.

       6. No endorsement. Nothing in this Public License constitutes or
          may be construed as permission to assert or imply that You
          are, or that Your use of the Licensed Material is, connected
          with, or sponsored, endorsed, or granted official status by,
          the Licensor or others designated to receive attribution as
          provided in Section 3(a)(1)(A)(i).

  b. Other rights.

       1. Moral rights, such as the right of integrity, are not
          licensed under this Public License, nor are publicity,
          privacy, and/or other similar personality rights; however, to
          the extent possible, the Licensor waives and/or agrees not to
          assert any such rights held by the Licensor to the limited
          extent necessary to allow You to exercise the Licensed
          Rights, but not otherwise.

       2. Patent and trademark rights are not licensed under this
          Public License.

       3. To the extent possible, the Licensor waives any right to
          collect royalties from You for the exercise of the Licensed
          Rights, whether directly or through a collecting society
          under any voluntary or waivable statutory or compulsory
          licensing scheme. In all other cases the Licensor expressly
          reserves any right to collect such royalties.


Section 3 -- License Conditions.

Your exercise of the Licensed Rights is expressly made subject to the
following conditions.

  a. Attribution.

       1. If You Share the Licensed Material (including in modified
          form), You must:

            a. retain the following if it is supplied by the Licensor
               with the Licensed Material:

                 i. identification of the creator(s) of the Licensed
                    Material and any others designated to receive
                    attribution, in any reasonable manner requested by
                    the Licensor (including by pseudonym if
                    designated);

                ii. a copyright notice;

               iii. a notice that refers to this Public License;

                iv. a notice that refers to the disclaimer of
                    warranties;

                 v. a URI or hyperlink to the Licensed Material to the
                    extent reasonably practicable;

            b. indicate if You modified the Licensed Material and
               retain an indication of any previous modifications; and

            c. indicate the Licensed Material is licensed under this
               Public License, and include the text of, or the URI or
               hyperlink to, this Public License.

       2. You may satisfy the conditions in Section 3(a)(1) in any
          reasonable manner based on the medium, means, and context in
          which You Share the Licensed Material. For example, it may be
          reasonable to satisfy the conditions by providing a URI or
          hyperlink to a resource that includes the required
          information.

       3. If requested by the Licensor, You must remove any of the
          information required by Section 3(a)(1)(A) to the extent
          reasonably practicable.

  b. ShareAlike.

     In addition to the conditions in Section 3(a), if You Share
     Adapted Material You produce, the following conditions also apply.

       1. The Adapter's License You apply must be a Creative Commons
          license with the same License Elements, this version or
          later, or a BY-SA Compatible License.

       2. You must include the text of, or the URI or hyperlink to, the
          Adapter's License You apply. You may satisfy this condition
          in any reasonable manner based on the medium, means, and
          context in which You Share Adapted Material.

       3. You may not offer or impose any additional or different terms
          or conditions on, or apply any Effective Technological
          Measures to, Adapted Material that restrict exercise of the
          rights granted under the Adapter's License You apply.


Section 4 -- Sui Generis Database Rights.

Where the Licensed Rights include Sui Generis Database Rights that
apply to Your use of the Licensed Material:

  a. for the avoidance of doubt, Section 2(a)(1) grants You the right
     to extract, reuse, reproduce, and Share all or a substantial
     portion of the contents of the database;

  b. if You include all or a substantial portion of the database
     contents in a database in which You have Sui Generis Database
     Rights, then the database in which You have Sui Generis Database
     Rights (but not its individual contents) is Adapted Material,
     including for purposes of Section 3(b); and

  c. You must comply with the conditions in Section 3(a) if You Share
     all or a substantial portion of the contents of the database.

For the avoidance of doubt, this Section 4 supplements and does not
replace Your obligations under this Public License where the Licensed
Rights include other Copyright and Similar Rights.


Section 5 -- Disclaimer of Warranties and Limitation of Liability.

  a. UNLESS OTHERWISE SEPARATELY UNDERTAKEN BY THE LICENSOR, TO THE
     EXTENT POSSIBLE, THE LICENSOR OFFERS THE LICENSED MATERIAL AS-IS
     AND AS-AVAILABLE, AND MAKES NO REPRESENTATIONS OR WARRANTIES OF
     ANY KIND CONCERNING THE LICENSED MATERIAL, WHETHER EXPRESS,
     IMPLIED, STATUTORY, OR OTHER. THIS INCLUDES, WITHOUT LIMITATION,
     WARRANTIES OF TITLE, MERCHANTABILITY, FITNESS FOR A PARTICULAR
     PURPOSE, NON-INFRINGEMENT, ABSENCE OF LATENT OR OTHER DEFECTS,
     ACCURACY, OR THE PRESENCE OR ABSENCE OF ERRORS, WHETHER OR NOT
     KNOWN OR DISCOVERABLE. WHERE DISCLAIMERS OF WARRANTIES ARE NOT
     ALLOWED IN FULL OR IN PART, THIS DISCLAIMER MAY NOT APPLY TO YOU.

  b. TO THE EXTENT POSSIBLE, IN NO EVENT WILL THE LICENSOR BE LIABLE
     TO YOU ON ANY LEGAL THEORY (INCLUDING, WITHOUT LIMITATION,
     NEGLIGENCE) OR OTHERWISE FOR ANY DIRECT, SPECIAL, INDIRECT,
     INCIDENTAL, CONSEQUENTIAL, PUNITIVE, EXEMPLARY, OR OTHER LOSSES,
     COSTS, EXPENSES, OR DAMAGES ARISING OUT OF THIS PUBLIC LICENSE OR
     USE OF THE LICENSED MATERIAL, EVEN IF THE LICENSOR HAS BEEN
     ADVISED OF THE POSSIBILITY OF SUCH LOSSES, COSTS, EXPENSES, OR
     DAMAGES. WHERE A LIMITATION OF LIABILITY IS NOT ALLOWED IN FULL OR
     IN PART, THIS LIMITATION MAY NOT APPLY TO YOU.

  c. The disclaimer of warranties and limitation of liability provided
     above shall be interpreted in a manner that, to the extent
     possible, most closely approximates an absolute disclaimer and
     waiver of all liability.


Section 6 -- Term and Termination.

  a. This Public License applies for the term of the Copyright and
     Similar Rights licensed here. However, if You fail to comply with
     this Public License, then Your rights under this Public License
     terminate automatically.

  b. Where Your right to use the Licensed Material has terminated under
     Section 6(a), it reinstates:

       1. automatically as of the date the violation is cured, provided
          it is cured within 30 days of Your discovery of the
          violation; or

       2. upon express reinstatement by the Licensor.

     For the avoidance of doubt, this Section 6(b) does not affect any
     right the Licensor may have to seek remedies for Your violations
     of this Public License.

  c. For the avoidance of doubt, the Licensor may also offer the
     Licensed Material under separate terms or conditions or stop
     distributing the Licensed Material at any time; however, doing so
     will not terminate this Public License.

  d. Sections 1, 5, 6, 7, and 8 survive termination of this Public
     License.


Section 7 -- Other Terms and Conditions.

  a. The Licensor shall not be bound by any additional or different
     terms or conditions communicated by You unless expressly agreed.

  b. Any arrangements, understandings, or agreements regarding the
     Licensed Material not stated herein are separate from and
     independent of the terms and conditions of this Public License.


Section 8 -- Interpretation.

  a. For the avoidance of doubt, this Public License does not, and
     shall not be interpreted to, reduce, limit, restrict, or impose
     conditions on any use of the Licensed Material that could lawfully
     be made without permission under this Public License.

  b. To the extent possible, if any provision of this Public License is
     deemed unenforceable, it shall be automatically reformed to the
     minimum extent necessary to make it enforceable. If the provision
     cannot be reformed, it shall be severed from this Public License
     without affecting the enforceability of the remaining terms and
     conditions.

  c. No term or condition of this Public License will be waived and no
     failure to comply consented to unless expressly agreed to by the
     Licensor.

  d. Nothing in this Public License constitutes or may be interpreted
     as a limitation upon, or waiver of, any privileges and immunities
     that apply to the Licensor or You, including from the legal
     processes of any jurisdiction or authority.


=======================================================================

Creative Commons is not a party to its public
licenses. Notwithstanding, Creative Commons may elect to apply one of
its public licenses to material it publishes and in those instances
will be considered the “Licensor.” The text of the Creative Commons
public licenses is dedicated to the public domain under the CC0 Public
Domain Dedication. Except for the limited purpose of indicating that
material is shared under a Creative Commons public license or as
otherwise permitted by the Creative Commons policies published at
creativecommons.org/policies, Creative Commons does not authorize the
use of the trademark "Creative Commons" or any other trademark or logo
of Creative Commons without its prior written consent including,
without limitation, in connection with any unauthorized modifications
to any of its public licenses or any other arrangements,
understandings, or agreements concerning use of licensed material. For
the avoidance of doubt, this paragraph does not form part of the
public licenses.

Creative Commons may be contacted at creativecommons.org.
```

## C. Creative Commons Attribution-ShareAlike 3.0 Unported（CC BY-SA 3.0）

仅适用于 MarioWiki F.L.U.D.D. 已存文字节选、既有变化及对应 selector；不授权 Nintendo 图像或游戏材料，不把当前4.0倒写为2023年许可。
官方法条：https://creativecommons.org/licenses/by-sa/3.0/legalcode

```text
Creative Commons Legal Code

Attribution-ShareAlike 3.0 Unported

    CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE
    LEGAL SERVICES. DISTRIBUTION OF THIS LICENSE DOES NOT CREATE AN
    ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS
    INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES
    REGARDING THE INFORMATION PROVIDED, AND DISCLAIMS LIABILITY FOR
    DAMAGES RESULTING FROM ITS USE.

License

THE WORK (AS DEFINED BELOW) IS PROVIDED UNDER THE TERMS OF THIS CREATIVE
COMMONS PUBLIC LICENSE ("CCPL" OR "LICENSE"). THE WORK IS PROTECTED BY
COPYRIGHT AND/OR OTHER APPLICABLE LAW. ANY USE OF THE WORK OTHER THAN AS
AUTHORIZED UNDER THIS LICENSE OR COPYRIGHT LAW IS PROHIBITED.

BY EXERCISING ANY RIGHTS TO THE WORK PROVIDED HERE, YOU ACCEPT AND AGREE
TO BE BOUND BY THE TERMS OF THIS LICENSE. TO THE EXTENT THIS LICENSE MAY
BE CONSIDERED TO BE A CONTRACT, THE LICENSOR GRANTS YOU THE RIGHTS
CONTAINED HERE IN CONSIDERATION OF YOUR ACCEPTANCE OF SUCH TERMS AND
CONDITIONS.

1. Definitions

 a. "Adaptation" means a work based upon the Work, or upon the Work and
    other pre-existing works, such as a translation, adaptation,
    derivative work, arrangement of music or other alterations of a
    literary or artistic work, or phonogram or performance and includes
    cinematographic adaptations or any other form in which the Work may be
    recast, transformed, or adapted including in any form recognizably
    derived from the original, except that a work that constitutes a
    Collection will not be considered an Adaptation for the purpose of
    this License. For the avoidance of doubt, where the Work is a musical
    work, performance or phonogram, the synchronization of the Work in
    timed-relation with a moving image ("synching") will be considered an
    Adaptation for the purpose of this License.
 b. "Collection" means a collection of literary or artistic works, such as
    encyclopedias and anthologies, or performances, phonograms or
    broadcasts, or other works or subject matter other than works listed
    in Section 1(f) below, which, by reason of the selection and
    arrangement of their contents, constitute intellectual creations, in
    which the Work is included in its entirety in unmodified form along
    with one or more other contributions, each constituting separate and
    independent works in themselves, which together are assembled into a
    collective whole. A work that constitutes a Collection will not be
    considered an Adaptation (as defined below) for the purposes of this
    License.
 c. "Creative Commons Compatible License" means a license that is listed
    at https://creativecommons.org/compatiblelicenses that has been
    approved by Creative Commons as being essentially equivalent to this
    License, including, at a minimum, because that license: (i) contains
    terms that have the same purpose, meaning and effect as the License
    Elements of this License; and, (ii) explicitly permits the relicensing
    of adaptations of works made available under that license under this
    License or a Creative Commons jurisdiction license with the same
    License Elements as this License.
 d. "Distribute" means to make available to the public the original and
    copies of the Work or Adaptation, as appropriate, through sale or
    other transfer of ownership.
 e. "License Elements" means the following high-level license attributes
    as selected by Licensor and indicated in the title of this License:
    Attribution, ShareAlike.
 f. "Licensor" means the individual, individuals, entity or entities that
    offer(s) the Work under the terms of this License.
 g. "Original Author" means, in the case of a literary or artistic work,
    the individual, individuals, entity or entities who created the Work
    or if no individual or entity can be identified, the publisher; and in
    addition (i) in the case of a performance the actors, singers,
    musicians, dancers, and other persons who act, sing, deliver, declaim,
    play in, interpret or otherwise perform literary or artistic works or
    expressions of folklore; (ii) in the case of a phonogram the producer
    being the person or legal entity who first fixes the sounds of a
    performance or other sounds; and, (iii) in the case of broadcasts, the
    organization that transmits the broadcast.
 h. "Work" means the literary and/or artistic work offered under the terms
    of this License including without limitation any production in the
    literary, scientific and artistic domain, whatever may be the mode or
    form of its expression including digital form, such as a book,
    pamphlet and other writing; a lecture, address, sermon or other work
    of the same nature; a dramatic or dramatico-musical work; a
    choreographic work or entertainment in dumb show; a musical
    composition with or without words; a cinematographic work to which are
    assimilated works expressed by a process analogous to cinematography;
    a work of drawing, painting, architecture, sculpture, engraving or
    lithography; a photographic work to which are assimilated works
    expressed by a process analogous to photography; a work of applied
    art; an illustration, map, plan, sketch or three-dimensional work
    relative to geography, topography, architecture or science; a
    performance; a broadcast; a phonogram; a compilation of data to the
    extent it is protected as a copyrightable work; or a work performed by
    a variety or circus performer to the extent it is not otherwise
    considered a literary or artistic work.
 i. "You" means an individual or entity exercising rights under this
    License who has not previously violated the terms of this License with
    respect to the Work, or who has received express permission from the
    Licensor to exercise rights under this License despite a previous
    violation.
 j. "Publicly Perform" means to perform public recitations of the Work and
    to communicate to the public those public recitations, by any means or
    process, including by wire or wireless means or public digital
    performances; to make available to the public Works in such a way that
    members of the public may access these Works from a place and at a
    place individually chosen by them; to perform the Work to the public
    by any means or process and the communication to the public of the
    performances of the Work, including by public digital performance; to
    broadcast and rebroadcast the Work by any means including signs,
    sounds or images.
 k. "Reproduce" means to make copies of the Work by any means including
    without limitation by sound or visual recordings and the right of
    fixation and reproducing fixations of the Work, including storage of a
    protected performance or phonogram in digital form or other electronic
    medium.

2. Fair Dealing Rights. Nothing in this License is intended to reduce,
limit, or restrict any uses free from copyright or rights arising from
limitations or exceptions that are provided for in connection with the
copyright protection under copyright law or other applicable laws.

3. License Grant. Subject to the terms and conditions of this License,
Licensor hereby grants You a worldwide, royalty-free, non-exclusive,
perpetual (for the duration of the applicable copyright) license to
exercise the rights in the Work as stated below:

 a. to Reproduce the Work, to incorporate the Work into one or more
    Collections, and to Reproduce the Work as incorporated in the
    Collections;
 b. to create and Reproduce Adaptations provided that any such Adaptation,
    including any translation in any medium, takes reasonable steps to
    clearly label, demarcate or otherwise identify that changes were made
    to the original Work. For example, a translation could be marked "The
    original work was translated from English to Spanish," or a
    modification could indicate "The original work has been modified.";
 c. to Distribute and Publicly Perform the Work including as incorporated
    in Collections; and,
 d. to Distribute and Publicly Perform Adaptations.
 e. For the avoidance of doubt:

     i. Non-waivable Compulsory License Schemes. In those jurisdictions in
        which the right to collect royalties through any statutory or
        compulsory licensing scheme cannot be waived, the Licensor
        reserves the exclusive right to collect such royalties for any
        exercise by You of the rights granted under this License;
    ii. Waivable Compulsory License Schemes. In those jurisdictions in
        which the right to collect royalties through any statutory or
        compulsory licensing scheme can be waived, the Licensor waives the
        exclusive right to collect such royalties for any exercise by You
        of the rights granted under this License; and,
   iii. Voluntary License Schemes. The Licensor waives the right to
        collect royalties, whether individually or, in the event that the
        Licensor is a member of a collecting society that administers
        voluntary licensing schemes, via that society, from any exercise
        by You of the rights granted under this License.

The above rights may be exercised in all media and formats whether now
known or hereafter devised. The above rights include the right to make
such modifications as are technically necessary to exercise the rights in
other media and formats. Subject to Section 8(f), all rights not expressly
granted by Licensor are hereby reserved.

4. Restrictions. The license granted in Section 3 above is expressly made
subject to and limited by the following restrictions:

 a. You may Distribute or Publicly Perform the Work only under the terms
    of this License. You must include a copy of, or the Uniform Resource
    Identifier (URI) for, this License with every copy of the Work You
    Distribute or Publicly Perform. You may not offer or impose any terms
    on the Work that restrict the terms of this License or the ability of
    the recipient of the Work to exercise the rights granted to that
    recipient under the terms of the License. You may not sublicense the
    Work. You must keep intact all notices that refer to this License and
    to the disclaimer of warranties with every copy of the Work You
    Distribute or Publicly Perform. When You Distribute or Publicly
    Perform the Work, You may not impose any effective technological
    measures on the Work that restrict the ability of a recipient of the
    Work from You to exercise the rights granted to that recipient under
    the terms of the License. This Section 4(a) applies to the Work as
    incorporated in a Collection, but this does not require the Collection
    apart from the Work itself to be made subject to the terms of this
    License. If You create a Collection, upon notice from any Licensor You
    must, to the extent practicable, remove from the Collection any credit
    as required by Section 4(c), as requested. If You create an
    Adaptation, upon notice from any Licensor You must, to the extent
    practicable, remove from the Adaptation any credit as required by
    Section 4(c), as requested.
 b. You may Distribute or Publicly Perform an Adaptation only under the
    terms of: (i) this License; (ii) a later version of this License with
    the same License Elements as this License; (iii) a Creative Commons
    jurisdiction license (either this or a later license version) that
    contains the same License Elements as this License (e.g.,
    Attribution-ShareAlike 3.0 US)); (iv) a Creative Commons Compatible
    License. If you license the Adaptation under one of the licenses
    mentioned in (iv), you must comply with the terms of that license. If
    you license the Adaptation under the terms of any of the licenses
    mentioned in (i), (ii) or (iii) (the "Applicable License"), you must
    comply with the terms of the Applicable License generally and the
    following provisions: (I) You must include a copy of, or the URI for,
    the Applicable License with every copy of each Adaptation You
    Distribute or Publicly Perform; (II) You may not offer or impose any
    terms on the Adaptation that restrict the terms of the Applicable
    License or the ability of the recipient of the Adaptation to exercise
    the rights granted to that recipient under the terms of the Applicable
    License; (III) You must keep intact all notices that refer to the
    Applicable License and to the disclaimer of warranties with every copy
    of the Work as included in the Adaptation You Distribute or Publicly
    Perform; (IV) when You Distribute or Publicly Perform the Adaptation,
    You may not impose any effective technological measures on the
    Adaptation that restrict the ability of a recipient of the Adaptation
    from You to exercise the rights granted to that recipient under the
    terms of the Applicable License. This Section 4(b) applies to the
    Adaptation as incorporated in a Collection, but this does not require
    the Collection apart from the Adaptation itself to be made subject to
    the terms of the Applicable License.
 c. If You Distribute, or Publicly Perform the Work or any Adaptations or
    Collections, You must, unless a request has been made pursuant to
    Section 4(a), keep intact all copyright notices for the Work and
    provide, reasonable to the medium or means You are utilizing: (i) the
    name of the Original Author (or pseudonym, if applicable) if supplied,
    and/or if the Original Author and/or Licensor designate another party
    or parties (e.g., a sponsor institute, publishing entity, journal) for
    attribution ("Attribution Parties") in Licensor's copyright notice,
    terms of service or by other reasonable means, the name of such party
    or parties; (ii) the title of the Work if supplied; (iii) to the
    extent reasonably practicable, the URI, if any, that Licensor
    specifies to be associated with the Work, unless such URI does not
    refer to the copyright notice or licensing information for the Work;
    and (iv) , consistent with Ssection 3(b), in the case of an
    Adaptation, a credit identifying the use of the Work in the Adaptation
    (e.g., "French translation of the Work by Original Author," or
    "Screenplay based on original Work by Original Author"). The credit
    required by this Section 4(c) may be implemented in any reasonable
    manner; provided, however, that in the case of a Adaptation or
    Collection, at a minimum such credit will appear, if a credit for all
    contributing authors of the Adaptation or Collection appears, then as
    part of these credits and in a manner at least as prominent as the
    credits for the other contributing authors. For the avoidance of
    doubt, You may only use the credit required by this Section for the
    purpose of attribution in the manner set out above and, by exercising
    Your rights under this License, You may not implicitly or explicitly
    assert or imply any connection with, sponsorship or endorsement by the
    Original Author, Licensor and/or Attribution Parties, as appropriate,
    of You or Your use of the Work, without the separate, express prior
    written permission of the Original Author, Licensor and/or Attribution
    Parties.
 d. Except as otherwise agreed in writing by the Licensor or as may be
    otherwise permitted by applicable law, if You Reproduce, Distribute or
    Publicly Perform the Work either by itself or as part of any
    Adaptations or Collections, You must not distort, mutilate, modify or
    take other derogatory action in relation to the Work which would be
    prejudicial to the Original Author's honor or reputation. Licensor
    agrees that in those jurisdictions (e.g. Japan), in which any exercise
    of the right granted in Section 3(b) of this License (the right to
    make Adaptations) would be deemed to be a distortion, mutilation,
    modification or other derogatory action prejudicial to the Original
    Author's honor and reputation, the Licensor will waive or not assert,
    as appropriate, this Section, to the fullest extent permitted by the
    applicable national law, to enable You to reasonably exercise Your
    right under Section 3(b) of this License (right to make Adaptations)
    but not otherwise.

5. Representations, Warranties and Disclaimer

UNLESS OTHERWISE MUTUALLY AGREED TO BY THE PARTIES IN WRITING, LICENSOR
OFFERS THE WORK AS-IS AND MAKES NO REPRESENTATIONS OR WARRANTIES OF ANY
KIND CONCERNING THE WORK, EXPRESS, IMPLIED, STATUTORY OR OTHERWISE,
INCLUDING, WITHOUT LIMITATION, WARRANTIES OF TITLE, MERCHANTIBILITY,
FITNESS FOR A PARTICULAR PURPOSE, NONINFRINGEMENT, OR THE ABSENCE OF
LATENT OR OTHER DEFECTS, ACCURACY, OR THE PRESENCE OF ABSENCE OF ERRORS,
WHETHER OR NOT DISCOVERABLE. SOME JURISDICTIONS DO NOT ALLOW THE EXCLUSION
OF IMPLIED WARRANTIES, SO SUCH EXCLUSION MAY NOT APPLY TO YOU.

6. Limitation on Liability. EXCEPT TO THE EXTENT REQUIRED BY APPLICABLE
LAW, IN NO EVENT WILL LICENSOR BE LIABLE TO YOU ON ANY LEGAL THEORY FOR
ANY SPECIAL, INCIDENTAL, CONSEQUENTIAL, PUNITIVE OR EXEMPLARY DAMAGES
ARISING OUT OF THIS LICENSE OR THE USE OF THE WORK, EVEN IF LICENSOR HAS
BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

7. Termination

 a. This License and the rights granted hereunder will terminate
    automatically upon any breach by You of the terms of this License.
    Individuals or entities who have received Adaptations or Collections
    from You under this License, however, will not have their licenses
    terminated provided such individuals or entities remain in full
    compliance with those licenses. Sections 1, 2, 5, 6, 7, and 8 will
    survive any termination of this License.
 b. Subject to the above terms and conditions, the license granted here is
    perpetual (for the duration of the applicable copyright in the Work).
    Notwithstanding the above, Licensor reserves the right to release the
    Work under different license terms or to stop distributing the Work at
    any time; provided, however that any such election will not serve to
    withdraw this License (or any other license that has been, or is
    required to be, granted under the terms of this License), and this
    License will continue in full force and effect unless terminated as
    stated above.

8. Miscellaneous

 a. Each time You Distribute or Publicly Perform the Work or a Collection,
    the Licensor offers to the recipient a license to the Work on the same
    terms and conditions as the license granted to You under this License.
 b. Each time You Distribute or Publicly Perform an Adaptation, Licensor
    offers to the recipient a license to the original Work on the same
    terms and conditions as the license granted to You under this License.
 c. If any provision of this License is invalid or unenforceable under
    applicable law, it shall not affect the validity or enforceability of
    the remainder of the terms of this License, and without further action
    by the parties to this agreement, such provision shall be reformed to
    the minimum extent necessary to make such provision valid and
    enforceable.
 d. No term or provision of this License shall be deemed waived and no
    breach consented to unless such waiver or consent shall be in writing
    and signed by the party to be charged with such waiver or consent.
 e. This License constitutes the entire agreement between the parties with
    respect to the Work licensed here. There are no understandings,
    agreements or representations with respect to the Work not specified
    here. Licensor shall not be bound by any additional provisions that
    may appear in any communication from You. This License may not be
    modified without the mutual written agreement of the Licensor and You.
 f. The rights granted under, and the subject matter referenced, in this
    License were drafted utilizing the terminology of the Berne Convention
    for the Protection of Literary and Artistic Works (as amended on
    September 28, 1979), the Rome Convention of 1961, the WIPO Copyright
    Treaty of 1996, the WIPO Performances and Phonograms Treaty of 1996
    and the Universal Copyright Convention (as revised on July 24, 1971).
    These rights and subject matter take effect in the relevant
    jurisdiction in which the License terms are sought to be enforced
    according to the corresponding provisions of the implementation of
    those treaty provisions in the applicable national law. If the
    standard suite of rights granted under applicable copyright law
    includes additional rights not granted under this License, such
    additional rights are deemed to be included in the License; this
    License is not intended to restrict the license of any rights under
    applicable law.


Creative Commons Notice

    Creative Commons is not a party to this License, and makes no warranty
    whatsoever in connection with the Work. Creative Commons will not be
    liable to You or any party on any legal theory for any damages
    whatsoever, including without limitation any general, special,
    incidental or consequential damages arising in connection to this
    license. Notwithstanding the foregoing two (2) sentences, if Creative
    Commons has expressly identified itself as the Licensor hereunder, it
    shall have all rights and obligations of Licensor.

    Except for the limited purpose of indicating to the public that the
    Work is licensed under the CCPL, Creative Commons does not authorize
    the use by either party of the trademark "Creative Commons" or any
    related trademark or logo of Creative Commons without the prior
    written consent of Creative Commons. Any permitted use will be in
    compliance with Creative Commons' then-current trademark usage
    guidelines, as may be published on its website or otherwise made
    available upon request from time to time. For the avoidance of doubt,
    this trademark restriction does not form part of the License.

    Creative Commons may be contacted at https://creativecommons.org/.
```

## D. The LaTeX Project Public License, Version 1.3c（LPPL 1.3c）

仅适用于原样 acl_natbib.bst 及其生成修改，保留原始归属与许可头注；原文允许 version 1 or any later version，此包选择1.3c，不声称仓库为 Current Maintainer。
官方法条：https://www.latex-project.org/lppl/lppl-1-3c.txt

```text
The LaTeX Project Public License
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

LPPL Version 1.3c  2008-05-04

Copyright 1999 2002-2008 LaTeX3 Project
    Everyone is allowed to distribute verbatim copies of this
    license document, but modification of it is not allowed.


PREAMBLE
========

The LaTeX Project Public License (LPPL) is the primary license under
which the LaTeX kernel and the base LaTeX packages are distributed.

You may use this license for any work of which you hold the copyright
and which you wish to distribute.  This license may be particularly
suitable if your work is TeX-related (such as a LaTeX package), but 
it is written in such a way that you can use it even if your work is 
unrelated to TeX.

The section `WHETHER AND HOW TO DISTRIBUTE WORKS UNDER THIS LICENSE',
below, gives instructions, examples, and recommendations for authors
who are considering distributing their works under this license.

This license gives conditions under which a work may be distributed
and modified, as well as conditions under which modified versions of
that work may be distributed.

We, the LaTeX3 Project, believe that the conditions below give you
the freedom to make and distribute modified versions of your work
that conform with whatever technical specifications you wish while
maintaining the availability, integrity, and reliability of
that work.  If you do not see how to achieve your goal while
meeting these conditions, then read the document `cfgguide.tex'
and `modguide.tex' in the base LaTeX distribution for suggestions.


DEFINITIONS
===========

In this license document the following terms are used:

   `Work'
    Any work being distributed under this License.
    
   `Derived Work'
    Any work that under any applicable law is derived from the Work.

   `Modification' 
    Any procedure that produces a Derived Work under any applicable
    law -- for example, the production of a file containing an
    original file associated with the Work or a significant portion of
    such a file, either verbatim or with modifications and/or
    translated into another language.

   `Modify'
    To apply any procedure that produces a Derived Work under any
    applicable law.
    
   `Distribution'
    Making copies of the Work available from one person to another, in
    whole or in part.  Distribution includes (but is not limited to)
    making any electronic components of the Work accessible by
    file transfer protocols such as FTP or HTTP or by shared file
    systems such as Sun's Network File System (NFS).

   `Compiled Work'
    A version of the Work that has been processed into a form where it
    is directly usable on a computer system.  This processing may
    include using installation facilities provided by the Work,
    transformations of the Work, copying of components of the Work, or
    other activities.  Note that modification of any installation
    facilities provided by the Work constitutes modification of the Work.

   `Current Maintainer'
    A person or persons nominated as such within the Work.  If there is
    no such explicit nomination then it is the `Copyright Holder' under
    any applicable law.

   `Base Interpreter' 
    A program or process that is normally needed for running or
    interpreting a part or the whole of the Work.    

    A Base Interpreter may depend on external components but these
    are not considered part of the Base Interpreter provided that each
    external component clearly identifies itself whenever it is used
    interactively.  Unless explicitly specified when applying the
    license to the Work, the only applicable Base Interpreter is a
    `LaTeX-Format' or in the case of files belonging to the 
    `LaTeX-format' a program implementing the `TeX language'.



CONDITIONS ON DISTRIBUTION AND MODIFICATION
===========================================

1.  Activities other than distribution and/or modification of the Work
are not covered by this license; they are outside its scope.  In
particular, the act of running the Work is not restricted and no
requirements are made concerning any offers of support for the Work.

2.  You may distribute a complete, unmodified copy of the Work as you
received it.  Distribution of only part of the Work is considered
modification of the Work, and no right to distribute such a Derived
Work may be assumed under the terms of this clause.

3.  You may distribute a Compiled Work that has been generated from a
complete, unmodified copy of the Work as distributed under Clause 2
above, as long as that Compiled Work is distributed in such a way that
the recipients may install the Compiled Work on their system exactly
as it would have been installed if they generated a Compiled Work
directly from the Work.

4.  If you are the Current Maintainer of the Work, you may, without
restriction, modify the Work, thus creating a Derived Work.  You may
also distribute the Derived Work without restriction, including
Compiled Works generated from the Derived Work.  Derived Works
distributed in this manner by the Current Maintainer are considered to
be updated versions of the Work.

5.  If you are not the Current Maintainer of the Work, you may modify
your copy of the Work, thus creating a Derived Work based on the Work,
and compile this Derived Work, thus creating a Compiled Work based on
the Derived Work.

6.  If you are not the Current Maintainer of the Work, you may
distribute a Derived Work provided the following conditions are met
for every component of the Work unless that component clearly states
in the copyright notice that it is exempt from that condition.  Only
the Current Maintainer is allowed to add such statements of exemption 
to a component of the Work. 

  a. If a component of this Derived Work can be a direct replacement
     for a component of the Work when that component is used with the
     Base Interpreter, then, wherever this component of the Work
     identifies itself to the user when used interactively with that
     Base Interpreter, the replacement component of this Derived Work
     clearly and unambiguously identifies itself as a modified version
     of this component to the user when used interactively with that
     Base Interpreter.
     
  b. Every component of the Derived Work contains prominent notices
     detailing the nature of the changes to that component, or a
     prominent reference to another file that is distributed as part
     of the Derived Work and that contains a complete and accurate log
     of the changes.
  
  c. No information in the Derived Work implies that any persons,
     including (but not limited to) the authors of the original version
     of the Work, provide any support, including (but not limited to)
     the reporting and handling of errors, to recipients of the
     Derived Work unless those persons have stated explicitly that
     they do provide such support for the Derived Work.

  d. You distribute at least one of the following with the Derived Work:

       1. A complete, unmodified copy of the Work; 
          if your distribution of a modified component is made by
          offering access to copy the modified component from a
          designated place, then offering equivalent access to copy
          the Work from the same or some similar place meets this
          condition, even though third parties are not compelled to
          copy the Work along with the modified component;

       2. Information that is sufficient to obtain a complete,
          unmodified copy of the Work.

7.  If you are not the Current Maintainer of the Work, you may
distribute a Compiled Work generated from a Derived Work, as long as
the Derived Work is distributed to all recipients of the Compiled
Work, and as long as the conditions of Clause 6, above, are met with
regard to the Derived Work.

8.  The conditions above are not intended to prohibit, and hence do not
apply to, the modification, by any method, of any component so that it
becomes identical to an updated version of that component of the Work as
it is distributed by the Current Maintainer under Clause 4, above.

9.  Distribution of the Work or any Derived Work in an alternative
format, where the Work or that Derived Work (in whole or in part) is
then produced by applying some process to that format, does not relax or
nullify any sections of this license as they pertain to the results of
applying that process.
     
10. a. A Derived Work may be distributed under a different license
       provided that license itself honors the conditions listed in
       Clause 6 above, in regard to the Work, though it does not have
       to honor the rest of the conditions in this license.
      
    b. If a Derived Work is distributed under a different license, that
       Derived Work must provide sufficient documentation as part of
       itself to allow each recipient of that Derived Work to honor the 
       restrictions in Clause 6 above, concerning changes from the Work.

11. This license places no restrictions on works that are unrelated to
the Work, nor does this license place any restrictions on aggregating
such works with the Work by any means.

12.  Nothing in this license is intended to, or may be used to, prevent
complete compliance by all parties with all applicable laws.


NO WARRANTY
===========

There is no warranty for the Work.  Except when otherwise stated in
writing, the Copyright Holder provides the Work `as is', without
warranty of any kind, either expressed or implied, including, but not
limited to, the implied warranties of merchantability and fitness for a
particular purpose.  The entire risk as to the quality and performance
of the Work is with you.  Should the Work prove defective, you assume
the cost of all necessary servicing, repair, or correction.

In no event unless required by applicable law or agreed to in writing
will The Copyright Holder, or any author named in the components of the
Work, or any other party who may distribute and/or modify the Work as
permitted above, be liable to you for damages, including any general,
special, incidental or consequential damages arising out of any use of
the Work or out of inability to use the Work (including, but not limited
to, loss of data, data being rendered inaccurate, or losses sustained by
anyone as a result of any failure of the Work to operate with any other
programs), even if the Copyright Holder or said author or said other
party has been advised of the possibility of such damages.


MAINTENANCE OF THE WORK
=======================

The Work has the status `author-maintained' if the Copyright Holder
explicitly and prominently states near the primary copyright notice in
the Work that the Work can only be maintained by the Copyright Holder
or simply that it is `author-maintained'.

The Work has the status `maintained' if there is a Current Maintainer
who has indicated in the Work that they are willing to receive error
reports for the Work (for example, by supplying a valid e-mail
address). It is not required for the Current Maintainer to acknowledge
or act upon these error reports.

The Work changes from status `maintained' to `unmaintained' if there
is no Current Maintainer, or the person stated to be Current
Maintainer of the work cannot be reached through the indicated means
of communication for a period of six months, and there are no other
significant signs of active maintenance.

You can become the Current Maintainer of the Work by agreement with
any existing Current Maintainer to take over this role.

If the Work is unmaintained, you can become the Current Maintainer of
the Work through the following steps:

 1.  Make a reasonable attempt to trace the Current Maintainer (and
     the Copyright Holder, if the two differ) through the means of
     an Internet or similar search.

 2.  If this search is successful, then enquire whether the Work
     is still maintained.

  a. If it is being maintained, then ask the Current Maintainer
     to update their communication data within one month.
     
  b. If the search is unsuccessful or no action to resume active
     maintenance is taken by the Current Maintainer, then announce
     within the pertinent community your intention to take over
     maintenance.  (If the Work is a LaTeX work, this could be
     done, for example, by posting to comp.text.tex.)

 3a. If the Current Maintainer is reachable and agrees to pass
     maintenance of the Work to you, then this takes effect
     immediately upon announcement.
     
  b. If the Current Maintainer is not reachable and the Copyright
     Holder agrees that maintenance of the Work be passed to you,
     then this takes effect immediately upon announcement.  
    
 4.  If you make an `intention announcement' as described in 2b. above
     and after three months your intention is challenged neither by
     the Current Maintainer nor by the Copyright Holder nor by other
     people, then you may arrange for the Work to be changed so as
     to name you as the (new) Current Maintainer.
     
 5.  If the previously unreachable Current Maintainer becomes
     reachable once more within three months of a change completed
     under the terms of 3b) or 4), then that Current Maintainer must
     become or remain the Current Maintainer upon request provided
     they then update their communication data within one month.

A change in the Current Maintainer does not, of itself, alter the fact
that the Work is distributed under the LPPL license.

If you become the Current Maintainer of the Work, you should
immediately provide, within the Work, a prominent and unambiguous
statement of your status as Current Maintainer.  You should also
announce your new status to the same pertinent community as
in 2b) above.


WHETHER AND HOW TO DISTRIBUTE WORKS UNDER THIS LICENSE
======================================================

This section contains important instructions, examples, and
recommendations for authors who are considering distributing their
works under this license.  These authors are addressed as `you' in
this section.

Choosing This License or Another License
----------------------------------------

If for any part of your work you want or need to use *distribution*
conditions that differ significantly from those in this license, then
do not refer to this license anywhere in your work but, instead,
distribute your work under a different license.  You may use the text
of this license as a model for your own license, but your license
should not refer to the LPPL or otherwise give the impression that
your work is distributed under the LPPL.

The document `modguide.tex' in the base LaTeX distribution explains
the motivation behind the conditions of this license.  It explains,
for example, why distributing LaTeX under the GNU General Public
License (GPL) was considered inappropriate.  Even if your work is
unrelated to LaTeX, the discussion in `modguide.tex' may still be
relevant, and authors intending to distribute their works under any
license are encouraged to read it.

A Recommendation on Modification Without Distribution
-----------------------------------------------------

It is wise never to modify a component of the Work, even for your own
personal use, without also meeting the above conditions for
distributing the modified component.  While you might intend that such
modifications will never be distributed, often this will happen by
accident -- you may forget that you have modified that component; or
it may not occur to you when allowing others to access the modified
version that you are thus distributing it and violating the conditions
of this license in ways that could have legal implications and, worse,
cause problems for the community.  It is therefore usually in your
best interest to keep your copy of the Work identical with the public
one.  Many works provide ways to control the behavior of that work
without altering any of its licensed components.

How to Use This License
-----------------------

To use this license, place in each of the components of your work both
an explicit copyright notice including your name and the year the work
was authored and/or last substantially modified.  Include also a
statement that the distribution and/or modification of that
component is constrained by the conditions in this license.

Here is an example of such a notice and statement:

  %% pig.dtx
  %% Copyright 2008 M. Y. Name
  %
  % This work may be distributed and/or modified under the
  % conditions of the LaTeX Project Public License, either version 1.3
  % of this license or (at your option) any later version.
  % The latest version of this license is in
  %   https://www.latex-project.org/lppl.txt
  % and version 1.3c or later is part of all distributions of LaTeX
  % version 2008 or later.
  %
  % This work has the LPPL maintenance status `maintained'.
  % 
  % The Current Maintainer of this work is M. Y. Name.
  %
  % This work consists of the files pig.dtx and pig.ins
  % and the derived file pig.sty.

Given such a notice and statement in a file, the conditions
given in this license document would apply, with the `Work' referring
to the three files `pig.dtx', `pig.ins', and `pig.sty' (the last being
generated from `pig.dtx' using `pig.ins'), the `Base Interpreter'
referring to any `LaTeX-Format', and both `Copyright Holder' and
`Current Maintainer' referring to the person `M. Y. Name'.

If you do not want the Maintenance section of LPPL to apply to your
Work, change `maintained' above into `author-maintained'.  
However, we recommend that you use `maintained', as the Maintenance
section was added in order to ensure that your Work remains useful to
the community even when you can no longer maintain and support it
yourself.

Derived Works That Are Not Replacements
---------------------------------------

Several clauses of the LPPL specify means to provide reliability and
stability for the user community. They therefore concern themselves
with the case that a Derived Work is intended to be used as a
(compatible or incompatible) replacement of the original Work. If
this is not the case (e.g., if a few lines of code are reused for a
completely different task), then clauses 6b and 6d shall not apply.


Important Recommendations
-------------------------

 Defining What Constitutes the Work

   The LPPL requires that distributions of the Work contain all the
   files of the Work.  It is therefore important that you provide a
   way for the licensee to determine which files constitute the Work.
   This could, for example, be achieved by explicitly listing all the
   files of the Work near the copyright notice of each file or by
   using a line such as:

    % This work consists of all files listed in manifest.txt.
   
   in that place.  In the absence of an unequivocal list it might be
   impossible for the licensee to determine what is considered by you
   to comprise the Work and, in such a case, the licensee would be
   entitled to make reasonable conjectures as to which files comprise
   the Work.

```
