---
consensus_grade_level: 10.2
headings_per_sentence: 0.0
lists_per_sentence: 0.0
smao_sentences_pct: 1.9
vague_words_per_sentence: 0.03
anaphora_per_sentence: 0.18
sentence_cv: 1.167
cpre_terms_per_sentence: 0.73
---
[ ]{.Apple-converted-space}TITLE[  ]{.Apple-converted-space}\\\*
MERGEFORMAT Software Requirements
Specification[ ]{.Apple-converted-space}

**SRS**

\

\

Version 2.0

\

[ ]{.Apple-tab-span}[ ]{.Apple-tab-span}[ ]{.Apple-tab-span}[
]{.Apple-tab-span}[ ]{.Apple-tab-span}[ ]{.Apple-tab-span}[
]{.Apple-tab-span} [                         ]{.Apple-converted-space}

VIPER TEAM (Team\#6)

\

[ ]{.Apple-tab-span}[ ]{.Apple-tab-span}[ ]{.Apple-tab-span}[
]{.Apple-tab-span}

  ------------------------- --------------
  **Name**                  **Stu ID\#**
  Abdulrahman Al-Thubaiti   245406
  Anas Al-Hasani            245050
  Faisal Al-Ghamdi          237263
  Mohammed Al-Mathami       245040
  Nasser Al-Al-Khaldi       226286
  Abdullah Al-Jallal        231945
  ------------------------- --------------

[]{.s1}**Revision History**

+-----------------+-----------------+-----------------+-----------------+
| **Date**        | **Version**     | **Description** | **Author**      |
+-----------------+-----------------+-----------------+-----------------+
| 26/Nov/2008     | 0.1             | \- Initializing | Abdulrahman     |
|                 |                 | the SRS         | Al-Thubaiti     |
|                 |                 | Document        |                 |
|                 |                 |                 |                 |
|                 |                 | -writing the    |                 |
|                 |                 | introduct       |                 |
|                 |                 | ion[ ]{.Apple-c |                 |
|                 |                 | onverted-space} |                 |
+-----------------+-----------------+-----------------+-----------------+
| 29/Nov/2008     | 1.0             | -complete SRS   | VIPER team      |
|                 |                 | Document.       | members         |
+-----------------+-----------------+-----------------+-----------------+
| 20/Dec/2008     | 1.1             | 1- In the UCs   | Mohammad        |
|                 |                 | discretion the  | AlMathami\      |
|                 |                 | precondition    | Faisal          |
|                 |                 | and the first   | Al-Ghamdi       |
|                 |                 | step in the UC  |                 |
|                 |                 | discretion are  |                 |
|                 |                 | not the same as |                 |
|                 |                 | well as the     |                 |
|                 |                 | some of         |                 |
|                 |                 | Branching       |                 |
|                 |                 | Action need to  |                 |
|                 |                 | be changed as   |                 |
|                 |                 | it is explained |                 |
|                 |                 | in the          |                 |
|                 |                 | meeting.[\      |                 |
|                 |                 | \               |                 |
|                 |                 | 2- Adding the   |                 |
|                 |                 | logical DB      |                 |
|                 |                 | section which   |                 |
|                 |                 | is the tables   |                 |
|                 |                 | that we have in |                 |
|                 |                 | our system.\    |                 |
|                 |                 | \               |                 |
|                 |                 | 3- Adding UC    |                 |
|                 |                 | diagram into    |                 |
|                 |                 | the appendix    |                 |
|                 |                 | section as a    |                 |
|                 |                 | last thing in   |                 |
|                 |                 | the             |                 |
|                 |                 | report.]{.s2}   |                 |
+-----------------+-----------------+-----------------+-----------------+
| 20/Dec/2008     | 1.2             | 1- Modifying    | Anas Al-Hasani  |
|                 |                 | and adding in   |                 |
|                 |                 | Communication   |                 |
|                 |                 | interface.      |                 |
|                 |                 |                 |                 |
|                 |                 | 2- Modify and   |                 |
|                 |                 | improve format  |                 |
|                 |                 | document.       |                 |
+-----------------+-----------------+-----------------+-----------------+
| 20/Dec/2008     | 2.0             | 1\. Adding      | Abdulrahman     |
|                 |                 | Change          | Al-Thubaiti     |
|                 |                 | Management      |                 |
|                 |                 | Process         |                 |
|                 |                 |                 |                 |
|                 |                 | 2\. Finalizing  |                 |
|                 |                 | the SRS and     |                 |
|                 |                 | release v2.0    |                 |
+-----------------+-----------------+-----------------+-----------------+
| \               | \               | \               | \               |
+-----------------+-----------------+-----------------+-----------------+
| \               | \               | \               | \               |
+-----------------+-----------------+-----------------+-----------------+

\

[]{.s3}**Table of Contents**

1\.
Introduction.....................................................................................4

1.1 Purpose
.................................................................................4

1.2
Scope....................................................................................4

1.3 Definitions, Acronyms and Abbreviations
........................................4

1.4 References
.............................................................................5

1.5 Overview
..............................................................................5

2\. Overall
Description............................................................................5

2.1 Product
Perspective...................................................................7

2.2 Product Functions
..................................................................\...8

2.3 User Characteristics
..................................................................8

2.4 Constraints
.............................................................................8

2.5 Assumptions & Dependencies
......................................................8

2.6 Apportioning of
Requirements......................................................8

3\. Specific Requirements
.....................................................................\...8

3.1 Interface Requirements
...............................................................8

3.1.1 User Interfaces
....................................................................9

3.1.2 Hardware Interfaces
.............................................................28

3.1.3 Software Interfaces
..............................................................28

3.1.4 Communication Interfaces
................................................\......28

3.2 Functional Requirements
......................................................\......29

3.3 Performance Requirements
................................................\.........85

3.4 Logical Database
Requirements....................................................85

3.5 Design
Constraints............................................................\........85

3.6 Software System
Attributes.........................................................85

3.6.1
Reliability.........................................................................85

3.6.2 Availability
.......................................................................85

3.6.3 Security
...........................................................................86

3.6.4
Maintainability....................................................................86

3.6.5 Portability
.........................................................................86

[ ]{.Apple-tab-span}4. Change Management
Process...........................................
......................86

Appendix...........................................................................................87

[[ ]{.Apple-tab-span}[ ]{.Apple-tab-span}]{.s1}Use Case
Diagrams.................................................................................87

\

**TITLE[  ]{.Apple-converted-space}\\\* MERGEFORMAT Software
Requirements Specification[ ]{.Apple-converted-space}**

**Introduction**

**Purpose**

The purpose of this document is to fully describe the external behavior
of the SCM system in terms of functional requirements. It also describes
the nonfunctional requirements such as usability, availability,
security, maintainability and reliability. In addition, it specifies the
design constraints and standards that are needed to be applied on SCM.

**Scope**

This document represents specification of the SCM system requirements.
It serves as the baseline document on which the subsequent software
development life cycle phases are built.

**Definitions, Acronyms and Abbreviations**

  ---------- -------------------------------------------------
  **Term**   **Description**
  SYSTEM     Supply Chain Management Software.
  KFUPM      King Fahad University of Petroleum and Minerals
  SCM        Supply Chain Management
  STD        State Transition Diagram
  SRS        Software Requirements Specification
  ERP        Enterprise Resource Planning
  ---------- -------------------------------------------------

\

**References[ ]{.Apple-converted-space}**

The references of this document are:[ ]{.Apple-converted-space}

SCM[  ]{.Apple-converted-space}TITLE[  ]{.Apple-converted-space}\\\*
MERGEFORMAT vision document v.1.2.

Use Case & STD Documentation[  ]{.Apple-converted-space}v1.5

SCM[  ]{.Apple-converted-space}HYPERLINK
\"http://ce8.kfupm.edu.sa/webct/editAssignmentSubmission.dowebct?actionEvent=viewReadOnly&projectId=6354536001\"
\\o \"View Submission\" [Conceptual Class Model and Sequence
Diagram]{.s4} document v.2.0

SCM Screen layouts document v.1.2.

[ ]{.Apple-converted-space}HYPERLINK
\"javascript:go(2404274001,1451391001)\" [SWE 417-SRS Template-USE]{.s4}

\

**Overview**

This SRS document is organized as flows:[ ]{.Apple-converted-space}

\

[]{.s5} Overall description of SCM which include product perspective,
product functions, SCM's user characteristics, constraints, assumptions
& dependencies and apportioning of requirements.

\

[]{.s5}[  ]{.Apple-converted-space}Specific Requirements which include
, interface requirements, functional requirements,[ 
]{.Apple-converted-space}performance requirements, logical database
requirements, design constraints and software system attributes.

\

[]{.s5}[  ]{.Apple-converted-space}Change management process.

\

**2. Overall Description**

\

\

**2.1 Product Perspective:**

The perspective of[  ]{.Apple-converted-space}product conduct in
delivering Ejada company products like IT products, Business
Consultation and other IT service in fast way and less cost than other
alternative way. There are other well known SCM systems from Oracle and
SAP, they are used in big companies and connecting with other systems
but with the same main functionality that is provided by our SCM. Our
system scope is limited by Ejada and there requests.

\

\

**2.2 Product Functions**

[ ]{.Apple-tab-span}

Ejada SCM will:

Provide a simple Customer service management
process[ ]{.Apple-converted-space}

Determine mutually satisfying goals between organization and
customers[ ]{.Apple-converted-space}

Establish and maintain customer rapport

Produce positive feelings in the organization and the customers

Maintain Procurement process[ ]{.Apple-converted-space}

Manage Product development and
commercialization[ ]{.Apple-converted-space}

Coordinate with customer relationship management to identify
customer-articulated needs

select materials and suppliers in conjunction with
procurement[ ]{.Apple-converted-space}

Develop production technology in manufacturing flow to manufacture and
integrate into the best supply chain flow for the product/market
combination.[ ]{.Apple-converted-space}

Maintain Manufacturing flow management
process[ ]{.Apple-converted-space}

Manage Physical distribution[ ]{.Apple-converted-space}

Maintain Outsourcing and Partnerships[ ]{.Apple-converted-space}

Maintain Measurement Performance[ ]{.Apple-converted-space}

Maintain Cost Performance[ ]{.Apple-converted-space}

Maintain Customer Service Performance

Maintain Productivity measures Performance[ ]{.Apple-converted-space}

Maintain Asset measurement Performance[ ]{.Apple-converted-space}

Maintain Quality Performance

\

\

**2.3 User Characteristics**

\

The users are Ejada's employees, customers and suppliers. It considers
that they have the high school level or higher and they can read and
write in English with basic knowledge of using computer programs.

\

**2.4 Constraints**

\

The system has many constraints. For example, the system must be
web-based and all tools must be compliant with .Net technologies, i.e.,
We must use ASP.NET and C\# as programming language and MS SQL as DBMS.
We are also constrained with Ejada\'s framework and the system will
later be integrated with other two modules in the framework. Ejada has
some programming standards that we must commit to.

\

**2.5 Assumptions & Dependencies**

\

[ ]{.Apple-tab-span}We assume that the server machine of the system has
a suitable Microsoft OS. This machine has a connection to internet.

\

**2.6 Apportioning of Requirements**

\

Our SCM system requires including all requirements prior to the first
delivery.

\

**3. Specific Requirements**

\

**3.1 Interface Requirements**

\

**3.1.1 User Interfaces**

The system is a web base system so, it will interact with its users with
web components interface. The users move through pages containing
activities or direction to some other activities.

The system interface will looks like following:

\

\

\

intro page to the system. Direct link to login page.

\

\

\

Log in page contain 2 text fields and 1 list box : username, password
and domain.

The user should write his/her username, password and select in which
domain he/she is.

Domain list box has 3 choices \[ coordinator, costumer and supplier \].

After the user click send or hit enter button the system will direct the
user to its domain if he/she is in coordinator, costumer or supplier
section.

If username or password is wrong the system will direct the user to an
error page.

\

\

\

if the information provided by the user is wrong this page will appear
to him/her.

User can click on \[ Try again \] link, so he/she can try to log in
again.

\

[]{.s6}[ ]{.s7}**Coordinator section:**

\

\

First page in the coordinator domain.

User can select customer, supplier, requests or items management
section.

User can click on \[ Logout \] link, so that he/she logged out from the
system.

\

\

\

Customer management section in coordinator domain.

This page display the last 5 new customer.

User can click on \[ view detail \] for more information about a
customer.

User can click on \[ view all customers \] link, he/she will directed to
page will full customer list.

User can click on \[ add new customer \] link, to add a new customer to
the system.

Navigation bar under the banner of the system that allow user to
navigate through pages.

User can click on \[ Logout \] link, so that he/she logged out from the
system.

\

\

\

add customer page contain 4 information fields.

After writing all the information, user will click on \[ add \] button
to add the customer to the system.

Navigation bar under the banner of the system that allow user to
navigate through pages.

User can click on \[ Logout \] link, so that he/she logged out from the
system.

\

\

\

when click on \[ view detail \] of some customer. The system will direct
the user to view customer details.

Two link appear above the box, edit and delete link. This will perform
on the current page.

Navigation bar under the banner of the system that allow user to
navigate through pages.

User can click on \[ Logout \] link, so that he/she logged out from the
system.

\

\

page to conform the deletion. User must click on either yes or no.

\

\

\

\

\

\

edit customer page contain 4 information fields.

After editing all the information, user will click on \[ edit \] button
to edit the customer information.

Navigation bar under the banner of the system that allow user to
navigate through pages.

User can click on \[ Logout \] link, so that he/she logged out from the
system.

\

\

\

Items management section in coordinator domain.

This page display the last 5 new Items.

User can click on \[ view detail \] for more information about item.

User can click on \[ view all Items \] link, he/she will directed to
page will full items list.

User can click on \[ add new Items \] link, to add a new item to the
system.

Navigation bar under the banner of the system that allow user to
navigate through pages.

User can click on \[ Logout \] link, so that he/she logged out from the
system.

\

\

\

when click on \[ view detail \] of item. The system will direct the user
to view item details.

Two link appear above the box, edit and delete link. This will perform
on the current page.

Navigation bar under the banner of the system that allow user to
navigate through pages.

User can click on \[ Logout \] link, so that he/she logged out from the
system.

\

\

\

\

edit item page contain 2 information fields.

After editing all the information, user will click on \[ save \] button
to edit the item information.

Navigation bar under the banner of the system that allow user to
navigate through pages.

User can click on \[ Logout \] link, so that he/she logged out from the
system.

\

\

\

Supplier management section in coordinator domain.

This page display the last 5 new supplier.

User can click on \[ view detail \] for more information about a
supplier.

User can click on \[ view all supplier \] link, he/she will directed to
page will full supplier list.

User can click on \[ add new supplier \] link, to add a new supplier to
the system.

Navigation bar under the banner of the system that allow user to
navigate through pages.

User can click on \[ Logout \] link, so that he/she logged out from the
system.

\

\

\

when click on \[ view detail \] of supplier. The system will direct the
user to view supplier details.

Two link appear above the box, edit and delete link. This will perform
on the current page.

Navigation bar under the banner of the system that allow user to
navigate through pages.

User can click on \[ Logout \] link, so that he/she logged out from the
system.

\

\

\

edit supplier page contain 4 information fields.

After editing all the information, user will click on \[ edit \] button
to edit the supplier information.

Navigation bar under the banner of the system that allow user to
navigate through pages.

User can click on \[ Logout \] link, so that he/she logged out from the
system.

\

\

\

Requests management section in coordinator domain.

This page display the last 5 new customer requests and the last 5
requests to suppliers.

User can click on \[ view detail \] for more information about a
requests.

User can click on \[ view all Requests \] link, he/she will directed to
page will full customer list.

User can click on \[ add new Requests \] link, to add a new requests to
the system.

Navigation bar under the banner of the system that allow user to
navigate through pages.

User can click on \[ Logout \] link, so that he/she logged out from the
system.

\

\

when click on \[ view detail \] of request. The system will direct the
user to view request details.

Two link appear above the box, edit and delete link. This will perform
on the current page.

Navigation bar under the banner of the system that allow user to
navigate through pages.

User can click on \[ Logout \] link, so that he/she logged out from the
system.

\

\

\

\

\

edit request page contain 2 information fields.

After editing all the information, user will click on \[ save \] button
to edit the request information.

Navigation bar under the banner of the system that allow user to
navigate through pages.

User can click on \[ Logout \] link, so that he/she logged out from the
system.

\

\

**Customer section:**

\

\

\

The main page in customer domain.

This page display the last 5 new requests.

User can click on \[ view detail \] for more information about request.

User can click on \[ view all requests \] link, he/she will directed to
page will full requests list.

User can click on \[ add new request \] link, to add a new requests to
the system.

User can edit his/her profile, a link \[ edit profile \] there to do so.

Navigation bar under the banner of the system that allow user to
navigate through pages.

User can click on \[ Logout \] link, so that he/she logged out from the
system.

\

\

\

add request page contain 2 information fields.

After writing all the information, user will click on \[ send \] button
to add the request information.

Navigation bar under the banner of the system that allow user to
navigate through pages.

User can click on \[ Logout \] link, so that he/she logged out from the
system.

\

\

\

\

\

\

when click on \[ view detail \] of request. The system will direct the
user to view request details.

Two link appear above the box, edit and delete link. This will perform
on the current page.

Navigation bar under the banner of the system that allow user to
navigate through pages.

User can click on \[ Logout \] link, so that he/she logged out from the
system.

\

\

\

\

\

\

\

edit request page contain 2 information fields.

After editing all the information, user will click on \[ save \] button
to edit the request information.

Navigation bar under the banner of the system that allow user to
navigate through pages.

User can click on \[ Logout \] link, so that he/she logged out from the
system.

\

\

edit customer profile contain 4 information fields.

After editing all the information, user will click on \[ save \] button
to edit the customer profile information.

Navigation bar under the banner of the system that allow user to
navigate through pages.

User can click on \[ Logout \] link, so that he/she logged out from the
system.

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

[[ ]{.Apple-converted-space}]{.s7}**Supplier section:**

\

\

\

The main page in supplier domain.

This page display the last 5 new requests.

User can click on \[ view detail \] for more information about request.

User can click on \[ view all supply requests \] link, he/she will
directed to page will full requests list.

User can edit his/her profile, a link \[ edit profile \] there to do so.

Navigation bar under the banner of the system that allow user to
navigate through pages.

User can click on \[ Logout \] link, so that he/she logged out from the
system.

\

\

\

when click on \[ view detail \] of request. The system will direct the
user to view request details.

Two link appear above the box, edit and delete link. This will perform
on the current page.

The page contain a feedback box, the supplier may send his feedback
about the request.

Navigation bar under the banner of the system that allow user to
navigate through pages.

User can click on \[ Logout \] link, so that he/she logged out from the
system.

\

\

\

\

\

Redirected page after sending the feedback.

\

\

\

\

\

\

edit supplier profile contain 4 information fields.

After editing all the information, user will click on \[ save \] button
to edit the supplier profile information.

Navigation bar under the banner of the system that allow user to
navigate through pages.

User can click on \[ Logout \] link, so that he/she logged out from the
system.

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

**3.1.2 Hardware Interfaces**

\

The system has no hardware interface requirements.

\

**3.1.3 Software Interfaces**

\

+-----------------------------------+-----------------------------------+
| Name                              | SQL-                              |
|                                   | Server[ ]{.Apple-converted-space} |
+-----------------------------------+-----------------------------------+
| Mnemonic                          | SQL-DB                            |
+-----------------------------------+-----------------------------------+
| Specification                     | \                                 |
|                                   |                                   |
| Number                            |                                   |
+-----------------------------------+-----------------------------------+
| Version                           | Version 7.0.1                     |
|                                   |                                   |
| Number                            |                                   |
+-----------------------------------+-----------------------------------+
| Source                            | http://www.microsoft.com/         |
|                                   | sqlserver/2008/en/us/default.aspx |
+-----------------------------------+-----------------------------------+
| Purpose of                        | The system must use SQL server as |
|                                   | its database.                     |
| Interfacing                       |                                   |
+-----------------------------------+-----------------------------------+

\

\

+-----------------------------------+-----------------------------------+
| Name                              | Internet Explorer                 |
+-----------------------------------+-----------------------------------+
| Mnemonic                          | IE                                |
+-----------------------------------+-----------------------------------+
| Specification                     | \                                 |
|                                   |                                   |
| Number                            |                                   |
+-----------------------------------+-----------------------------------+
| Version                           | Version 6 and Version 7           |
|                                   |                                   |
| Number                            |                                   |
+-----------------------------------+-----------------------------------+
| Source                            | h                                 |
|                                   | ttp://www.microsoft.com/windows/p |
|                                   | roducts/winfamily/ie/default.mspx |
+-----------------------------------+-----------------------------------+
| Purpose of                        | The user should use this browser, |
|                                   | so that he can display the system |
| Interfacing                       | and work on it.                   |
+-----------------------------------+-----------------------------------+

\

\

+-----------------------------------+-----------------------------------+
| Name                              | Mozilla                           |
|                                   | f                                 |
|                                   | irefox[ ]{.Apple-converted-space} |
+-----------------------------------+-----------------------------------+
| Mnemonic                          | Firefox                           |
+-----------------------------------+-----------------------------------+
| Specification                     | \                                 |
|                                   |                                   |
| Number                            |                                   |
+-----------------------------------+-----------------------------------+
| Version                           | Version 2 and Version 3           |
|                                   |                                   |
| Number                            |                                   |
+-----------------------------------+-----------------------------------+
| Source                            | http                              |
|                                   | ://www.mozilla.com/en-US/firefox/ |
+-----------------------------------+-----------------------------------+
| Purpose of                        | The user should use this browser, |
|                                   | so that he can display the system |
| Interfacing                       | and work on it.                   |
+-----------------------------------+-----------------------------------+

\

**3.1.4 Communication Interfaces**

\

The SCM system will use TCP/IP as the main communication protocol trough
internet/network.

\

Also, it might communicate with external systems in the future, such as
customer relation management system and HR systems. The scope of our
system does not require to interact with other interfaces but it can be
customized. [ ]{.Apple-converted-space}

[]{.s4}**3.2 Functional Requirements**

\

**3.2.1.1 Manage[  ]{.Apple-converted-space}Requests**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \# 1**     | Manage[               |                       |
|                       | ]{.Apple-converted    |                       |
|                       | -space}Requests[ ]{.A |                       |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | The main requests     |                       |
|                       | management page that  |                       |
|                       | coordinator will      |                       |
|                       | manage all[           |                       |
|                       | ]{.Apple-co           |                       |
|                       | nverted-space}request |                       |
|                       | from customer or to   |                       |
|                       | suppliers             |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company, Summary      |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login                 |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | manage his request    |                       |
|                       | can add ,view or edit |                       |
|                       | his requests          |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | Login in failed       |                       |
| Condition**           |                       |                       |
|                       | There is No suppliers |                       |
|                       | for his               |                       |
|                       | requests[ ]{.A        |                       |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator ,         |                       |
|                       | Supplier, Customer    |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | \                     |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "Manage[              |
|                       |                       | ]{.Apple-conv         |
|                       |                       | erted-space}Requests" |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The coordinator use   |
|                       |                       | any function.         |
+-----------------------+-----------------------+-----------------------+
| \                     | 3                     | The coordinator will  |
|                       |                       | manage all requests   |
|                       |                       | function.[ ]{.A       |
|                       |                       | pple-converted-space} |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | \                     | \"Error!\" message.   |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | Coordinator may use   |
|                       |                       | phone to request from |
|                       |                       | suppliers[ ]{.A       |
|                       |                       | pple-converted-space} |
+-----------------------+-----------------------+-----------------------+

\

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | Manage                            |
|                                   | Re                                |
|                                   | quests[ ]{.Apple-converted-space} |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Top                               |
+-----------------------------------+-----------------------------------+
| **Performance**                   | \                                 |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | \                                 |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | \                                 |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What is the coordinator cannot    |
| IS                                | manage requests?                  |
| SUES[ ]{.Apple-converted-space}** |                                   |
|                                   | What is the coordinator cannot    |
|                                   | use requests functions?           |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | Login                             |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | Add Request , View Requests       |
+-----------------------------------+-----------------------------------+

\

\

\

\

\

\

\

**3.2.2.1 Add Request**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \#2**      | Add Request           |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | Coordinator can add   |                       |
|                       | new request[          |                       |
|                       | ]{.Appl               |                       |
|                       | e-converted-space}and |                       |
|                       | send it to his        |                       |
|                       | supplier              |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login                 |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | add new request.      |                       |
|                       |                       |                       |
|                       | The request sent to   |                       |
|                       | supplier              |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | Login in failed       |                       |
| Condition**           |                       |                       |
|                       | There is No suppliers |                       |
|                       | for his requests or   |                       |
|                       | send                  |                       |
|                       | error[ ]{.A           |                       |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator ,         |                       |
|                       | Supplier              |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the coordinator  |                       |
|                       | needs to add new      |                       |
|                       | request.              |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "Add Request"         |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The coordinator fills |
|                       |                       | the request form.     |
+-----------------------+-----------------------+-----------------------+
| \                     | 3                     | The coordinator will  |
|                       |                       | send the request to   |
|                       |                       | supplier[ ]{.A        |
|                       |                       | pple-converted-space} |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \- \"Error!\"[        |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | Coordinator may use   |
|                       |                       | phone to request from |
|                       |                       | suppliers             |
+-----------------------+-----------------------+-----------------------+

\

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | Add Request                       |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Top                               |
+-----------------------------------+-----------------------------------+
| **Performance**                   | 10 minutes for request, 2 days    |
|                                   | until accept                      |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What is the coordinator cannot    |
| IS                                | add new requests?                 |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | Requests Management               |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | None                              |
+-----------------------------------+-----------------------------------+

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

**3.2.2.2 Sequence Diagram**

\

\

\

**3.2.3.1 View Requests**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \#3**      | View Requests         |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | Coordinator issues    |                       |
|                       | requests ,            |                       |
|                       | coordinator can show  |                       |
|                       | all[                  |                       |
|                       | ]{.Apple-con          |                       |
|                       | verted-space}requests |                       |
|                       | that sent his         |                       |
|                       | supplier or that came |                       |
|                       | from his customer     |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login[ ]{.A           |                       |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | show all requests.    |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | Login in failed       |                       |
| Condition**           |                       |                       |
|                       | The coordinator       |                       |
|                       | cannot view all       |                       |
|                       | requests.             |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator ,         |                       |
|                       | Supplier, Customer    |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the coordinator  |                       |
|                       | needs to view         |                       |
|                       | requests.             |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "View Requests"       |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The coordinator view  |
|                       |                       | list of requests.     |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | Coordinator may want  |
|                       |                       | to see the customers  |
|                       |                       | requests              |
|                       |                       | only[ ]{.A            |
|                       |                       | pple-converted-space} |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | Coordinator may want  |
|                       |                       | to see the requests   |
|                       |                       | that sent to[         |
|                       |                       | ]{.Apple-converted-   |
|                       |                       | space}suppliers[ ]{.A |
|                       |                       | pple-converted-space} |
+-----------------------+-----------------------+-----------------------+

\

\

\

\

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | View Requests                     |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Top                               |
+-----------------------------------+-----------------------------------+
| **Performance**                   | [ ]{.Apple-converted-space}10     |
|                                   | seconds to show the list          |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What is the coordinator cannot    |
| IS                                | view requests?                    |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | Manage                            |
|                                   | Re                                |
|                                   | quests[ ]{.Apple-converted-space} |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | View Request Details              |
+-----------------------------------+-----------------------------------+

\

**3.2.3.2 Sequence Diagram**

\

**3.2.4.1 View Request Details**

+-----------------------+-----------------------+-----------------------+
| **USE CASE \#4**      | View Request Details  |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | Coordinator can show  |                       |
|                       | the details of any    |                       |
|                       | request that he       |                       |
|                       | chose.                |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login                 |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | show the details of a |                       |
|                       | request.              |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | The coordinator       |                       |
| Condition**           | cannot show the       |                       |
|                       | details of a request. |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator ,         |                       |
|                       | Supplier, Customer    |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the coordinator  |                       |
|                       | need to view the      |                       |
|                       | details of a request. |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "View Request         |
|                       |                       | Details"              |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The coordinator views |
|                       |                       | the details of a      |
|                       |                       | request.              |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | \                     | \                     |
+-----------------------+-----------------------+-----------------------+

\

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | View Request Details              |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Middle                            |
+-----------------------------------+-----------------------------------+
| **Performance**                   | [ ]{.Apple-converted-space}10     |
|                                   | seconds to show the details of a  |
|                                   | request.                          |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What is the coordinator cannot    |
| IS                                | view the details of a request?    |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | View Requests                     |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | Delete Request, Edit Request      |
+-----------------------------------+-----------------------------------+

\

\

**3.2.1.2 Sequence Diagram**

\

\

\

\

**3.2.5.1 Edit Request**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \# 5**     | Edit Request          |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | The Coordinator can   |                       |
|                       | edit[                 |                       |
|                       | ]{.Apple-co           |                       |
|                       | nverted-space}request |                       |
|                       | and notify his        |                       |
|                       | supplier              |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login[ ]{.A           |                       |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | edit exist request.   |                       |
|                       |                       |                       |
|                       | The notification will |                       |
|                       | send to supplier.     |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | Login in failed       |                       |
| Condition**           |                       |                       |
|                       | The coordinator       |                       |
|                       | cannot edit exist     |                       |
|                       | request.              |                       |
|                       |                       |                       |
|                       | The notification      |                       |
|                       | cannot send to        |                       |
|                       | supplier.             |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator ,         |                       |
|                       | Suppliers             |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the coordinator  |                       |
|                       | needs to edit any     |                       |
|                       | exist request.        |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "Edit Request"        |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The coordinator       |
|                       |                       | modifies the request  |
|                       |                       | information.          |
+-----------------------+-----------------------+-----------------------+
| \                     | 3                     | The coordinator will  |
|                       |                       | send a notification   |
|                       |                       | to                    |
|                       |                       | supplier[ ]{.A        |
|                       |                       | pple-converted-space} |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | Coordinator may use   |
|                       |                       | phone to request from |
|                       |                       | suppliers             |
+-----------------------+-----------------------+-----------------------+

\

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | Edit Request                      |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Top                               |
+-----------------------------------+-----------------------------------+
| **Performance**                   | 10 minutes for edit, on time      |
|                                   | change                            |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What is the coordinator cannot    |
| IS                                | edit any request?                 |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | View Request Details              |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | None                              |
+-----------------------------------+-----------------------------------+

\

**3.2.5.2 Sequence Diagram**

\

\

\

\

\

\

\

\

\

**3.2.6.1 Delete Request**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \#6**      | Delete Request        |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | The Coordinator can   |                       |
|                       | delete[               |                       |
|                       | ]{.Apple-co           |                       |
|                       | nverted-space}request |                       |
|                       | and notify his        |                       |
|                       | supplier              |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login                 |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | delete exist request. |                       |
|                       |                       |                       |
|                       | The notification will |                       |
|                       | send to supplier.     |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | Login in failed       |                       |
| Condition**           |                       |                       |
|                       | The coordinator       |                       |
|                       | cannot delete exist   |                       |
|                       | request.              |                       |
|                       |                       |                       |
|                       | The notification      |                       |
|                       | cannot send to        |                       |
|                       | supplier.             |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator ,         |                       |
|                       | Suppliers             |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the coordinator  |                       |
|                       | needs to delete any   |                       |
|                       | exist request.        |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "Delete Request"      |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The information about |
|                       |                       | the request will      |
|                       |                       | show.                 |
+-----------------------+-----------------------+-----------------------+
| \                     | 3                     | Press "Delete" to     |
|                       |                       | processing the        |
|                       |                       | deleting              |
+-----------------------+-----------------------+-----------------------+
| \                     | 4                     | The coordinator will  |
|                       |                       | send a notification   |
|                       |                       | to supplier           |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | Coordinator may use   |
|                       |                       | phone to delete the[  |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}request |
|                       |                       | from suppliers        |
+-----------------------+-----------------------+-----------------------+

\

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | Delete Request                    |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | \                                 |
+-----------------------------------+-----------------------------------+
| **Performance**                   | 1 minute for delete               |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What is the coordinator cannot    |
| IS                                | delete requests?                  |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | View Request Details              |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | None                              |
+-----------------------------------+-----------------------------------+

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

**3.2.6.2 Sequence Diagram**

\

\

\

**3.2.7.1 Manage Items**

\

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \# 7**     | Manage                |                       |
|                       | Items[ ]{.A           |                       |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | The main items        |                       |
|                       | management page that  |                       |
|                       | coordinator will      |                       |
|                       | manage the items that |                       |
|                       | he have and may       |                       |
|                       | supply to customer    |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company, Summary      |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login                 |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | manage his items can  |                       |
|                       | add ,view or edit his |                       |
|                       | items                 |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | Login in failed       |                       |
| Condition**           |                       |                       |
|                       | There is No items to  |                       |
|                       | manage or supply      |                       |
|                       | it[ ]{.A              |                       |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator ,         |                       |
|                       | Supplier, Customer    |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | \                     |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "Manage Items"        |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The coordinator use   |
|                       |                       | any function.         |
+-----------------------+-----------------------+-----------------------+
| \                     | 3                     | The coordinator will  |
|                       |                       | manage all items      |
|                       |                       | function.[ ]{.A       |
|                       |                       | pple-converted-space} |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | Coordinator may use   |
|                       |                       | some different items  |
+-----------------------+-----------------------+-----------------------+

\

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | Manage Items                      |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Top                               |
+-----------------------------------+-----------------------------------+
| **Performance**                   | 5 second to show items functions  |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | \                                 |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | Not yet determine                 |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What is the coordinator cannot    |
| IS                                | manage items?                     |
| SUES[ ]{.Apple-converted-space}** |                                   |
|                                   | What is the coordinator cannot    |
|                                   | use items functions?              |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | Login                             |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | Add Item , View Items             |
+-----------------------------------+-----------------------------------+

\

\

\

**3.2.8.1 Add Item**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE\#          | Add Item              |                       |
| 8[ ]{.App             |                       |                       |
| le-converted-space}** |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | Coordinator can add   |                       |
|                       | new items[            |                       |
|                       | ]{.Appl               |                       |
|                       | e-converted-space}and |                       |
|                       | may supply it to our  |                       |
|                       | customer[ ]{.A        |                       |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login                 |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | add new item          |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | The coordinator       |                       |
| Condition**           | cannot add new item   |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator ,         |                       |
|                       | Supplier ,Customer    |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the coordinator  |                       |
|                       | needs to add new      |                       |
|                       | item.                 |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "Add Item"            |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The coordinator fills |
|                       |                       | the item form.        |
+-----------------------+-----------------------+-----------------------+
| \                     | 3                     | The coordinator will  |
|                       |                       | save the item.        |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | \                     | \                     |
+-----------------------+-----------------------+-----------------------+

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | Add Item                          |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Top                               |
+-----------------------------------+-----------------------------------+
| **Performance**                   | 10 minutes for add item           |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What is the coordinator cannot    |
| IS                                | add new items?                    |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | Manage Items                      |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | None                              |
+-----------------------------------+-----------------------------------+

\

\

**3.2.8.2 Sequence Diagram**

\

\

\

**3.2.9.1 View Items**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \#         | View Items            |                       |
| 9[ ]{.App             |                       |                       |
| le-converted-space}** |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | The coordinator can   |                       |
|                       | view all[             |                       |
|                       | ]{.Apple-             |                       |
|                       | converted-space}items |                       |
|                       | that he have ,that    |                       |
|                       | may receive from      |                       |
|                       | supplier and may      |                       |
|                       | supply it for his     |                       |
|                       | customers             |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login                 |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | view all Items.       |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | Login in failed       |                       |
| Condition**           |                       |                       |
|                       | The coordinator       |                       |
|                       | cannot view all       |                       |
|                       | Items.                |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator ,         |                       |
|                       | Supplier, Customer    |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the coordinator  |                       |
|                       | needs to view all     |                       |
|                       | Items.                |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "View Items"          |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The coordinator view  |
|                       |                       | list of Items         |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | Coordinator may want  |
|                       |                       | to see the Items      |
|                       |                       | category              |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | Coordinator may want  |
|                       |                       | to see the Items that |
|                       |                       | sent to customers     |
+-----------------------+-----------------------+-----------------------+

\

\

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | View Items                        |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Top                               |
+-----------------------------------+-----------------------------------+
| **Performance**                   | [ ]{.Apple-converted-space}10     |
|                                   | seconds to show the list          |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What is the coordinator cannot    |
| IS                                | view items?                       |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | Manage[                           |
|                                   | ]{.Apple-converted-space}Items    |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | View Item Details                 |
+-----------------------------------+-----------------------------------+

\

**3.2.9.2 Sequence Diagram**

\

\

**3.2.10.1 View Item Details**

+-----------------------+-----------------------+-----------------------+
| **USE CASE \# 10**    | View Item Details     |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | Coordinator can show  |                       |
|                       | the details of any    |                       |
|                       | items that he         |                       |
|                       | chooses.              |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login[ ]{.A           |                       |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | show the details of   |                       |
|                       | an item.              |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | The coordinator       |                       |
| Condition**           | cannot show the       |                       |
|                       | details of an item.   |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator ,         |                       |
|                       | Supplier, Customer    |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the coordinator  |                       |
|                       | need to view the      |                       |
|                       | details of an item.   |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "View Item Details"   |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The coordinator views |
|                       |                       | the details of an     |
|                       |                       | item.                 |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | \                     | \                     |
+-----------------------+-----------------------+-----------------------+

\

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | View Item Details                 |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | middle                            |
+-----------------------------------+-----------------------------------+
| **Performance**                   | [ ]{.Apple-converted-space}10     |
|                                   | seconds to show the details of an |
|                                   | item.                             |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What is the coordinator cannot    |
| IS                                | view the details of an item?      |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | View Items                        |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | Delete Item, Edit Item            |
+-----------------------------------+-----------------------------------+

\

**3.2.10.2 Sequence Diagram**

\

\

\

**3.2.11.1 Edit Item**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \# 11**    | Edit Item.            |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | The Coordinator can   |                       |
|                       | edit item that he     |                       |
|                       | want.                 |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login[ ]{.A           |                       |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | edit exist item.      |                       |
|                       |                       |                       |
|                       | The notification will |                       |
|                       | send to supplier and  |                       |
|                       | customer if need.     |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | Login in failed       |                       |
| Condition**           |                       |                       |
|                       | The coordinator       |                       |
|                       | cannot edit exist     |                       |
|                       | item.                 |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator ,         |                       |
|                       | Supplier, Customer    |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the coordinator  |                       |
|                       | needs to edit any     |                       |
|                       | exist item.           |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "Edit Item"           |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The coordinator       |
|                       |                       | modifies the item     |
|                       |                       | information.          |
+-----------------------+-----------------------+-----------------------+
| \                     | 3                     | The coordinator will  |
|                       |                       | send a notification   |
|                       |                       | to supplier or        |
|                       |                       | customer if           |
|                       |                       | need.[ ]{.A           |
|                       |                       | pple-converted-space} |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | \                     | \                     |
+-----------------------+-----------------------+-----------------------+

\

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | Edit Item                         |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Top                               |
+-----------------------------------+-----------------------------------+
| **Performance**                   | 10 minutes for edit, on time      |
|                                   | change                            |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What is the coordinator cannot    |
| IS                                | edit any request?                 |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | View Items Details                |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | None                              |
+-----------------------------------+-----------------------------------+

\

**3.2.11.2 Sequence Diagram**

\

\

**3.2.12.1 Delete Item**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \# 12**    | Delete Item           |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | The Coordinator can   |                       |
|                       | delete any item from  |                       |
|                       | his list and his      |                       |
|                       | supply.               |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login[ ]{.A           |                       |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | delete exist item.    |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | Login in failed       |                       |
| Condition**           |                       |                       |
|                       | The coordinator       |                       |
|                       | cannot delete exist   |                       |
|                       | item.                 |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator.          |                       |
|                       |                       |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the coordinator  |                       |
|                       | needs to delete any   |                       |
|                       | exist item.           |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "Delete Item"         |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The information about |
|                       |                       | the item will show.   |
+-----------------------+-----------------------+-----------------------+
| \                     | 3                     | Press "Delete" to     |
|                       |                       | processing the        |
|                       |                       | deleting              |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | \                     | \                     |
+-----------------------+-----------------------+-----------------------+

\

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | Delete Item                       |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | \                                 |
+-----------------------------------+-----------------------------------+
| **Performance**                   | 1 minute for delete               |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What is the coordinator cannot    |
| IS                                | delete an item?                   |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | View Item Details                 |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | None                              |
+-----------------------------------+-----------------------------------+

\

\

**3.2.12.2 Sequence Diagram**

\

\

\

\

**3.2.13.1 Manage Resources Locations**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \# 13**    | Manage Resources      |                       |
|                       | Locations             |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | The main resources    |                       |
|                       | locations management  |                       |
|                       | page that coordinator |                       |
|                       | will manage the       |                       |
|                       | resources locations   |                       |
|                       | that he have and may  |                       |
|                       | use it to store or    |                       |
|                       | supplying.            |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company, Summary      |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login                 |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | manage his resources  |                       |
|                       | locations can add,    |                       |
|                       | view or edit his      |                       |
|                       | resources locations.  |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | Login in failed       |                       |
| Condition**           |                       |                       |
|                       | There is No resources |                       |
|                       | locations to manage   |                       |
|                       | or supply from it     |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator[ ]{.A     |                       |
|                       | pple-converted-space} |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | \                     |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "Manage Resources     |
|                       |                       | Locations"            |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The coordinator use   |
|                       |                       | any function.         |
+-----------------------+-----------------------+-----------------------+
| \                     | 3                     | The coordinator will  |
|                       |                       | manage all resources  |
|                       |                       | locations             |
|                       |                       | function.[ ]{.A       |
|                       |                       | pple-converted-space} |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | Coordinator may use   |
|                       |                       | some different        |
|                       |                       | locations             |
+-----------------------+-----------------------+-----------------------+

\

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | Manage Resources Locations        |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Top                               |
+-----------------------------------+-----------------------------------+
| **Performance**                   | 5 second to show resources        |
|                                   | locations functions               |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | \                                 |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | Not yet determine                 |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What is the coordinator cannot    |
| IS                                | manage resources locations?       |
| SUES[ ]{.Apple-converted-space}** |                                   |
|                                   | What is the coordinator cannot    |
|                                   | use resources locations           |
|                                   | functions?                        |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | Login                             |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | Add Location , View Locations     |
+-----------------------------------+-----------------------------------+

\

\

\

\

**3.2.14.1 Add Location**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \# 14**    | Add Location          |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | Coordinator can add   |                       |
|                       | new resources         |                       |
|                       | locations and may     |                       |
|                       | start to use it in    |                       |
|                       | our supply and        |                       |
|                       | storing.              |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login.[ ]{.A          |                       |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | add new resource      |                       |
|                       | location.             |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | The coordinator       |                       |
| Condition**           | cannot add new        |                       |
|                       | resource location.    |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator[ ]{.A     |                       |
|                       | pple-converted-space} |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the coordinator  |                       |
|                       | needs to add new      |                       |
|                       | resource location.    |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "Add Location"        |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The coordinator fills |
|                       |                       | the location form.    |
+-----------------------+-----------------------+-----------------------+
| \                     | 3                     | The coordinator will  |
|                       |                       | save the location.    |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | \                     | May add nearest       |
|                       |                       | resources locations.  |
+-----------------------+-----------------------+-----------------------+

\

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | Add Location                      |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Top                               |
+-----------------------------------+-----------------------------------+
| **Performance**                   | 10 minutes for add location       |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What is the coordinator cannot    |
| IS                                | add new locations?                |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | Manage[                           |
|                                   | ]                                 |
|                                   | {.Apple-converted-space}Resources |
|                                   | Locations                         |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | None                              |
+-----------------------------------+-----------------------------------+

\

\

\

\

\

\

\

\

**3.2.14.2 Sequence Diagram**

\

\

\

**3.2.15.1 View Locations**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \# 15**    | View Locations        |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | The coordinator can   |                       |
|                       | view all resources    |                       |
|                       | locations that he     |                       |
|                       | have, that use to     |                       |
|                       | supplying our         |                       |
|                       | customer and store    |                       |
|                       | our items.            |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login[ ]{.A           |                       |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | view all resources    |                       |
|                       | locations.            |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | Login in failed       |                       |
| Condition**           |                       |                       |
|                       | The coordinator       |                       |
|                       | cannot view all       |                       |
|                       | resources locations.  |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator[ ]{.A     |                       |
|                       | pple-converted-space} |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the coordinator  |                       |
|                       | needs to view all     |                       |
|                       | locations.            |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "View Locations".     |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The coordinator view  |
|                       |                       | list of Locations.    |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | Coordinator may want  |
|                       |                       | to see the Locations  |
|                       |                       | category              |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | Coordinator may want  |
|                       |                       | to see the Locations  |
|                       |                       | that nearest to our   |
|                       |                       | customer.             |
+-----------------------+-----------------------+-----------------------+

\

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | View Locations                    |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Top                               |
+-----------------------------------+-----------------------------------+
| **Performance**                   | [ ]{.Apple-converted-space}10     |
|                                   | seconds to show the list          |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What is the coordinator cannot    |
| IS                                | view locations?                   |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | Manage Resources                  |
|                                   | Loc                               |
|                                   | ations[ ]{.Apple-converted-space} |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | View Locations Details            |
+-----------------------------------+-----------------------------------+

\

**3.2.15.2 Sequence Diagram**

\

\

\

**3.2.16.1 View Location Details**

+-----------------------+-----------------------+-----------------------+
| **USE CASE \# 16**    | View Location Details |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | Coordinator can show  |                       |
|                       | the details of        |                       |
|                       | resource location     |                       |
|                       | that he chooses.      |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login.                |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | show the details of a |                       |
|                       | location.             |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | The coordinator       |                       |
| Condition**           | cannot show the       |                       |
|                       | details of a          |                       |
|                       | location.             |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator[ ]{.A     |                       |
|                       | pple-converted-space} |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the coordinator  |                       |
|                       | need to view the      |                       |
|                       | details of a          |                       |
|                       | location.             |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "View Location        |
|                       |                       | Details"              |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The coordinator views |
|                       |                       | the details of a      |
|                       |                       | location.             |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | \                     | \                     |
+-----------------------+-----------------------+-----------------------+

\

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | View Location Details             |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | middle                            |
+-----------------------------------+-----------------------------------+
| **Performance**                   | [ ]{.Apple-converted-space}10     |
|                                   | seconds to show the details of a  |
|                                   | location.                         |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What is the coordinator cannot    |
| IS                                | view the details of a location?   |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | View Locations                    |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | Delete Locations, Edit Location   |
+-----------------------------------+-----------------------------------+

\

**3.2.16.2 Sequence Diagram**

\

\

\

**3.2.17.1 Edit Location**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \#         | Edit Location.        |                       |
| 17[ ]{.App            |                       |                       |
| le-converted-space}** |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | The Coordinator can   |                       |
|                       | edit a location that  |                       |
|                       | he wants.             |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login[ ]{.A           |                       |
|                       | pple-converted-space} |                       |
|                       |                       |                       |
|                       | -The coordinator      |                       |
|                       | press "Edit Location" |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | edit exist location.  |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | Login in failed       |                       |
| Condition**           |                       |                       |
|                       | The coordinator       |                       |
|                       | cannot edit exist     |                       |
|                       | location.             |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator[ ]{.A     |                       |
|                       | pple-converted-space} |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the coordinator  |                       |
|                       | needs to edit any     |                       |
|                       | exist location.       |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "Edit Location"       |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The coordinator       |
|                       |                       | modifies the location |
|                       |                       | information.          |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | \                     | \                     |
+-----------------------+-----------------------+-----------------------+

\

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | Edit Location                     |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Top                               |
+-----------------------------------+-----------------------------------+
| **Performance**                   | 10 minutes for edit, on time      |
|                                   | change                            |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What is the coordinator cannot    |
| IS                                | edit any location?                |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | View Locations Details            |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | None                              |
+-----------------------------------+-----------------------------------+

\

**3.2.17.2 Sequence Diagram**

\

\

\

**3.2.18.1 Delete Location**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \#         | Delete Location       |                       |
| 18[ ]{.App            |                       |                       |
| le-converted-space}** |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | The Coordinator can   |                       |
|                       | delete any location   |                       |
|                       | from his list.        |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login                 |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | delete exist          |                       |
|                       | location.             |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | Login in failed       |                       |
| Condition**           |                       |                       |
|                       | The coordinator       |                       |
|                       | cannot delete exist   |                       |
|                       | location.             |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator.          |                       |
|                       |                       |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the coordinator  |                       |
|                       | needs to delete any   |                       |
|                       | exist location.       |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "Delete Location"     |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The information about |
|                       |                       | the location will     |
|                       |                       | show.                 |
+-----------------------+-----------------------+-----------------------+
| \                     | 3                     | Press "Delete" to     |
|                       |                       | processing the        |
|                       |                       | deleting              |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | \                     | \                     |
+-----------------------+-----------------------+-----------------------+

\

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | Delete Location                   |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | \                                 |
+-----------------------------------+-----------------------------------+
| **Performance**                   | 1 minute for delete               |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What is the coordinator cannot    |
| IS                                | delete a location?                |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | View Location Details             |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | None                              |
+-----------------------------------+-----------------------------------+

\

**3.2.18.2 Sequence Diagram**

\

\

\

\

\

\

**3.2.19.1 Edit Profile**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \# 19**    | Edit Profile          |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | The supplier can edit |                       |
|                       | his profile. The      |                       |
|                       | profile contains the  |                       |
|                       | name of the supplier, |                       |
|                       | the address, contact  |                       |
|                       | person and e-mail...  |                       |
|                       | etc.                  |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Primary Task          |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | The actor has logged  |                       |
|                       | in.                   |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The supplier profile  |                       |
| Condition**           | is updated to the     |                       |
|                       | newly entered values. |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | The older profile     |                       |
| Condition**           | remains as is. An     |                       |
|                       | error message is      |                       |
|                       | generated.            |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Primary: Supplier     |                       |
|                       |                       |                       |
| **[ ]{.Apple-conv     | Secondary:            |                       |
| erted-space}Secondary | Coordinator (by use   |                       |
| Actors**              | case Edit Supplier)   |                       |
|                       |                       |                       |
|                       | \                     |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | Clicking on the       |                       |
|                       | proper link for       |                       |
|                       | editing the profile.  |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | He clicks on the      |
|                       |                       | proper link to edit   |
|                       |                       | his profile.          |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | Whether he make       |
|                       |                       | changes or not, when  |
|                       |                       | he clicks on the      |
|                       |                       | proper link to submit |
|                       |                       | the profile values,   |
|                       |                       | the current values of |
|                       |                       | the profile is saved  |
|                       |                       | and he is returned to |
|                       |                       | the main menu.        |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | Invalid input         |
|                       |                       | :[ ]{.A               |
|                       |                       | pple-converted-space} |
|                       |                       |                       |
|                       |                       | Generating error      |
|                       |                       | message and discard   |
|                       |                       | changes.              |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | \                     | none                  |
+-----------------------+-----------------------+-----------------------+

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | Edit Profile                      |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Critical (some functions depend   |
|                                   | on successfulness of this UC)     |
+-----------------------------------+-----------------------------------+
| **Performance**                   | Must not exceed 1 sec to save the |
|                                   | new input values.                 |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | Once every 2-3 months.            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | Database.                         |
+-----------------------------------+-----------------------------------+
| **OPEN                            | \                                 |
| IS                                |                                   |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | \                                 |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | \                                 |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | \                                 |
+-----------------------------------+-----------------------------------+

\

**3.2.19.2 Sequence Diagram**

\

\

\

**3.2.20.1 View Supply Requests**

+-----------------------+-----------------------+-----------------------+
| **USE CASE \# 20**    | View Supply Requests  |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | To show a list of     |                       |
|                       | pending               |                       |
|                       | requests.[ ]{.A       |                       |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Primary Task          |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | The actor has logged  |                       |
|                       | in.                   |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The list of pending   |                       |
| Condition**           | requests is rendered. |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | An error message is   |                       |
| Condition**           | generated.            |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Primary: Supplier     |                       |
|                       |                       |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | Clicking on the       |                       |
|                       | proper link for       |                       |
|                       | viewing the supply    |                       |
|                       | requests.             |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | \                     | \                     |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | He clicks on the      |
|                       |                       | proper link to view   |
|                       |                       | supply requests.      |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | A list of pending     |
|                       |                       | requests is listed.   |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | If there is no        |
|                       |                       | requests              |
|                       |                       | :[ ]{.A               |
|                       |                       | pple-converted-space} |
|                       |                       |                       |
|                       |                       | A message is          |
|                       |                       | displayed stating     |
|                       |                       | that there is no      |
|                       |                       | requests.             |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | \                     | \                     |
+-----------------------+-----------------------+-----------------------+

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | View Supply Requests              |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Critical                          |
+-----------------------------------+-----------------------------------+
| **Performance**                   | Less than 1 second                |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | Usually every time the supplier   |
|                                   | logins to the system. Almost      |
|                                   | daily.                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | Database                          |
+-----------------------------------+-----------------------------------+
| **OPEN                            | \                                 |
| IS                                |                                   |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | \                                 |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | \                                 |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | \                                 |
+-----------------------------------+-----------------------------------+

\

**3.2.20.2 Sequence Diagram**

\

\

\

\

**3.2.21.1 View Request Details**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \#21**     | View Request Details  |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | To view extended      |                       |
|                       | details of the chosen |                       |
|                       | request.              |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Primary Task          |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | The actor has logged  |                       |
|                       | in.                   |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | Details of the chosen |                       |
| Condition**           | request are           |                       |
|                       | displayed.            |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | An error message is   |                       |
| Condition**           | generated.            |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Primary:              |                       |
|                       | Supplier[ ]{.A        |                       |
| **[ ]{.Apple-conv     | pple-converted-space} |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | Clicking on the       |                       |
|                       | proper link on a      |                       |
|                       | certain displayed     |                       |
|                       | request to show its   |                       |
|                       | full details.         |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | \                     | \                     |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | He clicks on the      |
|                       |                       | proper link to view   |
|                       |                       | supply requests.      |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | A list of pending     |
|                       |                       | requests is listed.   |
+-----------------------+-----------------------+-----------------------+
| \                     | 3                     | He clicks on the      |
|                       |                       | proper link on a      |
|                       |                       | request to display    |
|                       |                       | its details.          |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | \                     |
+-----------------------+-----------------------+-----------------------+

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | View Request Details              |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Critical                          |
+-----------------------------------+-----------------------------------+
| **Performance**                   | Less than 1 second.               |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | Usually every time the supplier   |
|                                   | logins to the system. Almost      |
|                                   | daily.                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | Database                          |
+-----------------------------------+-----------------------------------+
| **OPEN                            | \                                 |
| IS                                |                                   |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | \                                 |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | \                                 |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | Send Feedback on Request          |
+-----------------------------------+-----------------------------------+

\

**3.2.21.2 Sequence Diagram**

\

\

\

\

\

**3.2.22.1 Send Feedback on Request**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \#22**     | Send Feedback on      |                       |
|                       | Request               |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | The supplier states   |                       |
|                       | whether he can supply |                       |
|                       | all the requested     |                       |
|                       | items or part of them |                       |
|                       | and the time frame to |                       |
|                       | deliver               |                       |
|                       | them.[ ]{.A           |                       |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Primary Task          |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | The actor has logged  |                       |
|                       | in.                   |                       |
|                       |                       |                       |
|                       | The actor views a     |                       |
|                       | certain request       |                       |
|                       | details.              |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | A message indicating  |                       |
| Condition**           | successful submission |                       |
|                       | is generated.         |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | An error message is   |                       |
| Condition**           | generated.            |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Primary:              |                       |
|                       | Supplier[ ]{.A        |                       |
| **[ ]{.Apple-conv     | pple-converted-space} |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | Clicking on the       |                       |
|                       | proper link on a      |                       |
|                       | certain displayed     |                       |
|                       | request to show its   |                       |
|                       | full details.         |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | \                     | \                     |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | He input his feedback |
|                       |                       | and submits.          |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | A success (or error)  |
|                       |                       | message is displayed. |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-con          |
|                       |                       | verted-space}message. |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | \                     |
+-----------------------+-----------------------+-----------------------+

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | Send Feedback on Request          |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Critical                          |
+-----------------------------------+-----------------------------------+
| **Performance**                   | Less than 1 second.               |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | Usually every time the supplier   |
|                                   | logins to the system and at least |
|                                   | one request exists. Almost daily. |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | Database                          |
+-----------------------------------+-----------------------------------+
| **OPEN                            | \                                 |
| IS                                |                                   |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | \                                 |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | \                                 |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | \                                 |
+-----------------------------------+-----------------------------------+

\

**3.2.21.2 Sequence Diagram**

\

\

**3.2.23.1 Edit Profile**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \# 23**    | Edit Profile          |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | The customer can edit |                       |
|                       | his profile. The      |                       |
|                       | profile contains the  |                       |
|                       | name of the customer, |                       |
|                       | his address, contact  |                       |
|                       | person and e-mail...  |                       |
|                       | etc.                  |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Primary Task          |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | The actor has logged  |                       |
|                       | in.                   |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The customer profile  |                       |
| Condition**           | is updated to the     |                       |
|                       | newly entered values. |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | The older profile     |                       |
| Condition**           | remains as is. An     |                       |
|                       | error message is      |                       |
|                       | generated.            |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Primary: Customer     |                       |
|                       |                       |                       |
| **[ ]{.Apple-conv     | Secondary:            |                       |
| erted-space}Secondary | Coordinator (by use   |                       |
| Actors**              | case Edit Customer)   |                       |
|                       |                       |                       |
|                       | \                     |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | Clicking on the       |                       |
|                       | proper link for       |                       |
|                       | editing the profile.  |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | \                     | \                     |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | He clicks on the      |
|                       |                       | proper link to edit   |
|                       |                       | his profile.          |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | Whether he makes      |
|                       |                       | changes or not, when  |
|                       |                       | he clicks on the      |
|                       |                       | proper link to submit |
|                       |                       | the profile values,   |
|                       |                       | the current values of |
|                       |                       | the profile is saved  |
|                       |                       | and he is returned to |
|                       |                       | the main menu.        |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | Invalid input         |
|                       |                       | :[ ]{.A               |
|                       |                       | pple-converted-space} |
|                       |                       |                       |
|                       |                       | Generating error      |
|                       |                       | message and discard   |
|                       |                       | changes.              |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | \                     | none                  |
+-----------------------+-----------------------+-----------------------+

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | Edit Profile                      |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Critical (some functions depend   |
|                                   | on successfulness of this UC)     |
+-----------------------------------+-----------------------------------+
| **Performance**                   | Must not exceed 1 sec to save the |
|                                   | new input values.                 |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | Once every 2-3 months.            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | Database.                         |
+-----------------------------------+-----------------------------------+
| **OPEN                            | \                                 |
| IS                                |                                   |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | \                                 |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | \                                 |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | \                                 |
+-----------------------------------+-----------------------------------+

\

**3.2.23.2 Sequence Diagram**

\

\

**3.2.24.1 Add Request**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \#24**     | Add Request           |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | Customer can add new  |                       |
|                       | request.              |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -The Customer has     |                       |
|                       | logged in.            |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | A new request is      |                       |
| Condition**           | added.                |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | An error message is   |                       |
| Condition**           | generated and the     |                       |
|                       | request is discarded. |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Customer ,            |                       |
|                       | Coordinator           |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the Customer     |                       |
|                       | clicks on the proper  |                       |
|                       | link for adding a     |                       |
|                       | request.              |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The Customer press    |
|                       |                       | "Add Request"         |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The Customer fills    |
|                       |                       | the request form.     |
+-----------------------+-----------------------+-----------------------+
| \                     | 3                     | The Customer will     |
|                       |                       | send the request to   |
|                       |                       | the Coordinator.      |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | Customer may use      |
|                       |                       | phone to request from |
|                       |                       | Coordinator. The      |
|                       |                       | Coordinator, then,    |
|                       |                       | adds the request      |
|                       |                       | manually.             |
+-----------------------+-----------------------+-----------------------+

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | Add Request                       |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Top                               |
+-----------------------------------+-----------------------------------+
| **Performance**                   | 10 minutes for request, 2 days    |
|                                   | until accept                      |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What if the Customer cannot add   |
| IS                                | new requests?                     |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | Requests Management               |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | None                              |
+-----------------------------------+-----------------------------------+

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

\

\

**3.2.24.2 Sequence Diagram**

\

\

**3.2.25.1 View Requests**

+-----------------------+-----------------------+-----------------------+
| **USE CASE \#25**     | View Requests         |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | Customer can view all |                       |
|                       | his pending requests  |                       |
|                       | that were sent to the |                       |
|                       | Coordinator.          |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -The Customer has     |                       |
|                       | logged in.            |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The Customer views    |                       |
| Condition**           | all requests.         |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | An error message is   |                       |
| Condition**           | generated and the     |                       |
|                       | request is discarded. |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Customer,             |                       |
|                       | Coordinator.          |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the Customer     |                       |
|                       | clicks on the proper  |                       |
|                       | link for adding a     |                       |
|                       | request.              |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The Customer press    |
|                       |                       | "View Requests"       |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The Customer view     |
|                       |                       | list of requests.     |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | Customer may want to  |
|                       |                       | refine viewed request |
|                       |                       | on certain criteria.  |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | Customer may want to  |
|                       |                       | see some older        |
|                       |                       | requests.             |
+-----------------------+-----------------------+-----------------------+

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | View Requests                     |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Top                               |
+-----------------------------------+-----------------------------------+
| **Performance**                   | [ ]{.Apple-converted-space}3      |
|                                   | seconds to show the list          |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What is the coordinator cannot    |
| IS                                | view requests?                    |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | Manage                            |
|                                   | Re                                |
|                                   | quests[ ]{.Apple-converted-space} |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | Delete Request                    |
|                                   |                                   |
|                                   | Edit Request                      |
+-----------------------------------+-----------------------------------+

\

**3.2.25.2 Sequence Diagram**

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

**3.2.27.1 Edit Request**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \# 27**    | Edit Request          |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | The Customer can      |                       |
|                       | edit[                 |                       |
|                       | ]{.Apple-co           |                       |
|                       | nverted-space}request |                       |
|                       | and notify the        |                       |
|                       | Coordinator.          |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -The Customer has     |                       |
|                       | logged in.            |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The chosen request is |                       |
| Condition**           | edited.               |                       |
|                       |                       |                       |
|                       | The notification will |                       |
|                       | send to the           |                       |
|                       | coordinator.          |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | An error message is   |                       |
| Condition**           | generated and the     |                       |
|                       | request is discarded. |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Customer, Coordinator |                       |
|                       |                       |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the Customer     |                       |
|                       | clicks on the proper  |                       |
|                       | link for editing a    |                       |
|                       | request.              |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The Customer press    |
|                       |                       | "Edit Request"        |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The Customer modifies |
|                       |                       | the request           |
|                       |                       | information.          |
+-----------------------+-----------------------+-----------------------+
| \                     | 3                     | A notification will   |
|                       |                       | be sent to the        |
|                       |                       | Coordinator.[ ]{.A    |
|                       |                       | pple-converted-space} |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | Coordinator may use   |
|                       |                       | phone to request from |
|                       |                       | suppliers             |
+-----------------------+-----------------------+-----------------------+

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | Edit Request                      |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Top                               |
+-----------------------------------+-----------------------------------+
| **Performance**                   | 10 minutes for edit, on time      |
|                                   | change                            |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What if the Customer cannot edit  |
| IS                                | any request?                      |
| SUES[ ]{.Apple-converted-space}** |                                   |
|                                   | Shouldn\'t we disable editing     |
|                                   | requests whenever they are        |
|                                   | acknowledged by the Coordinator?  |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | View Request Details              |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | None                              |
+-----------------------------------+-----------------------------------+

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

**3.2.27.2 Sequence Diagram**

\

\

\

**3.2.28.1 Delete Request**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \#28**     | Delete Request        |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | The Coordinator can   |                       |
|                       | delete[               |                       |
|                       | ]{.Apple-co           |                       |
|                       | nverted-space}request |                       |
|                       | and notify his        |                       |
|                       | supplier              |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -The Customer has     |                       |
|                       | logged in.            |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The Customer can      |                       |
| Condition**           | delete a chosen       |                       |
|                       | request.              |                       |
|                       |                       |                       |
|                       | The notification will |                       |
|                       | be sent to the        |                       |
|                       | Coordinator.          |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | An error message is   |                       |
| Condition**           | generated.            |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Customer, Coordinator |                       |
|                       |                       |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the Customer     |                       |
|                       | clicks on the proper  |                       |
|                       | link for deleting a   |                       |
|                       | request.              |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The Customer press    |
|                       |                       | "Delete Request"      |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The information about |
|                       |                       | the request will      |
|                       |                       | show.                 |
+-----------------------+-----------------------+-----------------------+
| \                     | 3                     | Press "Delete" to     |
|                       |                       | processing the        |
|                       |                       | deleting              |
+-----------------------+-----------------------+-----------------------+
| \                     | 4                     | The Customer will     |
|                       |                       | send a notification   |
|                       |                       | to supplier           |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | Customer may use      |
|                       |                       | phone to delete the   |
|                       |                       | request by the        |
|                       |                       | Coordinator.          |
+-----------------------+-----------------------+-----------------------+

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | Delete Request                    |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | \                                 |
+-----------------------------------+-----------------------------------+
| **Performance**                   | 5 seconds for delete              |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What is the coordinator cannot    |
| IS                                | delete requests?                  |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | View Request Details              |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | None                              |
+-----------------------------------+-----------------------------------+

\

**3.2.28.2 Sequence Diagram**

\

\

\

**3.2.29.1 Manage Customers**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \# 29**    | Manage                |                       |
|                       | Customers[ ]{.A       |                       |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | The main customers    |                       |
|                       | management page that  |                       |
|                       | coordinator will      |                       |
|                       | manage all customers  |                       |
|                       | information           |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company, Summary      |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login                 |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator       |                       |
| Condition**           | should add ,view,     |                       |
|                       | edit or delete        |                       |
|                       | customers             |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | An error message is   |                       |
| Condition**           | generated.[ ]{.A      |                       |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator ,         |                       |
|                       | Customer              |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | \                     |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "Manage[              |
|                       |                       | ]{.Apple-conve        |
|                       |                       | rted-space}Customers" |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The coordinator use   |
|                       |                       | any function.         |
+-----------------------+-----------------------+-----------------------+
| \                     | 3                     | The coordinator will  |
|                       |                       | manage all customers  |
|                       |                       | function.[ ]{.A       |
|                       |                       | pple-converted-space} |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | \                     | \                     |
+-----------------------+-----------------------+-----------------------+

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | Manage Customers                  |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Top                               |
+-----------------------------------+-----------------------------------+
| **Performance**                   | \                                 |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | \                                 |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | \                                 |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What if the coordinator cannot    |
| IS                                | manage cutomers?                  |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | Login                             |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | Add Customer , View Customers     |
+-----------------------------------+-----------------------------------+

\

\

\

**3.2.30.1 Add Customer**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \#30**     | Add Customer          |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | Coordinator can add   |                       |
|                       | new Customer.         |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login                 |                       |
|                       |                       |                       |
|                       | -The coordinator      |                       |
|                       | press "Add Customer"  |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | add new customer.     |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | Login in failed       |                       |
| Condition**           |                       |                       |
|                       | An error message is   |                       |
|                       | generated.[ ]{.A      |                       |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator , Cutomer |                       |
|                       |                       |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the coordinator  |                       |
|                       | needs to add new      |                       |
|                       | customer.             |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "Add Customer"        |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The coordinator fills |
|                       |                       | the new customer      |
|                       |                       | form.                 |
+-----------------------+-----------------------+-----------------------+
| \                     | 3                     | The coordinator will  |
|                       |                       | send the customer to  |
|                       |                       | supplier[ ]{.A        |
|                       |                       | pple-converted-space} |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | \                     | \                     |
+-----------------------+-----------------------+-----------------------+

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | Add Customer                      |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Top                               |
+-----------------------------------+-----------------------------------+
| **Performance**                   | 1 minutes for request, 2 days     |
|                                   | until accept                      |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What is the coordinator cannot    |
| IS                                | add new customer?                 |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | Customers Management              |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | None                              |
+-----------------------------------+-----------------------------------+

\

**3.2.30.2 Sequence Diagram**[**:**]{.s4}

\

\

\

\

\

\

**3.2.31.1 View Customers**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \#31**     | View Customers        |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | coordinator can view  |                       |
|                       | a list of all         |                       |
|                       | customers.            |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login[ ]{.A           |                       |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | show all customers.   |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | Login in failed       |                       |
| Condition**           |                       |                       |
|                       | The coordinator       |                       |
|                       | cannot view all       |                       |
|                       | customers.            |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator ,         |                       |
|                       | Customer              |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the coordinator  |                       |
|                       | needs to view         |                       |
|                       | customers and clicks  |                       |
|                       | on the proper link to |                       |
|                       | that function.        |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "View Customers"      |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The coordinator view  |
|                       |                       | list of customers.    |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | Coordinator may want  |
|                       |                       | to see refined list   |
|                       |                       | on certain criteria   |
|                       |                       | only.[ ]{.A           |
|                       |                       | pple-converted-space} |
+-----------------------+-----------------------+-----------------------+

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | View Customers                    |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Top                               |
+-----------------------------------+-----------------------------------+
| **Performance**                   | [ ]{.Apple-converted-space}10     |
|                                   | seconds to show the list          |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What if the coordinator cannot    |
| IS                                | view customers?                   |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | Manage Customers                  |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | View Customer Details             |
+-----------------------------------+-----------------------------------+

\

**3.2.31.2 Sequence Diagram**[**:**]{.s4}

\

\

**3.2.32.1 View Customer Details**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \#32**     | View Customer Details |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | Coordinator can show  |                       |
|                       | the details of any    |                       |
|                       | customer that he      |                       |
|                       | chose.                |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login                 |                       |
|                       |                       |                       |
|                       | -The coordinator      |                       |
|                       | press "View Customer  |                       |
|                       | Details"              |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | show the details of a |                       |
|                       | customer.             |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | The coordinator       |                       |
| Condition**           | cannot show the       |                       |
|                       | details of a          |                       |
|                       | customer.             |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator ,         |                       |
|                       | Customer              |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the coordinator  |                       |
|                       | need to view the      |                       |
|                       | details of a          |                       |
|                       | customer.             |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "View Customer        |
|                       |                       | Details"              |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The coordinator views |
|                       |                       | the details of a      |
|                       |                       | customer.             |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | \                     | \                     |
+-----------------------+-----------------------+-----------------------+

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | View Customer Details             |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Middle                            |
+-----------------------------------+-----------------------------------+
| **Performance**                   | [ ]{.Apple-converted-space}10     |
|                                   | seconds to show the details of a  |
|                                   | customer.                         |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What is the coordinator cannot    |
| IS                                | view the details of a customer?   |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | View Customers                    |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | Delete Customer, Edit Customer    |
+-----------------------------------+-----------------------------------+

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

\

**3.2.31.2 Sequence Diagram:**

\

\

**3.2.33.1 Edit Customer**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \# 33**    | Edit Customer         |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | The Coordinator can   |                       |
|                       | edit[                 |                       |
|                       | ]{.Apple-con          |                       |
|                       | verted-space}customer |                       |
|                       | him.                  |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login[ ]{.A           |                       |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | edit exist customer.  |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | Login in failed       |                       |
| Condition**           |                       |                       |
|                       | An error message is   |                       |
|                       | generated.            |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator ,         |                       |
|                       | Customer              |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the coordinator  |                       |
|                       | needs to edit any     |                       |
|                       | exist customer.       |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "Edit Customer"       |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The coordinator       |
|                       |                       | modifies the request  |
|                       |                       | information.          |
+-----------------------+-----------------------+-----------------------+
| \                     | 3                     | The coordinator will  |
|                       |                       | send a notification   |
|                       |                       | to the customer.      |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | \                     | \                     |
+-----------------------+-----------------------+-----------------------+

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | Edit Customer                     |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Top                               |
+-----------------------------------+-----------------------------------+
| **Performance**                   | 1 minutes for edit, on time       |
|                                   | change                            |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What if the Coordinator cannot    |
| IS                                | edit any customer?                |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | ViewCustomer Details              |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | None                              |
+-----------------------------------+-----------------------------------+

\

**3.2.33.2 Sequence Diagram**

\

\

**3.2.34.1 Delete Customer**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \#34**     | Delete Customer       |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | The coordinator can   |                       |
|                       | delete a certain      |                       |
|                       | customer              |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login                 |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | delete exist          |                       |
|                       | customer.             |                       |
|                       |                       |                       |
|                       | The customer will be  |                       |
|                       | notified by option.   |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | Login in failed       |                       |
| Condition**           |                       |                       |
|                       | An error message is   |                       |
|                       | generated.            |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator ,         |                       |
|                       | Customer              |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the coordinator  |                       |
|                       | needs to delete any   |                       |
|                       | exist customer.       |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "Delete Customer"     |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The information about |
|                       |                       | the customer will     |
|                       |                       | show.                 |
+-----------------------+-----------------------+-----------------------+
| \                     | 3                     | Press "Delete" to     |
|                       |                       | processing the        |
|                       |                       | deleting              |
+-----------------------+-----------------------+-----------------------+
| \                     | 4                     | The coordinator will  |
|                       |                       | send a notification   |
|                       |                       | to the customer on    |
|                       |                       | option.               |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | \                     | \                     |
+-----------------------+-----------------------+-----------------------+

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | Delete Customer                   |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | \                                 |
+-----------------------------------+-----------------------------------+
| **Performance**                   | 1 minute for delete               |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What is the coordinator cannot    |
| IS                                | delete customer?                  |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | View Customer Details             |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | None                              |
+-----------------------------------+-----------------------------------+

\

**3.2.34.2 Sequence Diagram**

\

\

**3.2.35.1 Manage Suppliers**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \# 35**    | Manage Suppliers      |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | The main suppliers    |                       |
|                       | management page that  |                       |
|                       | coordinator will      |                       |
|                       | manage all suppliers  |                       |
|                       | information           |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company, Summary      |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login                 |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator       |                       |
| Condition**           | should add ,view,     |                       |
|                       | edit or delete his    |                       |
|                       | suppliers.            |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | An error message is   |                       |
| Condition**           | generated.[ ]{.A      |                       |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator ,         |                       |
|                       | Supplier              |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | \                     |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "Manage[              |
|                       |                       | ]{.Apple-conve        |
|                       |                       | rted-space}Suppliers" |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The coordinator use   |
|                       |                       | any function.         |
+-----------------------+-----------------------+-----------------------+
| \                     | 3                     | The coordinator will  |
|                       |                       | manage all suppliers  |
|                       |                       | function.[ ]{.A       |
|                       |                       | pple-converted-space} |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | \                     | \                     |
+-----------------------+-----------------------+-----------------------+

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | Manage Suppliers                  |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Top                               |
+-----------------------------------+-----------------------------------+
| **Performance**                   | \                                 |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | \                                 |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | \                                 |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What if the coordinator cannot    |
| IS                                | manage suppliers?                 |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | Login                             |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | Add Supplier, View Supplier       |
+-----------------------------------+-----------------------------------+

\

\

\

**3.2.36.1 Add Supplier**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \#36**     | Add Supplier          |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | Coordinator can add   |                       |
|                       | new Supplier          |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login                 |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | add new Supplier.     |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | Login in failed       |                       |
| Condition**           |                       |                       |
|                       | An error message is   |                       |
|                       | generated.[ ]{.A      |                       |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator ,         |                       |
|                       | Supplier              |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the coordinator  |                       |
|                       | needs to add new      |                       |
|                       | Supplier.             |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "Add Supplier"        |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The coordinator fills |
|                       |                       | the new Supplier      |
|                       |                       | form.                 |
+-----------------------+-----------------------+-----------------------+
| \                     | 3                     | The coordinator will  |
|                       |                       | send the Supplier to  |
|                       |                       | supplier[ ]{.A        |
|                       |                       | pple-converted-space} |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | \                     | \                     |
+-----------------------+-----------------------+-----------------------+

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | Add Supplier                      |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Top                               |
+-----------------------------------+-----------------------------------+
| **Performance**                   | 1 minutes for application, 2 days |
|                                   | until accept                      |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What is the coordinator cannot    |
| IS                                | add new Supplier?                 |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | Suppliers Management              |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | None                              |
+-----------------------------------+-----------------------------------+

\

**3.2.36.2 Sequence Diagram**

\

\

\

**3.2.37.1 View Suppliers**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \#37**     | View Suppliers        |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | coordinator can view  |                       |
|                       | a list of all         |                       |
|                       | Suppliers.            |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login[ ]{.A           |                       |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | show all Supplier.    |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | Login in failed       |                       |
| Condition**           |                       |                       |
|                       | The coordinator       |                       |
|                       | cannot view all       |                       |
|                       | Suppliers.            |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator ,         |                       |
|                       | Supplier              |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the coordinator  |                       |
|                       | needs to view         |                       |
|                       | Suppliers and clicks  |                       |
|                       | on the proper link to |                       |
|                       | that function.        |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "View Suppliers"      |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The coordinator view  |
|                       |                       | list of Suppliers.    |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | Coordinator may want  |
|                       |                       | to see refined list   |
|                       |                       | on certain criteria   |
|                       |                       | only.[ ]{.A           |
|                       |                       | pple-converted-space} |
+-----------------------+-----------------------+-----------------------+

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | View Suppliers                    |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Top                               |
+-----------------------------------+-----------------------------------+
| **Performance**                   | [ ]{.Apple-converted-space}10     |
|                                   | seconds to show the list          |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What if the coordinator cannot    |
| IS                                | view Suppliers?                   |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | Manage Suppliers                  |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | View Supplier Details             |
+-----------------------------------+-----------------------------------+

\

**3.2.37.2 Sequence Diagram**

\

\

**3.2.38.1 View Supplier Details**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \#38**     | View Supplier Details |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | Coordinator can show  |                       |
|                       | the details of any    |                       |
|                       | Supplier that he      |                       |
|                       | chose.                |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login                 |                       |
|                       |                       |                       |
|                       | -The coordinator      |                       |
|                       | press "View Supplier  |                       |
|                       | Details"              |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | show the details of a |                       |
|                       | Supplier.             |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | The coordinator       |                       |
| Condition**           | cannot show the       |                       |
|                       | details of a          |                       |
|                       | Supplier.             |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator ,         |                       |
|                       | Supplier              |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the coordinator  |                       |
|                       | need to view the      |                       |
|                       | details of a          |                       |
|                       | Supplier.             |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "View Supplier        |
|                       |                       | Details"              |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The coordinator views |
|                       |                       | the details of a      |
|                       |                       | Supplier.             |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | \                     | \                     |
+-----------------------+-----------------------+-----------------------+

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | View Supplier Details             |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Middle                            |
+-----------------------------------+-----------------------------------+
| **Performance**                   | [ ]{.Apple-converted-space}10     |
|                                   | seconds to show the details of a  |
|                                   | Supplier.                         |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What is the coordinator cannot    |
| IS                                | view the details of a Supplier?   |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | View Supplier                     |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | Delete Supplier, Edit Supplier    |
+-----------------------------------+-----------------------------------+

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

**3.2.38.2 Sequence Diagram**[**:**]{.s4}

\

\

\

**3.2.39.1 Edit Supplier**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \# 39**    | Edit Supplier         |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | The Coordinator can   |                       |
|                       | edit[                 |                       |
|                       | ]{.Apple-con          |                       |
|                       | verted-space}Supplier |                       |
|                       | and notify him (on    |                       |
|                       | option.)              |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login[ ]{.A           |                       |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | edit exist Supplier.  |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | Login in failed       |                       |
| Condition**           |                       |                       |
|                       | An error message is   |                       |
|                       | generated.            |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator ,         |                       |
|                       | Supplier              |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the coordinator  |                       |
|                       | needs to edit any     |                       |
|                       | exist Supplier.       |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "Edit Supplier"       |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The coordinator       |
|                       |                       | modifies the Supplier |
|                       |                       | information.          |
+-----------------------+-----------------------+-----------------------+
| \                     | 3                     | The coordinator will  |
|                       |                       | send a notification   |
|                       |                       | to the Supplier.      |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | \                     | \                     |
+-----------------------+-----------------------+-----------------------+

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | Edit Supplier                     |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | Top                               |
+-----------------------------------+-----------------------------------+
| **Performance**                   | 1 minutes for edit, on time       |
|                                   | change                            |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What if the Coordinator cannot    |
| IS                                | edit any Supplier?                |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | View Supplier Details             |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | None                              |
+-----------------------------------+-----------------------------------+

\

**3.2.39.2 Sequence Diagram**

\

\

\

**3.2.40.1 Delete Supplier**

\

+-----------------------+-----------------------+-----------------------+
| **USE CASE \#40**     | Delete Supplier       |                       |
+-----------------------+-----------------------+-----------------------+
| **Goal in Context**   | The coordinator can   |                       |
|                       | delete a certain      |                       |
|                       | Supplier              |                       |
+-----------------------+-----------------------+-----------------------+
| **Scope & Level**     | Company , Summary     |                       |
+-----------------------+-----------------------+-----------------------+
| **Preconditions**     | -Must the coordinator |                       |
|                       | login                 |                       |
+-----------------------+-----------------------+-----------------------+
| **Success End         | The coordinator can   |                       |
| Condition**           | delete exist          |                       |
|                       | Supplier.             |                       |
|                       |                       |                       |
|                       | The Supplier will be  |                       |
|                       | notified by option.   |                       |
+-----------------------+-----------------------+-----------------------+
| **Failed End          | Login in failed       |                       |
| Condition**           |                       |                       |
|                       | An error message is   |                       |
|                       | generated.            |                       |
+-----------------------+-----------------------+-----------------------+
| **Primary,**          | Coordinator ,         |                       |
|                       | Supplier              |                       |
| **[ ]{.Apple-conv     |                       |                       |
| erted-space}Secondary |                       |                       |
| Actors**              |                       |                       |
+-----------------------+-----------------------+-----------------------+
| **Trigger**           | When the coordinator  |                       |
|                       | needs to delete any   |                       |
|                       | exist Supplier.       |                       |
+-----------------------+-----------------------+-----------------------+
| **DESCRIPTION**       | **Step**[ ]{.A        | **Action**            |
|                       | pple-converted-space} |                       |
+-----------------------+-----------------------+-----------------------+
| \                     | 1                     | The coordinator press |
|                       |                       | "Delete Supplier"     |
+-----------------------+-----------------------+-----------------------+
| \                     | 2                     | The information about |
|                       |                       | the customer will     |
|                       |                       | show.                 |
+-----------------------+-----------------------+-----------------------+
| \                     | 3                     | Press "Delete" to     |
|                       |                       | processing the        |
|                       |                       | deleting              |
+-----------------------+-----------------------+-----------------------+
| \                     | 4                     | The coordinator will  |
|                       |                       | send a notification   |
|                       |                       | to the Supplier on    |
|                       |                       | option.               |
+-----------------------+-----------------------+-----------------------+
| **EXTENSIONS**        | **Step**              | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | 1a                    | \"Error!\"[           |
|                       |                       | ]{.Apple-co           |
|                       |                       | nverted-space}message |
+-----------------------+-----------------------+-----------------------+
| **SUB-VARIATIONS**    | \                     | **Branching Action**  |
+-----------------------+-----------------------+-----------------------+
| \                     | \                     | \                     |
+-----------------------+-----------------------+-----------------------+

\

+-----------------------------------+-----------------------------------+
| **RELATED INFORMATION**           | Delete Supplier                   |
+-----------------------------------+-----------------------------------+
| **Priority:**                     | \                                 |
+-----------------------------------+-----------------------------------+
| **Performance**                   | 1 minute for delete               |
+-----------------------------------+-----------------------------------+
| **Frequency**                     | 10/day                            |
+-----------------------------------+-----------------------------------+
| **Channels to actors**            | not yet determined                |
+-----------------------------------+-----------------------------------+
| **OPEN                            | What is the coordinator cannot    |
| IS                                | delete Supplier?                  |
| SUES[ ]{.Apple-converted-space}** |                                   |
+-----------------------------------+-----------------------------------+
| **Due Date**                      | Release 1.0                       |
+-----------------------------------+-----------------------------------+
| **\...any                         | \                                 |
| o                                 |                                   |
| ther[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **manage                          |                                   |
| ment[ ]{.Apple-converted-space}** |                                   |
|                                   |                                   |
| **information\...**               |                                   |
+-----------------------------------+-----------------------------------+
| **Superordinates**                | View Supplier Details             |
+-----------------------------------+-----------------------------------+
| **Subordinates**                  | None                              |
+-----------------------------------+-----------------------------------+

\

**3.2.40.2 Sequence Diagram**

\

**3.3 Performance Requirements**

The system must handle at least 100 concurrent users and their
operations. The system must accomplish 90% for transactions in less than
1 second. This is due to the nature of data, which is only text
information that does not usually exceed 50 KB per transaction.

\

\

**3.4 Logical Database Requirements**

The DB tables shall reflect following:

\- [ ]{.Apple-tab-span}Coordinator

Customer

Supplier

Resource Location

Item

Request

\

\

**3.5 Design Constraints**

\

[**3.5.1** ]{.s4}**Programming language:**

Our System will be web based system which we will use a web developing
language. We will use ASP.NET and C\# languages. The system has to be
designed on .NET Framework 3.5 using Visual Studio family.

**3.5.2 Database:**

The system will use MS SQL for our database.

**3.5.3[ ]{.Apple-tab-span}Software Process:**

The system shall follow the Waterfall software process model. Also the
system shall be designed in an Object Oriented approach so that future
features can be easily integrated with the system.

\

**3.5.4[ ]{.Apple-tab-span}Ejada framework:**

The system has to use the Ejada .Net frame work and also our system will
integrate with two modules in Ejada.[ ]{.Apple-converted-space}

\

**3.6 Software System Attributes**

\

**3.6.1[ ]{.Apple-tab-span}Reliability**

All data will be backed-up everyday automatically and also the system
administrator can back-up the data as a function for him. Also if any
errors, fault or failures happen the system will detected and inform the
user about problems and also if there is any transaction with the
database and in that time happen no action to the data and the system
will back to the previous state of database. Also our system will cover
the quality assurance.[ ]{.Apple-converted-space}

\

**3.6.2[ ]{.Apple-tab-span}Availability**

The system has to be available 100% of the time. Once there is a fatal
error, the system should give understandable feedback to the user.

\

**3.6.3[ ]{.Apple-tab-span}Security**

\

The system have only three roles for coordinators , suppliers and
customers only that make our system secure access online and these
authentications will prevent and illegal access.

[  ]{.Apple-converted-space}

**3.6.4[ ]{.Apple-tab-span}Maintainability**

\

The system is designed in modules where errors can be detected and fixed
easily. This makes it easier to install updates and new functionality if
required.

\

**3.6.5[ ]{.Apple-tab-span}Portability**

\

The system can operate in any of the latest Microsoft operating systems
with the latest .Net framework. Due to the web based nature of the
system, the host machine must also have Microsoft IIS installed

\

\

\

**4. Change Management Process[ ]{.Apple-converted-space}**

\

Every change in the SRS will be done by the developing team and it is
updated in the SRS review report which contains all the information of
the change shush as change date, author, the change is applied on what ,
and why the changed is applied.

**Appendix**

\

Use Case Diagrams

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

[**KFUPM**]{.s8}[ ]{.Apple-tab-span}[ ]{.Apple-tab-span}[
]{.Apple-tab-span}[ ]{.Apple-tab-span}[ ]{.Apple-tab-span}[
]{.Apple-tab-span}[ ]{.Apple-tab-span}[ ]{.Apple-tab-span}[
]{.Apple-tab-span}[ ]{.Apple-tab-span}[ ]{.Apple-tab-span}[
]{.Apple-tab-span}[ ]{.Apple-tab-span}

VIPER Team

\

**Supply Chain**

**Management**

**System For Ejada Company**

\

\

PAGE [ ]{.Apple-converted-space}

\

\

\

\

\

\

  ------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------
  Supply Chain Management System                                                                                     [  ]{.Apple-converted-space}Version: [          ]{.Apple-converted-space}1.1
  [ ]{.Apple-converted-space}TITLE[  ]{.Apple-converted-space}\\\* MERGEFORMAT Software Requirements Specification   [  ]{.Apple-converted-space}Date:[  ]{.Apple-converted-space}20/12/2008
  ------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------

\

\

  -------------------------------------------------------------------
  ConfidentialTeam\#6 , 2008Page[ ]{.Apple-converted-space} PAGE 66
  -------------------------------------------------------------------

\

\

\

\

\

\

\

\
