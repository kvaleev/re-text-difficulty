---
consensus_grade_level: 11.2
headings_per_sentence: 0.01
lists_per_sentence: 0.06
smao_sentences_pct: 1.2
vague_words_per_sentence: 0.12
anaphora_per_sentence: 0.36
sentence_cv: 1.262
cpre_terms_per_sentence: 0.86
---
**COMPREHENSIVE WATERSHED MANAGEMENT**
**WATER USE TRACKING PROJECT**

# **Software Requirements Specification**


Southwest Florida Water Management District
2379 Broad Street
Brooksville, FL 34604-6899


|Date|Revision|Description|Author|
|---|---|---|---|
|||||
|||||
|||||
|||||


# **Table of Contents**

1 Introduction.............................................................................................................................. 1
1.1 Purpose............................................................................................................................ 1
1.2 Overview......................................................................................................................... 1
2 Project Scope ........................................................................................................................... 2
2.1 Problem Statement.......................................................................................................... 2
2.2 Product Position Statement............................................................................................. 2
2.3 Stakeholder Summary..................................................................................................... 3
2.4 Project Environment ....................................................................................................... 6
2.4.1 Hardware/Software Environment ............................................................................... 6
2.4.1.1 IBM DB2 Data Server ............................................................................................ 6
2.4.1.2 HP-UX ArcSDE/Oracle Data Server...................................................................... 6
2.4.1.3 Communications/Data Network.............................................................................. 6
2.4.1.4 Web/ArcIMS Servers.............................................................................................. 6
2.4.1.5 Desktop Workstations............................................................................................. 6
2.5 Product Perspective......................................................................................................... 6
2.5.1 WUP Data................................................................................................................... 6
2.5.2 Geographic Data ......................................................................................................... 7
2.5.3 Water Resource Data .................................................................................................. 7
2.5.4 GIS/RDB/WMDB Data Integration............................................................................ 7
2.6 Assumptions and Dependencies ..................................................................................... 7
2.7 Needs............................................................................................................................... 8
2.8 Other Product Requirements........................................................................................... 9
3 Requirements Gathering Process............................................................................................. 9
3.1 Requirement Workshops and Summaries....................................................................... 9
3.2 Requirements Traceability Matrix.................................................................................. 9
3.3 Use Case Model and Use Cases.................................................................................... 10
3.4 Supplementary Specification ........................................................................................ 11
4 WUT Requirements............................................................................................................... 13
4.1 WUT Requirements Traceability Matrix...................................................................... 13
4.1.1 Functional Requirements by Category...................................................................... 13
4.1.1.1 SWUCA................................................................................................................ 13
4.1.1.2 Water Use Permits ................................................................................................ 17
4.1.1.3 Water Use.............................................................................................................. 19
4.1.1.4 Water Management Database ............................................................................... 21
4.1.1.5 Compliance ........................................................................................................... 21
4.1.1.6 Minimum Flows and Levels ................................................................................. 22
4.1.1.7 Water Estimates .................................................................................................... 23
4.1.1.8 External Data ........................................................................................................ 23
4.1.1.9 Crop Reports......................................................................................................... 23
4.1.1.10 Data Integration ................................................................................................ 23
4.1.2 Requirements Identified for a Possible Subsequent Release of the WUT System... 23
4.2 WUT Use Case Model.................................................................................................. 25


i


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


4.2.1 Actors........................................................................................................................ 26
4.2.2 Use Cases.................................................................................................................. 26
4.2.2.1 Process WUT System Startup............................................................................... 28
4.2.2.2 Generate Well Package......................................................................................... 28
4.2.2.3 Maintain Business Rule Parameters...................................................................... 28
4.2.2.4 Maintain Quick Links ........................................................................................... 28
4.2.2.5 Maintain Water Use Estimates.............................................................................. 29
4.2.2.6 Maintain WUT News............................................................................................ 29
4.2.2.7 Process Database Replication ............................................................................... 29
4.2.2.8 View Change in Use Type or Owner.................................................................... 29
4.2.2.9 View Compliance Information ............................................................................. 30
4.2.2.10 View Crop Report Information......................................................................... 30
4.2.2.11 View Land Use Information ............................................................................. 30
4.2.2.12 View Lapsed or Project Quantities Summary................................................... 31
4.2.2.13 View Map.......................................................................................................... 31
4.2.2.14 View Mitigation of MFL Impacts..................................................................... 31
4.2.2.15 View Net Benefit Summary.............................................................................. 32
4.2.2.16 View Report...................................................................................................... 32
4.2.2.17 View Resource Information.............................................................................. 33
4.2.2.18 View Use of Lapsed Quantities ........................................................................ 33
4.2.2.19 View Use of Quantities Associated With District Projects .............................. 34
4.2.2.20 View Water Use Permit .................................................................................... 34
4.2.2.21 View Water Use Permit Search ........................................................................ 34
4.2.2.22 View Water Withdrawal Credit ........................................................................ 35
4.2.2.23 View Well Construction Information ............................................................... 35
4.2.2.24 View Withdrawal Pumpage Information.......................................................... 35
4.2.3 WUT Supplementary Specification.......................................................................... 36
4.2.3.1 Usability................................................................................................................ 36
4.2.3.2 Reliability.............................................................................................................. 37
4.2.3.3 Performance.......................................................................................................... 37
4.2.3.4 Supportability – Definition ................................................................................... 38
Appendix A …………………………………………………………………….………………..39


ii


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


1


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


2


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


_**Records and Data Staff –**_ The system will provide tools to assist in the quality control/quality
assurance of WUP data.

_**Resource Conservation and Development Department –**_ The system will provide information
that can be used to assist in the calibration of ground water models. The system will also provide
information on WUPs that can support the establishment and monitoring of Minimum Flows and
Levels. In addition, the system will provide information that assists in the development of
estimated water use

**Planning Department** _**–**_ The system will provide tools to assist in studies analyzing impacts of
changing demographics and economic conditions on water use within the SWUCA.

_**Executive Staff/Governing Board –**_ The system will provide standard reports that are published
as hardcopy or web-accessible documents. Web accessible maps and documents could be
interactive, allow users to zoom, pan, and query areas of interest.

_**External Customers –**_ External customers potentially include local governments, the media, and
the general public. Standard interactive map interfaces will provide information in a consistent,
low maintenance environment.

_**Other Users –**_ This system is in line with the objectives of the CWM Information Technology
initiative presented to the Governing Board in June 2002. It will provide improved access to
WUP data for all District staff.

# **2.3 Stakeholder Summary**

The following is a list of Stakeholders that will participate in the development of the Water Use
Tracking System:

|Name|Role|Title|
|---|---|---|
|**Executive Sponsors:**|**Executive Sponsors:**|**Executive Sponsors:**|
|Bruce Wirth|Executive level view of<br>requirements.|Deputy Executive Director|
|Gene Heath|Executive level view of<br>requirements.|Assistant Executive Director|
|John Heuer|Executive level view of<br>requirements.|Deputy Executive Director|


|Name|Role|Title|
|---|---|---|
|**Co-Sponsors:**|**Co-Sponsors:**|**Co-Sponsors:**|
|B. J. Jarvis|Oversees the computer entry of<br>permit and pumpage data.|Director, Records and Data<br>Department|
|Mark Barcelo|Oversees Groundwater modeling<br>activities and ensures the project<br>adheres to SWUCA Rules.|<br>Hydrologic Evaluation<br>Manager|



3


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


|Name|Role|Title|
|---|---|---|
|**Science Business Experts:**|**Science Business Experts:**|**Science Business Experts:**|
|Albert Bond|Estimates past water usage and<br>projects future water use.|Hydrologist|
|Chris Zajac|Estimates past water usage and<br>projects future water use.|Senior Water Conservation<br>Analyst|
|Granville Kinsman|Compare Regulatory Database to<br>Water Mgmt Database for<br>redundant well points.|<br>Manager, Hydrologic Data<br>Collection Section|
|Mike Beach|Use data in model to track<br>minimum flows and levels<br>changes.|Senior Professional Engineer|
|Mike Hancock|Use data in model to track<br>minimum flows and levels<br>changes.|Senior Professional Engineer|
|Ron Basso|Use data in model to track<br>minimum flows and levels<br>changes.|Senior Professional<br>Geologist/Engineer|
|Rand Frahm|Track the project for ways<br>planning department can use<br>information.|Planning Manager|
|Margit Crowell|Water management database<br>expertise.|Staff Hydrologist|
||||
|**Regulatory Business Experts:**|**Regulatory Business Experts:**|**Regulatory Business Experts:**|
|Christine Jackson|Provide Water Use Permitting<br>and SWUCA Expertise.|Senior Professional<br>Geologist/Engineer|
|Jay Yingling|Use to study cost impacts in<br>regards to water use rule<br>changes.|Senior Economist|
|Deanna Naugler|Expertise on administrative<br>aspect of the permitting process.|Senior Regulatory Systems<br>Analyst|
|Debbie Ammendola|Computer entry of permit and<br>pumpage data that will be<br>utilized.|Records Processing Supervisor|
|Jim Whalen|Familiar with the issues that<br>people are trying to resolve.|Regulatory Data Analyst|
|Martha Norris|Knowledge of permit data.|Permit Data Analyst|
|John Parker|Ensure that permit rule criteria<br>and compliance issues are<br>satisfied.|Water Use Regulatory<br>Manager|


4


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


|Name|Role|Title|
|---|---|---|
|Karen Lloyd|Monitor how well the project can<br>be used to implement District<br>rules.|<br>Senior Attorney|
|Ken Weber|Ensures that the project adheres<br>to SWUCA Rules.|Regulation Program Director|
|Mike Balser|Ensure that permit rule criteria<br>and compliance issues are<br>satisfied.|Water Use Regulatory<br>Manager|
|Susan Caye|Familiar with the issues that<br>people are trying to resolve.|Senior Regulatory Systems<br>Analyst|
|Ralph Kerr|Ensure that permit rule criteria<br>and compliance issues are<br>satisfied.|Water Use Regulatory<br>Manager|
|Scott Laidlaw|Ensure that permit rule criteria<br>and compliance issues are<br>satisfied.|Water Use Regulatory<br>Manager|
||||
|**Technical Experts:**|**Technical Experts:**|**Technical Experts:**|
|Axel Griner|Geodatabase design support.|Senior GIS Analyst|
|Cheryl Glenn|Supply GIS aspects of<br>permitting.|GIS Analyst 2|
|Eileen Burns-Wilson|Provide expertise on how the<br>Regulatory database is built.|Computer Systems Support –<br>Scientific|
|Priscilla Thoopthong|ArcGIS programming support|Lead Programmer Analyst|
|Robin Allen|Provide expertise on how the<br>Regulatory database is built.|Senior Systems Analyst|
|Sherrie Kubis|Oracle database design support.|Computer Systems Support –<br>Scientific|
|Steven Dicks|Technical Team Leader|Mapping & GIS Manager|
||||
|**Other Impacted Parties:**|**Other Impacted Parties:**|**Other Impacted Parties:**|
|Diana Burdick|Coordinate with Land Resources<br>Dept. Database Project|Senior GIS Analyst|
|Richard Owen|Provide planning perspective to<br>project.|Planning Director|
|Kurt Fritsch|Provide District-wide, cross-<br>cultural view of the project, and<br>help to ensure scope is<br>maintained.|Inspector General|


5





Water Use Tracking Project – February 13, 2007
Software Requirements Specification


# **2.4 Project Environment**

_**2.4.1**_ _**Hardware/Software Environment**_
The proposed system does not appear to require any significant hardware or software resources
beyond that which currently exists, or is planned for implementation, at the District.


_2.4.1.1_ _IBM DB2 Data Server_
The IBM DB2 data server was upgraded in January 2003 and it is anticipated that it has
sufficient capacity to support the proposed system. It is likewise anticipated that the current DB2
database software configuration will support the proposed system.


_2.4.1.2_ _HP-UX ArcSDE/Oracle Data Server_
The District is currently retiring the obsolete HP Tru-64 computer system and replacing it with
an HP-UX system. It is anticipated that when this upgrade is completed in fiscal year (FY) 2004
that the system will have sufficient capacity to support the proposed system. It is likewise
anticipated that when the upgrade is completed, current ArcSDE/Oracle database system
configuration will support the proposed system.


_2.4.1.3_ _Communications/Data Network_
The primary impact of this system on the network will occur during the transfer of data between
the IBM and HP-UX systems. Since this transfer will occur only during non-business hours, it is
not anticipated that it will have a significant impact on the current network.


_2.4.1.4_ _Web/ArcIMS Servers_
The current Web/ArcIMS Server environment will be expanded in FY 2004 to support of CWM
activities and it is anticipated that it will have sufficient capacity to support the proposed system.
In the event that these servers are not adequate, they are relatively inexpensive to upgrade.


_2.4.1.5_ _Desktop Workstations_
It is anticipated that this system will operate within the ArcGIS ArcView and ArcIMS web
browser environment that is currently implemented at the District.

# **2.5 Product Perspective**

The system will require a combination of permitting, geographic, and water resource data
derived from the following sources.


_**2.5.1**_ _**WUP Data**_
The data source for WUPs is the Regulatory Database (RDB). This database is implemented in
the IBM DB2 environment on the District's IBM mainframe data server located in the Tampa
Data Center. The Records and Data Department is the primary entity responsible for the entry
and maintenance of the data in the RDB. The Information Resources Department (IRD) is
responsible for the design, development, and maintenance of the RDB.


6


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


_**2.5.2**_ _**Geographic Data**_
The data source for geographic data is the GIS. This database is implemented in the
ArcSDE/Oracle environment on the District's HP-UX data server located in the Brooksville
computer room. The Mapping and GIS Section (MGIS) is the primary entity responsible for the
entry and maintenance of most of the data in the GIS. The Land Resources, Operations, and
Records and Data Departments maintain specialized datasets within the GIS. IRD and MGIS are
jointly responsible for the design, development, and maintenance of the GIS.


_**2.5.3**_ _**Water Resource Data**_
It is anticipated that data on ground and surface water levels, water quality, stream flows, and
climatological trends will be used in this system. The source for these data is the Water
Management Database (WMDB). This database is implemented in the IBM DB2 environment
on the District's IBM mainframe data server located in the Tampa Data Center. The Operations
Department is the primary entity responsible for the entry and maintenance of the water
levels/flows and meteorological data in the RDB. Water quality data stored in the WMDB are
collected by multiple departments, processed by the District's laboratory, and loaded into the
WMDB. It is important to note that while almost all water level information collected by the
District is entered into the WMDB, loading of water quality data is less common. The WMDB,
therefore, does not provide a comprehensive collection of water quality data. The Information
Resources Department (IRD) is responsible for the design, development, and maintenance of the
WMDB.


_**2.5.4**_ _**GIS/RDB/WMDB Data Integration**_
The proposed system will require the integration of data in the GIS, RDB, and WMDB. Data in
these systems are logically linked using a common identifier known as the Universal ID (UID).
Each WUP withdrawal point and data collection site is assigned a UID. UIDs are unique for
physical objects such as wells, rain gauges, and stream gauges. Unique UIDs are also assigned
to surface water quality sample sites. In cases where a well is both associated with a WUP and
also serves as a data collection site, it is assigned a single UID that provides linkages to data
stored in both the RDB and WMDB. In the GIS, the UID is associated with a physical location
and, therefore, can be represented within a data layer representing WUPs, stream gauges, or
rainfall stations.

Data are physically transferred from the DB2-based WMDB and RDB to the ArcSDE/Oracle
based GIS using the Transformation Server software. This software provides tools for moving
data between databases in their entirety or as selected subsets. While this transfer is currently
only done from the WMDB/RDB to the GIS, it is technically possible to transfer data in the other
direction.

# **2.6 Assumptions and Dependencies**

Requirements have surfaced that require data that is currently not available, either not collected
or not stored in one of the databases (e.g., relocated quantities, lapsed quantities, etc.). It is
assumed that the needed changes, to collect and store the data, will be made within the current
application and database. These changes would need to be implemented on the mainframe and it


7


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


is assumed this would not be within the scope of this project. However, if the required changes
cannot be completed to the current systems in a timely manner, the WUT System will need to
implement these requirements within the new application.

It is also assumed that the current databases mentioned above are still available in their current
form during the development of the WUT System. The WUT System will be dependent on the
data stored in the WUP, WMDB, GIS, and RDB databases. Changes to the current systems
would need to be done in collaboration with the WUT Project Development Team.
Communication between the responsible parties is key in the success of the development of this
system.

One requirement for the WUT System is that it will be developed with the hardware and
software architecture currently in place at the District. Changes to the current architecture
requirements could have a negative impact on the development of this system and cause delays
in the release of the system.

# **2.7 Needs**

The following is a list of needs that were captured in the _SWUCA Permitted Water Use Tracking_
_Application – Feasibility Study_ . These needs and the requirements gathered at the Requirements
Workshops will be consolidated and presented to the Stakeholders at the Requirements Summary
Workshop for discussion and prioritization.

Needs:

- Depict geographic and temporal trends in permitted and/or actual pumpage within the
SWUCA

- "Cradle to grave" tracking and analysis of individual ground and surface water withdrawal
points

- Identification of sources for withdrawal points (surface versus ground, aquifer, status,
alternative sources, etc.)

- Monitoring changes in permitted and actual pumping

- Tracking changes in predominant use types

- Tracking changes in permit ownership

- Identifying withdrawal points with lapsed permitted quantities. As used here, lapsed
quantities refer to any reductions in permitted pumpage for a particular well. These may be
the result of expiration of a permit, purchase of land that leads to retiring of a WUP, changes
in predominant use type, plugging of well, or any other event that leads to a reduction in the
permitted withdrawal from that point.

- Aggregate permitted pumpage, actual use, and lapsed quantities for defined geographic areas

- Must be able to analyze the impacts of alternative supplies on pumpage in a particular
geographic area


8


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


9


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


success by prioritizing the features and/or requirements associated with each feature across the
various releases of the WUT System.

For purposes of requirements management and traceability, the requestor(s) of each requirement
is included in the matrix. This allows the project development team to easily know whom to
contact if questions or concerns arise during the development of the system regarding a certain
requirement. The capability to map these requirements increases the likelihood that upon the
customer acceptance of a software solution that supports all the use cases within the Use Case
Model, the project development team will have delivered a software product that fulfills the
customer’s needs.

As more detailed and precise information is learned about the water use permitting analysis and
reporting business processes throughout the WUT Project life cycle, the WUT RTM will be
updated to refine existing requirements statements and to capture new business and functional
requirements as they are identified. Keeping the WUT RTM updated is a critical success factor
because it provides one of the primary mechanisms for measuring and ensuring the success of
the WUT Project. That is, the mapping of business and functional requirements to use cases
ensures that these requirements drive the software engineering effort through design,
implementation, and testing as a result of the use case realization process utilized by the WUT
Project Development Team. Once all the use cases within the WUT Use Case Model have been
implemented, then all the business and functional requirements have been satisfied and the WUT
Project will have completed successfully.

# **3.3 Use Case Model and Use Cases**

The use case model primarily sets the functional requirements on the system, and is used as an
essential input to analysis and architectural design. In essence, the use case model and use cases
are a contract between the project development team and the stakeholders with regards to the
functionality of the system. The initial release of the model in the inception phase is used to
outline the scope of the system. The use case model is refined by more detailed flows of events
during the elaboration and construction phases. The use case model is continuously kept
consistent with the design model.

The use case model consists of use case packages. A use case package is a collection of use
cases, actors, relationships, diagrams, and other packages. It is used to structure the model by
dividing it into smaller parts. The WUT Use Case Model consists of two packages:

- Maintain Water Use Tracking Information

- View Water Use Permit Information

The functionality of a system is defined by use cases, each of which represents a specific flow of
events. The description of a use case defines what happens in the system when the use case is
performed. All functional requirements must be able to be linked to at least one use case. This
ensures all required functionality is being included in the system to be built. Use cases contain
several key items:

- Business Context – A description of the business need of the use case.


10


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


- Pre-Conditions – A list of any conditions that must be met before the use case can be
executed.

- Flow of Events – The sequence of events that can take place during the execution of the use
case. This includes the Primary Flow, or basic path, Alternate Flows, Warning Flows, and
Exception Flows.

- Post-Conditions – A list of conditions that can be expected after the use cases ends,
dependent on the flow of events executed.

- Special Requirements – A list of any special requirements for a particular use case. This is a
“catch-all” section where any information regarding a use case can be captured and stored.

The users and any other system that may interact with the system are the actors. Because they
represent system users, actors help delimit the system and give a clearer picture of what it is
supposed to do. Use cases are developed on the basis of the actors' needs. This ensures that the
system will turn out to be what the users expected.

Also included in the use case model are the use case diagrams. These diagrams illustrate the use
cases and the actors and the interaction between the two. Use case diagrams can also be
organized by use case packages to show only what is relevant within a particular package.

The WUT Use Case Model was created and is currently stored in the Enterprise Architect
modeling tool. The model includes all requirements gathered to-date for the project. The model
also has all use cases that will be developed for the WUT System. All requirements are linked
within the model to one or more use cases. All the actors identified for the project are also in the
model. The use case diagrams show the interaction between the actors and the use cases.

# **3.4 Supplementary Specification**

In contrast to business and functional requirements, non-functional requirements are system
requirements that cannot be readily traced to specific use cases within the Use Case Model but
are nonetheless critical to the overall success of the software project. In general, there are two
types of non-functional requirements, qualitative and general systems. The first type of nonfunctional requirements are actually constraints upon the various functions, tasks, or behaviors
that constitute the system’s business and functional requirements and are, thus, commonly
considered to be the qualitative aspects of the proposed software system.

Qualitative systems requirements include considerations like:

- Usability

- Reliability

- Performance

- Supportability

- Performance Measures

The other type of non-functional requirements is general systems requirements typical to most
software engineering projects. No specific general systems requirements were gathered during
the requirement workshops for the WUT Project. However, these topics will be covered in the


11


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


Software Architecture Document created during the Elaboration Phase of the project. General
systems requirements include considerations like:

- Security

- Relational Database Management System

- Backup and Recovery and Disaster Recovery

- User Documentation and Training

Because non-functional requirements cannot be traced to specific use cases within the use case
model or, in some cases like security, apply to all use cases within the use case model, these
requirements are typically not documented in the Requirements Traceability Matrix. Rather,
non-functional requirements are documented and managed through a separate deliverable called
a Supplementary Specification.

The purpose of the WUT Supplementary Specification is to document and manage the nonfunctional requirements, or the qualitative and general systems requirements that are not mapped
to a specific use cases within the WUT Use Case Model. These requirements were collected
during the Requirement Workshops held during the Inception Phase of the project. This
Supplementary Specification will be managed and iteratively refined as appropriate throughout
the life of the WUT Project.

The Supplementary Specification will be a valuable aid to all members of the WUT Project
Development Team. This specification will be used as a communication medium between the
development team and the Project Stakeholders with regards to both qualitative and general
systems requirements. The Development Team itself will use the supplementary specification as
a reference when designing responsibilities, operations, and attributes on classes within the WUT
Design Model, and when adjusting the classes within the model to the proposed implementation
environment. Finally, the supplementary specification will be used to verify compliance of the
non-functional requirements during the testing of the WUT software.


12


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


|Col1|4 WUT Requirements<br>4.1 WUT Requirements Traceability Matrix<br>The current version of the WUT RTM is organized into two sections:<br>• Requirements for the Initial Release of the WUT System<br>• Requirements Identified for a Possible Subsequent Release of the WUT System<br>The first section identifies the set of business and functional requirements that will be supported<br>in the initial release of the WUT System and the second section is comprised of the balance of<br>the requirements that will be prioritized by the WUT Project Manager for a subsequent release of<br>system. Within each section, the requirements are organized into a number of features, each of<br>which is a logically related set of requirements. Within each feature, the requirements are<br>documented and managed within a matrix or table comprised of the following columns:<br>• Req ID – A unique identifier for each requirement<br>• Requirement Statement – Individual WUT business and functional requirements expressed<br>as a sentence that includes the word shall, will or must<br>• Use Case – A unique name that identifies the WUT Use Case that supports the requirement<br>4.1.1 Functional Requirements by Category<br>4.1.1.1 SWUCA|Col3|Col4|Col5|
|---|---|---|---|---|
||**Req ID**|**Requirement Statement**|**Use Case**||
|<br> <br> <br> <br> <br>|EW11b<br>RW16<br>SR20<br>SR21<br>SR22<br>SR23|Track the movement of lapsed quantities in an area,<br>including:<br>• Which permit and well obtained the lapsed<br>quantities.<br>• Where the lapsed quantities are located.<br>• Why the quantities are lapsed (i.e. expired,<br>cancelled, retired).<br>• What MFL zone the lapsed quantities are in.|• <br>View Lapsed and<br>Project Quantities<br>Summary<br>• <br>View Report<br>• <br>View Use of Lapsed<br>Quantities||
|<br> <br>|EW11a<br>SR18<br>RW1|Track the relocation of active water use within the<br>SWUCA.<br>|• <br>View Net Benefit<br>Summary<br>• <br>View Report||
|<br> <br> <br> <br> <br>|EW11b<br>RW16<br>SR20<br>SR21<br>SR22<br>SR23|Track the movement of lapsed quantities in an area,<br>including:<br>• Which permit and well obtained the lapsed<br>quantities.<br>• Where the lapsed quantities are located.<br>• Why the quantities are lapsed (i.e. expired,<br>cancelled, retired).<br>• What MFL zone the lapsed quantities are in.|• <br>View Lapsed and<br>Project Quantities<br>Summary<br>• <br>View Report<br>• <br>View Use of Lapsed<br>Quantities||
|<br> <br> <br> <br> <br>|||||



13


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||**Req ID**|**Requirement Statement**|**Use Case**||
|<br>|JY4<br>SR7|Report on the history of irrigation water conserving<br>credits, including the balance, how much earned, and<br>how much used, and drought quantities. Know who<br>uses them and who has accumulated them, and be able<br>to report on an individual basis, by a geographic area,<br>or aggregate the data.|• <br>View Water Use<br>Permit<br>• <br>View Report||
|<br> <br>|RW13<br>RW18<br>SR32|Track and report on the history of permitted data, such<br>as use type, irrigated acres, and pumpage (one use<br>would be to know whether expired permits have had<br>quantities reallocated).|• <br>View Water Use<br>Permit<br>• <br>View Withdrawal<br>Pumpage Information||
|<br>|RW14<br>SR8|Track and measure alternative source projects (note:<br>some of these may be included in table 8):<br>• Surface water or stormwater projects.<br>• Reclaimed water (reuse water).<br>• Augmented surface water (reservoirs, harvesting<br>of high flows (floodwaters).<br>• ASR (Aquifer storage recovery)<br>• Desalination.<br>• Conservation (defined as a beneficial reduction of<br>water use resulting in:<br>`o` modification of water use practices,<br>`o` reduction of unaccounted-for losses, or<br>`o` installation and maintenance of low<br>volume water use systems, processes,<br>fixtures, or devices.|• <br>View Map<br>• <br>View Report<br>• <br>View Use of<br>Quantities Associated<br>With District Projects||
|<br> <br> <br>|RW28<br>RW20<br>SR4<br>SR6|View the spatial impact of a person's application with<br>other active applications on-line so the applicant or<br>evaluator has a visual of who else is available to<br>compete for quantities with. Also include application<br>and permit data on-line, either with scanned<br>documents or access to database. The historical data<br>should also be available, but viewing restrictions for<br>certain legal documents has to be followed. Be able to<br>query by geographic area or permit number.|• <br>View Map<br>• <br>View Water Use<br>Permit Search<br>• <br>View Report||
||RW30a|Create heat map indicating who was over-pumping,<br>who was not over-pumping, or who was using their<br>water credits.|• <br>View Map||
||RW30b|Heat map for water quality. Add the District WUPnet<br>sentinel wells on this map - those are the District wells<br>that have been in existence the longest time and we<br>have the best data with. So if we bring them up in an<br>area we know we have reliable data.|• <br>View Map||
||||||


14



Water Use Tracking Project – February 13, 2007
Software Requirements Specification


|Col1|Col2|Col3|
|---|---|---|
|**Req ID**|**Requirement Statement**|**Use Case**|
|SR12a|Report on the permits that have been relocated by a<br>permit holder.|• <br>View Net Benefit<br>Summary<br>• <br>View Report<br>• <br>View Change in Use<br>Type or Owner|
|SR12b<br>SR13<br>SR26a<br>EW12|Track the impact that water use has to the set MFL<br>levels. In particular, compare the affects of the new or<br>modified use to the actual flow and level of the water<br>body or aquifer to make sure the actual level will not<br>go below the MFL level. Types of things to check<br>are:<br>• New applications, renewals, or modifications.<br>• Relocated uses.<br>• Change of use type.<br>• Lapsed quantities.<br>• Retired permits (some are lapsed - some are not).|• <br>View Net Benefit<br>Summary<br>• <br>View Change in Use<br>Type or Owner<br>• <br>View Use of Lapsed<br>Quantities<br>• <br>View Water<br>Withdrawal Credit<br>• <br>View Land Use<br>Information<br>• <br>View Lapsed and<br>Project Quantities<br>Summary|
|SR14<br>SR26b<br>EW2<br>SR15|Track net benefit changes. Some things involved are:<br>• Relocated permits<br>• Permits with a change of use<br>• Old and new locations<br>• Lapsed quantities<br>• Reclaimed water (not in database yet)<br>• Projects<br>• Amount of net benefit gained or lost from the<br>change<br>• New permits that came from an older permit due<br>to a new benefit gain|• <br>View Net Benefit<br>Summary<br>• <br>View Change in Use<br>Type or Owner<br>• <br>View Use of Lapsed<br>Quantities<br>• <br>View Water<br>Withdrawal Credit<br>• <br>View Land Use<br>Information<br>• <br>View Lapsed and<br>Project Quantities<br>Summary|
|SR16|Report the net benefit amount in MGD for:<br>• Change of permitted location or use<br>• Land use change<br>• Use of lapsed quantities<br>• Water withdrawal credit (replacement, reclaimed<br>water)|• <br>View Net Benefit<br>Summary<br>• <br>View Change in Use<br>Type or Owner<br>• <br>View Use of Lapsed<br>Quantities<br>• <br>View Water<br>Withdrawal Credit<br>• <br>View Land Use<br>Information<br>• <br>View Lapsed and<br>Project Quantities<br>Summary|


15


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||**Req ID**|**Requirement Statement**|**Use Case**||
||SR17|Mark those permits that have a land use change so the<br>quantities can be relocated to the public supply utility.|• <br>View Change in Use<br>Type or Owner<br>• <br>View Report||
||SR19|Create layer that includes "cones of depression" for<br>the MFL information, which will indicate the area of<br>influence to an MFL.|• <br>View Map||
|<br>|SR24<br>SR25|Report on any water use amounts sold or given from<br>one permit to another permit, especially reclaimed<br>water (reclaimed water can be taken away, depending<br>on the contract. It is kind-of-like “leasing” the water,<br>but can be taken away).|• <br>View Net Benefit<br>Summary<br>• <br>View Water<br>Withdrawal Credit||
||SR28|For mitigation of MFL impacts, report on the<br>improvement percentage amount, where it was<br>located, the cost, how the decrease was obtained and<br>what impacts it had.|• <br>View Mitigation of<br>MFL Impacts||
|<br>|SR29<br>SR9|Report on how much water was made available<br>through the District's water resource development<br>projects. Elements of the report should be:<br>• Source of benefit (aquifer or surface water).<br>• The locations of the alternative sources.<br>• What permits are using the quantities generated by<br>the projects, and what project they are getting the<br>water from.|• <br>View Mitigation of<br>MFL Impacts<br>• <br>View Use of<br>Quantities Associated<br>With District Projects<br>• <br>View Map||
||SR3|Report on the permit duration (To track expiration<br>dates for those looking for someone to compete with).|• <br>View Report<br>• <br>View Water Use<br>Permit Search||
||SR31|Should allow comparison to adjacent districts GIS<br>layers to permit GIS layer to access adjacent data.|• <br>View Map<br>• <br>Maintain Quicklinks||
||SR33|Report compliance on a permit (not wells). Crop<br>reports on permits (not wells).|• <br>View Report||
||SR5|Report on competing applications (including ones that<br>are in modification or expiring).|• <br>View Report<br>• <br>View Water Use<br>Permit Search||
||SW20|Supply the Regulatory requirements of MFL data:<br>• What water levels are in relationship to MFL so<br>you know who has to mitigate or how much excess<br>flow there is.<br>• Need the historic and current levels so applicant<br>knows how much to mitigate or what is available.|• <br>View Report||
||TW9|Be able to determine the availability of alternative use<br>supplies, such as reclaimed water and desalination.|• <br>View Map||
||SR2|Report the Reservation from use amounts allocated to<br>certain participants.|• <br>View Water Use<br>Permit Search||
||||||


16





Water Use Tracking Project – February 13, 2007
Software Requirements Specification


|Col1|4.1.1.2 Water Use Permits|Col3|Col4|Col5|
|---|---|---|---|---|
||**Req ID**|**Requirement Statement**|**Use Case**||
||EW14|Track ownership of wells or permits over the life of<br>the withdrawal point so the relocated quantities can be<br>traced from owner to owner.  Quantities that are<br>relocated will have certain restrictions placed on them,<br>as well as any quantities that remain on the original<br>permit.  For permits that have multiple withdrawal<br>points, we need the ability to track ownership of<br>specific withdrawal points over time.|• <br>View Report<br>• <br>View Water Use<br>Permit||
||EW21|Be able to look at permitted quantities, actual<br>quantities (pumpage), and the resources it uses (Water<br>Management DB)|• <br>View Water Use<br>Permit<br>• <br>View Report||
||EW9|Ability to track requested and permitted quantities.|• <br>View Water Use<br>Permit<br>||
||JY1|Identify when a standby permit is reactivated due to<br>the loss of alternative quantities.|• <br>View Net Benefit<br>Summary<br>• <br>View Water<br>Withdrawal Credit||
||RW19|Have a heat map that shows permit information for<br>specific time periods.  You should be able to input a<br>geographic area (whether by county, department, or<br>entire District area), select the time period(s) you<br>want, and select one of two views:  permits issued or<br>active permits in that time period, and produce the<br>map show the locations.  On a high-level view, you<br>need to be able to see the locations with the<br>predominate use type reflected on the map itself, and<br>include a graph or chart showing the total number of<br>permits, predominate use shown by %, and the time<br>period involved.  If you click on it, bring up the permit<br>details, such as name, permit number, issue date,<br>expire date, use type, wuca, and average quantities.|• <br>View Map<br>• <br>View Report||
||||||



17


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||**Req ID**|**Requirement Statement**|**Use Case**||
||RW27|Automate some of the requests that Jim Whalen<br>receives.  The majority of request are related to<br>permitted and pumpage quantities, both at the permit<br>level and well level.   They are usually sorted<br>temporally or geographically.|• <br>View Water Use<br>Permit<br>• <br>View Report<br>• <br>View Withdrawal<br>Pumpage Information<br>• <br>View Well<br>Construction<br>Information<br>• <br>View Resource<br>Information<br>• <br>View Crop Report<br>Information<br>• <br>View Land Use<br>Information<br>• <br>View Compliance<br>Information||
||RW29|Ability for public utilities and internal staff to find<br>existing permits in or near their service area so they<br>can spatially see what water is available, or may<br>become available, when they plan for their future<br>growth and water resources.  They will need to view<br>the use type (interested mainly in agricultural and<br>mining), owned acres, and the current permittee's<br>contact information.|• <br>View Map<br>• <br>View Water Use<br>Permit Search||
|<br>|RW37<br>TW4|Analyze permits using a soils type GIS layer.  Have a<br>second soils layer based on the soil types indicated on<br>the permittees compliance to conditions.|• <br>View Map||
||RW4|Ability to have printable and customizable maps|• <br>View Map||
||RW46a|Identify when the District or another governmental<br>agency purchases land, a link should be available to<br>show if there is a permit on that area so it can be<br>retired.|• <br>View Map||
||RW46b|Need to know how water use changes when land use<br>changes.|• <br>View Report<br>• <br>View Land Use<br>Information||
|<br> <br>|RW6<br>SW17<br>RW26a|Have an easy way to query data by various fields:<br>• Issue date<br>• Expiration date<br>• Use type or other commodity<br>• Predominate use<br>• Pumpage reports<br>• Permitted quantities<br>• Permit status (active/delete/app/permit)|• <br>View Water Use<br>Permit Search<br>||
|<br> <br>|||||



18


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||**Req ID**|**Requirement Statement**|**Use Case**||
||SW18|Ability to pull a well package that provides a view of<br>water use at a particular time that is then plugged into<br>models used to generate water use amounts. The data<br>would include wells, land elevation, aquifer, and total<br>and cased depths.|• <br>Generate Well<br>Package||
|<br>|SW24<br>SW25|The ability to associate permitted quantities, pumpage<br>quantities, and use code data at the well level.|• <br>View Water Use<br>Permit<br>• <br>View Withdrawal<br>Pumpage Information||
||TW12|Track changes in land use and how it affects water<br>availability.|• <br>View Report<br>• <br>View Land Use<br>Information||
||TW16|Need historical data for Water Use Permits including<br>their spatial representations (polygons)|• <br>View Map||
||<br>_4.1.1.3 Water Use_|<br>_4.1.1.3 Water Use_|<br>_4.1.1.3 Water Use_|<br>_4.1.1.3 Water Use_|
||**Req ID**|**Requirement Statement**|**Use Case**||
||EW1|Must be able to track trends in land use and water use<br>changes. These include several means by which a<br>proposed new withdrawal that impacts an MFL<br>waterbody can achieve a "Net Benefit," including the<br>provisions for relocated, lapsed, and water withdrawal<br>credits.|• <br>View Report<br>• <br>View Land Use<br>Information||
|<br> <br>|EW4<br>EW5<br>EW7|Ability to track water use over time and negotiate<br>reasonable new water use based on water use<br>pumpage trends.|• <br>View Withdrawal<br>Pumpage Information<br>• <br>View Report||
||RW15|Track by withdrawal source – what aquifer or USGS<br>water body are general and Individual permits<br>pumping from.|• <br>View Water Use<br>Permit Search<br>• <br>View Map||
||RW33|Have map be able to show quantity of pumpage.<br>Hover over or click a point in the map and see the<br>average rolling 12, peak month, and max month<br>compared to the pumpage of the well. Also get the<br>cumulative quantities for an area you enter manually.|• <br>View Report||
||RW49|Provide the ability for applicants or District staff to<br>compare the percentage a permit is over-pumping,<br>based on use type, against the regional average for the<br>same use type. The region would be the area that fell<br>within the buffer distance entered, and the time of<br>interest would also be entered.|• <br>View Report<br>• <br>View Withdrawal<br>Pumpage Information||
||||||


19





Water Use Tracking Project – February 13, 2007
Software Requirements Specification


|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||**Req ID**|**Requirement Statement**|**Use Case**||
||SW11|Need to know what aquifer is being pumped from.<br>There are permitting constraints in ETB MIA that no<br>additional water from the Floridan Aquifer can be<br>pumped, but it is allowed from Intermediate aquifer.|• <br>View Withdrawal<br>Pumpage Information||
|<br>|SW15<br>SW9|Select water use data temporally or with geographic<br>overlays, which can be from another layer or graphics<br>on the page.  Also be able to place it in an Excel<br>spreadsheet.|• <br>View Map||
||SW21|Select water use based on predominant use, use types,<br>and regions they fall in.  The predominant use would<br>be agricultural, industrial, mining & dewatering,<br>public supply, and recreational.  Each predominate use<br>is further broken down into more detailed categories,<br>such as melons or citrus for the agricultural<br>predominate use.  This needs historical data for trend<br>analysis.|• <br>View Report<br>• <br>View Water Use<br>Permit Search||
||SW6|Generate monthly reports for Board Packet that shows<br>the difference in quantities permitted every month for<br>specified geographic areas (i.e., counties, MIA, etc.).|• <br>View Report||
||TW1|Establish relationships between inputs (i.e. rainfall)<br>and pumpage data.<br>(Note:  In response to one of Kurt's comments<br>regarding the amount of pumping in areas in<br>relationship to amount of rainfall and irrigation system<br>efficiency.)|• <br>View Report||
|<br>|TW10<br>TW11|Show the intensity of water use in a geographic area<br>on a color-coded map.|• <br>View Map||
||TW15|Identify different types of water use, such as<br>groundwater, surface water, and re-use.|• <br>View Water Use<br>Permit||
||TW8|Know how much water has been permitted and how<br>much has been used based on land use over time.|• <br>View Report||
||<br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br>|



20


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


|Col1|4.1.1.4 Water Management Database|Col3|Col4|Col5|
|---|---|---|---|---|
||**Req ID**|**Requirement Statement**|**Use Case**||
||EW13|Support extraction or reporting of data for ad-hoc<br>geographic areas by using spatial queries such as<br>graphics or polygon buffering.  The ability to<br>aggregate the data must be there and any type of<br>polygon should be able to be used.|• <br>View Map||
|<br> <br> <br>|RW22<br>RW23<br>RW24<br>RW48|Track aquifer level changes, lake level changes,<br>rainfall level changes, and stream flow changes by<br>area over time (i.e. monthly).|• <br>View Report||
||RW25|Create layer that shows the Developments of Regional<br>Impacts (DRI) and their status.  This layer will be<br>plugged into the new model for population projections<br>and water supply demand projections.|• <br>View Map||
||RW45|Identify what lakes are stressed, when they became<br>stressed, and if/when they came off stressed list.|• <br>View Report<br>• <br>View Map||
||<br>_4.1.1.5 Compliance_|<br>_4.1.1.5 Compliance_|<br>_4.1.1.5 Compliance_|<br>_4.1.1.5 Compliance_|
||**Req ID**|**Requirement Statement**|**Use Case**||
|<br>|RW10<br>RW9b|Track pumpage oddities.  Two examples are:<br>A.  Permittees that have consistent pumpage readings<br>even when some of the data is missing.  Use this<br>information to predict whether they are in compliance<br>in spite of the missing data.<br>B.  Permittees that enter zero on their pumpage<br>reports.|• <br>View Report<br>• <br>View Withdrawal<br>Pumpage Information<br>• <br>View Compliance<br>Information<br>• <br>View Resource<br>Information<br>• <br>View Water Use<br>Permit Search||
|<br>|RW34<br>RW9a|Track permittees not submitting conditional/pumpage<br>reports, and generate a map showing their locations.|• <br>View Map<br>• <br>View Compliance<br>Information<br>• <br>View Resource<br>Information||
|<br>|TW13<br>TW14|Obtain report of those out of compliance of permit<br>conditions by over-pumping their allowable quantities.<br>Show how much over pumping is done, and have<br>option to select by time period or by area.  Need to<br>break down to a permit-by-permit basis, but also show<br>the whole thing on a map.|<br>• <br>View Map<br>• <br>View Report<br>• <br>View Compliance<br>Information||
|<br>|<br> <br>|<br> <br>|<br> <br>|<br> <br>|



21


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


|Col1|4.1.1.6 Minimum Flows and Levels|Col3|Col4|Col5|
|---|---|---|---|---|
||**Req ID**|**Requirement Statement**|**Use Case**||
||EW6|Need a protocol to assess how the actual flow and<br>levels (AFL) compare to the established minimum<br>flows and levels (MFL), including general trending<br>information and whether waterbody-specific criteria<br>are being met. There are 3 major provisions to track:<br>• Minimum aquifer level - The saltwater intrusion<br>MFL is met when the moving 10-year AFL is at or<br>above the MFL for five consecutive years. The<br>MFL is not met when the 10-year moving AFL in<br>the reference wells is below the MFL for two<br>consecutive years.<br>• Minimum flows on the upper Peace River - The<br>MFL is met when the MFL's are at or above the<br>established MFL for three consecutive years. Once<br>the MFL has been considered met, if it is followed<br>by two years where the MFL is not met within a<br>rolling ten-year period, then the AFL shall be<br>considered below the MFL. A determination of<br>whether AFL's are meeting the established MFL is<br>made at each one of the established minimums<br>(Bartow, Ft. Meade and Zolfo Springs).<br>• Minimum lake levels - The proposed MFL is<br>achieved when the long-term P50 is at or above<br>the MFL and the long-term P10 is at or above the<br>High Minimum Lake Level for five consecutive<br>years. Once in compliance, MFL is not met when<br>the long-term P50 is below the MFL for two or<br>more consecutive years or the long-term P10 is<br>below the High Minimum Lake Levels for two or<br>more consecutive years.|• <br>View Report||
|<br>|SW19<br>SR34|Use system to publish a chart or graph that compares<br>the MFL to a running average of AFL's. This should<br>reflect how the AFL's are moving along the MFL line<br>and indicate how different resources impact the MFL.<br>The resources to include are pumpage, new projects,<br>and rainfall. It will probably be run on a monthly<br>basis.|• <br>View Report||
|<br>|<br> <br>|<br> <br>|<br> <br>|<br> <br>|


22





Water Use Tracking Project – February 13, 2007
Software Requirements Specification


|Col1|4.1.1.7 Water Estimates|Col3|Col4|Col5|
|---|---|---|---|---|
||**Req ID**|**Requirement Statement**|**Use Case**||
||EW19|Ability to add estimated quantities for unmetered<br>permits, which is found in the Water Estimates<br>Database.|• <br>Maintain Water Use<br>Estimates||
||<br>_4.1.1.8 External Data_|<br>_4.1.1.8 External Data_|<br>_4.1.1.8 External Data_|<br>_4.1.1.8 External Data_|
||**Req ID**|**Requirement Statement**|**Use Case**||
||RW42|Provide access to population data in system that are<br>aggregated to appropriate geographic areas (services<br>areas, counties, etc.).|• <br>View Map||
||<br>_4.1.1.9 Crop Reports_|<br>_4.1.1.9 Crop Reports_|<br>_4.1.1.9 Crop Reports_|<br>_4.1.1.9 Crop Reports_|
||**Req ID**|**Requirement Statement**|**Use Case**||
||SW26|The ability to access crop report information spatially<br>and temporally.|• <br>View Crop Report<br>Information<br>• <br>View Map||
||<br>_4.1.1.10 Data Integration_|<br>_4.1.1.10 Data Integration_|<br>_4.1.1.10 Data Integration_|<br>_4.1.1.10 Data Integration_|
||**Req ID**|**Requirement Statement**|**Use Case**||
|<br>|RW2<br>SW16|Link between Water Use Permits (WUP),<br>Environmental Resource Permits (ERP), and Well<br>Construction Permits. One use would be as a means<br>of notifying appropriate District staff when pertinent<br>land use changes. (i.e. want to know if an ERP is<br>issued or applied for a subdivision where permit has<br>been issued for a farm.)|• <br>View Report<br>• <br>View Map||
|<br>|<br>**_4.1.2 Requirements Identified for a Possible Subsequent Release of the WUT System_**|<br>**_4.1.2 Requirements Identified for a Possible Subsequent Release of the WUT System_**|<br>**_4.1.2 Requirements Identified for a Possible Subsequent Release of the WUT System_**|<br>**_4.1.2 Requirements Identified for a Possible Subsequent Release of the WUT System_**|
||**Req ID**|**Requirement Statement**|**Requirement Statement**||
||RW11|Calculate water quality trends by geographic area.|Calculate water quality trends by geographic area.||
||SR11|Compare the population reported to the Bureau of Economic and Business<br>Research (BEBR) report.|Compare the population reported to the Bureau of Economic and Business<br>Research (BEBR) report.||
||RW47|Ability to provide external customers a means to query and view application<br>information and locations by entering spatial, temporal, or data specific<br>information. Current applications satisfying the criteria would be viewed<br>immediately; future applications would be e-mailed.|Ability to provide external customers a means to query and view application<br>information and locations by entering spatial, temporal, or data specific<br>information. Current applications satisfying the criteria would be viewed<br>immediately; future applications would be e-mailed.||
||RW21|Create a consistent grid to analyze data through time, including population, water<br>use, etc).|Create a consistent grid to analyze data through time, including population, water<br>use, etc).||
||||||


23


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


|Col1|Col2|Col3|Col4|
|---|---|---|---|
||**Req ID**|**Requirement Statement**||
||EW16|Use GIS layers to analyze how salt-water intrusion is affecting water quality, etc.<br>Layer would need to be updated either quarterly or annually.||
||RW41|Develop a link between pumpage, water quality, and water levels (both of MFL's<br>and other water bodies). The permittee has to stop pumping when certain levels are<br>reached:<br>• Augment lake when water levels are too high.<br>• Pump water when chlorides concentrations too high.<br>• Pump more out of well to pond & from pond to golf course.<br>• Use more ground water when allowed to, when also q's for surface water.||
|<br> <br> <br>|SW22<br>SW4<br>SW5<br>SW3|Need tool to be able to estimate water use (now being done in SAS). To do this<br>estimate, you need to be able to query the water use data with various variables,<br>such as time period, use types, withdrawal type (groundwater or surfacewater), and<br>geographic areas. Once the initial query is complete, you need to be able to refine<br>the resulting data set. An example is when you select active permits in a time<br>period. If a permit expired inside of the time period, the refine tool would help<br>determine if that permit would or would not be a part of the result set, perhaps by<br>determining at what point in the time line it expired.||
||RW5|Capture crop report data and link it with the corresponding use quantities, so you<br>can observe changing crop patterns, see where land has shifted out of crops, and<br>track water use per planted acre per crop to see patterns in water use by geography.<br>The accumulation (or depletion) of credits by geographic area could point out<br>potential problems in permitting in specific geographic areas. It may point to soil<br>type or local cultural practice problems. Link to requirement JY4/SR7, the report<br>of water credits used and earned.||
||SR33|Report compliance on a permit (not wells). Crop reports on permits (not wells) (I<br>think this was a requirement to report this data some how at a well level).||
||SR1|Report the Reservation from use amounts associated with some surface water.||
||SR10|Report the per capita daily water figures for the permitted amount, reported amount<br>and adjusted number for per utility. The formula for adjusted gross capita is:<br> WD + IM - EX -TL - SU - EM <br>       Population<br> <br>where:<br>WD = ground water & surface water withdrawals<br>IM = water imported/bought from another supplier<br>EX = Water exported/sold to other suppliers<br>TL = treatment loss (typically R/O or sand filtration<br>SU = Significant uses<br>EM = Environmental mitigation, if required as a District permit condition.<br>Population = Functional population||
|||||


24


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


|Col1|Col2|Col3|Col4|
|---|---|---|---|
||**Req ID**|**Requirement Statement**||
|<br> <br>|JY5<br>RW32<br>J6|Provide the ability to obtain data necessary to determine and access the population<br>estimates for an area or on a permit-by-permit basis. Needs to accommodate how it<br>is determined now and how it will be determined under the SWUCA 2 rules. This<br>would include:<br>• Seasonal residential report based on AHCA hospital report (determine seasonal<br>populations).<br>• Block group and "place" level Census Transportation Planning Package data on<br>total workers in Parts A and B for calculating net service area commuter<br>populations (the planned highway and road construction - to see commuter data<br>and areas of growth).<br>• Census group and block data (total and by age), housing units, household, and<br>group quarters population.<br>• Zip code tabulation areas (ZCTA) by age.<br>• Public Supply Service areas.<br>• Development of Regional Impact (DRI).<br>(Note: To calculate projections for service area population and water supply<br>demand the new model needs the DRI's and Road Construction layers.)||
||RW44|Access well construction data for domestic wells using locational data, such as GPS<br>or section, township, and range.||
||EW8|The external users need to be able to click on an area and obtain data for the<br>surrounding area, such as lapsed quantities, historical use, and adjacent permits.<br>Need to support decision-making on the applicant's part, especially when their<br>request does not meet the MFL requirements.||
||JY2|Make the following property appraiser data available so you can improve the<br>ability to project service area populations in inter-Census years in several ways:<br>• Provide a more discreet and up-to-date count of housing units in a utility<br>service area.<br>• Help determine when a DRI is completed.<br>• Match commercial properties by the connection data provided by utilities.<br>• Use lot sizes, where available, to determine its role in household water use<br>compared to other variables in research projects.<br>• There may be other data of use as well (wells, pools, etc).||
||<br>**4.2 WUT Use Case Model**<br>As explained above, the WUT Use Case Model has been created and is maintained within the<br>Enterprise Architect modeling software. For a detailed view of the model, the Enterprise<br>Architect tool can be used to view such items as:<br>• <br>Requirements of the system and their relationships to use cases<br>• <br>All the actors that have been identified for the system<br>• <br>The use case packages used to organize the model<br>• <br>The use cases, organized by package.<br>• <br>The actors and their interaction with the use cases|<br>**4.2 WUT Use Case Model**<br>As explained above, the WUT Use Case Model has been created and is maintained within the<br>Enterprise Architect modeling software. For a detailed view of the model, the Enterprise<br>Architect tool can be used to view such items as:<br>• <br>Requirements of the system and their relationships to use cases<br>• <br>All the actors that have been identified for the system<br>• <br>The use case packages used to organize the model<br>• <br>The use cases, organized by package.<br>• <br>The actors and their interaction with the use cases|<br>**4.2 WUT Use Case Model**<br>As explained above, the WUT Use Case Model has been created and is maintained within the<br>Enterprise Architect modeling software. For a detailed view of the model, the Enterprise<br>Architect tool can be used to view such items as:<br>• <br>Requirements of the system and their relationships to use cases<br>• <br>All the actors that have been identified for the system<br>• <br>The use case packages used to organize the model<br>• <br>The use cases, organized by package.<br>• <br>The actors and their interaction with the use cases|


25


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


The following sections will describe the various components of a use case model.


_**4.2.1**_ _**Actors**_
Over forty actors, with very specific job duties, were identified for the WUT System during a use
case workshop. All these actors were consolidated into more general categories. Since a
majority of the WUT System is reporting in nature, all the actors will have the ability to run
reports, view maps, and query water use permits (i.e., General WUT User). Only a few of the
features within the system involve the editing of data used by the system. These features will
only be available to a select few users (i.e., WUT Administrator, Water Use Estimator). Figure 1
shows all the actors that were identified during the workshops, the general categories of these
actors, as well as three non-human actors (i.e., Data Integration System, Oracle Read Only
Database, Regulatory Database).


**Figure 1 – WUT Actors**


_**4.2.2**_ _**Use Cases**_
Identifying use cases in a use case model is only the critical first step. The business processes
identified by each use case in the use case model must be described in detail in a narrative
document. This narrative describes the behaviors the resulting software system must be designed
to support. However, following the iterative nature of RUP, not all use cases are fully completed
during the initial phase of the project. A selection of critical and architecturally significant use
cases were identified to be completed during the initial phase of the project. Figure 2 below
shows the Use Case diagram illustrating all the use cases identified to-date for the WUT Project.


26


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


**Figure 2 – WUT Use Case Diagram**

The critical and architecturally significant use cases identified for the initial release have been
completed and are included in the Appendix of this document. They are:

- Process Database Replication

- Process WUT System Startup

- View Map

- View Report

- View Water Use Permit

- View Water Use Permit Search


27


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


Although not all use cases will be fully realized during the initial release of the system, a
Business Context has been created for every use case shown in the diagram in Figure 2. The
following sections contain these business contexts.


_4.2.2.1_ _Process WUT System Startup_
This use case will be used when an actor needs to access the Water Use Tracking (WUT)
System, a browser-based, distributed 3-tier client/server application initially deployed on
SWFWMD’s Intranet. To access the WUT System, the actor will request the browser to display
the WUT System Startup Page. This startup page will display information (e.g., WUT System
News) as well as provide access to the various features supported by the WUT System (e.g.,
View Water Use Permit information, performing spatial analysis using Geographic Information
Systems (GIS) maps, or running a report).

The information and features available to the actor will be controlled through the WUT System
role-based security and WUT System Roles and their associated privileges. When the actor
initially requests access, the WUT System will determine the actor’s role and this will, in turn,
determine the features available to the actor. Any actor not explicitly assigned to a WUT System
Access Criteria role (i.e., WUT Admin User, WUT Manager User) will, by default, be assigned
to the WUT System General User Role. This general role will be allowed to access all features
that are not restricted to a specific WUT user role.


_4.2.2.2_ _Generate Well Package_
This use case will be used when an actor needs to generate a well package file for import into
Groundwater Vistas to model the impact of well/withdrawal changes. The well package is a
comma-delimited file that contains many attributes, including location information, regarding
water withdrawal wells within the District. The well package is used as input into in the creation
of the District-wide Regulatory Model, as well as in the creation of regional models.


_4.2.2.3_ _Maintain Business Rule Parameters_
This use case will be used when an actor needs to update business rule parameters within the
WUT System. Generally, these parameters are used in making specific calculations within the
system. For example, information in the SWUCA II rules explicitly defines how a Lapsed
Quantity or Water Withdrawal Credits are calculated. Any parameter that could be used in a
calculation could be maintained using this use case. It is important to note that these parameters
will not be used to change the original information stored in the database, but would be used to
create "derived" data to be shown within reports or on the screen.


_4.2.2.4_ _Maintain Quick Links_
This use case will be used when an actor needs to manage the quick links located on the WUT
Home Page. These are links to other websites that could be helpful to a WUT user. For
example, a link to other water district's websites to possibly view water use permit information
could helpful. If a permit is requested near the boundary of the District, the ability to view data
from the adjacent District would be helpful in determining the impacts of the new permit.


28


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


_4.2.2.5_ _Maintain Water Use Estimates_
This use case will be used when an actor needs to maintain water use estimation values for water
use permits. The permitted quantity is known for all water use permits. However, the actual
pumpage is only known for those permittees that submit their data. For those permits that do not
submit pumpage data, their water use is estimated, based on the data that is submitted from other
wells. Currently, the water use estimates are stored in Excel spreadsheets and SAS datasets.
Currently, this data can only be viewed in summarized form in the Water Use Estimates
document published annually. This use case will allow the actor to import water use estimate
data for each water use permit into a database table that can be used by the WUT System. This
will allow users of the system to view pumpage data, as an estimated value, even for permittees
that do not submit their pumpage information.


_4.2.2.6_ _Maintain WUT News_
This use case is used when the actor needs to maintain WUT news items for communication to
users when they access the WUT Home Page. For example, the system administrator may need
to inform WUT users that the system will be down for maintenance over the weekend. Using
this feature, the system administrator can create a system maintenance news item for display
starting and ending on specified dates. Displaying news on the WUT Home Page ensures that all
users will have access to this important information when they first access the application.


_4.2.2.7_ _Process Database Replication_
This use case will be used when an actor needs to replicate and normalize (restructure) data that
has been copied directly from a DB2 database on the IBM mainframe to a read-only Oracle
database. The current data structure was implemented to support a data entry system and not for
the use in a decision support reporting system. The data is being restructured to take advantage
of the strengths of a relational database management system. After the initial replication of the
DB2 tables, nightly updates are made to the Oracle tables with the data that has changed since
the previous replication process. By normalizing the data into relational tables, it will allow the
data to be more accessible using ad-hoc query tools.


_4.2.2.8_ _View Change in Use Type or Owner_
This use case will be used when an actor needs to view information about the relocation of
permitted quantities associated with a specific water use permit. When an application is made to
relocate permitted quantities and change the use type or owner of an existing permitted quantity
that impacts an MFL waterbody that is below its minimum level, the application is subject to
certain criteria. The previously permitted quantity is first reviewed under the reasonable
beneficial use test. The quantity available for the new owner or new use type is limited to 90
percent of the permitted historically used portion of the reasonable-beneficial quantity, not
including any Drought Credit quantities. This 10 percent reduction in historically used permitted
reasonable-beneficial quantity impacting the MFL waterbodies constitutes a Net Benefit.

If any reasonable beneficial, historically unused quantities will remain on the source permit,
these quantities are also reduced by the Net Benefit provision (i.e., 10 percent) and are available
only for the existing use type at the source permit site. If any reasonable-beneficial, historically


29


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


used quantities will remain on the source permit, these quantities are not subject to the Net
Benefit provisions and may be used for the existing use type. Any future application to modify
the use type or owner, or to relocate with a change in use type or owner, these remaining
reasonable-beneficial, historically used quantities will be subject to the Net Benefit provisions.
Any historically unused quantities remaining at the source permit site may not be relocated in the
future and may not have a change in use type.

The following information will be displayed pertaining to the relocation of a WUP:

- Historical used quantity

- Historical unused quantity

- Reasonable beneficial quantity

- The WUP that the relocated amount came from

- The WUP that the relocated amount went to

- The dates that any of these values took affect or changed


_4.2.2.9_ _View Compliance Information_
This use case will be used when an actor needs to view Compliance data associated with a
specific water use permit. Depending on the data submitted by the permittee, compliance data
could include pumpage quantities, meter readings, crop reports, well construction specifications,
and any other condition data associated with a water use permit. Providing compliance
information will give District staff time-saving devices with which they can better monitor the
enforcement activities of the District, with minimal impact to staff time. Better access to those
who are not submitting pumpage information will help evaluators better determine the site
conditions while evaluating the impacts of new applications in the same area.


_4.2.2.10_ _View Crop Report Information_
This use case will be used when an actor needs to view crop report data associated with a
specific permit. Crop report data is collected on an annual or semi-annual basis and is submitted
by the permittee. A different form is submitted for recreational use, annual crops, and seasonal
crops. It contains the crop or use type, acreage for each use, predominate soil type, and planting
dates. The data submitted with crop reports, in many cases, is not audited for accuracy, and is
often incomplete or inaccurate. The primary purposes of this form are to verify the actual soil
type for the location so that more accurate water allocations can be made, link the actual ground
conditions to the use information in the database, and monitor the use of water conserving
credits.


_4.2.2.11_ _View Land Use Information_
This use case will be used when an actor needs to view land use data associated with a specific
water use permit. Possible scenarios include viewing trends for specified areas or determining
how water use changed as land use changes.

Land use data can be collected during permit submittal or as conditions set on a permit, as well
as from map analysis. Permittees will supply land use information as water use code types or
from crop reports submitted for certain WUPs. Map analysis is conducted from the land use


30


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


layer derived from Florida's land use cover classification system (FLUCCS), color infrared (CIR)
digital orthophoto quarter quadrangles (DOQQs), or other aerial photography.


_4.2.2.12_ _View Lapsed or Project Quantities Summary_
This use case will be used when an actor needs to view lapsed or project quantities data
associated with a specific water use permit. With the implementation of the new SWUCA rules,
this process will allow the actor to track these quantities.

Most of the land within the SWUCA is associated with an existing water use permit. Over time,
permits are reduced, abandoned due to land use changes or abandonment of an activity, retired
due to acquisition of land for preservation purposes, or by other means. Historically, this permit
activity has resulted in an overall reduction in water use. Now, however, these lapsed quantities
will be available for new and expanding water users to meet their needs. Another way for a
water use permit applicant to get water that meets their needs is by the use of quantities that are
associated with District projects.


_4.2.2.13_ _View Map_
This use case will be used when an actor needs to view water use permit (WUP) information
spatially using a map created with the functionality provided by a Geographic Information
Systems (GIS). Viewing WUP information in a pre-defined report format can be very effective
from the point of view of efficiency, organization, and the presentation of large amounts of data.
Even so, a report is simply a one-dimensional presentation of information when that information
has at its basis a spatial context. When viewing WUP information in a report, the subtlety and
complexity of the spatial relationships cannot be presented at all or is, at best, difficult to
comprehend.  The viewing of information within its spatial context is exactly where GIS excels
and is the primary reason for this View Map Use Case. When additional GIS layers are added to
a map, the multi-dimensional presentation of information provides for a richness of analysis
simply not possible using a report format.

Although not intended exclusively for this actor, one of the primary actors who will use this use
case is the WUP Evaluators. They are responsible for the analysis of all new, modified, and
renewed WUPs. During the analysis process, the evaluator will frequently require access to a
map to view WUP data within its spatial context. Doing so will enable the evaluator to view
other important data within the area of interest resulting in a far richer analytical effort. By
having the ability to add different GIS layers to the map, the evaluator will have more
information at their disposal to assist in their analytical effort. Add to this the capability to pan,
zoom, and print at any time, the evaluator will have all the information and functionality required
to make better, more informed decisions.


_4.2.2.14_ _View Mitigation of MFL Impacts_
This use case will be used when an actor needs to view information of how a specific water use
permit has mitigated its impact on a MFL waterbody. When an applicant demonstrates
compliance with all conditions for issuance, except that it impacts a minimum flow or level
waterbody, the applicant can apply for a permit if they provide a Net Benefit to the impacted
MFL waterbody. This mitigation strategy could include the proposition of a water resource

31


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


development project that more than negates their proposed impact or it could be the purchasing
of adjacent land with water use permits for their own use.

The following information will be displayed to show the mitigation of MFL impacts:

- The permits and their quantities that were bought out to mitigate the MFL impact

- The District’s projects and their quantities used to mitigate the MFL impact

- The self-funded projects and their quantities used to mitigate the MFL impact


_4.2.2.15_ _View Net Benefit Summary_
This use case will be used when an actor needs to analyze Net Benefit data associated with a
specific water use permit. With the implementation of the new SWUCA rules, this process will
allow the actor to track the Net Benefits. A Net Benefit is obtained when the proposed
withdrawal, coupled with other activities or measures, will result in an improvement to the MFL
waterbody that more than offsets the impact of the withdrawal. In all Net Benefit options,
reasonable beneficial use plays a key part. Permits are granted based upon meeting numerous
rule criteria including that the quantities requested are fully needed for the proposed use, or
existing use in case of a renewal.

The applicant for a new permit or for a modification or renewal of an existing permit is required
to file detailed information to demonstrate and justify to the reasonable satisfaction of the
District the reasonable beneficial quantities intended to be used during the term of the proposed
permit before it will be issued. This requirement is intended to assist the District in seeking to
reduce the difference between permitted quantities and used quantities. For those cases in which
an applicant is seeking a modification or renewal of an existing permit, the District will consider
historical use, metered pumping data, trends and patterns of usage, actual type of usage, and
other relevant factors.

A Net Benefit can be obtained in several ways including:

- Relocation with a change in use type or owner

- Water withdrawal credits

- Mitigation of minimum flow and level impacts

There are several ways that the District is going to gain water with the new SWUCA rules, from
reclaimed water lines, lapsed quantities, water withdrawal credits, and the relocations rules.


_4.2.2.16_ _View Report_
This use case will be used when an actor needs to produce a report from within the WUT Report
Library. It is anticipated that the WUT System will have a large number of reports available in
its report library. Every report use case within the WUT Report Library will extend this use case
as appropriate for the specific report.

A report in this library provides information in a pre-defined format. While the information
content of the report is pre-defined, the system enhances the flexibility of the report by providing
the actor with the capability to optionally limit the information in any given report to the actor’s


32


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


specific area of interest (e.g., a specific county). This is accomplished through report
specifications. While a given report may be run frequently, the information content will often
vary from report to report based upon the run-time report specifications given by the actor.

This use case provides support for the numerous reports within the WUT Report Library. Once
the actor specifies the report of interest and optionally supplies any run-time report criteria, the
system will retrieve the information for the actor and present it in the pre-defined format. The
actor can then choose to simply view the report online or download the report for analysis,
printing, or saving as an electronic file in a variety of supported formats.


_4.2.2.17_ _View Resource Information_
This use case will be used when an actor needs to view water resource data associated with a
specific water use permit. The water resource data is collected by the permittee, and varies
depending on the requirements of the permit including water quality data, water flows and levels,
total dissolved mineral levels (TDML), and rainfall amounts.


_4.2.2.18_ _View Use of Lapsed Quantities_
This use case will be used when an actor needs to view the use of lapsed quantities associated
with a specific water use permit. Historically, reduced, abandoned, and retired permits have
resulted in an overall reduction in water use. But now, these quantities will be a primary means
for many new or expanding water users to meet their needs. Where an applicant demonstrates
compliance with all conditions for issuance, except that it impacts an MFL waterbody, the
applicant can apply for up to 90% of the water it has identified as historically used by a water use
permit holder that has permanently discontinued their use and abandoned their permit. The
applicant must also demonstrate that other Net Benefit options, including relocation, mitigation,
participation in a District Source Augmentation Project, are not feasible. This Net Benefit
provision applies only when the previous water use was derived from a source where the
permanently discontinued use had a similar or greater effect on the impacted MFL waterbody as
the proposed use.

One of the main goals of the WUT System is to track changes in permitted and used quantities so
that historically used, reasonable beneficial quantities potentially available from reduced,
abandoned, or retired permits and their relation to MFL waterbodies will be known for potential
applicants and for District decision making. Quantities of water retired from land acquisition
programs are included for use as lapsed quantities unless the acquiring agency specifically
requests for them to be excluded from use.

The following information will be displayed pertaining to lapsed quantities associated with
reduced, abandoned, and retired permits:

- The quantities a retired WUP has contributed to another WUP

- The quantities a WUP has received from a retired WUP

- The retired WUP that a lapsed quantity came from

- The quantities from the retired WUP available as lapsed quantities

- The WUP that a lapsed quantity went to


33


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


- Whether a WUPs quantity has been excluded from the lapsed quantity pool as a result of a
land acquisition program

- The dates that any of these values took affect or changed


_4.2.2.19_ _View Use of Quantities Associated With District Projects_
This use case will be used when an actor needs to view the quantities used from District Source
Augmentation Projects associated with a specific water use permit. Where applicants
demonstrate compliance with all conditions for issuance except that it impacts an MFL
waterbody, the applicant can apply for the source augmentation accomplished through a District
water resource development project, provided that the source of supply is the same source being
augmented.


_4.2.2.20_ _View Water Use Permit_
This use case will be used when an actor needs to view information about a specific water use
permit. This water use permit information is collected at the time the permit is submitted and
approved by the District. A water use permit is required from the District when:

- Total capacity of the permit is greater than or equal to 1 million gallons per day

- Total annual average quantities for the permit is greater than or equal to 100,000 gallons per
day

- Well diameter is greater than or equal to 6 inches

- Surface water withdrawal pipe diameters are greater than or equal to 4 inches

- Cumulative well diameters greater than or equal to 6 inches, if in MIA and constructed after
April 11, 1994, and is not a replacement well of same or smaller diameter of one being
plugged

- If withdrawal is likely to cause significant adverse impacts to existing water or land uses, or
the surrounding water resources

The actual area of the permit is digitized as a polygon into a GIS layer based on color infrared
(CIR) digital orthophoto quarter quadrangles (DOQQs). The general data that is collected with
the permit includes the permittee information, acreage amounts, permitted quantities, water use
information, expiration date, and aquifer information. This information will be displayed to the
actor, with the option to "drill-down" to get more detailed information, such as well information
or actual pumpage quantities.


_4.2.2.21_ _View Water Use Permit Search_
This use case will be used when an actor needs to search for and identify a water use permit for
analysis. This use case, as well as the View Map Use Case, is considered among the class of
Find use cases. A Find use case provides the capability to identify, locate, and access
information within the WUT System, as it pertains to a water use permit. The View Water Use
Permit Search use case enables the actor to efficiently and effectively search for and identify
permits that meet a given search criteria. The system returns basic information about the permit
with the ability to get more detailed information regarding the permit (i.e., wells, Net Benefits,
compliance data). This use case is used in support of the View Water Use Permit Use Case.


34


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


_4.2.2.22_ _View Water Withdrawal Credit_
This use case will be used when an actor needs to view water withdrawal credit information
associated with a specific water use permit. A water withdrawal credit is an incentive for an
applicant to provide other water use permit holders with alternative supplies. The holder of the
credits can use them to provide a Net Benefit in order to obtain water from an MFL waterbody
because the overall impact will be an improvement. The applicant (Supplier) provides an
alternative supply to offset actual withdrawals from an existing permit holder (Receiver). The
credit is 50% of the offset amount. The discontinued quantities are placed in a standby permit
and are given back to the Receiver in the event the Supplier ever stops providing the alternative
source, essentially giving the Receiver their original quantity back.

The following information will be displayed pertaining to the water withdrawal credits for a
WUP:

- The offset quantity coming from an alternative source

- Where the alternative source coming from

- The Supplier of the alternative source

- The Receiver of the alternative source

- The distribution of the credit (50% of the offset) between the Supplier and Receiver

- The discontinued quantities to be stored in a standby permit

- The dates that any of these values took affect or changed


_4.2.2.23_ _View Well Construction Information_
This use case will be used when an actor needs to view well construction information that is
associated with a specific water use permit. Well construction information is gathered during the
construction and permitting of the wells. This information includes well depth, casing depth,
well diameter, status code, drilling method, and completion date. When a well also requires a
Water Use Permit, some of this information is entered in both the Well Construction database
and the Water Use Permit Well database. The two tables are loosely linked. When the Water
Use Permit and well number are entered into the Well Construction database, a link is created to
that permit in the Water Use Permit Well database. The actual information in the table is not
updated, but another page of well construction information (well construction number,
completion date, diameter, total and case depth, and well status) is available to view, but only on
the specified revision. The well completion information in the Well Construction database is
considered to supersede the WUP Well information, which can contain estimated data. Depth
information is important in determining what aquifer a well is pumping water from so the
drawdown impacts for new water use can be calculated accurately.


_4.2.2.24_ _View Withdrawal Pumpage Information_
This use case will be used when an actor needs to view withdrawal pumpage information
associated with a specific water use permit. Pumpage data is collected at certain wells and
estimated for others based on several categories of water and land use. Most pumpage data is
collected on a monthly basis, either through a permittee submittal or a utility company meter
reading. Based on these actual values, other wells that are not metered can be estimated.
Permittees submit their readings by mail, e-mail, or the Internet. The older permits are required


35


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


|to submit actual pumpage values, while new permits submit the meter readings that are then used<br>to calculate the actual pumpage amount.<br>4.2.3 WUT Supplementary Specification<br>The WUT Supplementary Specification will organize all non-functional requirements into the<br>following qualitative categories:<br>• Usability<br>• Reliability<br>• Performance<br>• Supportablity<br>For each category within the supplementary specification, the following information will be<br>provided:<br>Non-Functional Requirement Category<br>The name of the non-functional requirement category<br>Non-Functional Requirement Category Definition<br>For each qualitative systems requirements category, a definition of the category will be provided.<br>For each general systems requirements category, an overview of the category will be provided.<br>Non-Functional Requirements<br>A matrix of all non-functional requirements identified to date for the WUT Project in the form of<br>a statement and organized by category. Similar to the Requirements Traceability Matrix, the<br>following will be provided for each non-functional requirement:<br>• Req ID – A unique identifier for each non-functional requirement<br>• Requirement Statement – Individual WUT non-functional requirements statements expressed<br>as a request.<br>4.2.3.1 Usability<br>Usability is defined as the ease with which a user can learn to operate, prepare inputs for, and<br>interpret outputs of a system or component.|Col2|
|---|---|
|**Req #**|**Requirement Statement**|
|EW15|Need quick access to currently published information to base decisions on.|
|EW17|Replicate the DB2 data daily in Oracle.|
|EW22|Support consistency in decision-making among various users.|
|RW12|Hire a metadata librarian to manage data associated with the Water Use Tracking<br>project.|
|RW26b|The value you enter should be the actual data value, not any code number associated<br>with it.|
|RW35|Have consistent way to report on permit status and withdrawal status.|
|RW43|Develop and make readily accessible metadata for the data (i.e. need to know the time<br>frames when the data is considered to be good).|
|||


36


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


|Col1|Col2|
|---|---|
|**Req #**|**Requirement Statement**|
|SW10|System has to be user-friendly.|
|SW12|Ability to customize queries.|
|SW2|A process needs to be established so corrections to the source data sets can be<br>initiated, i.e. when errors are discovered when running models.|
|SW23|The same datasets need to be used by all departments or sections of the District.|
|SW27|Need to receive job-specific training and support.|
|SW7|The data has to be available in real time.|
|TW17|Clear documentation that lends to the defensibility of system for when permits are<br>denied or modified.|
|TW18|Clear documentation that lends to the defensibility of system for when permits are<br>denied or modified.|
|TW19|Could have wizards to help users perform tasks.|
|TW20|Have a decision tree for the help desk personnel that will receive questions.|
|TW27|Clear hours of availability need to be established.|
|TW3|System has to have the flexibility to handle different scenarios, or "what-if" questions,<br>or 1-10,2-10, and 5-10 drought events.|
|TW31|Need on-line help and training.|
|TW32|Need training material for in-house training.|
|TW35|Need to be able to save (or download) the results of queries into an outside system.|
|TW7|Has to manage the metadata, and metadata has to be FGDC compliant.|
|<br>_4.2.3.2 Reliability_<br>Reliability is defined as the ability of a system or component to perform its required functions<br>under stated conditions for a specified period of time.<br>|<br>_4.2.3.2 Reliability_<br>Reliability is defined as the ability of a system or component to perform its required functions<br>under stated conditions for a specified period of time.<br>|
|**Req #**|**Requirement Statement**|
|EW18|Update interval protocols for updating different data types.|
|RW17|Populate missing data in the database, especially permits and pumpage reports.|
|SW1|The results from queries need to be consistent and reliable over time.|
|SW14|The tools the system will use to access the data need to be better than what is<br>available now.|
|SW8|The data has to be accurate.|
|<br>_4.2.3.3 Performance_<br>Performance is defined as the degree to which a device or system fulfills its specifications.<br>|<br>_4.2.3.3 Performance_<br>Performance is defined as the degree to which a device or system fulfills its specifications.<br>|
|**Req #**|**Requirement Statement**|
|EW3|Application must fit into statutory time frames for evaluating permitting applications,<br>so there must be a quick turn-around time.|
|TW28|Reasonable refresh rates.|
|TW30|Need to establish response rates if it will be on a web page.|
|||


37


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


|4.2.3.4 Supportability – Definition<br>Supportability is defined as the ability of the system to be supported by the resources required for<br>specific maintenance tasks. For large complex systems, supportability considerations will be<br>significant and will have a major impact upon the total life cycle cost. It is therefore particularly<br>important that the appropriate level of supportability is determined in relation to other system<br>characteristics and cost.|Col2|
|---|---|
|**Req #**|**Requirement Statement**|
|SW13|Data to support requirements must exist in the database, and be readily available.|
|TW21|Get compilable versions of code stored in SourceSafe.|
|TW22|Do not use SDE log files.|
|TW23|Be consistent in naming and terminology conventions.|
|TW24|A web application is preferred. If ArcMap, has to be able to run in Citrix ArcView.|
|TW25|If toolbars are written, must be in .dll format.|
|TW26|Consider the ease of deployment of application.|
|TW29|Can extend the current District architecture, i.e. Oracle Spatial, if needed.|
|TW33|Need technical documentation for maintainability.|
|TW34|Follow District change management standards.|
|TW36|Do not join features based on the shape column.|
|TW5|System should be written in map.net – either VB or C#.|
|TW6|Follow District programming standards.|
|||


38


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


# **Appendix A – Use Cases**

1. Process Database Replication
2. Process WUT System Startup
3. View Map
4. View Report
5. View Water Use Permit
6. View Water Use Permit Search


39


Water Use Tracking Project – February 13, 2007
Software Requirements Specification


