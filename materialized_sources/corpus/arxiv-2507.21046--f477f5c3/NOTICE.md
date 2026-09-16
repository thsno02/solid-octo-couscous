# arXiv CC BY 4.0、TMLR Apache 2.0 与 LPPL 1.3c 组合许可说明

## 本仓库使用说明（repository use note）

本文件是 `arxiv:2507.21046` 固定 v4 文本胶囊的独立组合许可资产，并作为现有生成器写入胶囊 `NOTICE.md` 的来源。以下三份法律文本分别适用于独立材料，不将论文许可外推到模板，也不以模板仓库的 Apache 2.0 覆盖组件内保留的 LPPL 声明：

- 论文作者的主文、附录文字及其文本转换：固定 arXiv v4 文章页面声明的 CC BY 4.0。
- 实存 `source/tmlr.sty`：TMLR 官方作者指南直接链接的 `JmlrOrg/tmlr-style-file` 仓库所授予的 Apache License 2.0；模板头注明 Hugo Larochelle 和 Fabian Pedregosa 的改编，以及 Chris J. Maddison 于 January 2021 的字体修改，署名原样保留。
- 实存 `source/tmlr.bst`：组件自身声明 LPPL version 1 or later，本包装选择 LPPL 1.3c。保留 Copyright 2010 Hal Daum\'e III、J. Fürnkranz 的标签修改说明，以及 Copyright 1993-2007 Patrick W Daly。
- 实存 `source/fancyhdr.sty`：组件自身声明 LPPL version 1.3 or later，本包装选择 LPPL 1.3c。保留 Copyright (C) 1994-2021 Pieter van Oostrum、`2021/01/28 v4.0.1` 运行时身份，以及 `fancyhdr.dtx` / docstrip 的原生成来源说明。

这三个组件与官方模板仓库固定 commit `7bf90efe3a0debbba703c05c43f3ff7e4d4a2992` 中相应文件逐字相同，本仓库没有修改其程序、文件名或运行时身份。LPPL 生成文件按原样可安装的编译作品（Compiled Work）路径保留；`tmlr.bst` 保留官方已分发的独立名称和完整上游归属。此说明不暗示论文作者、模板作者或 LPPL 上游作者为本胶囊提供支持。它不会解除其他文件另行注明的附加分发条件；本胶囊没有实存 `natbib.sty`，模板中的 `RequirePackage{natbib}` 只是外部依赖，不是该组件的再分发。

`source/main.bib` 中三段额外摘要不能视为论文作者原创或元数据 CC0；各段的作品级许可和署名在 canonical package 中逐一绑定。两段 ACL 摘要分别来自 AppBench（2024.emnlp-main.856）和 ARIA（2025.emnlp-industry.115），官方作品页面直接展示对应摘要，ACL 将 2016 年及以后发布的 ACL materials 归于 CC BY 4.0。ACM SIGIR 2024 `tool_tut` 条目对应 DOI `10.1145/3626772.3661381`；ACM 提交的 Crossref 作品记录声明 Version of Record 的 CC BY 4.0，起始日 2024-07-10、delay-in-days 0。其 DOI、题名、五作者、SIGIR 2024 proceedings 和页码与实存条目一致，没有不同预印本或相反声明，本包据此合理依赖正式作品许可覆盖该实际摘要。Crossref 记录不包含 abstract，本包不冒称 ACM 摘要或 PDF 已逐字复核；作品许可声明不是元数据 CC0 推断，也不构成人工审批或发布准入。

`source/00README.json` 是 arXiv 自动处理/编译元数据；官方 00README 文档说明其自动生成用途，arXiv submission agreement 对 arXiv/提交者有权许可的 metadata 使用 CC0。这个依据只用于事实编译元数据，不覆盖 Bib 摘要或其所引用作品。

每项材料的确切作者、固定版本、源 revision、转换说明与实际保存范围，以该项 canonical metadata 的 `rights.redistribution_package` 为准。本包不授权已省略的图像/PDF、外链作品、代码、数据、商标、专利或权利人无权许可的材料。将独立作品放入集合（collection）不改变各自许可；引用、共享与派生输出仍须分别保留相应许可、署名和修改标记。

固定证据与官方权利页面：

- arXiv v4 文章与许可：https://arxiv.org/abs/2507.21046v4
- 固定源响应：https://export.arxiv.org/e-print/2507.21046v4
- TMLR 官方作者指南：https://jmlr.org/tmlr/author-guide.html
- TMLR 官方固定模板树：https://github.com/JmlrOrg/tmlr-style-file/tree/7bf90efe3a0debbba703c05c43f3ff7e4d4a2992
- 模板 Apache 2.0：https://raw.githubusercontent.com/JmlrOrg/tmlr-style-file/7bf90efe3a0debbba703c05c43f3ff7e4d4a2992/LICENSE
- tmlr.sty：https://raw.githubusercontent.com/JmlrOrg/tmlr-style-file/7bf90efe3a0debbba703c05c43f3ff7e4d4a2992/tmlr.sty
- tmlr.bst：https://raw.githubusercontent.com/JmlrOrg/tmlr-style-file/7bf90efe3a0debbba703c05c43f3ff7e4d4a2992/tmlr.bst
- fancyhdr.sty：https://raw.githubusercontent.com/JmlrOrg/tmlr-style-file/7bf90efe3a0debbba703c05c43f3ff7e4d4a2992/fancyhdr.sty
- LPPL 1.3c 官方法律文本：https://www.latex-project.org/lppl/lppl-1-3c/
- LPPL 1.3c 官方纯文本：https://www.latex-project.org/lppl/lppl-1-3c.txt
- AppBench：https://aclanthology.org/2024.emnlp-main.856/
- ARIA：https://aclanthology.org/2025.emnlp-industry.115/
- ACL copyright FAQ：https://aclanthology.org/faq/copyright/
- ACM SIGIR 2024 tool-learning tutorial：https://doi.org/10.1145/3626772.3661381
- ACM 提交的 Crossref 作品许可记录：https://api.crossref.org/works/10.1145/3626772.3661381
- arXiv 00README 处理说明：https://info.arxiv.org/help/00README.html
- arXiv metadata 许可：https://info.arxiv.org/help/policies/submission_agreement.html#metadata-license

官方模板固定树完整且 `truncated=false`，十个文件中没有上游 NOTICE。本地 `NOTICE.md` 是本仓库包装文件名，不虚构上游 NOTICE。以下法律文本完整原样保存：CC BY 4.0 与 Apache 2.0 复用本仓库已核验共享资产的法律块；LPPL 1.3c 来自上述 LaTeX Project 官方纯文本。核对日期为 2026-09-16。

---

## A. Creative Commons Attribution 4.0 International（CC BY 4.0）

- 标准许可标识（SPDX identifier）：`CC-BY-4.0`
- 官方法律文本：https://creativecommons.org/licenses/by/4.0/legalcode.en
- 官方纯文本：https://creativecommons.org/licenses/by/4.0/legalcode.txt

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

## B. Apache License, Version 2.0

- 标准许可标识（SPDX identifier）：`Apache-2.0`
- 官方文本：https://www.apache.org/licenses/LICENSE-2.0

```text
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## C. The LaTeX Project Public License, Version 1.3c

- 标准许可标识（SPDX identifier）：`LPPL-1.3c`
- 官方文本：https://www.latex-project.org/lppl/lppl-1-3c.txt

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
