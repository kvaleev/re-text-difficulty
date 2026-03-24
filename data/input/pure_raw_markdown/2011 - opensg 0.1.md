---
consensus_grade_level: 13.5
headings_per_sentence: 0.0
lists_per_sentence: 0.0
smao_sentences_pct: 0.0
vague_words_per_sentence: 0.09
anaphora_per_sentence: 0.11
sentence_cv: 2.216
cpre_terms_per_sentence: 0.33
---
\

\

\

\

\

\

[**[ ]{.Apple-converted-space}TITLE [  ]{.Apple-converted-space}\\\*
MERGEFORMAT** ]{.s1}**OpenSG EIM System Requirements Specification**

\

***Version:*** *v0.1*

***Release Date:*** *March 7, 2011****[ ]{.Apple-converted-space}***

\

\

\

\

\

\

\

\

\

\

\

\

\

\

\

\

\

**Acknowledgements**

The following individuals and their companies are members of the UCAiug
OpenSG and have contributed and/or provided support to the work of
the[ ]{.Apple-converted-space}[ TITLE [  ]{.Apple-converted-space}\\\*
MERGEFORMAT ]{.s2}OpenSG EIM System Requirements Specification:

Frank Wilhoit from AEP

Melissa Stephenson from Boeing[ ]{.Apple-converted-space}

Mark Ortiz from Consumers Energy

Joseph Thomas -- DTE Energy

Anuja Nakkana -- Florida Power and Light

Andre Cassulo -- Florida Power and Light

Donny Helm -- ONCOR

Larry Kohrmann from ONCOR

Jim Horstman from Southern California Edison

Rich Stephenson from Southern California Edison

Greg Robinson from Xtensible Solutions

James Meyer from Xtensible Solutions

Joe Zhou from Xtensible Solutions

\

\

The OpenSG Task Force wishes to thank all of the above-mentioned
individuals and their companies for their support of this important
endeavor, as it sets a key foundation for interoperable Smart Grid of
the future.[ ]{.Apple-converted-space}

[]{.s3}**Document History**

**Revision History**

Date of this revision: January 25, 2011

\

+-------------+-------------+-------------+-------------+-------------+
| **Revision  | **Revision  | *           | **Summary   | **Changes   |
| Number**    | Date**      | *Revision** | of          | marked**    |
|             |             |             | Changes**   |             |
|             |             | **By**      |             |             |
+-------------+-------------+-------------+-------------+-------------+
| 0.1         | Ja          | James Meyer | SRS initial | N           |
|             | nuary252011 |             | draft       |             |
|             |             |             | created.    |             |
+-------------+-------------+-------------+-------------+-------------+
| \           | \           | \           | \           | \           |
+-------------+-------------+-------------+-------------+-------------+
| \           | \           | \           | \           | \           |
+-------------+-------------+-------------+-------------+-------------+
| \           | \           | \           | \           | \           |
+-------------+-------------+-------------+-------------+-------------+

**Open Issues Log**

Last updated: January 25, 2011

\

+-----------------+-----------------+-----------------+-----------------+
| **Issue         | **Issue Date**  | **Provided**    | **Summary of    |
| Number**        |                 |                 | the Issue**     |
|                 |                 | **By**          |                 |
+-----------------+-----------------+-----------------+-----------------+
| \               | \               | \               | \               |
+-----------------+-----------------+-----------------+-----------------+
| \               | \               | \               | \               |
+-----------------+-----------------+-----------------+-----------------+
| \               | \               | \               | \               |
+-----------------+-----------------+-----------------+-----------------+
| \               | \               | \               | \               |
+-----------------+-----------------+-----------------+-----------------+
| \               | \               | \               | \               |
+-----------------+-----------------+-----------------+-----------------+
| \               | \               | \               | \               |
+-----------------+-----------------+-----------------+-----------------+
| \               | \               | \               | \               |
+-----------------+-----------------+-----------------+-----------------+
| \               | \               | \               | \               |
+-----------------+-----------------+-----------------+-----------------+

\

**Contents**

[ ]{.Apple-converted-space}TOC \\o \"1-3\" \\h \\z \\u HYPERLINK \\l
\"\_Toc283632091\"[1.]{.s4}[[
]{.Apple-tab-span}]{.s5}[Introduction]{.s4}[ ]{.Apple-tab-span} PAGEREF
\_Toc283632091 \\h 5

HYPERLINK \\l \"\_Toc283632092\"[1.1]{.s4}[[
]{.Apple-tab-span}]{.s5}[Purpose]{.s4}[ ]{.Apple-tab-span} PAGEREF
\_Toc283632092 \\h 5

HYPERLINK \\l \"\_Toc283632093\"[1.2]{.s4}[[
]{.Apple-tab-span}]{.s5}[Scope]{.s4}[ ]{.Apple-tab-span} PAGEREF
\_Toc283632093 \\h 5

HYPERLINK \\l \"\_Toc283632094\"[1.3]{.s4}[[
]{.Apple-tab-span}]{.s5}[Acronyms and Abbreviations]{.s4}[
]{.Apple-tab-span} PAGEREF \_Toc283632094 \\h 5

HYPERLINK \\l \"\_Toc283632095\"[1.4]{.s4}[[
]{.Apple-tab-span}]{.s5}[External Considerations and References]{.s4}[
]{.Apple-tab-span} PAGEREF \_Toc283632095 \\h 5

HYPERLINK \\l \"\_Toc283632096\"[1.5]{.s4}[[
]{.Apple-tab-span}]{.s5}[Document Overview]{.s4}[ ]{.Apple-tab-span}
PAGEREF \_Toc283632096 \\h 5

HYPERLINK \\l \"\_Toc283632097\"[2.]{.s4}[[
]{.Apple-tab-span}]{.s5}[Problem Statement]{.s4}[ ]{.Apple-tab-span}
PAGEREF \_Toc283632097 \\h 8

HYPERLINK \\l \"\_Toc283632098\"[3.]{.s4}[[
]{.Apple-tab-span}]{.s5}[Architecture Overview]{.s4}[ ]{.Apple-tab-span}
PAGEREF \_Toc283632098 \\h 9

HYPERLINK \\l \"\_Toc283632099\"[3.1]{.s4}[[
]{.Apple-tab-span}]{.s5}[EIM Framework]{.s4}[ ]{.Apple-tab-span} PAGEREF
\_Toc283632099 \\h 9

HYPERLINK \\l \"\_Toc283632100\"[3.2]{.s4}[[
]{.Apple-tab-span}]{.s5}[EIM Reference Architecture]{.s4}[
]{.Apple-tab-span} PAGEREF \_Toc283632100 \\h 9

HYPERLINK \\l \"\_Toc283632101\"[3.3]{.s4}[[
]{.Apple-tab-span}]{.s5}[EIM Architecture Guiding Principles]{.s4}[
]{.Apple-tab-span} PAGEREF \_Toc283632101 \\h 9

HYPERLINK \\l \"\_Toc283632102\"[4.]{.s4}[[ ]{.Apple-tab-span}]{.s5}[EIM
Systems Architecture]{.s4}[ ]{.Apple-tab-span} PAGEREF \_Toc283632102
\\h 10

HYPERLINK \\l \"\_Toc283632103\"[4.1]{.s4}[[
]{.Apple-tab-span}]{.s5}[EIM Business Architecture View]{.s4}[
]{.Apple-tab-span} PAGEREF \_Toc283632103 \\h 10

HYPERLINK \\l \"\_Toc283632104\"[4.1.1]{.s4}[[
]{.Apple-tab-span}]{.s5}[EIM Use Cases]{.s4}[ ]{.Apple-tab-span} PAGEREF
\_Toc283632104 \\h 10

HYPERLINK \\l \"\_Toc283632105\"[4.1.2]{.s4}[[
]{.Apple-tab-span}]{.s5}[EIM Requirements]{.s4}[ ]{.Apple-tab-span}
PAGEREF \_Toc283632105 \\h 10

HYPERLINK \\l \"\_Toc283632106\"[4.2]{.s4}[[
]{.Apple-tab-span}]{.s5}[EIM Application Architecture View]{.s4}[
]{.Apple-tab-span} PAGEREF \_Toc283632106 \\h 10

HYPERLINK \\l \"\_Toc283632107\"[4.3]{.s4}[[
]{.Apple-tab-span}]{.s5}[EIM Data Architecture View]{.s4}[
]{.Apple-tab-span} PAGEREF \_Toc283632107 \\h 11

HYPERLINK \\l \"\_Toc283632108\"[4.4]{.s4}[[
]{.Apple-tab-span}]{.s5}[EIM Technical Architecture View]{.s4}[
]{.Apple-tab-span} PAGEREF \_Toc283632108 \\h 12

HYPERLINK \\l \"\_Toc283632109\"[5.]{.s4}[[ ]{.Apple-tab-span}]{.s5}[EIM
Competency Center]{.s4}[ ]{.Apple-tab-span} PAGEREF \_Toc283632109 \\h
13

**List of Figures**

[[ ]{.Apple-converted-space}TOC \\h \\z \\t \"Caption\" \\c HYPERLINK
\\l \"\_Toc283630467\"]{.s6}[Figure 1.[  ]{.Apple-converted-space}The
Open Group Architecture Framework (TOGAF) showing the architecture
development cycle.]{.s7}[[ ]{.Apple-tab-span} PAGEREF \_Toc283630467 \\h
6]{.s6}

\

**Introduction**

\

**Purpose**

\

**Scope**

\

\

\

**Acronyms and Abbreviations**

This subsection provides a list of all acronyms and abbreviations
required to properly interpret the Enterprise Information Management
System Requirements Specification.[ ]{.Apple-converted-space}

\

  ----- -----------------------------------
  EIM   Enterprise Information Management
  SRS   System Requirements Specification
  ----- -----------------------------------

**External Considerations and References**

The work of EIM SRS is dependent upon the best practices available from
the following entities and standards
organizations:[ ]{.Apple-converted-space}

\

The Open Group, TOGAF 9.0

\

\

**Document Overview**

TOGAF 9.0 defines four architecture domains that are commonly accepted
as subsets of overall enterprise architecture, all of which TOGAF is
designed to support, see Figure 1:

**Architecture Vision** defines overall architecture guiding principles,
goals and objectives and desired traits.[ ]{.Apple-converted-space}

The **Business Architecture** defines the business strategy, governance,
organization, and key business processes.

The **Data Architecture** describes the structure of an organization\'s
logical and physical data assets and data management resources.[ 
]{.Apple-converted-space}This is part of the **Information Systems
Architecture**.

The **Application Architecture** provides a blueprint for the individual
application systems to be deployed, their interactions, and their
relationships to the core business processes of the organization. This
is part of the **Information Systems Architecture**.

The **Technology Architecture** describes the logical software and
hardware capabilities that are required to support the deployment of
business, data, and application services. This includes IT
infrastructure, middleware, networks, communications, processing,
standards, etc.

\

**Figure[  ]{.Apple-converted-space}SEQ Figure \\\* ARABIC 1.[ 
]{.Apple-converted-space}The Open Group Architecture Framework (TOGAF)
showing the architecture development cycle.**

\

As such, the document will be structured as
follows:[ ]{.Apple-converted-space}

\

**Section[  ]{.Apple-converted-space}REF \_Ref283630218 \\r \\h 2**
describes the problem statement and what issues can be resolved through
the use of an EIM strategy.

\

\

**Section[  ]{.Apple-converted-space}REF \_Ref283629997 \\r \\h 3**
describes the overall Architecture Vision for the system, including
Guiding Principles, Framework, and the EIM Reference Model, all relevant
to providing a consistent framework within which the four architecture
components can be developed.[ ]{.Apple-converted-space}

\

**Section[  ]{.Apple-converted-space}REF \_Ref283630027 \\r \\h 4**
provides the details of the four architecture
components:[ ]{.Apple-converted-space}

**Business Architecture:[ ]{.Apple-converted-space}** This will refer to
work products produced by the Use Case and Service Definition Teams of
EIM, which includes the list of use cases and integration requirements
and business services at the functional level.
[ ]{.Apple-converted-space}

**Application Architecture:** This provides the technical level
requirements relative to how applications are modeled as logical
components, and what services each logical components may provide or
consume. This should be an instantiation of the business services
identified within the Business Architecture.[ ]{.Apple-converted-space}

**Data Architecture:**[  ]{.Apple-converted-space}This provides the
technical level requirements relative to how the EIM data should be
modeled and represented consistently across all integration services to
ensure semantic interoperability.[ ]{.Apple-converted-space}

**Technology Architecture**: This provides the technical level
requirements relative to how services will interact with each other to
support end-to-end EIM business processes.[ ]{.Apple-converted-space}

\

**Section[  ]{.Apple-converted-space}REF \_Ref283630135 \\r \\h 5**
contains the considerations for an EIM Competency Center which includes
topics such as governance and knowledge distribution.

**Problem Statement**

What are the challenges that organizations are seeking to address
through the deployment of an EIM strategy?

**Architecture Overview[ ]{.Apple-converted-space}**

**EIM Framework**

\

**EIM Reference Architecture**

\

**EIM Architecture Guiding Principles**

\

**Role of Information Security in EIM**

Information security plays a central role in the enterprise information
management framework.[  ]{.Apple-converted-space}As such the Task Force
has made a conscious decision not to create a separate section
addressing information security.[  ]{.Apple-converted-space}Instead,
security will be addressed and its impact will be identified in each of
the subsequent sections of this document.[  ]{.Apple-converted-space}In
this manner, the System Requirements Specification shall address
securing the data artifacts and the processes supporting the creation,
retrieval, updating, and deletion of information objects.

\

**EIM Systems Architecture[ ]{.Apple-converted-space}**

**EIM Business Architecture View**

***EIM Use Cases***

\

\

***EIM Requirements***

**Ability to share model with external entities**

Common model sharing requirements

Business to business model sharing requirements

Consumer (B2C) model sharing requirements

**Information management requirements**

Common data management requirements

Smart Grid data management requirements

Non-Smart Grid data management requirements

Joint Smart Grid and Non-Smart Grid data requirements

**Architectural requirements**

Smart Grid architectural requirements

Application architectural requirements

Business unit architectural requirements

Project architectural requirements

\

**EIM Application Architecture View**

Logical breakdown of EIM capabilities such as data validation.

NOTE: Resolve EIM support for process-oriented information perspectives

NOTE: Include self healing and self discovery capabilities

NOTE: Define patterns of using new technologies to create interfaces
with older systems

\

\

**EIM Data Architecture View**

Subject area models, enterprise semantic model, incorporating standards,
data architecture approach, data classification, etc.

Persistent data store architectural requirements

Persistent data store requirements with collocated smart grid and
non-smart grid data

Use of localized data stores

Use of centralized data stores

Standard model incorporation into enterprise information management

Incorporating IEC Common Information Model (CIM) into the EIM

Using EIM to enable IEC Common Information Model-based messaging

Using EIM to enable IEC Common Information Model-based persistent data
store creation

Using IEC Common Information Model to create a semantic model supporting
NIST

Enterprise information management lifecycle management

The information model shall define common definitions of data concepts

The information model shall allow aliases of data concepts

How to initiate and maintain enterprise semantic management

Use a reference architecture to create an enterprise information
architecture

Model how semantic modeling supports information modeling

Define patterns of introducing business units to smart grid semantic
modeling

\

\

\

**EIM Technical Architecture View**

Infrastructure components such as the metadata repository, etc.

***Analytics***

\

\

\

**EIM Competency Center**

Governance, resources, knowledge distribution, etc.

Introducing smart grid EIM lessons to the rest of the organization

Introducing data movement patterns[ ]{.Apple-converted-space}

Introducing data movement tools and methodologies

Introducing new patterns of logical data models

Enhancing the organization's ability to create, maintain, and reuse
logical data models

\

\

\

\

\

\

\

\

\

**[ ]{.Apple-tab-span}OpenSG EIM Task Force[ ]{.Apple-tab-span}**

**[ ]{.Apple-tab-span}** TITLE [  ]{.Apple-converted-space}\\\*
MERGEFORMAT **OpenSG EIM System Requirements Specification**

\

Draft v0.1, Mar. 7, 2011[
]{.Apple-tab-span}Page[ ]{.Apple-converted-space}[ PAGE 1]{.s8}
of[ ]{.Apple-converted-space}[ NUMPAGES 14]{.s8}

[[ ]{.Apple-tab-span}]{.s8}**© Copyright 2011, OpenSG, All Rights
Reserved**

\

\

Added.[  ]{.Apple-converted-space}JM

\

\
