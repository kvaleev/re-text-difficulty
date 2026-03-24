---
consensus_grade_level: 15.8
headings_per_sentence: 0.12
lists_per_sentence: 0.3
smao_sentences_pct: 4.7
vague_words_per_sentence: 0.2
anaphora_per_sentence: 0.49
sentence_cv: 1.158
cpre_terms_per_sentence: 1.33
---
**N.V. Getronics Belgium S.A.**


Rue de Genèvestraat 10


1140 BRUXELLES/BRUSSEL


                                                     - (32) 2 229.91.11

### **DG TREN**

# **TACHOnet**

## **Software Requirements Specification**


**01_00**


**21-Feb-03**


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00


**Document Approval**

|Col1|NAME|DATE|SIGNATURE|
|---|---|---|---|
|<br>Prepared by:|<br>F. Silvestre|<br>21-Feb-03|<br>|
|<br>Checked by:|<br>Ph. Francis|<br>21-Feb-03|<br>|
|<br>Quality control by:|<br>P. Delmée|<br>21-Feb-03|<br>|
|<br>Approved by:|<br>Yves Hardy<br>(DG TREN)|<br>|<br>|



**Distribution List**

|COMPANY|NAME|FUNCTION|FOR INFO / APPROVAL|
|---|---|---|---|
|<br>DG TREN|<br>Y. Hardy|<br>Project Manager|<br>Approval|
|<br>Getronics|<br>P. Delmée|<br>Project Manager|<br>Info|
|<br>Getronics|<br>Ph. Francis|<br>|<br>|
|<br>Getronics|<br>W. Van Acker|<br>|<br>|



**Change Control History**

|VERSION|DATE|AUTHOR|DESCRIPTION|PARAGRAPHS|
|---|---|---|---|---|
|<br>00_01|<br>04-Dec-03|<br>F. Silvestre|<br>Original issue|<br>|
|01_00|21-Feb-03|F. Silvestre|Release iteration C1||
|<br>|<br>|<br>|<br>|<br>|
|<br> <br>|<br>|<br>|<br>|<br>|



**Document information**

|CREATION DATE:|04-Dec-03|
|---|---|
|**FILENAME: **|<br>TCN-SRS-01_00-EN.doc|
|**LOCATION: **||
|**NUMBER OF PAGES: **|<br>76|
|<br>|<br>|



21-Feb-03 - Page 2


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

##### **CONTENTS**


Introduction..........................................................................................................................................4


**Chapter 1: Requirements...........................................................................................................................5**
Overview..............................................................................................................................................5
Types of Requirements.........................................................................................................................6
List of Functional Requirements........................................................................................................10
List of Non-functional Requirements.................................................................................................12


**Chapter 2: Use-Case Model .....................................................................................................................15**
Overview............................................................................................................................................15
Introduction........................................................................................................................................16
Actor Catalog .....................................................................................................................................17
Use Case Catalog ...............................................................................................................................18
Section 2.1 - Use Case Package “TCN Administrative Tasks”.............................................................20
Overview............................................................................................................................................20
Use Case 01 – Check driver(s)’ issued cards .....................................................................................22
Use Case 02 – Check tachograph card status.....................................................................................25
Use Case 03 – Declaration of card status modification......................................................................28
Use Case 04 – Send Card/Driving License Assignment ....................................................................32
Use Case 05 – Get Phonex Search Keys............................................................................................35
Use Case 06 – Get US/Ascii Transliteration......................................................................................37
Section 2.2 - Use Case Package “TCN Statistics Tasks”.......................................................................39
Overview............................................................................................................................................39
Use Case 07 – “Add a new CIA” .......................................................................................................40
Use Case 08 – “Reset Password” .......................................................................................................42
Use Case 09 – “Generate Statistics”...................................................................................................44
Use Case 10 – “Browse Statistics”.....................................................................................................47
Use Case 11 – Log the message.........................................................................................................52
Section 2.3 - Use Case Package “TCN System Tasks” .........................................................................53
Overview............................................................................................................................................53
Use-Case 12 – “Monitor the system”.................................................................................................54
Use-Case 13 – “Manage Member State”............................................................................................55


21-Feb-03 - Page 3


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Introduction**


**Purpose** This document aims at capturing the complete software requirements for the system.
It fully describes the external behaviour of the application(s) or subsystem(s)
identified. It also describes non-functional requirements, design constraints and other
factors necessary to provide a complete and comprehensive description of the
requirements for the software.

The current version of this document is the one released at end of iteration C1.


**References** The present document makes references to the following documents:


         - [1] Specific Agreement n°36 under framework contract n° DI/02450-00 – 13Nov-03

         - [2] TCN XML Messaging Reference Guide V1.40.

         - [3] Card Issuing Working Group – General Report – URBA 2000.


**Abbreviations** - CIA – Card Issuing Authority

         - MS – Member State

         - SPOC – Single Point Of Contact

         - TCN – TACHOnet


**Structure of the** The first chapter describes the functional and non-functional requirements. The
**document** second chapter describes the use-case model comprehensively, in terms of how the
model is structured into packages and what use cases and actors are in the model.


21-Feb-03 - Page 4


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Chapter 1: Requirements** **Overview**


**Introduction** This chapter describes the different requirements (functional and non-functional).


**Contents** This chapter contains the following topics.

|Topic|See Page|
|---|---|
|<br>Types of Requirements|<br>6|
|<br>List of Functional Requirements|<br>10|
|<br>List of Non-functional Requirements|<br>12|



21-Feb-03 - Page 5


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Types of Requirements**


**Definition** A **requirement** is defined as "a condition or capability to which a system must
conform".

**Functional requirements** specify actions that a system must be able to perform,
without taking physical constraints into consideration. These are often best described
in a use-case model and in use cases. Functional requirements thus specify the input
and output behaviour of a system.

Requirements that are not functional are sometimes called **non-functional**
**requirements** . Many requirements are non-functional, and describe only attributes
of the system or attributes of the system environment.


**FURPS+** There are a many different kinds of requirements. One way of categorizing them is
described as the **FURPS+** model [GRA92], using the acronym FURPS to describe
the major categories of requirements with subcategories as shown below.


         - **F** unctionality,

         - **U** sability,

         - **R** eliability,

         - **P** erformance and

         - **S** upportability


The "+" in FURPS+ helps you to also remember to also include such requirements as


         - design constraints,

         - interface requirements and

         - physical requirements.


**Functionality** Functional requirements may include:
**(FUN)**

         - feature sets,

         - capabilities, and

         - security.


_Continued on next page_


21-Feb-03 - Page 6


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### Types of Requirements, Continued


**Usability (USA)** Usability requirements may include such sub-categories as:


         - human factors,

         - aesthetics,

         - consistency in the user interface,

         - online and context-sensitive help,

         - wizards and agents,

         - user documentation, and

         - training materials.


**Reliability** Reliability requirements to be considered are:
**(REL)**

         - Availability (percentage of time available, hours of use, maintenance access,…)

         - frequency / severity of failure,

         - recoverability,

         - predictability,

         - accuracy, and

         - mean time between failure (MTBF).


**Performance** A performance requirement imposes conditions on functional requirements. For
**(PER)** example, for a given action, it may specify performance parameters for:


         - throughput (e.g. transactions per second),

         - response time,

         - recovery time, or

         - resource usage (memory, disk, cpu,…).


_Continued on next page_


21-Feb-03 - Page 7


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### Types of Requirements, Continued


**Supportability** Supportability requirements may include:
**(SUP)**

         - testability,

         - extensibility,

         - adaptability,

         - maintainability,

         - compatibility,

         - configurability,

         - serviceability,

         - installability, or

         - localizability (internationalization).



**Design**
**Requirement**
**(DES)**


**Interface**
**Requirement**
**(INT)**



A design requirement, often called a **design constraint**, specifies or constrains the
design of a system.

This section should indicate any design constraints on the system being built. Design
constraints represent design decisions that have been mandated and must be adhered
to. Examples include software languages, software process requirements, prescribed
use of developmental tools, architectural and design constraints, purchased
components, class libraries, etc.


This section defines the interfaces that must be supported by the application. It
should contain adequate specificity, protocols, ports and logical addresses, etc., so
that the software can be developed and verified against the interface requirements.

An interface requirement may be classified into:


- User interface (user interfaces that are to be implemented by the software)

- Hardware interface (hardware interfaces that are to be supported by the software,
including logical structure, physical addresses, expected behavior, etc.)

- Software interface (software interfaces to other components of the software
system. These may be purchased components, components reused from another
application or components being developed for subsystems outside of the scope
of this project, but with which this software application must interact).


_Continued on next page_


21-Feb-03 - Page 8


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### Types of Requirements, Continued



**Physical**
**Requirement**
**(HAR)**


**Applicable**
**Standards**
**Requirements**
**(STD)**



A physical requirement specifies a physical characteristic that a system must possess;
for example,


- material,

- shape,

- size, and

- weight.


This type of requirement can be used to represent hardware requirements, such as


- the physical network configurations required


This section describes by reference any applicable standards and the specific sections
of any such standards that apply to the system being described. For example, this
could include legal, quality and regulatory standards, industry standards for usability,
interoperability, internationalization, operating system compliance, etc.


21-Feb-03 - Page 9


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **List of Functional Requirements**


**Introduction** Functional requirements specify actions that a system must be able to perform,
without taking physical constraints into consideration. Functional requirements thus
specify the input and output behaviour of a system.

A list of these functional requirements is given below with an identification and a
short description for each of them.

These functional requirements are best described once translated into use cases (see
Use Case Model chapter).



**List of**
**functional**
**requirements**



Each identified functional requirement is assigned a unique key “ **FUN-** _**nn**_ ” where _**nn**_
is a sequence number identifying the functional requirement. The table hereafter lists
all the functional requirements :








|Functional<br>Requirement<br>Id|Description|
|---|---|
|<br>FUN-01|The system must allow a member of the network to send requests<br>to a particular or all the other members about possible delivery of<br>a driver’s smart card to a similar person.|
|FUN-02|<br>The system must allow a member of the network to send a bulk<br>request on all or a large part of its driver’s smart card holders to a<br>particular or all members of the network.|
|FUN-03|<br>The system must allow a member to do statistics on messages<br>issued and received from/to his system.|
|FUN-04|<br>The system must provide automatic reply to the sender of the<br>request through the use of a standard interface to the Members<br>systems.|
|FUN-05|<br>The system must track the workflow between senders and related<br>replies.|
|FUN-06|<br>The system must be able, in accordance with the rules on delays<br>for each transaction, to automatically transmit alert messages to<br>senders/replier/administrator when, f.i. a constraint on delay for<br>reply is not fulfilled.|
|FUN-07|The system must allow the administrator to extract statistics of<br>use, standard delay of reply by member/period, percentage of<br>unsuccessful transaction,... .|
|FUN-08|<br>The system must provide the management of user rights and<br>permissions.|
|FUN-09|<br>The system must be able to define and manage various type of<br>messages already in the driver’s smart card holder like pre-<br>delivery check, stolen/lost cards, renewals, exchanges and<br>duplicates.|
|FUN-10|The system must be able to include new members in the network<br>through simple administrative tasks.|



_Continued on next page_


21-Feb-03 - Page 10


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### List of Functional Requirements, Continued



**List of functional requirements** (continued)






|Functional<br>Requirement<br>Id|Description|
|---|---|
|<br>FUN-11|The system must be highly automatic to relieve the users of as<br>many repetitive and tedious tasks as possible.|
|FUN-12|The system must provide at application level a full security<br>(~~including non repudiation)~~ and encryption policy compatible<br>with the level of security required in such situation.|
|FUN-13|<br>~~The system must guarantee that none of the Member of the~~<br>~~network, including the administrator, is technically able to re-~~<br>~~construct a consolidated European database through the use of~~<br>~~the messages exchanged.~~ <br>The system must be such that none of the Member States of the<br>network, including the administrator, re-construct a consolidated<br>European database.|
|FUN-14|<br>The system must allow a Member State (through its Card Issuing<br>Authority) to ask for the status of card (lost, stolen,…) to the<br>corresponding Card Issuing Authority of the Member State<br>having issued the card.|
|FUN-15|The system must allow a Member State (through its Card Issuing<br>Authority) to send card status modification requests (lost,<br>stolen,…) to the corresponding Card Issuing Authority of the<br>Member State having issued the card.|
|FUN-16|<br>The system must allow enforcement authorities (through its Card<br>Issuing Authority) to ask for driver’s card status (based on either<br>card number + issuing Member State code or driver’s surname,<br>first names, date of birth and issuing Member State code) to the<br>corresponding Card Issuing Authority of the Member State<br>having issued the card.|
|FUN-17|The system must allow enforcement authorities (through its Card<br>Issuing Authority) to ask for workshop card status (based on<br>workshop card number + issuing Member State code) to the<br>corresponding Card Issuing Authority of the Member State<br>having issued the card.|



21-Feb-03 - Page 11


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **List of Non-functional Requirements**


**Introduction** Non-functional requirements describe only attributes of the system or attributes of
the system environment.

Each identified non-functional requirement is assigned a unique key “ **XXX-** _**nn**_ ”
where _**XXX**_ identifies the type of requirement (e.g. PER for performance
requirement) and _**nn**_ is a sequence number identifying the non-functional
requirement.


**Usability** The table hereafter lists all the non-functional “usability” requirements :
**requirements**








|Usability<br>Requirement<br>Id|Description|
|---|---|
|<br>USA-01|The system must guide users through an interface based on end<br>user concepts.|
|USA-02|The system must be easy to learn and does not obstruct the<br>thematic understanding of the users.|
|USA-03|The system must make it easy to correct mistakes.|



**Reliability** The table hereafter lists all the non-functional “reliability” requirements:
**requirements**








|Reliability<br>Requirement<br>Id|Description|
|---|---|
|<br>REL-01|The system is to be designed as a robust and dependable<br>operational system which is tolerant to operator errors and<br>which will recover cleanly from power cuts or other disasters.|
|REL-02|The system must function reliably, with few or no interruptions<br>in its first operational year and fewer still thereafter.|
|REL-03|The system must give stable and reproducible results.|



_Continued on next page_


21-Feb-03 - Page 12


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### List of Non-functional Requirements, Continued


**Performance** The table hereafter lists all the non-functional “performance” requirements:
**requirements**








|Performance<br>Requirement<br>Id|Description|
|---|---|
|<br>PER-01|~~The system should be able to cover more than one contact point~~<br>~~per country depending on the administrative organisation~~<br>~~adopted by each country and able to work in a multi~~<br>~~hierarchical environment.~~ This is no longer the case since<br>everybody agrees upon having a single point of contact per<br>Member State (even though the Member State is organized with<br>several Card Issuing Authorities – up to the Member State to<br>manage its own organisation).|
|PER-02|<br>There will be no restriction in time or place for the use of the<br>software built from the specifications produced under this<br>contract.|
|PER-03|The system must be able to establish and keep the dialog with<br>the Members systems despite the various technical<br>environments and technologies used on their sites.|
|PER-04|<br>The system will be designed so that background tasks can<br>continue while the user performs foreground tasks.|
|PER-05|The system will be used 24x7 by operators under pressure to<br>produce results rapidly. The system must respond rapidly to<br>user requests irrespective of any background tasks. Such high-<br>availability (24x7) is also required from the Member States<br>systems to ensure acceptable response time (less than 1 minute)<br>to enforcement authorities requests.|



**Supportability** The table hereafter lists all the non-functional “supportability” requirements:
**requirements**








|Supportability<br>Requirement<br>Id|Description|
|---|---|
|<br>SUP-01|The system should be able to support other types of message<br>structure to cover f.i. a future driving licence network and<br>correlated activities.|
|SUP-02|The system must be maintainable and extensible.|
|SUP-03|The system must be designed so that it can migrate to upgraded<br>hardware or new versions of the operating systems involved.|
|SUP-04|<br>The system must be able to migrate to other type of network<br>than the one proposed by TESTA-II.|
|SUP-05|<br>The system must provide solutions/rules regarding data<br>encoding problems such as supporting different character sets,<br>name truncation rules, name matching in case of misspelling,...|



_Continued on next page_


21-Feb-03 - Page 13


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### List of Non-functional Requirements, Continued


**Design** The table hereafter lists all the non-functional “design” requirements:
**requirements**








|Design<br>Requirement<br>Id|Description|
|---|---|
|<br>DES-01|The system must be designed and documented with the<br>expectation that its operational lifetime will be many years.|
|DES-02|<br>Each Member of this network will organise its data about smart<br>card holders with no constraints or recommendations on<br>operating system and/or technology used. The system will be<br>able to dialog with these environments or specify a generic<br>interface to dialog with the Member’s applications.|



**Implementation** The table hereafter lists all the non-functional “implementation” requirements:
**requirements**






|Implementation<br>Requirement<br>Id|Description|
|---|---|
|<br>IMP-01|-|



**Interface** The table hereafter lists all the non-functional “interface” requirements:
**requirements**








|Interface<br>Requirement<br>Id|Description|
|---|---|
|<br>INT-01|The system must use the network facilities supplied by the<br>TESTA-II network.|
|INT-02|<br>The algorithms in the software will be based on existing<br>techniques and no research will be required to develop new<br>algorithms under this contract.|
|INT-03|<br>Most of the functionality of the new software shall depend on<br>pre-existing or commercially available software.|



**Physical** The table hereafter lists all the non-functional “physical” requirements:
**requirements**






|Physical<br>Requirement<br>Id|Description|
|---|---|
|<br>HAR-01|-|



21-Feb-03 - Page 14


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Chapter 2: Use-Case Model** **Overview**


**Introduction** This chapter describes the use-case model comprehensively, in terms of how the
model is structured into packages and what use cases and actors are in the model.


**Contents** This chapter contains the following topics:

|Topic|See Page|
|---|---|
|<br>Introduction|<br>16|
|<br>Actor Catalog|<br>17|
|<br>Use Case Catalog|<br>18|
|<br>Use Case Package “TCN Administrative Tasks”|<br>20|
|<br>Use Case Package “TCN Statistics Tasks”|<br>39|
|<br>Use Case Package “TCN System Tasks”|<br>53|



21-Feb-03 - Page 15


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Introduction**


**What’s a Use-** A use-case model is a model of the system's intended functions and its surroundings.
**Case Model ?** It serves as a contract between the customer, the users and the system developers on
the functionality of the system, which allows :


         - Customers and users to validate that the system will become what they
expected.

         - System developers to build what is expected.


The same use-case model is used in system analysis, design, implementation, and
testing.

The use-case model consists of **use cases** and **actors** .


**What’s an** An **actor** defines a coherent set of roles that users of the system can play when
**Actor ?** interacting with it. A user can either be an individual or an external system.


**What’s a Use** A **use case** defines a set of use-case instances, where each instance is a sequence of
**Case ?** actions a system performs that yields an observable result of value to a particular
actor. Each use case in the model is described in detail, showing step-by-step how
the system interacts with the actors, and what the system does in the use case. Use
cases function as a unifying thread throughout the software lifecycle.


21-Feb-03 - Page 16


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Actor Catalog**


**Introduction** This map describes the list of identified actors.


**List of actors** The following figure describes the different actors:



CIA Appl ication


CIA User


CIA Admini strator


TCN Administrator



TACHOnet considers a whole CIA (Card Issuing Authority) as a single user (the CIA administrator
excepted) through the CIA application, in charge of exchanging XML messages with TACHOnet.
TACHOnet does not manage CIA users working with the CIA application (e.g. the clerks or
enforcers performing administrative tasks). These latter ones have to be managed accordingly by
each Member State's CIA under their own responsibility.
From the TACHOnet viewpoint, the CIA application acts as a single user and will be defined
accordingly (a single digital certificate will be delivered for a CIA application). Therefore,
enforcers are also considered as CIA users who should then be managed by each Member State
(TACHOnet only have a SPOC CIA).
A CIA Application will be granted the rights for carrying out any of the administrative tasks (see
Administrative tasks for more details).


Even though TACHOnet doesn't m anage any CIA user (see above), a CIA user (i.e. clerks or
enforcers) may have access to a web appl ication providi ng a user i nterface on top of the
TACHOnet web servcices (phonex and transliterati on).


A CIA Administrator is a single user who is in charge of administering the CIA application
(exchanging XML messages with TACHOnet) in a Member State.
From the TACHOnet viewpoint, the CIA Administrator will be assigned an account and will be
granted the rights to browse the TCN usage statistics reports through a secure web site.


The TCN (TACHOnet) Administrator is in charge of administering the whole TACHOnet
services in terms of configuration, performance, logging, tracking,... .
The TCN Administrator is not related to any CIA and works for the EC or Trusted Third Party
company hosting and managing the TACHOnet services.


**Figure 1 – List of Actors**


21-Feb-03 - Page 17


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Use Case Catalog**


**Introduction** This map describes the list of identified use cases. For clarity reasons, use cases are
organized as packages. The description of each of the use cases packages is given in
the next sections.


**Use Case Model** The following figure outlines the actors and use cases of the TACHOnet system:
**Diagram**


TACHOnet Administrative Tasks



TACHOnet Statistics Tasks



Send Card/Driving License
Assignment





CIA Administrator


(from Actors)



Generate Statistics


Log the message





Manage Member State


_Continued on next page_


21-Feb-03 - Page 18



**Figure 2 – Use Case Model Diagram**


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### Use Case Catalog, Continued


**List of Use Case** For organizational purposes, use cases are gathered in packages. The list of the TCN
**Packages** Use Case Packages is outlined in the following diagram:








|Col1|Col2|
|---|---|
|TCN Administrative<br>Tasks|TCN Administrative<br>Tasks|


|Col1|Col2|
|---|---|
|TCN Statistics<br>Tasks|TCN Statistics<br>Tasks|


|Col1|Col2|
|---|---|
|TCN System<br>Tasks|TCN System<br>Tasks|



**Figure 3 – List of Use Case Packages**


**List of Use** The table hereafter lists all the use cases along with their assigned id:
**Cases**

|The UC Package…|Contains the following Use Cases…|
|---|---|
|<br>TCN Administrative<br>Tasks|<br> <br>Check Driver’s Issued Cards<br> <br>Check Tachograph Card Status<br> <br>Declaration of Card Status Modification<br> <br>Send card/Driving License Assignment<br> <br>Get Phonex Search Keys<br> <br>Get US/Ascii Transliteration<br>|
|TCN Statistics Tasks|<br> <br>Add a new CIA<br> <br>Reset Password<br> <br>Browse Statistics<br> <br>Generate Statistics<br> <br>Log the message<br>|
|TCN System Tasks|<br> <br> <br>Monitor the system<br> <br>Manage Member State|



21-Feb-03 - Page 19


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Section 2.1 - Use Case Package “TCN Administrative Tasks”** **Overview**


**Introduction** This section describes the use cases related to the “TCN Administrative Tasks”
package. The following diagram gives a high-level view of the use cases of this
package:



Get Phonex Search Keys



Get US/Ascii Transliteration





Send Card/Driving License
Assignment



**Figure 4 –Use Case Package “TCN Administrative Tasks”**


_Continued on next page_


21-Feb-03 - Page 20


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### Overview, Continued


**Contents** This section contains the following topics:

|Topic|See Page|
|---|---|
|<br>Use Case 01 – Check driver(s)’ issued cards|<br>22|
|<br>Use Case 02 – Check tachograph card status|<br>25|
|Use Case 03 – Declaration of card status modification|28|
|<br>Use Case 04 – Send Card/Driving License Assignment|<br>32|
|<br>Use Case 05 – Get Phonex Search Keys|<br>35|
|Use Case 06 – Get US/Ascii Transliteration|37|



21-Feb-03 - Page 21


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Use Case 01 – Check driver(s)’ issued cards**


**Description** This use case consists of processing a request for checking driver’s issued card
coming from a Card Issuing Authority ( _CIA_ ). Such request could contain the data for
a single driver ( _online_ mode) or several drivers ( _batch_ mode).

This use case is also used by enforcers (on behalf of CIA – as TACHOnet only sees
CIA as SPOC) during road checks.


**Basic flow** The basic flow consists of the following steps:

|Step|Action|
|---|---|
|<br>1|<br>TACHOnet deciphers the received request and logs the received request<br>as-is in its tracking database.|
|2|<br>TACHOnet validates its syntax and assigns it a TACHOnet refid<br>(TCNRefId).|
|3|<br>TACHOnet will build as many new requests as issuing Member State<br>codes identified in the original request (+ another one for all sub-<br>requests not mentioning any issuing Member State code) by applying<br>defined name encoding rules to the given surname(s) and first name(s) in<br>order to compute the search keys.|
|4|<br>For each issuing Member State identified (if any) in the original request,<br>TACHOnet builds, logs and encrypts a new request (only containing<br>sub-requests for the corresponding issuing Member State), sends it to the<br>corresponding Member State’s CIA application and waits for receiving<br>the response.<br>For the sub-request mentioning any issuing Member State code (if any),<br>TACHOnet builds, logs and encrypts a new request (only containing<br>sub-requests not mentioning any issuing Member State), broadcasts it to<br>all the Member States configured in TACHOnet (except the Member<br>State having sent the original request) and waits for receiving each<br>response.|
|5|<br>For each received response, TACHOnet deciphers it, logs it as-is in its<br>tracking database and validates its syntax. If it is valid, TACHOnet<br>stores the response data (linked to the TCN refid) in the database (for<br>later building the single consolidated response that TACHOnet will send<br>when all responses are received or when the timeout is reached).|
|6|<br>When all responses are received or when the timeout is reached,<br>TACHOnet builds, from the received responses stored in its database,<br>the single consolidated response.|
|7|TACHOnet logs the consolidated response is in its tracking database,<br>encrypts it and sends it to the original caller.|



_Continued on next page_


21-Feb-03 - Page 22


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### Use Case 01 – Check driver(s)’ issued cards, Continued


**Alternate flows** Several alternate flows may exist depending on the result of some events/actions of
the basic flow:

|Alternate<br>flow|Description|
|---|---|
|<br>ALT-01|When TACHOnet receives a negative response from a Member State<br>CIA, it should log it and consider the request sent to that Member<br>State CIA as completed (with error).|
|ALT-02|<br>When TACHOnet receives multiple responses (corresponding to a<br>single request) from a Member State CIA, it should ignore the<br>superfluous additional responses. The first received response is the<br>processed one.|
|ALT-03|When TACHOnet doesn’t receive within time a Member State CIA<br>response, it should mention ‘timeout’ as status code for that Member<br>State CIA in the consolidated response.|
|ALT-04|<br>When TACHOnet receives a late Member State CIA response, it<br>should log it and ignore it.|
|ALT-05|<br>When TACHOnet receives a syntactically invalid request / response,<br>it should always send back a negative receipt with ‘Invalid Format<br>request’ as status code and warn the TCN Administrator.|
|ALT-06|When TACHOnet receives an invalid XML message (request,<br>response), it will respond with a negative receipt mentioning the<br>reason (invalid format).|



**Special** ~~•~~ ~~Non-repudiation of transaction must be guaranteed~~
**requirements** - Data privacy must also be guaranteed

         - All Member State _CIA_ s must provide services (using proposed messages formats
below and proposed technical rules in [2]) for:

          - Sending a request for checking driver’s issued cards to TACHOnet

          - Receiving and handling a TACHOnet request for checking driver’s issued cards

          - Sending TACHOnet a response to such TACHOnet request (asynchronous)

          - Receiving and handling a TACHOnet response to original request for checking
driver’s issued cards (asynchronous)


**Pre-conditions** - The _CIA_ requesting the check must be defined in TACHOnet

         - The _CIA_ requesting the check must send its request using the TACHOnet required
request format (see below)


**Post-conditions** - The _CIA_ requesting the check has received a response to its request.


_Continued on next page_


21-Feb-03 - Page 23


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### Use Case 01 – Check driver(s)’ issued cards, Continued


**Actors** - A _CIA application_ (named _CIA_ ) requesting the check (CIA’s clerk or enforcer)

         - All _CIA applications_ (named _CIAs_ ) to which TACHOnet will broadcast the request

         - The TACHOnet system


**Messages flow** The following diagram outlines the flow of messages exchanged between actors:
**diagram**

**Card Issuing** **Member State 1**
**TACHOnet**
**Authority (CIA)** **(CIA)**
**Member State 2**

|XML|XML|(CIA)|
|---|---|---|
|MS2TCN_x_REQ|MS2TCN_x_REQ|MS2TCN_x_REQ|
|XML|XML|XML|
|XML|TCN2MS_x_REQ|TCN2MS_x_REQ|
|XML|XML<br>MS2TCN_x_RES|XML<br>MS2TCN_x_RES|
|TCN2MS_x_RES|TCN2MS_x_RES|TCN2MS_x_RES|



**Figure 5 – UC-01 messages flow**

|XML|Col2|
|---|---|
|||


|XML|Col2|
|---|---|
|||



**XML Messages** Please refer to [2] for a complete description.


**Additional** - In case of problems (e.g. network problem,...) when sending a message (request,
**remarks** response), TACHOnet will automatically retry to send it 3 times at regular interval
till request timeout. Afterwards, if still unsuccessful, it will record a ‘Server Error’
status code.


21-Feb-03 - Page 24


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Use Case 02 – Check tachograph card status**


**Description** This use case consists of checking the status of a tachograph card based on its card
number. This use case is very useful for _CIAs_ in order to check the validity of a card
prior to performing some administrative tasks (e.g. to avoid from declaring a
lost/stolen card for a wrongly keyed-in card number,...). It is also useful for
enforcement authorities during road-checks where workshop could also be checked
(beside driver cards).

The checked card is identified by its card number and its issuing Member State code.
As an issued card must be unique, it should only exist in a single _CIA_ data store (the
_CIA_ having issued the card).


**Basic flow** The basic flow consists of the following steps:

|Step|Action|
|---|---|
|<br>1|<br>TACHOnet deciphers the received request and logs the received request<br>as-is in its tracking database.|
|2|TACHOnet validates its syntax and assigns it a TACHOnet refid<br>(TCNRefId).|
|3|TACHOnet will build as many new requests as issuing Member State<br>codes identified in the original request. TACHOnet figures out the target<br>issuing Member State(s) from the issuing Member State code given for<br>each to-be-checked card. Every new request only contains card<br>number(s) issued by a particular Member State.|
|4|For each identified issuing Member State(s), TACHOnet builds, logs and<br>encrypts the new request, sends it to it and waits for receiving the<br>response.|
|5|<br>For each received response, TACHOnet deciphers it, logs it as-is in its<br>tracking database and validates its syntax. If it’s valid, TACHOnet stores<br>the response message (linked to the TCNRefId) in the database (for later<br>building the single consolidated response that TACHOnet will send<br>when all responses are received or when the timeout is reached).|
|6|When all responses are received or when the timeout is reached,<br>TACHOnet builds, logs and encrypts the consolidated response (from<br>the responses received so far), and sends it to the original caller.|



**Alternate flows** The same alternate flows as described for UC-01 (page 23) may exist depending on
the result of some events/actions of the basic flow.


_Continued on next page_


21-Feb-03 - Page 25


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### Use Case 02 – Check tachograph card status, Continued


**Special** ~~•~~ ~~Non-repudiation of transaction must be guaranteed~~
**requirements** - Data privacy must also be guaranteed

         - All Member State _CIA_ s must provide services (using proposed messages formats
below and proposed technical rules in [2]) for:

          - Sending a request for checking a card number to TACHOnet

          - Receiving and handling a TACHOnet request for checking a card number

          - Sending TACHOnet a response to such TACHOnet request (asynchronous)

          - Receiving and handling a TACHOnet response to original request for checking a
card number (asynchronous)


**Pre-conditions** - The _CIA_ sending the request must be defined in TACHOnet

         - The _CIA_ sending the request must send it using the TACHOnet required request
format (see below)


**Post-conditions** - The _CIA_ sending the request has received a response to its request.


**Actors** - A _CIA_ requesting the check (CIA’s clerk or enforcer)

         - All _CIAs_ to which TACHOnet will broadcast the request

         - The TACHOnet system


**XML Messages** Please refer to [2] for a complete description.


_Continued on next page_


21-Feb-03 - Page 26


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### Use Case 02 – Check tachograph card status, Continued


**Messages flow** The following diagram outlines the flow of messages exchanged between actors
**diagram** (assuming a single card number is specified in the original request, meaning
TACHOnet has to forward the request to the Member State having issued the card):

|ssuing rity (CIA) TACH|HOnet Issuin State|
|---|---|
|XML|XML|
|MS2TCN_x_REQ|MS2TCN_x_REQ|
|XML|XML|
|XML|TCN2MS_x_REQ|
|XML|XML<br>MS2TCN_x_RES|
|TCN2MS_x_RES|TCN2MS_x_RES|


|XML|Col2|
|---|---|
|||


|XML|Col2|
|---|---|
|||



**Figure 6 – UC-03 messages flow**


**Additional** - In case of problems (e.g. network problem,...) when sending a message (request,
**remarks** response), TACHOnet will automatically retry to send it 3 times at regular interval
till request timeout. Afterwards, if still unsuccessful, it will record a ‘Server Error’
status code.


21-Feb-03 - Page 27


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Use Case 03 – Declaration of card status modification**


**Description** This use case consists of processing a request for declaring the modification of the
status of card. It can be asked by CIA clerks or by enforcers.

The following table describes which new card status codes are allowed when
declaring a card status modification:

|Card Status|MS2TCN_ModCardStatus_Req|Reason|
|---|---|---|
|<br>Application|N|<br>|
|<br>Approved|<br>N|<br>|
|<br>Personalised|<br>N|<br>|
|<br>Dispatched|<br>N|<br>|
|<br>**HandedOver**|<br>**Y **|<br>**valid again (after wrong declaration)**|
|<br>**Confiscated**|<br>**Y **|<br>**Confiscation card declaration**|
|<br>**Suspended**|<br>**Y **|<br>**Suspended card declaration**|
|<br>Withdrawn|<br>N|<br> <br>|
|<br>Surrendered|<br>N|<br>~~Card returned to CIA and no longer~~<br>needed|
|<br>**Lost**|<br>**Y **|<br>**Lost card declaration**|
|<br>**Stolen**|<br>**Y **|<br>**Stolen card declaration**|
|<br>**Malfunctioning**|<br>**Y **|<br>**Defective card declaration**|
|Expired|<br>N|<br>|
|<br>Replaced|<br>N|<br>|
|<br>Renewed|<br>N|<br>|
|<br>**InExchange**|<br>**Y **|<br>**Exchange of a card (start)**|
|<br>**Exchanged**|<br>**Y **|<br>**exchange of a card (end)**|



The card status values in red ('Y' in 2nd column) will be defined as the only values allowed as
new card status values in the TCN "ModCardStatus" transaction (XML message). TCN will not
check the validity of the state transition declared in this transaction (e.g. it will not prevent
declaring a card 'Exchanged' while its current status was 'Stolen' as TCN doesn't know the
current card status). It's up the MS responsibility to check the validity of such state transition
(and return a ModStatusCode=CardStatusInvalid in the XML response message).


**Table 1 – New card status**


**Basic flow** The basic flow consists of the following steps:

|Step|Action|
|---|---|
|<br>1|<br>TACHOnet deciphers the received request and logs the received request<br>as-is in its tracking database.|
|2|<br>TACHOnet validates its syntax and assigns it a TACHOnet refid<br>(TCNRefId).|



_Continued on next page_


21-Feb-03 - Page 28


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Use Case 03 – Declaration of card status modification,**

Continued


**Basic flow** (continued)

|Step|Action|
|---|---|
|<br>3|<br>TACHOnet will build as many new requests as issuing Member State<br>codes identified in the original request. TACHOnet figures out the target<br>issuing Member States based on the CIA country code given in the<br>original request. Every new request only contains card number(s) issued<br>by a particular Member State.|
|4|<br>For each identified issuing Member State(s), TACHOnet builds, logs and<br>encrypts the new request, sends it to the Member State and waits for<br>receiving the response.|
|5|For each received response, TACHOnet deciphers it, logs it as-is in its<br>tracking database and validates its syntax. If it’s valid, TACHOnet stores<br>the response message (linked to the TCNRefId) in the database (for later<br>building the single consolidated response that TACHOnet will send when<br>all responses are received or when the timeout is reached).|
|6|When all responses are received or when the timeout is reached,<br>TACHOnet builds, logs and encrypts the consolidated response (from the<br>responses received so far), and sends it to the original caller.|



**Alternate flows** The same alternate flows as described for UC-01 (page 23) may exist depending on
the result of some events/actions of the basic flow.


**Special** ~~•~~ ~~Non-repudiation of transaction must be guaranteed~~
**requirements** - Data privacy must also be guaranteed

         - All Member State _CIA_ s must provide services (using proposed messages formats
below and proposed technical rules in [2]) for:

          - Sending a request for declaring card status modification to TACHOnet

          - Receiving and handling a TACHOnet request for declaring card status
modification

          - Sending TACHOnet a response to such TACHOnet request (asynchronous)

          - Receiving and handling a TACHOnet response to original request for declaring
card status modification (asynchronous)


**Pre-conditions** - The _CIA_ sending the declaration must be defined in TACHOnet

         - The _CIA_ sending the declaration must send its request using the TACHOnet
required request format (see below)

         - The _CIA_ sending the declaration must have first sent a request for checking the
card number for which status modification is required.


_Continued on next page_


21-Feb-03 - Page 29


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Use Case 03 – Declaration of card status modification,**

Continued


**Post-conditions** - The _CIA_ sending the declaration has received a response to its request.

         - The _CIA_ having issued the card has received the request and processed it.


**Actors** - A _CIA_ declaring the card status modification (CIA’s clerk or enforcer)

         - The _CIA_ having issued the card

         - The TACHOnet system


**Messages flow** The following diagram outlines the flow of messages exchanged between actors
**diagram** (assuming a single card number is specified in the original request, meaning
TACHOnet has to forward the request to the Member State having issued the card):

|ssuing rity (CIA) TACH|HOnet Issuin State|
|---|---|
|XML|XML|
|MS2TCN_x_REQ|MS2TCN_x_REQ|
|XML|XML|
|XML|TCN2MS_x_REQ|
|XML|XML<br>MS2TCN_x_RES|
|TCN2MS_x_RES|TCN2MS_x_RES|


|XML|Col2|
|---|---|
|||


|XML|Col2|
|---|---|
|||



**Figure 7 – UC-03 messages flow**


_Continued on next page_


21-Feb-03 - Page 30


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Use Case 03 – Declaration of card status modification,**

Continued


**XML Messages** Please refer to [2] for a complete description.


**Additional** - In case of problems (e.g. network problem,...) when sending a message (request,
**remarks** response), TACHOnet will automatically retry to send it 3 times at regular interval
till request timeout.


21-Feb-03 - Page 31


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Use Case 04 – Send Card/Driving License Assignment**


**Description** This use case is born from the “Luxemburg agreement” (see [3] for more details). It
should be used by CIAs in the particular case when a card has been issued to a driver
who showed a foreign driving license. The CIA must then warn, via TACHOnet, the
Member State having issued the driving license that a brand new card has been
issued with the corresponding driving license number. Upon receipt of such request,
the Member State having issued the driving license should store that information
(issued card number associated to the driving license number) in its own local data
store.


**Basic flow** The basic flow consists of the following steps:

|Step|Action|
|---|---|
|<br>1|<br>TACHOnet deciphers the received request and logs the received request<br>as-is in its tracking database.|
|2|<br>TACHOnet validates its syntax and assigns it a TACHOnet refid<br>(TCNRefId).|
|3|<br>TACHOnet will build as many new requests as issuing Member State<br>codes identified in the original request (e.g. if more than one card/driving<br>license number is given in the request). TACHOnet figures out the issuing<br>Member State code(s) based on the driving license issuing nation (and not<br>the card issuing Member State code) given for each sub request. Every<br>new request only contains card and driving license number(s) issued by a<br>particular Member State.|
|4|<br>For each identified issuing Member State(s), TACHOnet builds, logs and<br>encrypts the new request, sends it to the Member State and waits for<br>receiving the response.|
|5|<br>For each received response, TACHOnet deciphers it, logs it as-is in its<br>tracking database and validates its syntax. If it’s valid, TACHOnet stores<br>the response message (linked to the TCNRefId) in the database (for later<br>building the single consolidated response that TACHOnet will send when<br>all responses are received or when the timeout is reached).|
|6|<br>When all responses are received or when the timeout is reached,<br>TACHOnet builds, logs and encrypts the consolidated response (from the<br>responses received so far), and sends it to the original caller.|



**Alternate flows** The same alternate flows as described for UC-01 (page 23) may exist depending on
the result of some events/actions of the basic flow.


_Continued on next page_


21-Feb-03 - Page 32


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Use Case 04 – Send Card/Driving License Assignment,**

Continued


**Special** ~~•~~ ~~Non-repudiation of transaction must be guaranteed~~
**requirements** - Data privacy must also be guaranteed

         - All Member State _CIA_ s must provide services (using proposed messages formats
below and proposed technical rules in [2]) for:

          - Sending a request for checking a card number to TACHOnet

          - Receiving and handling a TACHOnet request for checking a card number

          - Sending TACHOnet a response to such TACHOnet request (asynchronous)

          - Receiving and handling a TACHOnet response to original request
(asynchronous)


**Pre-conditions** - The _CIA_ sending the request must be defined in TACHOnet

         - The _CIA_ sending the request must send it using the TACHOnet required request
format (see below)


**Post-conditions** - The _CIA_ sending the request has received a receipt and a response to its request.


**Actors** - A _CIA_ requesting the update

         - All _CIAs_ to which TACHOnet will broadcast the request

         - The TACHOnet system


**XML Messages** Please refer to [2] for a complete description.


_Continued on next page_


21-Feb-03 - Page 33


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Use Case 04 – Send Card/Driving License Assignment,**

Continued


**Messages flow** The following diagram outlines the flow of messages exchanged between actors
**diagram** (assuming a single card number is specified in the original request, meaning
TACHOnet has to forward the request to the Member State having issued the card):



**Card Issuing**
**TACHOnet**
**Authority (CIA)**



**Member State**
**having issued**
**the driving**


|XML|Col2|
|---|---|
|||



|XML|XML|Col3|
|---|---|---|
|MS2TCN_x_REQ|MS2TCN_x_REQ|MS2TCN_x_REQ|
|XML|XML|XML|
|XML|TCN2MS_x_REQ|TCN2MS_x_REQ|
|XML|XML<br>MS2TCN_x_RES|XML<br>MS2TCN_x_RES|
|TCN2MS_x_RES|TCN2MS_x_RES|TCN2MS_x_RES|


|XML|Col2|
|---|---|
|||


**Figure 8 – UC-04 messages flow**


**Additional** - In case of problems (e.g. network problem,...) when sending a message (request,
**remarks** response), TACHOnet will automatically retry to send 3 times it at regular interval
till request timeout.


21-Feb-03 - Page 34


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Use Case 05 – Get Phonex Search Keys**


**Description** This use case consists of getting from TACHOnet the computed search keys (based
on the Phonex algorithm) corresponding to the given last name and first names.

The Member State CIAs should call upon this service when issuing a new card to get
the computed search keys of the driver’s surname and first names, so to store them in
their local data store. When a Member State CIA will receive a TACHOnet request
for checking driver’s issued card, it should use the search keys given in the request to
search against their local data store (along with the given driver’s birth date). It’s
therefore of major importance to use a common algorithm and to store computed
search keys in the local data store.

Nevertheless, Member States are free to use their own Phonetic algorithm (if existing
like in Germany). In such a case, it’s the Member State responsibility to compute the
search keys based on the given driver’s surname and first of the first names.


**Basic flow** The basic flow consists of the following steps:

|Step|Action|
|---|---|
|<br>1|<br>The CIA calls the TACHOnet service giving the driver’s surname and<br>first names.|
|2|<br>TACHOnet checks the input parameters and, if valid, computes the<br>corresponding surname and first of the first names search keys.|
|3|<br>TACHOnet returns the computed search keys as output parameters.|



**Alternate flows** 2a If the input parameters are invalid (e.g. illegal character,…), TACHOnet
returns a negative status code to the request.


**Special** - This service should ideally be implemented as a synchronous Web Service.
**requirements** - A web interface on top of this service should also be supplied to allow the CIA
users to access manually these TACHOnet services.

         - A downloadable version of this web service should also be made available (.NET
and Java) to enable some Member States to install and use it locally.


**Pre-conditions** The caller must provide the mandatory input parameters.


**Post-conditions** The caller has received the computed search keys (or a negative error code).


**Actors** - A _CIA_ (when issuing a new card) or an enforcer (via a CIA)

         - The TACHOnet system


_Continued on next page_


21-Feb-03 - Page 35


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### Use Case 05 – Get Phonex Search Keys, Continued


**Message flow** The following diagram outlines the flow of messages exchanged between actors:
**diagram**

**Card Issuing**
**TACHOnet**
**Authority (CIA)**


GetSearchKeys( sSN, sFN, sKSN, sKFN)


**Figure 9 – UC-05 messages flow**


**Input data** - **Surname (sSN):** driver’s surname

         - **First names (sFN):** driver’s first names


**Output data** - **Surname (sKSN):** computed search key of driver’s surname

         - **First names (sKFN):** computed search key of driver’s first of first names


**Additional** - Parameters should be UTF-8 encoded.
**remarks** - These services are opened to anyone connected on TESTA (no special security).


**Open issues** 

21-Feb-03 - Page 36


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Use Case 06 – Get US/Ascii Transliteration**


**Description** This use case consists of getting from TACHOnet the US/Ascii (ISO 646 IRV)
transliteration (From Latin or Greek) of the given driver’s surname, first names,
place of birth and driving license number.


Up to now, this use case only provides the transliteration from Greek (according to
the ISO 843:1997 standard) or Latin to US/Ascii. Other transliterations (e.g. Cyrillic
to US/Ascii according to ISO 9:1995) will be provided when needed.


**Basic flow** The basic flow consists of the following steps:

|Step|Action|
|---|---|
|<br>1|<br>The CIA calls the TACHOnet service giving the driver’s surname, first<br>names, place of birth and driving license number.|
|2|<br>TACHOnet checks the input parameters and, if valid, transliterates the<br>corresponding values into US/Ascii.|
|3|<br>TACHOnet returns the transliterated values as output parameters.|



**Alternate flows** 2a If the input parameters are invalid (e.g. illegal character,…), TACHOnet
returns a negative status code to the request.


**Special** - This service should ideally be implemented as a synchronous Web Service.
**requirements** - A web interface on top of this service should also be supplied to allow the CIA
users to access manually these TACHOnet services.

         - A downloadable version of this web service should also be made available (.NET
and Java) to enable some Member States to install and use it locally.


**Pre-conditions** The caller must provide the mandatory input parameters.


**Post-conditions** The caller has received the computed search keys (or a negative error code).


**Actors** - A _CIA_ (when issuing a new card) or an enforcer (via a CIA)

         - The TACHOnet system


_Continued on next page_


21-Feb-03 - Page 37


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### Use Case 06 – Get US/Ascii Transliteration, Continued


**Message flow** The following diagram outlines the flow of messages exchanged between actors:
**diagram**

**Card Issuing**
**TACHOnet**
**Authority (CIA)**


TransliterateToUSAscii(SN,FN,PB,DLN)


**Figure 10 – UC-06 messages flow**


**Input data** - **Surname (SN):** driver’s surname

         - **First names (FN):** driver’s first names

         - **Place of Birth (PB):** driver’s place of birth

         - **Driving license number (DLN):** driver’s driving license number


**Output data** The transliterated values as an array of strings


**Additional** - Parameters should be UTF-8 encoded.
**remarks** - These services are opened to anyone connected on TESTA (no special security).


**Open issues** 

21-Feb-03 - Page 38


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Section 2.2 - Use Case Package “TCN Statistics Tasks”** **Overview**


**Introduction** This section describes the use cases related to the “TCN Statistics Tasks” package.
The following diagram lists the use cases of this package:



CIA Administrator


(f rom Actors)



Generate Statistics


Log the message





**Figure 11 –Use Case Package “TCN Statistics Tasks”**


**Contents** This section contains the following topics:

|Topic|See Page|
|---|---|
|<br>Use Case 07 – “Add a new CIA”|<br>40|
|Use Case 08 – “Reset Password”|42|
|<br>Use Case 09 – “Generate Statistics”|<br>44|
|Use Case 10 – “Browse Statistics”|47|
|Use Case 11 – Log the message|52|



21-Feb-03 - Page 39


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Use Case 07 – “Add a new CIA”**


**Brief** In order to get access to the Statistics Reporting part of the TACHOnet system, every
**Description** Member State will be assigned a CIA Administrator’s account (and password).

This use case enables the TCN Administrator to create a new CIA Administrator
account in the Active Directory for a CIA Administrator using the `Microsoft`
```
        Management Console Active Directory Users and Computers
```

`(MMC)` .


**Primary Actor** TCN Administrator (or delegates to the operator).


**Preconditions** The actor has access to the `Microsoft Management Console Active`
`Directory Users and Computers` .


**Postconditions** The new CIA Administrator has been created and has now access to the
ReportManager Web site.


**Stakeholders** Access to the ReportManager Web site (providing the TCN usage statistics reports)
**and Interest** should only be allowed to the CIA Administrators. Therefore, every CIA
Administrator must be assigned a user account and password.


**Sequence**
**Diagram**


_Continued on next page_


21-Feb-03 - Page 40


|: TCN Administrator|Col2|Col3|MCC|Col5|Col6|
|---|---|---|---|---|---|
|: TCN Administrator|: TCN Administrator|: TCN Administrator|MCC|MCC||
|: TCN Administrator||||||


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### Use Case 07 – “Add a new CIA”, Continued


**Basic Flow** 
|Step|Action|
|---|---|
|<br>1|<br>A new Member State is added to the TACHOnet configuration (see Use-<br>Case 13 – “Manage Member State” at page 55). The TCN Administrator<br>(or operator) creates the new CIA Administrator account (and password)<br>using the`Microsoft Management Console Active`<br>`Directory Users and Computers`.|



**Alernative Flow** 


**Technology and**
**Data Variations**
**List**




- Access to the ReportManager web site will be secured by using Windows
accounts.



**Assumptions** - The TCN Administrator has access to the `Microsoft Management`

`Console Active Directory Users and Computers` . In the
production environment (if not, he may ask the operator to perform the steps).

         - Only one CIA Administrator account will be created per Member State.

         - All users are managed in the Active Directory.

         - The TACHOnet Administrator will also be assigned one account.


**Open issues** 

21-Feb-03 - Page 41


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Use Case 08 – “Reset Password”**


**Brief** This use case enables the TCN Administrator to reset in the Active Directory the
**Description** password of a CIA Administrator using the `Microsoft Management`
`Console Active Directory Users and Computers (MMC)` .


**Primary Actor** TCN Administrator (or delegates to the operator).


**Preconditions** The actor has access to the `Microsoft Management Console Active`
`Directory Users and Computers` and the CIA Administrator’s account has
already been created.


**Postconditions** The CIA Administrator’s password has been reset.


**Stakeholders** A CIA Administrator might forget her password. Therefore, the TCN Administrator
**and Interest** should be able to reset it.


**Sequence**
**Diagram**


_Continued on next page_


21-Feb-03 - Page 42


|: TCN Administrator|Col2|Col3|MCC|Col5|Col6|
|---|---|---|---|---|---|
|: TCN Administrator|: TCN Administrator|: TCN Administrator|MCC|MCC||
|: TCN Administrator||||||


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### Use Case 08 – “Reset Password”, Continued


**Basic Flow** 
|Step|Action|
|---|---|
|<br>1|<br>The CIA Administrator warns (via email) the TCN Administrator that<br>she forgots her password.|
|2|<br>The TCN Administrator (or operator) resets the corresponding CIA<br>Administrator account’s password using the`Microsoft`<br>`Management Console Active Directory Users and`<br>`Computers`.|
|3|The TCN Administrator warns the CIA Administrator (via email) to log<br>on again and change her password.|



**Alernative Flow** 


**Technology and**
**Data Variations**
**List**



Access to the ReportManager web site will be secured by using Windows accounts.



**Assumptions** - The TCN Administrator has access to the `Microsoft Management`

`Console Active Directory Users and Computers` . In the
production environment (if not, he may ask the operator to perform the steps).

         - Only one CIA Administrator account will be created per Member State.

         - All users are managed in the Active Directory.

         - The TACHOnet Administrator will also be assigned one account.


**Open issues** 

21-Feb-03 - Page 43


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Use Case 09 – “Generate Statistics”**


**Brief** This use case consists of transferring (at regular interval – nightly basis) all expired
**Description** TACHOnet transactions (completed or after timeout), storing them and generating
some usage statistics for the TCN Administrator and every CIA Administrators.

The usage statistics should give information about the incoming requests (from a
CIA to TACHOnet) for a given period:


         - The list of requests for the last 14 days (List).

         - The percentage of each status code values (Timeout, ServerError,…) for each
CIA (Consolidated chart).

         - The count and percentage of each status code values for each CIA (Consolidated
list).

         - The count and percentage of each CIA for each type of requests (Consolidated
list).

         - The count and percentage of each type of requests (CheckIssuedCards,
CheckCardStatus,…) for each mode – Batch and On-line - (Consolidated list).


The usage statistics should give information about the outgoing requests (from
TACHOnet to a CIA) for a given period:


         - The list of requests for the last 14 days (List).

         - The percentage of OK status code value for each CIA (Consolidated chart).

         - The percentage of each status code values (Timeout, ServerError,…) for each
CIA (Consolidated chart).

         - The count and percentage of each status code values for each CIA (Consolidated
list).

         - The count and percentage of each CIA for each type of requests (Consolidated
list).

         - The count and percentage of each type of requests for each mode – Batch and
On-line - (Consolidated list).


The consolidated lists should also give information about the minimum, maximum
and average value of the time it took to complete the transaction and for the given
timeout value.


**Primary Actor** TCN Reporting System.


**Preconditions** Expired transactions are available and the Agent is scheduled on a nightly base.


_Continued on next page_


21-Feb-03 - Page 44


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### Use Case 09 – “Generate Statistics”, Continued


**Postconditions** Transactions are transferred and statistics are generated.


**Stakeholders** Statistics are a major measurement tool for identifying potential problems, assessing
**and Interests** the overall usage of the system.



**Sequence**
**Diagram**










|Agent Job:Tachonet SP:TransferInfo SP:ProcessInfo Dts:TachonetDWOlap<br>Transfer Processing<br>Execute<br>Execute<br>Nightly<br>execution based<br>on a schedule. Execute Execute|Col2|Col3|Col4|Col5|Dts:TachonetDWOlap|Col7|
|---|---|---|---|---|---|---|
|Agent<br>Job:Tachonet<br>Transfer<br>SP:TransferInfo<br>Dts:TachonetDWOlap<br>Processing<br>SP:ProcessInfo<br>Execute<br>Nightly<br>execution based<br>on a schedule.<br>Execute<br>Execute<br>Execute|Agent<br>Job:Tachonet<br>Transfer<br>SP:TransferInfo<br>Dts:TachonetDWOlap<br>Processing<br>SP:ProcessInfo<br>Execute<br>Nightly<br>execution based<br>on a schedule.<br>Execute<br>Execute<br>Execute|Agent<br>Job:Tachonet<br>Transfer<br>SP:TransferInfo<br>Dts:TachonetDWOlap<br>Processing<br>SP:ProcessInfo<br>Execute<br>Nightly<br>execution based<br>on a schedule.<br>Execute<br>Execute<br>Execute|Agent<br>Job:Tachonet<br>Transfer<br>SP:TransferInfo<br>Dts:TachonetDWOlap<br>Processing<br>SP:ProcessInfo<br>Execute<br>Nightly<br>execution based<br>on a schedule.<br>Execute<br>Execute<br>Execute|Agent<br>Job:Tachonet<br>Transfer<br>SP:TransferInfo<br>Dts:TachonetDWOlap<br>Processing<br>SP:ProcessInfo<br>Execute<br>Nightly<br>execution based<br>on a schedule.<br>Execute<br>Execute<br>Execute|<br>Processing|<br>Processing|
|Agent<br>Job:Tachonet<br>Transfer<br>SP:TransferInfo<br>Dts:TachonetDWOlap<br>Processing<br>SP:ProcessInfo<br>Execute<br>Nightly<br>execution based<br>on a schedule.<br>Execute<br>Execute<br>Execute|Agent<br>Job:Tachonet<br>Transfer<br>SP:TransferInfo<br>Dts:TachonetDWOlap<br>Processing<br>SP:ProcessInfo<br>Execute<br>Nightly<br>execution based<br>on a schedule.<br>Execute<br>Execute<br>Execute|Agent<br>Job:Tachonet<br>Transfer<br>SP:TransferInfo<br>Dts:TachonetDWOlap<br>Processing<br>SP:ProcessInfo<br>Execute<br>Nightly<br>execution based<br>on a schedule.<br>Execute<br>Execute<br>Execute|Agent<br>Job:Tachonet<br>Transfer<br>SP:TransferInfo<br>Dts:TachonetDWOlap<br>Processing<br>SP:ProcessInfo<br>Execute<br>Nightly<br>execution based<br>on a schedule.<br>Execute<br>Execute<br>Execute|Agent<br>Job:Tachonet<br>Transfer<br>SP:TransferInfo<br>Dts:TachonetDWOlap<br>Processing<br>SP:ProcessInfo<br>Execute<br>Nightly<br>execution based<br>on a schedule.<br>Execute<br>Execute<br>Execute|<br>Processing||
|Agent<br>Job:Tachonet<br>Transfer<br>SP:TransferInfo<br>Dts:TachonetDWOlap<br>Processing<br>SP:ProcessInfo<br>Execute<br>Nightly<br>execution based<br>on a schedule.<br>Execute<br>Execute<br>Execute|||||||
|Agent<br>Job:Tachonet<br>Transfer<br>SP:TransferInfo<br>Dts:TachonetDWOlap<br>Processing<br>SP:ProcessInfo<br>Execute<br>Nightly<br>execution based<br>on a schedule.<br>Execute<br>Execute<br>Execute||Exec|Exec|Exec|Exec|Exec|
|Agent<br>Job:Tachonet<br>Transfer<br>SP:TransferInfo<br>Dts:TachonetDWOlap<br>Processing<br>SP:ProcessInfo<br>Execute<br>Nightly<br>execution based<br>on a schedule.<br>Execute<br>Execute<br>Execute|||||||



**Basic Flow** The basic flow for this use case is the following.

|Step|Action|
|---|---|
|<br>1|<br>The Agent executes the Job: Tachonet Transfer based on its schedule.|
|<br>2|<br>The Job: Tachonet Transfer executes the SP: TransferInfo which<br>transfers expired transactions from the production database to the<br>datawarehouse database.|
|3|<br>The Job: Tachonet Transfer executes the SP: ProcessInfo.|
|<br>4|<br>The SP: ProcessInfo executes the Dts: TachonetDWOlap Processing<br>which processes cubes in the OLAP database.|



**Alernative Flow** 

_Continued on next page_


21-Feb-03 - Page 45


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### Use Case 09 – “Generate Statistics”, Continued


**Special** There are two special requirements.
**Requirements**


|Requirement<br>Id|Description|
|---|---|
|<br>1|Usage statistics should be made available as a web-based<br>interface.|
|2|The web-based interface should support download of the<br>rendered statistics in different formats as xml and Excel.|



**Technology and**
**Data Variations**
**List**




- SQL Reporting Services (brand new service of SQL Server 2000) will be used
to provide the whole TCN reporting solution (user interface, report generation,
report design,…).



**Assumptions** 

**Open issues** 


21-Feb-03 - Page 46


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Use Case 10 – “Browse Statistics”**


**Brief** This use case consists of allowing the TCN Administrator and every CIA
**Description** Administrator to browse, via a secure Web interface, the usage statistics reports.

There are five reports available:


         - **Requests from MS – List** for the list of requests for the last 14 days (List).

         - **Requests from MS – Consolidation** for the percentage of each status code
value for each CIA (Consolidated chart), the count and percentage of each status
code value for each CIA (Consolidated list), the count and percentage of each
CIA for each type of requests (Consolidated list) and the count and percentage
of each type of requests for each mode – Batch and On-line - (Consolidated
list).

         - **Requests to MS – List** for the list of requests for the last 14 days (List).

         - **Requests to MS – Top** for the percentage of OK status code value for each CIA
(Consolidated chart).

         - **Requests to MS – Consolidation** for the percentage of each status code value
for each CIA (Consolidated chart), the count and percentage of each status code
value for each CIA (Consolidated list), the count and percentage of each CIA
for each type of requests (Consolidated list) and the count and percentage of
each type of requests for each mode – Batch and On-line - (Consolidated list).


**Primary Actor** - TCN Administrator.

         - CIA Administrator.


**Preconditions** - Transactions are transferred and statistics are generated.

         - The actor has access to the ReportManager Web site.


**Postconditions** The actor has browsed and downloaded report(s).


**Stakeholders** Statistics are a major measurement tool for identifying potential problems, assessing
**and Interests** the overall usage of the system.


_Continued on next page_


21-Feb-03 - Page 47


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### Use Case 10 – “Browse Statistics”, Continued


**Sequence**
**Diagram**

|ReportManager Users<br>: CIA Administrator : TCN Administrator<br>Login<br>ChangePassword<br>AskReport<br>Login<br>ChangePassword<br>AskReport|Col2|Col3|Col4|Users|Col6|
|---|---|---|---|---|---|
|: CIA Administrator<br>ReportManager<br>Users<br> : TCN Administrator<br>Login<br>ChangePassword<br>AskReport<br>Login<br>ChangePassword<br>AskReport|: CIA Administrator<br>ReportManager<br>Users<br> : TCN Administrator<br>Login<br>ChangePassword<br>AskReport<br>Login<br>ChangePassword<br>AskReport|: CIA Administrator<br>ReportManager<br>Users<br> : TCN Administrator<br>Login<br>ChangePassword<br>AskReport<br>Login<br>ChangePassword<br>AskReport|: CIA Administrator<br>ReportManager<br>Users<br> : TCN Administrator<br>Login<br>ChangePassword<br>AskReport<br>Login<br>ChangePassword<br>AskReport|Users||
|: CIA Administrator<br>ReportManager<br>Users<br> : TCN Administrator<br>Login<br>ChangePassword<br>AskReport<br>Login<br>ChangePassword<br>AskReport|: CIA Administrator<br>ReportManager<br>Users<br> : TCN Administrator<br>Login<br>ChangePassword<br>AskReport<br>Login<br>ChangePassword<br>AskReport|ChangePas|ChangePas|ChangePas|ChangePas|
|: CIA Administrator<br>ReportManager<br>Users<br> : TCN Administrator<br>Login<br>ChangePassword<br>AskReport<br>Login<br>ChangePassword<br>AskReport|: CIA Administrator<br>ReportManager<br>Users<br> : TCN Administrator<br>Login<br>ChangePassword<br>AskReport<br>Login<br>ChangePassword<br>AskReport|AskReport||||
|: CIA Administrator<br>ReportManager<br>Users<br> : TCN Administrator<br>Login<br>ChangePassword<br>AskReport<br>Login<br>ChangePassword<br>AskReport|: CIA Administrator<br>ReportManager<br>Users<br> : TCN Administrator<br>Login<br>ChangePassword<br>AskReport<br>Login<br>ChangePassword<br>AskReport|gin|gin|gin|gin|
|: CIA Administrator<br>ReportManager<br>Users<br> : TCN Administrator<br>Login<br>ChangePassword<br>AskReport<br>Login<br>ChangePassword<br>AskReport||ChangePassword|ChangePassword|ChangePassword|ChangePassword|
|: CIA Administrator<br>ReportManager<br>Users<br> : TCN Administrator<br>Login<br>ChangePassword<br>AskReport<br>Login<br>ChangePassword<br>AskReport|AskR|eport||||
|: CIA Administrator<br>ReportManager<br>Users<br> : TCN Administrator<br>Login<br>ChangePassword<br>AskReport<br>Login<br>ChangePassword<br>AskReport||||||



**Basic Flow** The basic flow for this use case is the following.

|Step|Action|
|---|---|
|<br>1|<br>The actor logs in the system using the standard basic security mechanism<br>of the web browser.|
|2|If the login succeeded, the actor browses the reports on the<br>ReportManager Web site.|
|3|<br>If it is the first access of the actor, he may change his password on the<br>Users Web site.|



_Continued on next page_


21-Feb-03 - Page 48


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### Use Case 10 – “Browse Statistics”, Continued


**Alernative Flow** Some alternatives are described below, referred to in the basic flow.


**Requests from**
**MS – List**
**Report**


**Requests from**
**MS –**
**Consolidation**
**Report**


**Requests to MS**

**– List Report**

|Step|Action|
|---|---|
|<br>2b|<br>If the login failed, the actor calls the TCN Administrator to reset his<br>password or to do the adequate operation.|



_Continued on next page_


21-Feb-03 - Page 49


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### Use Case 10 – “Browse Statistics”, Continued


**Requests to MS**

**– Top Report**


**Requests to MS**

**– Consolidation**
**Report**


**Special** There is one special requirement.
**Requirements**


|Requirement<br>Id|Description|
|---|---|
|<br>1|The generated reports should be dynamic reports.|



**Technology and**
**Data Variations**
**List**




- SQL Reporting Services (brand new service of SQL Server 2000) will be used
to provide the whole TCN reporting solution (user interface, report generation,
report design,…).



**Assumptions** - A special web site (single page) will also be built to allow the CIA
Administrator to change her account’s password.

         - Only one CIA Administrator account will be created per Member State.

         - All users are managed in the Active Directory.

         - The TACHOnet Administrator will also be assigned one account.


_Continued on next page_


21-Feb-03 - Page 50


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### Use Case 10 – “Browse Statistics”, Continued


**Open issues** 

21-Feb-03 - Page 51


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Use Case 11 – Log the message**


**Description** This use case consists of logging as-is every message sent or received by
TACHOnet.

Such logging is provided out-of-the-box by BizTalk and will be configured at the
channel level using the `BizTalk Messaging Manager` tool.


**Basic flow** The basic flow consists of the following steps:

|Step|Action|
|---|---|
|<br>1|<br>Upon receiving a message, TACHOnet should log it as-is in the tracking<br>database.|
|2|<br>Prior to sending a message, TACHOnet should log it as-is in the tracking<br>database.|



**Alternate flows** - TACHOnet should also provide a system for archiving (e.g. removing from the
tracking database to flat files) “old” messages (how long should TACHOnet keep
track of a message?).


**Special** - Great care must be taken when setting up the tracking database in terms of sizing
**requirements** (the number of the messages to be logged might quickly become huge),
performance (the logging mechanism should not impede overall TACHOnet
system performance), availability (high availability must be guaranteed through
clustering,...) and security (restricted administrative access, strong backup
policies,...).


**Pre-conditions** - A message (request, response) is received by TACHOnet or about to be sent by
TACHOnet.


**Post-conditions** - The received/sent message is logged in the tracking database


**Actors** - TACHOnet system


**Additional** **remarks**


**Open issues** - How long should TACHOnet keep track of a message?


21-Feb-03 - Page 52


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Section 2.3 - Use Case Package “TCN System Tasks”** **Overview**


**Introduction** This section describes the use cases related to the “TCN Monitoring” package. The
following diagram lists the use cases of this package:


Manage Member State


**Figure 12 –Use Case Package “TCN System Tasks”**


**Contents** This section contains the following topics:

|Topic|See Page|
|---|---|
|<br>Use-Case 12 – “Monitor the system”|<br>54|
|<br>Use-Case 13 – “Manage Member State”|<br>55|



21-Feb-03 - Page 53


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Use-Case 12 – “Monitor the system”**


**Brief** This use case consists of monitoring the whole TACHOnet system.
**Description**

Such monitoring will be based on the MOM (Microsoft Operations Manager)
product, used as standard monitoring tool by the EC DI’s Data Center.

Managing BizTalk through MOM is made possible by installing the BizTalk
Management Pack for MOM. Nevertheless, as this pack consists of more than 700
rules, some configuration need to be made (in close collaboration with EC DI’s Data
Center people) to configure the set of rules required for monitoring the BizTalk
configuration of TACHOnet.


**Primary Actor** - TCN Administrator


**Preconditions** The TCN Administrator has access to the MOM console.


**Postconditions** The TCN Administrator has managed alerts sent through the MOM console.


**Stakeholders** In order to constantly keep the availability and performance of the TACHOnet
**and Interests** system at an optimum level, the system must constantly monitored and should raise
some events when particular problems (HW, SW,…) occur.


**Basic Flow** See MOM documentation.



**Technology and**
**Data Variations**
**List**







**Assumptions** - MOM is used as central monitoring system.


**Open issues** - Will the TACHOnet servers be directly monitored from the central MOM
console or should TACHOnet provide ?

         - Is there any special FW configuration between the TACHOnet servers and the
central MOM console?

         - What are the BizTalk rules that need be configured in MOM and how?


21-Feb-03 - Page 54


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### **Use-Case 13 – “Manage Member State”**


**Brief** This use case consists of managing a Member State CIA in terms of TACHOnet
**Description** configuration (add, edit, remove a Member State CIA).


**Primary Actor** - TCN Administrator


**Preconditions** The TCN Administrator has access to the `BizTalk Messaging Manager` and
`BizTalk Server Administration` tools.


**Postconditions** The Member State CIA configuration in TACHOnet has been updated.


**Stakeholders** All Member States will not be ready at production day 1. Moreover, new candidate
**and Interests** Member States will potentially join TACHOnet in the near future. The configuration
of existing Member States could also change. Therefore, it’s important to provide the
TCN Administrator with the tools or procedures to manage the TACHOnet
configuration of a Member State.


**Basic Flow** Managing Member States consists of adding a new Member State or modifying the
current configuration of a Member State (url address, digital certificates,…) or
removing a Member State (?). All these manual tasks will be described in details in
the “ **TCN Operational Guide”** document. Anyway, some of these major tasks are
outlined below:

**Adding a new Member State** :

The following table lists the activities to carry out to add a new Member State in the
TACHOnet configuration:


         - BizTalk configuration:




- Create the BizTalk organization corresponding to the new Member State
(“ `TCN_<countrycode>”)` with its relevant properties.




- Create the corresponding BizTalk messaging ports.




- Create the corresponding BizTalk distribution list (“ `All-`
`<countrycode>”)` .




- Update all the other BizTalk distribution lists to add the new messaging port
(send request) corresponding to the new Member State.




- Create the corresponding BizTalk channels.




   - Create the corresponding BizTalk receive functions (in test environment).

- Reporting System:




- Add a new CIA Administrator account



_Continued on next page_


21-Feb-03 - Page 55


TACHOnet - DG TREN GETRONICS BELGIUM
Software Requirements Specification – version 01_00

#### Use-Case 13 – “Manage Member State”, Continued


**Basic Flow** **Modifying the current configuration of a Member State** :
(continued)

         - Changing the phone/fax/email of the Member State:

               - Update the custom properties of the BizTalk organization corresponding to
the Member State

         - Changing the url address where TACHOnet should send XML messages:

               - Update the transport type of the BizTalk messaging port corresponding to
the Member State.



**Technology and**
**Data Variations**
**List**




- BizTalk Server 2002 provides the necessary tools to manage its configuration.
These will be leveraged to update the Member States configuration.



**Assumptions** The TCN Administrator is a BizTalk Administrator and has access to the `BizTalk`
`Messaging Manager` and `BizTalk Server Administration` tools (or
will delegate to the effective BizTalk Administrator).


**Open issues** 

<End of the document/>


21-Feb-03 - Page 56


