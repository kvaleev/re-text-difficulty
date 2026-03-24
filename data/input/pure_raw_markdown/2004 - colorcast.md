---
consensus_grade_level: 12.3
headings_per_sentence: 0.12
lists_per_sentence: 0.02
smao_sentences_pct: 2.4
vague_words_per_sentence: 0.11
anaphora_per_sentence: 0.27
sentence_cv: 1.004
cpre_terms_per_sentence: 0.71
---
# **Software Requirements** **Specification**

## **for**

# **CS179G / ABC Paint Project**

#### **Version 1.0** **Prepared by Benjamin Arai and Conley Read**

����������

#### **Friday, February 13, 2004**


_**Software**_ _**Requirements Specification for CS179g / ABC Paint Project**_ _**Page ii**_

### **Table of Contents**


**Table of Contents.......................................................................................................................... ii**
**Revision History............................................................................................................................ ii**
**1.** **Introduction..............................................................................................................................1**
1.1 Purpose ........................................................................................................................................1
1.2 Document Conventions................................................................................................................1
1.3 Intended Audience and Reading Suggestions..............................................................................1
1.4 Product Scope ..............................................................................................................................2
1.5 References....................................................................................................................................2
**2.** **Overall Description..................................................................................................................3**
2.1 Product Perspective .....................................................................................................................3
2.2 Product Functions........................................................................................................................3
2.3 User Classes and Characteristics.................................................................................................3
2.4 Operating Environment................................................................................................................4
2.5 Design and Implementation Constraints......................................................................................4
2.6 User Documentation ....................................................................................................................4
2.7 Assumptions and Dependencies ..................................................................................................4
**3.** **External Interface Requirements ...........................................................................................6**
3.1 User Interfaces.............................................................................................................................6
3.2 Hardware Interfaces.....................................................................................................................6
3.3 Software Interfaces ......................................................................................................................6
3.4 Communications Interfaces .........................................................................................................7
**4.** **System Features........................................................................................................................8**
4.1 Graphical Color Chooser.............................................................................................................8
4.2 Color Translator...........................................................................................................................8
4.3 Closest Colors..............................................................................................................................8
4.4 Color Search Engine....................................................................................................................8
4.5 User Color Palette........................................................................................................................9
4.6 Administrative Interface ..............................................................................................................9
4.7 Color Sample Matcher.................................................................................................................9
**5.** **Other Nonfunctional Requirements.....................................................................................10**
5.1 Performance Requirements........................................................................................................10
5.2 Safety Requirements..................................................................................................................10
5.3 Security Requirements...............................................................................................................10
5.4 Software Quality Attributes.......................................................................................................11
5.5 Business Rules...........................................................................................................................11
**Appendix A: Glossary..................................................................................................................12**
**Appendix B: Analysis Models.....................................................................................................14**
**Appendix C: To Be Determined List..........................................................................................15**
**Approval Signatures: Approve Version.....................................................................................16**

### **Revision History**


|Name|Date|Reason For Changes|Version|
|---|---|---|---|
|<br>|<br>|<br>|<br>|
|<br>||||


_**Software**_ _**Requirements Specification for CS179g / ABC Paint Project**_ _**Page 1**_

### **1. Introduction**

#### **1.1 Purpose**


In third quarter 2004, ABC Paint will migrate to a new paint numbering scheme. This migration
comes at a time that ABC Paint will be adding and discontinuing a number of paints and
_**collection**_ s. Although the remaining customers who utilize these soon-to-be-discontinued products
are encouraged to begin using other paints in our product line, the initial transition is not occurring
as rapidly or as easily as ABC Paint would like.

For ABC Paint customers to remain loyal and happy, we will create an easy to use system,
allowing conversion to the new paints and _**collection**_ s. The new system must be in place by the
second quarter of 2004, allowing customers the time to adjust to the new scheme before they will
not be able to order the discontinued products. The use of the _**application**_ will be long-term, used
for the immediate transition and in the future when previous customers may return for more paint
with old-scheme numbers.

This single _**application**_ will be a version 1.0 product with no previous revisions in use. This standalone product includes features to enable ABC Paint to easily and seamlessly include the
_**application**_ in their current website.

#### **1.2 Document Conventions**


Two primary typographical conventions were followed in the generation of this specification paper.
First, all acronyms are fully defined in their first use and then identified. They are also redundantly
defined in the glossary, Appendix A. Any _**bold italicized**_ item in the specification is also briefly
defined in the Appendix A glossary.

You may find it helpful to review the list of documents related to the project as referenced in the
references section, section 1.5, of this specification. You can also review the exhaustive list of
documents and interviews related to the ABC Paint Project at:

_**HTTP**_ ://cs179g.conleyread.net/exec/project/docs.htm

#### **1.3 Intended Audience and Reading Suggestions**


This document is intended for reading by developers and project managers. These readers will
find that this document is a product specification only, not a design document. It is recommended
that all readers complete the introduction section before continuing onto the other sections. The
introduction section that you are now reading provides a broad overview of the entire project and
serves as a guide to the other sections. Developers will find sections two, four most useful to them
while sections three and five will most likely be paid the most attention by project managers.

Sections two and four provide both overall descriptions of the project and the product itself.
Sections three and five present an outline of the product interface requirements and other nonfunctional or performance requirements, which the final product must meet. The project manager
will find these requirements most enlightening to peruse, as they will help guide decisions and
performance choices throughout the entire product development process.


_**Software**_ _**Requirements Specification for CS179g / ABC Paint Project**_ _**Page 2**_

#### **1.4 Product Scope**


Ensure that you have read section 1.1 before continuing to this section.

This system must enable a smooth transition to the new paint numbers and scheme. The system
will be designed for use as long as the hardware and operating systems specified in this document
remain available. The product will be highly accessible to ABC Paint _**client**_ s and distributors. To
enable this wide access to the _**application**_, the new system will be integrated into the current ABC
Paint website.

Each main feature of the _**application**_ will be modularized. Each module will fit on a single
webpage. The _**application**_ will provide a theme and styling mechanism to allow ABC Paint web
designers to integrate the _**application**_ .

ABC Paint has made it very clear that they will make trade-offs to retain the benefits of the
_**application**_ being available on the web, retaining high accessibility. The product will also include
documentation available to website users, paint distributors, and full setup documentation for the
ABC Paint information technology department so that they may manage the _**application**_ them
selves.

#### **1.5 References**


ABC Paint Project Disaster Recovery Plan
_**HTTP**_ ://cs179g.conleyread.net/docs/disaster_recovery.pdf

ABC Paint Design Problem Statement
_**HTTP**_ ://cs179g.conleyread.net/docs/ProblemStatement.pdf

Karl E. Wiegers, Software Requirements, Second Edition
_**HTTP**_ ://www.microsoft.com/mspress/books/index/6496.asp


_**Software**_ _**Requirements Specification for CS179g / ABC Paint Project**_ _**Page 3**_

### **2. Overall Description**

#### **2.1 Product Perspective**


As defined in sections 1.1 and 1.4, the _**application**_ for ABC Paint will be a first-of-type solution to
ensure that their business and their customer’s paint selecting experience maintains continuity and
consistency throughout their transition to an entirely new product line.

The product is a stand-alone web _**application**_ with a theme mechanism to allow easy integration
of the _**application**_ into the ABC Paint website. The ColorKast solution is a _**server**_ based
_**application**_ with a web-based _**client**_ for consumer and enterprise access.

In some respects, the _**application**_ is the next generation of the old mechanical, hand-select,
palette board system located in paint stores everywhere.

Primarily, the _**application**_ will include a old to new product-line “translator,” a graphical color
chooser, a color search-engine, a user color palette, possibly, an easy to use color matching
system, and an administrative interface. All of these will be defined and described later in this
same document. The actual user interface will be described in a separate user interface
specification whitepaper.

All references to performance or specification apply to the _**application**_ _**client**_ . Specifications and
performance estimates apply to the _**application**_ _**server**_ only if explicitly stated.

#### **2.2 Product Functions**


These functions are modularized sub-components of the _**client**_ _**application**_ . Each of the functions
has a single purpose and can accomplish its mission without the other components. Together, the
components function as a stand-alone _**application**_ .

  - Color Chooser ( _**Pointing device**_ driven color selection utility)

  - Color number translator (old scheme -> new scheme)

  - Find a particular number of colors near a given color

  - Session persistent user _**color palette**_ (colors picked, images uploaded)

  - Color search engine (all _**collection**_ s, specific collection)

  - Color matching (uploaded image, see section 4)

  - Administrative interface (update, add, delete colors, add users)

#### **2.3 User Classes and Characteristics**


ColorKast has identified two user classes for access to the new _**application**_ . The first user class is
default for all users and allows no administrative functionality whatsoever. The second class, the
administrative user, is composed of several subclasses for the secure management of access to
data and permissions throughout the organization.


_**Software**_ _**Requirements Specification for CS179g / ABC Paint Project**_ _**Page 4**_


Default: This user has access to all functionality of the _**application**_ except the administrative
function. The user data stored by this user is not password protected but is session
persistent.

Administrative: This user is composed of three subclasses. Level 3, the highest level
administrative user has all access, update, add, delete permissions, and can
create other administrative users at any level. Level 2, has update, add
permissions, and can create administrative users up to Level 2. Level 1, has
add permissions and can add administrative users at Level 1 only.

#### **2.4 Operating Environment**


The proposed ColorKast Solution will be implemented in a _**client**_ / _**server**_ model. All processing of
searches and storing of information will be local to the _**server**_ .

_**Server**_ : The _**server**_ requires at least a 1GHz processor and 512 MB of system memory for
each group of 50 employee or consumer users.

_**Client**_ : The web-based _**client**_ is compatible with most operating systems and requires a
working installation of Internet Explorer 4.01, Netscape 6.0, or Mozilla 1.0 or later.
The _**client**_ computer should match or exceed the system requirements specified for
the web browser intended for use with the _**client**_ _**application**_ .

#### **2.5 Design and Implementation Constraints**


A few issues limit our choices when implementing a suitable solution for the ABC Paint Project.

It is very important that the _**application**_ be web-based. We understand that in any design choice,
precedence should be given to the implementation of a completely web-based _**client**_ .

Wherever possible, the _**application**_ should retain full usability with a keyboard input device only.
This allows an easy transition for employees who are primarily used to keyboard input in current
ABC Paint business _**application**_ s.

Finally, a utility should be available to report errors. In all instances, the _**application**_ should
attempt full recovery and report errors automatically to ColorKast without encroaching on the user
experience.

#### **2.6 User Documentation**


Documentation for users will be made available in the form of on-line help within the _**client**_
_**application**_ itself. An online tutorial will also be made available.

#### **2.7 Assumptions and Dependencies**


ColorKast assumes that any use of the _**application**_ will occur in an environment with full
compliance to this specification.

The _**application**_ will be used on a _**client**_ computer that matches or exceeds the requirements laid
out in section 2.4. The _**server**_ component of the _**application**_ will run on a computer system that
matches or exceeds the requirements laid out for the _**server**_ in section 2.4.


_**Software**_ _**Requirements Specification for CS179g / ABC Paint Project**_ _**Page 5**_


We assume that the _**application**_ will only be in use for duration of the wide-installation of the
software and hardware, as defined in this document, that is required for installation of the _**server**_
component and use of the _**client**_ _**application**_ .

We assume that finding the nearest colors in the red-green-blue color space will always give
acceptably similar colors to the given color for the purpose of color search.

The _**application**_ will be dependant on third-party databases for storage of paint information and
implementation of the color search engine. The databases will give responses to _**Queries**_ in subsecond time.


_**Software**_ _**Requirements Specification for CS179g / ABC Paint Project**_ _**Page 6**_

### **3. External Interface Requirements**

#### **3.1 User Interfaces**


The _**application**_ will have a task-based screen interface for increased usability and workflow pace.
The interface will use accelerator keys heavily to allow limited “keyboard-only” _**application**_ use.

A task-pane will be available in all workflow scenarios to allow easy access to on-line help and
next-step options. The navigation options in every screen will be similar to lower or eliminate the
_**application**_ learning curve.

Input confirmation and error notification will be consistent throughout the _**application**_ .

Themeing of the _**application**_ allows consumers to use the _**application**_ in the context of the ABC
Paint website, while ABC Paint employees may use the new system in the familiar environment of
a enterprise _**LAN**_ .

A _**Pointing device**_ will be required for color selection, for example, when matching colors or using
the graphical color chooser.

#### **3.2 Hardware Interfaces**


The _**application**_ is dependent on existing hardware for a display device and for data-entry via a
keyboard and _**Pointing device**_ . The new system does not support legacy monochrome displays.
The _**application**_ provides minimal support for _**client**_ computers without a _**Pointing device**_ .

Display dependency: The _**client**_ computer must have a display device capable of display of 16.7
million colors or greater. Colors displayed on the target _**client**_ computer will
only be accurate when the device is properly calibrated.

Keyboard: The keyboard is used to enter and place _**Paint name**_ and paint number
searches. The keyboard also provides “keyboard-only” _**application**_
functionality when a _**Pointing device**_ is not available.

_**Pointing device**_ : The _**Pointing device**_ provides intuitive, fluid control of the _**application**_ for
less sophisticated consumer users, and ease-of-use for the graphical color
chooser interface.

#### **3.3 Software Interfaces**


The ColorKast software will interface with other software for storage of paint information, paint
_**collection**_ data, and the matching and translation of paint _**color value**_ s.

Interface 1: Connection to database for storage of information for paint number, name,
_**collection**_, and company.

Interface 2: Database connection for color search, matching, and paint number scheme
translation.


_**Software**_ _**Requirements Specification for CS179g / ABC Paint Project**_ _**Page 7**_


These connections are implemented on the _**server**_ . The interface protocol is not specified, but will
meet the requirements of the intended interaction

#### **3.4 Communications Interfaces**


This product will require communication via the Hyper Text Transfer Protocol ( _**HTTP**_ ) to complete
transaction based services with _**client**_ computers. As identified in the Assumptions and
Dependencies section 2.7, this product requires a web browser to function. The Web Browser
must comply with standards for _**HTTP**_ version 1.0 or 1.1. _**HTTP**_ version 1.0 is a well founded and
highly supported protocol. Now considered legacy by some organizations, we believe this is a safe
foundation for the product.

The product also indirectly requires some network connection to the internet, over which it may
communicate in _**HTTP**_ . This network connection assumes a physical or wireless connection from
the _**client**_ computer to a consumer Internet Service Provider ( _**ISP**_ ) or enterprise environment Local
Area Network ( _**LAN**_ ).


_**Software**_ _**Requirements Specification for CS179g / ABC Paint Project**_ _**Page 8**_

### **4. System Features**

Each feature has a single mission it can complete independently. This feature set is a modularized
representation of the stand-alone _**application**_ . The modularization approach allows for a more
robust _**application**_ with fault tolerance and easy module replacement for _**security**_ and
upgradeability.

#### **4.1 Graphical Color Chooser**


The graphical color chooser will be a pointing device driven intuitive color selection tool.
**4.1.1 Priority**

High priority.
**4.1.2 Functional Requirements**

The color chooser requires the presence of a hardware pointing device.

#### **4.2 Color Translator**


The color translator is a special case of the color search engine. The color translator allows old
scheme to new scheme paint number translation, given a paint number, collection and a target
collection.
**4.1.1 Priority**

High priority.
**4.1.2 Functional Requirements**

The color translator requires the presence of the software color search module.

#### **4.3 Closest Colors**


The closest color tool is a special case of the color search engine. The closest color tool allows the
user to locate an arbitrary number of close colors to given a paint number, collection in a target
collection.
**4.1.1 Priority**

High priority
**4.1.2 Functional Requirements**

The closest colors tool requires the presence of the software color search module.

#### **4.4 Color Search Engine**


The color search engine tool will allow locating an arbitrary number of colors in any or all
collections based on initial input of a paint name, number, or color value in a industry standard
common format.
**4.1.1 Priority**


_**Software**_ _**Requirements Specification for CS179g / ABC Paint Project**_ _**Page 9**_


High priority
**4.1.2 Functional Requirements**

The color search engine requires the color space and paint information databases
to be present. These two databases store paint and collection information.

#### **4.5 User Color Palette**


This is a user experience tool. The user color palette tool will store a list of the user’s recent color
searches. If the color sample matcher is loaded, the user color palette tool will also store recent
uploaded images for matching. The user color matcher only associates this information with a
single client based on a persistent client session. This user data will be removed from the server
after 30 days. This information is private but not secure.
**4.1.1 Priority**

High priority
**4.1.2 Functional Requirements**

The User Color Palette requires the color search engine for color requests and the
color sample matcher to enable the storing of uploaded images for matching.

#### **4.6 Administrative Interface**


The administrative interface allows administrative users to update, add, and delete paint
information. Administrative users are also able to add users. Refer to section 2.3 for development
and implementation of user classes and access permissions.
**4.1.1 Priority**

High priority
**4.1.2 Functional Requirements**

The application administrative interface requires the color space and paint
information databases to be present.

#### **4.7 Color Sample Matcher**


The color sample matcher allows the client user to upload images in a common format for
matching. The color sample matcher will allow the user to graphically select with a hardware
pointing device the color or blended color group they wish to use in a color search.
**4.1.1 Priority**

Low priority. This module is not a requirement of the project. It is included for
specification purposes only.
**4.1.2 Functional Requirements**

The color sample matcher requires the color search engine module to function. The
color chooser requires the presence of a hardware pointing device.


_**Software**_ _**Requirements Specification for CS179g / ABC Paint Project**_ _**Page 10**_

### **5. Other Nonfunctional Requirements**

#### **5.1 Performance Requirements**


Color searches among the various _**collection**_ s defined by ABC Paint will be processed in subsecond time on the _**server**_ .

Changes to Paint and _**collection**_ information will occur in _**Real-time**_, although the actual
processing time will vary with respect to the amount of information to be updated, added, or
deleted on the _**server**_ .

While performance requirements are transparently defined at the _**server**_, ColorKast makes no
guarantees as to the speed, completeness, or timeliness of service over the greater internet.
Performance of the _**application**_ will vary on the speed and type of internet access to which the
_**client**_ computer has access.

To verify the performance of the _**application**_, ColorKast will show the amount of time the _**server**_
takes to process a request. The time shown will not take into account the transit time of the
information over various computer networks.

#### **5.2 Safety Requirements**


Analysis of the proposed product requirements and features has not brought any safety concerns
to light. ColorKast recommends that a full legal review of the final product be undertaken prior to
any public use of the product or business-wide rollout. This will ensure that ABC Paint is allowed
full indemnification of liability.

Refer to current state and federal regulations regarding workplace use of keyboard-based
products. Experts have concluded that the continued, repetitive use of data-entry and _**Pointing**_
_**device**_ s leads to injury in almost all circumstances. ColorKast takes no responsibility for injury or
resulting damages from the use of these devices.

#### **5.3 Security Requirements**


Due to the nature of the product, the data stored in repositories of the product is generally public
information consisting of _**paint name**_ s and _**color value**_ s not easily secured or obfuscated and
always recoverable by a sophisticated end user. No attempts will be made to secure this
information.

Information that the product will collect or store, which need access protections include user
specified _**color palette**_ s and their store of access permissions. Access to this information must be
private. Most important, the store of access permissions to administrative features and access
permissions must be secure.

Implementations of _**Privacy**_ and _**security**_ must be on par with industry standards.


_**Software**_ _**Requirements Specification for CS179g / ABC Paint Project**_ _**Page 11**_

#### **5.4 Software Quality Attributes**


The proposed modular specification of the _**application**_ lends itself to adaptability, robustness, and
reusability.

Questions of _**application**_ correctness come to light with respect to the accurate display of color
samples on the target _**client**_ computer. In the enterprise environment, we can assume that the
kiosk or employee computer will have a correctly calibrated display device. In the consumer
market, we cannot make this same assumption. To allow calibration of the _**client**_ display device is
a possible extension of this _**application**_, but is not currently included in the specification.

#### **5.5 Business Rules**


ColorKast recommends that ABC Paint apply their conventional business processes and **security**
regimen to granting administrative access to the new system. ColorKast believes that a typical
employee or consumer should be granted default privileges only. A limited number of
administrative users should be created to manage the paint data updates. Administrative users
can give other users administrative access up to their own access level only.


_**Software**_ _**Requirements Specification for CS179g / ABC Paint Project**_ _**Page 12**_

### **Appendix A: Glossary**

Terms:

_**Application**_ : The software product being developed by ColorKast for ABC Paint.

_**Client**_ : _A computer or program that can run_ _**application**_ _s or request_
_**application**_ _-based services from a_ _**server**_ _._

_**Color collection**_ : _A group of colors made by the same company, designed by a_
_specific designer, or provided in a separate group from other paints._
_For example, the Ralph Lauren_ _**Collection**_ _._

_**Color palette**_ : _A card, list, or other utility for displaying available or selected colors._

_**Color value**_ : _Logical color numbers used to represent physical colors normally_
_represented as_ _**RGB**_ _triplets._

_**Data-entry device**_ : _Hardware, a keyboard or mouse used to interact with an_
_**application**_ _._

_**Paint name**_ : A _distinctive title given a paint. Not a paint’s product number._

_**Pointing device**_ : _An input device, such as a mouse, joystick, or trackball, with which_
_one can move or manipulate a cursor or pointer to interact with an_
_**application**_ _._

_**Privacy**_ : _Limited_ _**security**_ _through indirect verification of identity. For example,_
_in the ColorKast_ _**application**_ _, persistent user data is linked to a_
_specific_ _**client**_ _session on a_ _**client**_ _computer, not a single individual._
_No_ _**security**_ _is implemented._

_**Query**_, _**Queries**_ : _A_ _**client**_ _’s request for information, generally as a formal request to a_
_database or search engine._

_**Real-time**_ _:_ _Not what you might think. This relates to computer systems that_
_update information at the same rate as they receive data. For_
_example, if the time required to update information on the_ _**server**_ _is_
_five minutes, then a_ _**Real-time**_ _update will take five minutes._

_**Security**_ : _Similar to_ _**Privacy**_ _, but much more secure. A individual is linked_
_directly to their persistent user data using a username and_
_associated pass phrase. This is required for all administrative level_
_access._

_**Server**_ : _A computer that processes requests for data and_ _**Queries**_ _that are_
_elements of the_ _**application**_ _._

_**Server side**_ : _Processing for the_ _**client**_ _or_ _**server**_ _that occurs only on the_ _**server**_ _._


_**Software**_ _**Requirements Specification for CS179g / ABC Paint Project**_ _**Page 13**_


Acronyms:

_**HTTP**_ : _Hyper Text Transfer Protocol._

_**ISP**_ : _Internet Service Provider._

_**LAN**_ : _Local Area Network._

_**RGB**_ : _Red Green Blue._

_**TBD**_ : _To Be Determined._


_**Software**_ _**Requirements Specification for CS179g / ABC Paint Project**_ _**Page 14**_

### **Appendix B: Analysis Models**

The project requirements elicitation interview conducted by
ColorKast helped to define the proposed architecture of the
product.

The proposed system breaks the problem into two distinct parts,
both separated by a connection to the internet.

In this proposed scenario, the _**client**_ computers access the
product _**application**_ over the internet on a _**server**_, which hosts the
_**application**_ . The _**application**_ stores all related paint, _**client**_ data
and authorization information in a local data cloud.


_**Software**_ _**Requirements Specification for CS179g / ABC Paint Project**_ _**Page 15**_

### **Appendix C: To Be Determined List**

This To Be Determined ( _**TBD**_ ) list serves to collect all currently outstanding decisions, choices, and
unresolved requirements, including questions the development team may need to ask of the ABC
Project Liaison.

Presently there are no remaining TBDs. All TBDs have been tracked to their closure.


_**Software**_ _**Requirements Specification for CS179g / ABC Paint Project**_ _**Page 16**_

### **Approval Signatures: Approve Version**


I hereby approve the attached Software Requirements Specification (SRS). The SRS satisfies all
design requirements. I acknowledge that my approval of the attached SRS is binding and that I
may no longer add or change any of the design requirements without the agreement of ColorKast.

Sign Date

Sign Date


