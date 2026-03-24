---
consensus_grade_level: 13.4
headings_per_sentence: 0.02
lists_per_sentence: 0.04
smao_sentences_pct: 6.9
vague_words_per_sentence: 0.09
anaphora_per_sentence: 0.24
sentence_cv: 1.335
cpre_terms_per_sentence: 1.03
---
## **Clarus Weather System Design**
### **DETAILED** **SYSTEM REQUIREMENTS** **SPECIFICATION**

##### December 2005 **Prepared By:**



Mixon/Hill, Inc.
12980 Metcalf Ave.
Suite 470
Overland Park, KS 66213
(913) 239-8400



Oklahoma Climatological Survey
100 East Boyd Street
Suite 1210
Norman, Oklahoma 73019
(405) 325-2541



Cambridge Systematics, Inc.
100 CambridgePark Drive
Suite 400
Cambridge, MA 02140
(617) 354-0167



Stephenson Group
400 Colony Square
Suite 200
Atlanta, Georgia 30361
(404) 699-9003



All documentation, software, and data related to this project are proprietary and
copyrighted. Use is governed by the contract requirements as defined in the U. S.
Department of Transportation Federal Highway Administration Contract No. DTFH61-05-C00022. Unauthorized use of this documentation is a violation of law except as provided for
in said contract.


Copyright © 2005 Mixon/Hill, Inc. All rights reserved.


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_

##### **Table of Contents**


**1** **INTRODUCTION..................................................................................................... 1**


**1.1** **Purpose............................................................................................................................................ 1**


**1.2** **Scope................................................................................................................................................ 3**


**1.3** **Definitions, Acronyms, and Abbreviations .................................................................................. 4**


**1.4** **References....................................................................................................................................... 5**


**1.5** **Overview ......................................................................................................................................... 6**


**2** **GENERAL DESCRIPTION.................................................................................... 8**


**2.1** **System Perspective......................................................................................................................... 8**


**2.2** **System Functions.......................................................................................................................... 10**


**2.3** **User Characteristics..................................................................................................................... 15**


**2.4** **General Constraints..................................................................................................................... 19**


**2.5** **Assumptions and Dependencies .................................................................................................. 20**


**3** **SYSTEM ARCHITECTURE ................................................................................ 21**


**4** **SPECIFIC REQUIREMENTS.............................................................................. 23**


**4.1** **Configuration & Administration Service (CAS) ....................................................................... 28**


**4.2** **Configuration & Administration User Interface (CAUI)......................................................... 33**


**4.3** **Collector Services (CS) ................................................................................................................ 36**


**4.4** **Watchdog (DOG) ......................................................................................................................... 45**


**4.5** **Environmental Metadata Cache (EMC) .................................................................................... 46**


**4.6** **Environmental Metadata Services (EMS).................................................................................. 49**


**4.7** **Manual Entry User Interface (MEUI)........................................................................................ 53**


**4.8** **Qualified Environmental Data (QEDC)..................................................................................... 53**


**4.9** **Qualified Environmental Data Services (QEDS)....................................................................... 56**


**4.10** **Quality Checking Services (QChS)............................................................................................. 66**


**4.11** **Schedule Service (SS)................................................................................................................... 73**



_04037-rq301srs0200_

_Page ii_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


**4.12** **Program Requirements................................................................................................................ 74**


**APPENDIX A -** **DEFINITIONS, ACRONYMS, AND ABBREVIATIONS .......... 87**


**APPENDIX B -** **SUPPLEMENTAL DESCRIPTION OF** _**CLARUS**_ **QC TESTS... 90**

##### **Table of Figures**


FIGURE 1 – SYSTEM ARCHITECTURAL DESCRIPTION CONTEXT................................................... 2
FIGURE 2 – _CLARUS_ DATA ACQUISITION, PROCESSING, AND PUBLICATION............................. 9
FIGURE 3 – BASIC _CLARUS_ SYSTEM OBJECTS AND FUNCTIONS.................................................. 11
FIGURE 4 – TIME HORIZONS FOR WEATHER DATA......................................................................... 14
FIGURE 5 – _CLARUS_ USER LAYERS AND TIME HORIZON RELATIONSHIPS................................ 16
FIGURE 6 – CONTEXT DIAGRAM OF _CLARUS_ USER NEEDS............................................................ 17
FIGURE 6 – DATA FLOWS WITHIN THE _CLARUS_ SYSTEM............................................................... 21
FIGURE 7 – HIGH-LEVEL REQUIREMENTS CONTEXT...................................................................... 23

##### **Table of Tables**


TABLE 1 – POTENTIAL _CLARUS_ ENVIRONMENTAL DATA ELEMENTS........................................ 13
TABLE 2 - EXPLANATION OF THE REQUIREMENTS TABLES ........................................................ 26
TABLE 3 – REQUIREMENT ID FORMAT............................................................................................... 26
TABLE 4 – ALLOCATION FORMAT....................................................................................................... 27


**Revision History**

|Revision|Issue Date|Status|Authority|Comments|
|---|---|---|---|---|
|00.05|October 2005|Draft|DTFH61-05-C-<br>00022|For Task Force review|
|01.00|December<br>2005|Final|DTFH61-05-C-<br>00022||



**Electronic File**

Saved As: **04037-rq301srs0200_Final_Detailed_Requirements**



_04037-rq301srs0200_

_Page iii_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_

##### **1 INTRODUCTION**

###### **_1.1 Purpose_**

The purpose of this requirements specification is to provide a repository for the
high-level and detailed requirements governing the design of the _Clarus_ system.
These requirements capture the expression of general needs in the _Clarus_ Concept
of Operations (ConOps), in meetings with potential users and participants, and in
subsequent documents identified below. These requirements will form the basis
for the design verification and validation of the system. The intended audience for
this document includes decision makers, stakeholders, designers, and testers.

This document may be updated periodically to reflect changes in the system
requirements, including changes reflected in subsequent versions of the system.

As indicated in the highlighted box in Figure 1, the Detailed Systems
Requirements Specification (DRS) is an intermediate deliverable in the larger
context of the _Clarus_ Weather System Design project, using criteria documented
in the Concept of Operations, High-Level Requirements Specification, Survey of
Environmental Sensor Stations, Analysis of COTS Systems, Analysis
Architectural Alternatives Analysis, and the Design Gaps Analysis as input to the
DRS.



_04037-rq301srs0200_

_Page 1_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_

# Clarus System Design Deliverables

































_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._







AAA – Architectural Alternatives Analysis
ConOps – Concept of Operations
COTS – Systems Engineering Analysis of _Clarus_ -Related Systems
DRS – Detailed Requirements Specification
ESS – _Clarus_ ESS Survey
GAP – Design Gaps Analysis
HRS – High-Level Requirements Specification





POCDP – Proof-of-Concept Deployment Plan
POCDR – Proof-of-Concept Demonstration Report
POCTP – Proof-of-Concept Test Plan
POCTR – Proof-of-Concept Test Results
SAD – System Architectural Description
SDD – System Design Document
SGAP – Solution to Fill Design Gaps





**Figure 1 –** _**Clarus**_ **System Documentation**


_04037-rq301srs0200_

_Page 2_


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_

###### **_1.2 Scope_**

_Clarus_ is an initiative sponsored by the U.S. Department of Transportation (U.S.
DOT) to organize and make more effective environmental and road condition
observation capabilities in support of four primary motivations.

1) Provide a North American resource to collect, quality check, and make
available surface transportation weather and road condition observations
so that State Departments of Transportation (DOTs) and other
transportation agencies can be more productive in maintaining safety and
mobility on all roads and surface transportation platforms. In addition to
increasing productivity, it will maximize their RWIS/ESS investments.

2) Surface transportation-based weather observations will enhance and
extend the existing weather data sources that support general purpose
weather forecasting for the protection of life and property.

3) Collection of real-time surface transportation-based weather observations
will support real-time operational responses to weather.

4) Surface transportation-based weather observations integrated with existing
observation data will permit broader support for the enhancement and
creation of models that make better predictions in the atmospheric
boundary layer and near the earth’s surface to support more accurate
forecasts.

The intent of the _Clarus_ Initiative is to demonstrate how an open and integrated
approach to observational data management can be used to collect, control the
quality of, and consolidate surface transportation environmental data. The _Clarus_
Initiative will address the necessary infrastructure to consolidate the data from a
multitude of independent data collection systems. This process offers the prospect
of enhancing data coverage, improving the performance of meteorological support
services, and providing guidance to owners of these data sources regarding the
quality of their data and performance of their data collection systems.

_Clarus_ represents the next step in bringing together surface transportation best
practices and the greater weather community. Surface transportation
environmental data collected by the _Clarus_ system will include atmospheric data,
pavement data [1], and hydrologic (water level) data.

The _Clarus_ Initiative consists of two development components.

       - The first component is the development of the _Clarus_ system – a network
for sharing, quality checking, and exchanging surface environmental data
and relevant surface transportation conditions.

       - The second component is the development of tools (such as decision
support systems) that make effective use of the _Clarus_ system.


1 “Pavement data” in this context includes surface and subsurface data specified in NTCIP 1204 (Ref. 8).



_04037-rq301srs0200_

_Page 3_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


The addition of _Clarus_ system data to national weather observations will further
enhance general purpose weather forecasting, providing a wider range of benefits
to the protection of life and property.

Data from the _Clarus_ system will have a wide variety of direct and indirect uses.
Users having the most immediate contact with the _Clarus_ system will include the
owners and operators of the observing systems that are providing information to
the _Clarus_ system, as well as the users directly accessing the data contained
within the _Clarus_ system. The following is an initial list — which will likely grow
as the initiative progresses — of these stakeholders:

       - Observation system owners including federal, state, local, and private
institutions;

       - Instrument and observation platform suppliers;

       - Direct data users including system owners and their contractors;

       - Surface transportation weather service providers (which may include the
observation system owners – e.g., state DOTs);

       - The National Oceanic and Atmospheric Administration (NOAA);

       - General weather service providers;

       - Research and engineering community; and

       - Climate data warehouse and other non-surface weather interests.

The deployed _Clarus_ system is envisioned to include:

       - A one-stop Internet portal for all surface transportation environmental
observations;

       - Data provided with and without post-processing, ready to be incorporated
into value-added products including weather and traffic models as well as
decision support systems;

       - Continuous quality checking of data with feedback to operators of the
originating sensor stations;

       - Data transferred in one common protocol with full metadata;

       - Management of users’ rights to input or extract specific data components;

       - Data retrieval tools; and

       - Support for the inclusion of new technologies such as vehicle-based
sensors, surface visibility information from traffic cameras, and remote
sensing technologies.

###### **_1.3 Definitions, Acronyms, and Abbreviations_**

This document may contain terms, acronyms, and abbreviations that are
unfamiliar to the reader. A dictionary of these terms, acronyms, and abbreviations
can be found in Appendix A.



_04037-rq301srs0200_

_Page 4_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_

###### **_1.4 References_**

The following documents contain additional information pertaining to this project
or have been referenced within this document:

1. _Clarus – The Nationwide Surface Transportation Weather Observing and_
_Forecast System_ ; Pisano, Pol, Stern, and Goodwin; TRB 2005.

2. _National ITS Architecture, Version 5.0_ ; FHWA, U.S. DOT; October 2003.

3. _Weather Information in the National ITS Architecture Version_ 5.0;
Meridian Environmental Technology, Inc.; August 2004.

4. _Clarus Initiative Coordinating Committee (ICC) Management Plan_
(Revision 1); James Pol, U.S. DOT; September 2004.

5. _Surface Transportation Decision Support Requirements,_ _Version 1.0_ ;
Mitretek Systems, Inc.; January 2000.

6. _Weather Information for Surface Transportation: National Needs_
_Assessment Report_ ; Office of the Federal Coordinator for Meteorology;
FCM-R18-2002; December 2002.

7. _Weather and Environmental Content on 511® Services_ ; 511 Deployment
Coalition; June 2003.

8. _NTCIP 1204 v02.23b NTCIP Environmental Sensor Station Interface_
_Standard – Version 02_ ; National Electrical Manufacturers’ Association,
American Association of State Highway and Transportation Officials, and
Institute of Transportation Engineers; 2005.

9. _Where the Weather Meets the Road: A Research Agenda for Improving_
_Road Weather_ ; The National Academies; BASC-U-02-06-A; 2004.

10. _Road Weather Information Systems (RWIS) Data Integration Guidelines_ ;
Castle Rock Consultants; October 2002.

11. _Draft Report: Joint TMC/TOC System Integration Study for Emergency_
_Transportation Operations and Weather: Baseline Conditions_ ; Battelle;
2004 (in review).

12. _Clarus Final Draft Concept of Operations;_ Iteris and Meridian
Environmental Technology, Inc.; June 24, 2005.

13. _IEEE Recommended Practice for Software Requirements Specifications_ ;
Software Engineering Standards Committee of the IEEE Computer
Society; IEEE Standard 830-1998, June 25, 1998.

14. _Security of Federal Automated Information Resources_ ; Appendix III to
OMB Circular No. A-130; Office of Management and Budget; February 8,
1996.


15. _Clarus Weather System Design – High-level System Requirements_
_Specification_ ; Mixon/Hill, Inc.; July 2005.



_04037-rq301srs0200_

_Page 5_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


16. _Clarus Weather System Design – System Architectural Description;_
Mixon/Hill, Inc.; October 2005.


17. _Clarus Weather System Design – Clarus ESS Survey_ ; Cambridge
Systematics, Inc.; September 2005.

18. _Clarus Weather System Design –_ _Systems Engineering Analysis of Clarus-_
_Related Systems;_ Mixon/Hill, Inc. and Oklahoma Climatological Survey;
September 2005.

19. _Clarus Weather System Design –Architectural Alternatives Analysis_ ;
Mixon/Hill, Inc.; September 2005.

20. _Clarus Weather System Design –_ _Design Gaps Analysis_ ; Mixon/Hill, Inc.;
October 2005.


Some portions of the _Clarus_ Concept of Operations (Ref. 12) have been
incorporated in this document, both for continuity of concept, and to help identify
the basis for the high-level and detailed requirements. Specific attributions of this
content are only included where they enhance the context of the requirements.

###### **_1.5 Overview_**

The organization and content of this document is generally based on the IEEE
standards for System Requirements Specifications (Ref. 13). The requirements
presented in this document represent the high-level and detailed objectives,
constraints, and desires for the _Clarus_ system.

Each requirement is identified by a unique _Clarus_ -specific identifier to allow the
requirement to be referenced in future documents, providing traceability
throughout the development process. Each detailed requirement is traced to its
parent through its identification number followed by a unique identifier.

A requirements document states what must be accomplished to fulfill the vision
described in a concept of operations. It does not state how it is to be
accomplished. This document describes each requirement and the basis for
inclusion of that requirement.

The remaining sections of the document contain the requirements for the system.
The sections and their content are as follows:

**Section 2 – General Description** provides a general overview of the
entire system. This section describes the general factors that affect the
system and its requirements.

**Section 3 – System Architecture** provides an overview of the _Clarus_
system’s components and their functions. Specific requirements in the
next section are allocated to and organized according to these components.

**Section 4 – Specific Requirements** contains the requirements developed
from reference documentation and stakeholder communications. This
section organizes the requirements into categories that facilitate the system



_04037-rq301srs0200_

_Page 6_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


development process. The categories in this document are: Configuration
& Administration Service (CAS), Configuration & Administration User
Interface (CAUI), Collector Services (CS), Watchdog (DOG),
Environmental Metadata Cache (EMC), Environmental Metadata Services
(EMS), Qualified Environmental Data (QEDC), Qualified Environmental
Data Services (QEDS), Quality Checking Services (QChS), Schedule
Service (SS), and program requirements.



_04037-rq301srs0200_

_Page 7_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_

##### **2 GENERAL DESCRIPTION**

This section provides an overview of the entire system and describes the general
factors that affect the system and its requirements. This section does not state
specific requirements, but instead is intended to make the requirements easier to
understand by giving them context. That context and the overall intent of the
_Clarus_ program are described in detail in the _Clarus_ Concept of Operations (Ref.
12), from which much of the description in this section was derived.

###### **_2.1 System Perspective_**

The _Clarus_ Initiative is essentially a plan to create a “network of networks” —
much like the Internet — for surface transportation environmental data. While the
Internet is an interconnection of computer networks, _Clarus_ will be an
interconnection of environmental (weather, pavement, and water level condition)
data collection networks. Each of the weather networks will function
autonomously; they will collect information and disseminate it internally without
direction or dependence on _Clarus_ .

Each participating weather network’s connection to _Clarus_ will add two new
possible modes of functionality. First, the participants will be able to _share_
_collected environmental data_ with _Clarus_ . Second, participants will be able to
_receive environmental data_ collected by _Clarus_ . The primary recipients of this
data will be weather service providers, but any _Clarus_ participants would be able
to receive data if they so chose. This concept of autonomous data sharing is
comparable to the World Wide Web layer of the Internet, where organizations can
publish information on web pages, or browse and download information
published by other organizations on the web. Ownership of the data is retained by
the organization that provided the data to _Clarus_, and the provider organization
can restrict the dissemination of the data through data sharing agreements with the
_Clarus_ program.

The _Clarus_ system will add a third mode of functionality, which might be called
“meta-librarian.” The _Clarus_ system will collect, organize, and quality check the
environmental data to be published by the system. The data will be collected from
the participants, organized by location and type of data, and quality flags will be
added. When this is done, the data will be published to the Service Providers and
other participant/consumers in _Clarus_ . Figure 2 shows the general process as data
progresses from collection through publication to service providers.



_04037-rq301srs0200_

_Page 8_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_









Field Instrumentation
and Remote Sensing



Service
Provider
Customers


**Figure 2 –** _**Clarus**_ **Data Acquisition, Processing, and Publication**

The principal interfaces that will be critical to _Clarus_ are the interface between
_Clarus_ and the participating collectors, and the interface between _Clarus_ and the
participating service providers. MADIS, for example, uses NetCDF files as a
standard interchange format. While the service provider interface is completely
within the control of the _Clarus_ Initiative, the interface(s) to the collectors may be
influenced by what interfaces these systems can support.

While the participants may want to access the network through “a one-stop
Internet portal for all surface transportation weather and pavement related
observations” (Ref. 12), there is no requirement that the system be a single
centralized system. Designers are free to explore centralized and de-centralized
architectures so long as the interfaces with participants give the appearance of a
“one-stop” portal.

The issues of data retention and archive are also not explicitly addressed. While
some data retention is likely to be necessary to support the quality checking
function and the publication function, there is a clear recognition that as the data
age, they lose value to all but climatological investigators and other researchers.
This phase of development does not include directly archiving the large volume of
environmental data in _Clarus_ . Considering the technical scope of such an effort,
archiving may be externalized or be deferred until the _Clarus_ network is
operational and proven.



_04037-rq301srs0200_

_Page 9_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_

###### **_2.2 System Functions_**

The _Clarus_ system will collect data from contributing members, organize and
quality check the data, and then publish the data for use by service providers and
other members of the network. These basic processes are shown in Figure 3 in
terms of _Clarus_ system objects and their interactions. The ellipses represent
specific types of data, user roles, or equipment, and the arrows represent the
interactions between them [2] . For example, a “Collector” administers a “Sensor,”
collects “Observation Data,” provides “Sensor Metadata,” and receives “Quality
Feedback”.


2 The arrows in Figure 3 do _not_ indicate data flows; they show the subject-object orientation of the
relationship.



_04037-rq301srs0200_

_Page 10_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


**Figure 3 – Basic** _**Clarus**_ **System Objects and Functions**


_04037-rq301srs0200_

_Page 11_



_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


The volume of data involved in this process has the potential to become very
large, which leads to a significant challenge in developing a system that can
effectively gather, organize, quality check, and disseminate the data. The _Clarus_
system should be a data collection system capable of handling a vast range of data
in a flexible manner that permits new data types to be added.

Determining data types will be a significant challenge. Proper understanding of
the available data versus the required information will dictate how the data
gathering processes and the database itself should be designed for greatest
efficiency.

While there are many types of environmental data that could be collected, the
_Clarus_ emphasis on surface weather and transportation puts the focus on those
weather elements that have a direct bearing on surface transportation systems.
These environmental data elements are described in the NTCIP 1204 standard for
Environmental Sensor Station (ESS) interfaces (Ref. 8) and summarized in Table
1 as potential environmental data elements to include in the _Clarus_ system.



_04037-rq301srs0200_

_Page 12_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


**Table 1 – Potential** _**Clarus**_ **Environmental Data Elements**





























|Identification Objects<br>Station Category<br>Site Description|Snapshot<br>Filename<br>Image|Visibility Data Objects<br>Visibility<br>Visibility Situation|
|---|---|---|
|Data Instrumentation Objects<br>Type of Station<br>Door Status<br>Battery Status<br>Line Volts<br>Station Meta Data Block<br>Weather Block<br>Mobile Block|Air Quality Parameters<br>Carbon Monoxide Parameter<br>Carbon Dioxide Parameter<br>Nitrous Oxide Parameter<br>Nitrogen Dioxide Parameter<br>Sulfur Dioxide Parameter<br>Ozone Parameter<br>Particulate Matter Parameter<br>Air Quality Block Object|Radiation Objects<br>Solar Radiation<br>Total Sun<br>Cloud Cover Situation<br>Terrestrial Radiation<br>Solar Radiation v2<br>Total Radiation<br>Total Radiation Period|
|Location Objects<br>Latitude<br>Longitude<br>Vehicle Speed<br>Vehicle Bearing<br>Odometer|Temperature Data Objects<br>Number of Temperature Sensors<br>Temperature Sensor Table<br>Temperature Sensor<br>Wetbulb Temperature<br>Dewpoint Temperature<br>Maximum Temperature<br>Minimum Temperature<br>|Pavement Sensor Objects<br>Number of Pavement Sensors<br>Pavement Sensor Table<br>Pavement Sensor<br>Number of Sub-Surface Sensors<br>Sub-Surface Sensor Table<br>Sub-Surface Sensor<br>Pavement Block<br>Sub-Surface Block Object|
|Station Elevation Objects<br>Reference Height<br>Pressure Height<br>Wind Sensor Height<br>Atmospheric Pressure|Snapshot Parameters<br>Number of Snapshot Cameras<br>Snapshot Camera Table<br>Snapshot Camera|Mobile Platform Objects<br>Detected Friction<br>Observed Ground State<br>Observed Pavement State|
|Wind Data Section<br>Average Wind Direction<br>Average Wind Speed<br>Spot Wind Direction<br>Spot Wind Speed<br>Wind Situation<br>Wind Gust Speed<br>Wind Gust Direction<br>Number of Wind Sensors<br>Wind Sensor Table<br>Wind Sensor|Humidity and Precipitation Data Objects<br>Relative Humidity<br>Water Depth<br>Adjacent Snow Depth<br>Roadway Snow Depth<br>Roadway Snow Pack Depth<br>Precipitation Indicator<br>Rainfall or Water Equivalent of Snow<br>Snowfall Accumulation Rate<br>Precipitation Situation<br>Ice Deposit (Thickness)<br>Precipitation Start Time<br>Precipitation End Time<br>Total Precipitation Past One Hour<br>Total Precipitation Past Three Hours<br>Total Precipitation Past Six Hours<br>Total Precipitation Past Twelve<br>Hours<br>Total Precipitation Past Twenty-Four<br>Hours<br>Precipitation Sensor Model<br>Information<br>Number of Water Level Sensors<br>Water Level Sensor Table<br>Water Level Sensor|Pavement Treatment Objects<br>Number of Treatments<br>Pavement Treatment Table<br>Pavement Treatment<br>Treatment Amount<br>Treatment Width<br>Pavement Treatment Block<br>Operational Mode<br>Command State<br>Sprayer State<br>Signal Duration<br>Signal Event Count<br>Last Signal Event<br>Active Event Count<br>Inactive Event Count<br>Last Active Event<br>Last Inactive Event<br>PTS Error Code<br>Monitoring Detectors|
|Water Quality Parameters|||


There are basic temporal limits for the data collection, quality checking,
processing, and publication of the environmental data. There is also a period for
which the Service Provider Customers have temporal-driven requirements. The
design of _Clarus_ will need to consider these time horizons when planning the
technical limitations of the system architecture. These data time horizons are
illustrated in Figure 4.



_04037-rq301srs0200_

_Page 13_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


**Figure 4 – Time Horizons for Weather Data**

The average elapsed time for the Autonomous Layer varies as a result of
configuration and communications latencies that are inherent within the operation
of the system to collect the data. The _Clarus_ component includes the time
required to communicate data from the Autonomous Layer to the _Clarus_ system
import process as well as the time required to process the input data into storage
structures. Further, the variation in the Service Provider component includes the
time required to add other data to the _Clarus_ data and to perform the human- and
machine-based product generation. The average data age grows as a result of the
aggregated times required to move through the various layers and eventually to
the Service Provider Customers. The _Clarus_ system design must address how best
to minimize these times to optimize the flow of data in a timely manner.

For the purposes of defining the boundaries of these time horizons, the following
definitions apply:

  - **Average Elapsed Time** is the estimated time for the process within a
given layer or layer subdivision to take place. The age of observed and
recorded values can vary widely within these bands.

  - **Average Data Age** is the estimated average age of an ESS observation as
it is transferred from the ESS to the end user.



_04037-rq301srs0200_

_Page 14_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_

###### **_2.3 User Characteristics_**

Direct and indirect use of the _Clarus_ system can be applied to a wide audience.
Because a variety of users can derive benefit from the _Clarus_ system, it is
necessary to focus upon those users who have the most immediate contact with
the system components.

The primary user classes include the owners and operators of the observing
systems collecting and sending information to _Clarus_, and the users directly
accessing the data published by the _Clarus_ system.

The following is an initial list of stakeholders whose user needs are considered:

       - Observation system owners including federal, state, local, and private
institutions;

       - Instrument and observation platform suppliers;

       - Direct data users including system owners and their contractors;

       - Surface transportation weather service providers (which may include the
observation system owners);

       - NOAA;

       - General weather service providers;

       - Research and engineering community; and

        - Climate data warehouse and other non-surface weather interests.

This list of direct users of data from the _Clarus_ system is a subset of the entire
population of stakeholders interested in the _Clarus_ Initiative. The requirements of
the broader stakeholder community are essential to the _Clarus_ Initiative and these
interests must serve as a framework for the core _Clarus_ system. From information
in the _Surface Transportation Weather Decision Support Requirements_
(STWDSR) (Ref. 5), _Weather Information for Surface Transportation_ (WIST)
(Ref. 6), and 511 Deployment Coalition (Ref. 7) documents, it is possible to
separate stakeholder groups into a condensed list based upon the user’s interface
or interaction with _Clarus_ data.

The users are viewed as defining layers in the process of transferring data from
raw field observations to various levels of data use. This is illustrated in Figure 5.



_04037-rq301srs0200_

_Page 15_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_







**Figure 5 –** _**Clarus**_ **User Layers and Time Horizon Relationships**

The **Autonomous Layer** is comprised of operational entities who utilize weather
and transportation data to make plans, decisions, and/or take action based upon
sensor data within their control. These data include observations collected by
ESS, mobile data acquisition platforms, cameras, and other transportation-related
measurement devices. The Autonomous Layer data comprises the vast majority of
the raw input data to the _Clarus_ system.

The _**Clarus**_ **Layer** lies between the Autonomous and Service Providers Layers
and represents the nationwide system and architecture to accomplish the
previously outlined goals of surface transportation environmental data collection
and management.

The **Service Providers Layer** is composed of both public and private entities that
provide basic and value-added weather support services to support the weather
information needs of the broader surface transportation community. These support
services rely on _Clarus_ data (raw and processed) combined with other



_04037-rq301srs0200_

_Page 16_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


environmental, road condition, or traffic information products to develop or
provide road weather information and enhanced products.

The **Service Provider Customer Layer** includes those groups who are direct
consumers of products generated by Service Providers and are generally not a
direct user of _Clarus_ data. The members of this group could be anyone using
weather information, but are largely found within the surface transportation
community. The weather products received by these end users are built from a
combination of _Clarus_ and non- _Clarus_ data. In some instances, the Service
Provider Customer Layer includes entities and agencies also found within the
Autonomous Layer who receive quality checking information on the data they
originally provided to _Clarus_ .

Figure 5 can also be viewed as a depiction of the time horizons that separate the
stakeholder groups. There is an inherent time scale, similar to Figure 4, emanating
from the center of the diagram outward, representing the flow and processing of
data through the _Clarus_ system and between the layers.

The context diagram in Figure 6 illustrates the relationship of the entities
interfacing with _Clarus_ . The diagram also describes the flow of data between the
entities and the _Clarus_ system. The data provider organizations maintain data
collection systems. These organizations make up the Autonomous Layer — the
primary contributors of surface transportation data to the _Clarus_ system. These
stakeholders can benefit from _Clarus_ by receiving quality-controlled data from
the _Clarus_ system. The quality-controlled data are not value-added data, but data
with flags indicating that elements do not meet quality checking thresholds.


**Figure 6 – Context Diagram of** _**Clarus**_ **User Needs**



_04037-rq301srs0200_

_Page 17_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


The private and public sector Service Providers are the principal _Clarus_ users.
These Service Providers generate value-added road and rail weather information
services for the transportation community. Additional Service Providers having
direct access to _Clarus_ data resources include research organizations, external
agencies that may choose to archive _Clarus_ data, and other related weather
service providers.

Within the context of Figure 6, the following roles can be assigned to each group
of users:

   - **Federal, State, and Local Agencies –** These are the transportation system
and road weather information system (RWIS) operators and owners who
directly provide the _Clarus_ data. This group places considerable emphasis
on the pavement-specific component of the data at the observational level
to make immediate decisions. These users, primarily maintenance and
operations personnel, are the principal consumers of information provided
by surface transportation weather service providers. Additional data from
this group may include closed circuit television (CCTV) images, road
condition information, and records of treatment activities such as plowing
and chemical application.

  - **Transit –** These are the owners and operators of transit systems who
contribute raw data to the _Clarus_ system and may receive qualitycontrolled data from it. This group places considerable emphasis on
understanding weather conditions along designated routes.

  - **Rail –** These are the owners and operators of rail systems who contribute
raw data to the _Clarus_ system and may receive quality-controlled data
from it. This group places considerable emphasis on understanding
weather conditions along designated routes plus weather-induced specifics
such as rail temperatures, frozen switches, icing on electrical power
distribution systems, and drifting snow.

  - **Vehicle –** Emerging technologies are developing that will encourage a
greater level of data collection from vehicles for the purpose of
understanding the nature of the transportation system state including the
impacts of weather. As this method of data collection matures, the
information obtained on weather and pavement conditions from
instrumentation on-board vehicles will be important _Clarus_ data.

  - **Surface Transportation Weather Service Providers (STWSP) –** These
surface transportation weather service providers are the private and public
weather service providers who assimilate the _Clarus_ data with other
available data to generate value-added products and services used by the
surface transportation decision-makers at state and local transportation
agencies.

  - **Weather Service Providers –** These include the weather support services
that are primarily interested in the meteorological and hydrologic
components of the _Clarus_ data. This group includes the efforts in public
forecasting by NOAA and the National Weather Service (NWS) along



_04037-rq301srs0200_

_Page 18_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


with private sector weather services and their value-added support to
markets such as agriculture, power utilities, and construction.

       - **Research –** This category incorporates federal, academic, and private
sector researchers who are working to improve the state of knowledge and
practice through the research of surface transportation weather.

       - **Archives –** This category includes operational and non-operational
interests who choose to include the _Clarus_ data in their endeavors. The
archiving of _Clarus_ data will be most effective when combined with other
meteorological archives beyond the scope of _Clarus_, but is not restricted
to such efforts.

###### **_2.4 General Constraints_**

Timeliness of information and reliability of the system are major constraints on
the design. Both of these factors can be addressed through appropriate system
architecture and implementation.

To address the timeliness factor, the system should be designed such that it can
both retrieve and disseminate large volumes of data from a variety of sources and
at potentially high rates. An architecture that spreads its data collection and
dissemination processes across multiple servers and communication channels may
address this issue. The inherent scalability of such a design may also enable the
system to expand and add new data sources and end-users.

Reliability can be achieved through a variety of design and deployment
considerations. Hardware, operating system, and development environment have
significant impacts on the inherent reliability of the system. To maximize system
uptime, redundancies may be required at both the hardware and software levels of
the system. The primary challenge here will be the trade-off between the desire
for reliability and the cost of redundancies.

While the availability of the system is covered in the Concept of Operations, the
criticality of the system is not explicitly addressed. Since _Clarus_ is not replacing
any existing application, the system is not currently critical to any operation or
transportation function; neither is it intended to support any “critical national
security missions.” [3] Nonetheless, once the _Clarus_ system is operational, many
DOTs will use the environmental data from the _Clarus_ system in their normal
management and operations of their infrastructure. If the _Clarus_ system fails,
requestors will need to use their legacy systems.

The system will be “open,” using architecture and communications interfaces that
are non-proprietary and broadly supported within the information technology
industry. The system should be standards based, where national standards are
applicable. Special consideration should be given to the national intelligent
transportation system (ITS) standards.


3 Security considerations for the _Clarus_ system fall under the guidance of Reference 14, OMB Circular No.
A-130, which, by its own definition, does not apply to “critical national security missions.” Future
applications of _Clarus_ may necessitate revisiting this classification.



_04037-rq301srs0200_

_Page 19_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_

###### **_2.5 Assumptions and Dependencies_**

The usefulness of the _Clarus_ system is dependent on participation by multiple
environmental data providers and multiple environmental data consumers. While
the system could be placed in operation with data from only a single contributing
network, there is no added value without the participation of other weather data
sources. Likewise, participation by a small number of data consumers would not
justify the cost of operating the system.

Several assumptions have been made as to how long it will take environmental
data contributors to collect, process, and publish their data. Data not collected in a
timely manner may be of limited use to the data consumers. Assumptions have
also been made about the accuracy of the data, and the ability of the contributing
systems to provide adequate location, time/date, and data qualification tags.
Accepting data from contributors who cannot provide these tags with the data
could seriously complicate the design of the data acquisition interfaces.

Even though the system will check the data and apply quality flags, consumers of
_Clarus_ -provided data will need to understand that neither FHWA nor the
contributing data providers will accept responsibility for the accuracy of any of
the data. The particular limitations and conditions will be defined in data sharing
agreements to be established with data providers, and disclaimer information will
be made available to data consumers by whatever means the data are published.

Several requirements deal with “regional” needs, without specifying regional
boundaries. It is unlikely that the regional boundaries from contributing systems
will correspond with the regional boundaries defined within data consumer
systems. It is even likely that participating data contributors will have different
(though possibly overlapping) coverage areas for their networks. Data consumers
will need to understand that data will be presented by geographic coordinates, not
by regional boundaries. Consumers will also need to understand that coverage
will not be uniform and will depend on sensor placement by the contributing
organizations.

The availability, format, and precision of geo-reference coordinates for data
collection points could present unusual problems for the data acquisition system.
Data in the system database and in published data sets will likely include georeference coordinates in decimal longitude, latitude, and elevation.

The availability, format, and precision of time/date stamps could also present
unusual problems for the data acquisition system, particularly if contributing
systems cannot manage Daylight Savings Time (DST), span time zones, or span
areas that do and do not participate in DST. _Clarus_ timestamps for data in the
database and in published data sets need to be referenced to a standard time
reference such as Coordinated Universal Time (UTC).

The base assumption regarding “database tools” is that the selected data storage
software will include appropriate programming interfaces, query tools, and
configuration and management tools. No special database tools will be developed
as a part of the _Clarus_ system. Some tools may developed in the future as part of
ongoing _Clarus_ Initiative activities.



_04037-rq301srs0200_

_Page 20_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_

##### **3 SYSTEM ARCHITECTURE**

The process of generating detailed system requirements has two major parts:
allocating the high-level requirements to specific system components, and
elaborating the requirements on the function and interchange between those
components. The functional components of the _Clarus_ system have been detailed
in the _Clarus_ System Architectural Description and are summarized in this
section. **Figure 7**, taken from that document, represents the general structure and
flow of information within the _Clarus_ system.


































|ED|Schedule<br>Collector QED QED<br>Services ED Cache request QED<br>QED Services<br>retrieval<br>command ED QED<br>Schedule<br>Service Schedule QCh Watchdog<br>Services<br>retrieval quality<br>parameters rules reqE uM est EM<br>Configuration/ EM EM<br>Adm Si en ris vt icra etion EM Cache re Equ Mest SeE rvM<br>ices<br>Quality Manual Flag<br>state system<br>update state<br>ED – Environmental Data<br>EM – Environmental Metadata<br>Configuration/ QCh – Quality Checking<br>Administration QED – Qualified Environmental Data<br>User Interface|QED|
|---|---|---|
|~~EM~~<br>|~~EM~~<br>|~~EM~~<br>|
|~~EM~~<br>|~~EM~~<br>|~~QED~~<br>request<br>EM<br>|
|||~~EM~~<br>request|



**Figure 7 – Data Flows within the** _**Clarus**_ **System**

Four of the components in **Figure 7** are modeled as sets of services: the collector,
quality checking (QCh), qualified environmental data, and environmental
metadata services. The collector, QED, and EM services are sets of services
because each individual service represents a particular data format interface. A set
of services is required to properly interpret and transform all the incoming and
outgoing environmental information. The particular collector, QED, or EM
service performing a transformation depends on the origin and destination of the
environmental data.

The fourth component modeled as a set is the quality checking service. It is a set
of services because it represents in one component all the QCh algorithms that
can be applied to environmental data collected by _Clarus_ . The specific algorithms
and sequence in which they are applied are determined by quality rules
established through the configuration & administration service. This arrangement
supports flexibility in adding and removing QCh algorithms to produce the best
possible qualified environmental data in the _Clarus_ system.



_04037-rq301srs0200_

_Page 21_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


There are two services that keep the _Clarus_ system operating: the watchdog and
schedule services. The watchdog service monitors the overall system state and
restarts unresponsive services as needed, thus preventing long-term service
disruption. The schedule service prioritizes requests to receive environmental data
from collectors and contributors. The schedule service will also prioritize and
respond to subscription requests for environmental data (not depicted in **Figure**
**7** ).

The set of collector services in the _Clarus_ system receives environmental data
from ED collectors and contributors through both push and pull methods. Each
collector service is capable of understanding a particular data format and is
responsible for extracting the environmental data and placing it into the qualified
environmental data cache flagged as unqualified environmental data.

Quality rules set up by the configuration & administration service are executed by
the quality checking services to apply sets of computations on the environmental
data stored in the qualified environmental data cache. Flagging out-of-range
values is one example of a quality rule. Other quality rules could be created to
derive environmental conditions from existing information such as dew point.
Multiple passes by the quality checking services on the QEDC information could
apply grid algorithms sequentially to further quality check the environmental data.
This allows constant access to qualified environmental data in-process. The
QEDC is still valuable to end-users since it will always identify its level of quality
and can be continuously delivered.

The QED services format the qualified environmental data to fulfill requests from
and information subscriptions for environmental service providers and end-users.
Similarly, the EM services format the metadata to meet requests from and
metadata subscriptions for environmental service providers. Each of these
components is a set of services, with each individual service supporting a
particular data format.

The configuration and administration service supports both the _Clarus_ system and
program. It maintains information about data provider redistribution restrictions
and controls who has access to modify the system state, quality rules, and set ED
retrieval schedules. The configuration & administration service manages environmental metadata, formatting it for internal storage. Data transactions and system
operational statistics are logged in the configuration and administration user
interface as well. The configuration and administration user interface allows
administrative users to interact with these functions and supports the manual
quality review processes.



_04037-rq301srs0200_

_Page 22_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_

##### **4 SPECIFIC REQUIREMENTS**

This section presents the high-level and detailed requirements for the _Clarus_
system and the associated institutional program necessary to achieve the needs
and goals described by the Concept of Operations. These requirements describe
the expected attributes and capabilities of the system and allocate capabilities to
specific components within the _Clarus_ system. The high-level requirements in
this document are limited to those that can be derived from a context diagram
(Figure 8) that pictures the _Clarus_ system as a single functional block with its
interfaces. The types of high-level requirements described in this section
correspond roughly to these functions and interfaces. Functional requirements
describe what happens inside the _Clarus_ system itself: quality checking,
development, and packaging of environmental data. Each interface to the _Clarus_
system has its own requirements with regard to the collection of data from
providers as input; the dissemination of data for output; the controlling rules and
constraints under which the system operates; and the means (primarily data
management) by which it works.


**Figure 8 – High-Level Requirements Context**

The high-level perspective assumed for these requirements has implications for
downstream development activities. The high-level requirements provide a basis
for components in system elaboration, and detailed requirements are subsequently
tied to specific components. Conformance to high-level requirements is shown
through testing based on plans derived from the detailed requirements. The entire
development process is tied together by lines of traceability anchored in the highlevel requirements.

In this section, the requirements are classified by the first letter in the requirement
identification as described in Table 2 and shown in Table 3.

       - Functional Requirements – Lists the characteristics that the system must
support for each interface. Identifies what is to be done by the system,



_04037-rq301srs0200_

_Page 23_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


what inputs should be transformed to what outputs, and what specific
operations are required. The functional requirements further include:

       - Functional Data Requirements, which describe requirements
specific to the definition and management of data used and
provided by the system; and

       - Functional Interface Requirements, which describe the functional
interfaces to the _Clarus_ system from information providers and
consumers.

  - Performance Requirements – Specifies static and dynamic capacity for the
number of users, connections, and other performance related factors.
Performance requirements further include:

       - Design Constraints, which identify constraints imposed by
standards, regulations, software or hardware limitations; and

       - Quality Requirements, which provide requirements which address
the general quality, usability, extensibility, flexibility, and
maintainability of the system.

  - Organizational Requirements – Includes requirements for policies and
procedures to support the implementation, operations, training, and
institutional requirements to support the system. This category also:

       - Details logical characteristics between the system and external data
sources;

       - Specifies level of integration with external systems and defines the
interfaces with each user class; and

       - Specifies any communications interfaces and protocols that should
be supported.

Table 2 shows the general layout of the requirements tables, and explains the
purpose or content of each column of the requirements table. The requirements in
this document are a subset of the requirements information that will be tracked in
the system “Requirements Matrix.” While this document is intended to record the
requirements that apply to a particular implementation of the system, the
Requirements Matrix tracks all proposed requirements for the system. The matrix
includes requirements that may apply to future versions of the system or which
have been deferred due to cost or complexity.

Table 3 provides an explanation of the requirement identification numbering
system. The high-level requirements are identified as A-NNN, where A is the
classification and NNN is a unique number. The detailed requirements are
identified as A-NNNUU, where A-NNN is the parent or high-level requirement
and UU is a unique identifier.

This section lists the functional characteristics that the system must support. It
also identifies what is to be done by the system, what inputs should be
transformed to what outputs, and what specific operations are required. The



_04037-rq301srs0200_

_Page 24_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


functional requirements are broken into subsections by each allocation to specific
modules listed in Table 4.

Detailed requirements are associated with a parent or high-level requirement.
They are used by developers in creating the design for the _Clarus_ system, by
testers to ensure all requirements are implemented during the build of the _Clarus_
system, and by the client for documenting their expectations.

Many of the high-level requirements are allocated to more than one module or
component of the _Clarus_ system. Within each table, the high-level requirements
show their allocations to particular modules. If the high-level requirement is
allocated to more than one module, then the high-level requirement will be
repeated in the corresponding allocation’s module.

Following the high-level requirement, detailed requirement(s) are shown to create
more refined requirements specific to the associated module. Figure 7 may be
referenced while reviewing the detailed requirements to maintain context of the
_Clarus_ system’s architecture.



_04037-rq301srs0200_

_Page 25_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


**Table 2 - Explanation of the Requirements Tables**














|ID|Requirement|Source|Allocation|Comment|Criticality|
|---|---|---|---|---|---|
|A unique identifier used<br>to trace requirements<br>from beginning to end in<br>a system development<br>process.|The text of the actual requirement.<br>Requirements formulated with “…<br>shall…” are direct requirements;<br>those using “… shall be able to…”<br>are conditioned on other<br>requirements being fulfilled or on<br>factors outside the control of the<br>requirement’s subject.|Source(s) for the<br>requirement; could<br>be a reference<br>document or a<br>“parent” requirement.|Identifies the<br>module(s) for the<br>high-level<br>requirement as<br>shown in Table 4.|Supporting text that<br>may help explain the<br>requirement, its<br>priority, or the risks<br>associated with<br>implementing the<br>requirement.|H = High<br>M = Medium<br>L = Low|



**Table 3 – Requirement ID Format**






|Requirement ID Format|Explanation of Format|
|---|---|
|High-level Requirement<br>A-NNN<br>Detailed Requirement<br>A-NNNUU|A <br>Represents the classification of the requirements within the requirements document. The following<br>classifications have been used in this requirements specification:<br>D <br>Design Constraints<br>F <br>General Functional Requirements<br>H <br>Functional Data Requirements<br>I <br>Functional Interface Requirements<br>P <br>System Performance Requirements<br>Q <br>Quality Requirements<br>X <br>Organizational Requirements<br>NNN<br>Provides unique identification. Numbering is not necessarily sequential; gaps in the sequence leave<br>room to add additional related requirements when they are discovered.<br>UU<br>Provides unique identification.|



_04037-rq301srs0100_

_Page 26_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


**Table 4 – Allocation Format**

|Allocation|Name of Allocation Module|
|---|---|
|CAS|Configuration and Administration Service|
|CAUI|Configuration and Administration User Interface|
|CS|Collector Services|
|DOG|Watchdog|
|EMC|Environmental Metadata Cache|
|EMS|Environmental Metadata Services|
|QEDC|Qualified Environmental Data|
|QEDS|Qualified Environmental Data Services|
|QChS|Quality Checking Services|
|SS|Schedule Service|



_04037-rq301srs0100_

_Page 27_



_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_

###### **_4.1 Configuration & Administration Service (CAS)_**

The requirements in this section specify the service to configure and administer the system. The CAS supports the _Clarus_
system and program, manages information about data provider redistribution restrictions, controls access for modifying the
system state and quality rules, applies manual quality flags, establishes environmental data retrieval schedules, and manages
environmental metadata.











|ID|Requirement|Source|Allocation<br>- CAS|Comment|Criticality|
|---|---|---|---|---|---|
|F-101|The_Clarus_ system shall<br>implement quality checking<br>processes as soon as data<br>become available.|ConOps §2.4|QChS, SS,<br>CAS||H|
|F-<br>101B1|The CAS shall be able to<br>configure schedules for<br>executing QChS.|||||
|F-151|The_Clarus_ system shall<br>record the methods applied<br>when deriving quality<br>checking information.|MHI|QChS,<br>CAS||H|
|F-<br>151B1|The CAS shall record the<br>quality checking methods<br>used.|||||
|F-155|The_Clarus_ system shall be<br>able to implement quality<br>checking rules for each<br>environmental parameter.|ConOps §3.5.1.4|QChS,<br>CAS,<br>CAUI||H|
|F-<br>155B1|The CAS shall be able to<br>configure the quality<br>checking rules for each<br>environmental parameter.|||||
|F-<br>155B2|The CAS shall enable<br>administrators to manage<br>quality checking rules.|||||


_04037-rq301srs0100_

_Page 28_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_










|ID|Requirement|Source|Allocation<br>- CAS|Comment|Criticality|
|---|---|---|---|---|---|
|F-161|The_Clarus_ system shall be<br>able to implement quality<br>checking rules for specific<br>environmental situations.|ConOps §3.5.1.4|QChS,<br>CAS|The rules for setting quality flags<br>on environmental data elements<br>may themselves depend on other<br>environmental data. For example,<br>stormy conditions may allow more<br>spatial and temporal variability in<br>wind speed observations than<br>under fair weather conditions.|H|
|F-<br>161B1|The CAS shall be able to<br>configure quality checking<br>rules for specific<br>environmental situations.|||||
|F-163|The_Clarus_ system shall be<br>able to implement quality<br>checking rules specific to<br>observation locations.|Task Force review|QChS,<br>CAS|Quality checking rules may vary<br>from region to region.|H|
|F-<br>163B1|The CAS shall be able to<br>configure quality checking<br>rules specific to observation<br>locations.|||||
|F-171|The_Clarus_ system shall be<br>able to base its quality<br>checking process on<br>historical environmental<br>data.|Inferred from ConOps<br>§3.5.1.4|QChS,<br>CAS||H|
|F-<br>171B1|The CAS shall be able to<br>configure historical<br>environmental data to be<br>used by quality checking<br>processes.|||||



_04037-rq301srs0100_

_Page 29_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_














|ID|Requirement|Source|Allocation<br>- CAS|Comment|Criticality|
|---|---|---|---|---|---|
|F-175|The_Clarus_ system shall be<br>able to use multiple<br>algorithms for its quality<br>checking process.|Inferred from ConOps §4.3|QChS,<br>CAS|Multiple methods or comparisons<br>may be needed for a given<br>observation.|M|
|F-<br>175B1|The CAS shall be able to<br>configure multiple<br>algorithms to be used in the<br>quality checking process.|||||
|F-213|The_Clarus_ system shall<br>allow access to new surface<br>transportation-related<br>environmental data.|ConOps §1, 2.4, 3.1|CS, QChS,<br>QEDC,<br>QEDS,<br>CAS, EMC,<br>EMS, DOG|Access could only be provided<br>when new data sources are<br>established and available.|L|
|F-<br>213B1|The CAS shall be<br>configurable to allow new<br>observation types to be<br>implemented as they become<br>available.|||||
|F-806|The_Clarus_ system shall<br>enable administrators to<br>manage security groups.|MHI|CAS,<br>CAUI|Manage means create, read,<br>update, and delete.|H|
|F-<br>806B1|The CAS system shall<br>enable administrators to<br>manage security group<br>members.|||||
|F-<br>806B2|The CAS shall have an<br>administrator security group.|||||
|F-<br>806B3|The CAS shall have a quality<br>manager security group.|||||



_04037-rq301srs0100_

_Page 30_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


















|ID|Requirement|Source|Allocation<br>- CAS|Comment|Criticality|
|---|---|---|---|---|---|
|F-811|The_Clarus_ system shall be<br>able to restrict environmental<br>data publication based on<br>source.|MHI & ConOps §4.5|QEDS,<br>CAS|Use MADIS as a template<br>(ConOps §3.6).|H|
|F-<br>811B1|The CAS shall be able to<br>record data sharing<br>restrictions.|||||
|F-901|The_Clarus_ system shall<br>record statistics about its<br>operation.|OCS|CAS||H|
|F-<br>901B1|The CAS shall record<br>statistics about the system<br>operation.|||||
|F-905|The_Clarus_ system shall log<br>data transactions.|MHI|CS, QEDS,<br>EMS,<br>QChS,<br>CAS, SS,<br>DOG||H|
|F-<br>905B1|The CAS shall log data<br>transactions.|||||
|H-120|The_Clarus_ system shall<br>acquire, process, and<br>disseminate environmental<br>metadata.|ConOps §3.3|CAS, EMC,<br>EMS,<br>CAUI|Roll up of H-121, H-122, H-123,<br>H-201, which were deprecated.||
|H-<br>120B1|The CAS shall manage<br>contributor metadata.|||For example, ESS & VII<br>contributor metadata.||
|H-<br>120B2|The CAS shall manage<br>collector metadata.|||For example, ESS & VII collector<br>metadata.||
|H-<br>120B3|The CAS shall manage<br>quality checking schedules.|||||



_04037-rq301srs0100_

_Page 31_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_








|ID|Requirement|Source|Allocation<br>- CAS|Comment|Criticality|
|---|---|---|---|---|---|
|H-<br>120B4|The CAS shall manage<br>environmental data<br>collection schedules.|||||
|H-<br>120B5|The CAS shall manage ESS<br>metadata.|Task Force||||
|I-032|The_Clarus_ system shall<br>manage environmental data<br>and metadata according to<br>the_Clarus_ data sharing<br>agreements.|MHI|CAS,<br>CAUI|Changed from “The_Clarus_ system<br>shall manage system user<br>privileges according to the_Clarus_ <br>data sharing agreements.”|H|
|I-032B1|The CAS shall manage data<br>sharing rules based on<br>contributor data sharing<br>agreements.|||||



_04037-rq301srs0100_

_Page 32_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_

###### **_4.2 Configuration & Administration User Interface (CAUI)_**

The requirements in this section specify the interface for administering the system and applying manual quality flags.


















|ID|Requirement|Source|Allocation -<br>CAUI|Comment|Criticality|
|---|---|---|---|---|---|
|F-100|The_Clarus_ system shall collect,<br>quality check, and disseminate<br>environmental data.|ConOps §1|CS, QChS,<br>QEDS,<br>CAUI|Environmental data includes all NTCIP<br>1204 data (summarized in Table 1).|H|
|F-100C1|The CAUI shall be able to initiate<br>CS on demand.|||||
|F-111|The_Clarus_ system shall provide<br>environmental data quality flags.|OCS|QChS,<br>CAUI,<br>QEDC||H|
|F-111C1|The CAUI shall enable a quality<br>manager to apply manual flags to<br>a set of observations from an<br>individual ESS.|||This requirement allows all observations<br>from an ESS to have manual flags applied.<br>Example, the ESS was destroyed by a car.||
|F-111C2|The CAUI shall enable a quality<br>manager to apply manual flags to<br>a set of observations.|||This requirement allows only some of the<br>observations from an ESS to have manual<br>flags applied. Example, a particular sensor<br>is out of service.||
|F-111C3|The CAUI shall enable a quality<br>manager to apply manual flags to<br>a set of observations over a fixed<br>time range.|||||
|F-111C4|The CAUI shall enable a quality<br>manager to apply manual flags to<br>a set of observations over a time<br>range with an open ended future<br>time.|||||
|F-141|The_Clarus_ system shall allow<br>human quality checks of<br>environmental data.|OCS|CAUI,<br>QChS|Changed from “The_Clarus_ system shall<br>allow human intervention to override<br>automatically applied quality assessment.”|M|



_04037-rq301srs0100_

_Page 33_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_






|ID|Requirement|Source|Allocation -<br>CAUI|Comment|Criticality|
|---|---|---|---|---|---|
|F-141C1|The CAUI shall allow a quality<br>manager to apply a manual quality<br>flag to environmental data.|||||
|F-141C3|The CAUI shall allow manual<br>quality flags to be entered.|||||
|F-155|The_Clarus_ system shall be able to<br>implement quality checking rules<br>specific to each environmental<br>parameter.|ConOps<br>§3.5.1.4|QChS, CAS,<br>CAUI||H|
|F-155C1|The CAUI shall enable quality<br>checking rules to be configured<br>specific to each environmental<br>parameter.|||||
|F-806|The_Clarus_ system shall enable<br>administrators to manage security<br>groups.|MHI|CAS, CAUI||H|
|F-806C1|The CAUI shall enable<br>administrators to manage security<br>group members.|||||
|H-120|The_Clarus_ system shall acquire,<br>process, and disseminate<br>environmental metadata.|ConOps §3.3|CAS, EMC,<br>EMS, CAUI|Roll up of H-121, H-122, H-123, H-201,<br>which were deprecated.||
|H-<br>120C1|The CAUI shall enable<br>administrators to acquire<br>environmental metadata.|||||
|H-<br>120C2|The CAUI shall enable<br>administrators to manage<br>environmental metadata.|||||



_04037-rq301srs0100_

_Page 34_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_










|ID|Requirement|Source|Allocation -<br>CAUI|Comment|Criticality|
|---|---|---|---|---|---|
|I-031|The_Clarus_ system shall provide a<br>user interface for administration.|MHI|CAUI||H|
|I-031C1|The CAUI shall enable<br>administrators to manage<br>contributor metadata.|||||
|I-031C2|The CAUI shall enable<br>administrators to manage collector<br>metadata.|||||
|I-031C3|The CAUI shall enable<br>administrators to manage quality<br>checking schedules.|||||
|I-031C4|The CAUI shall enable<br>administrators to manage<br>environmental data collection<br>schedules.|||||
|I-032|The_Clarus_ system shall manage<br>environmental data and metadata<br>according to the_Clarus_ data<br>sharing agreements.|MHI|CAS, CAUI|Changed from “The_Clarus_ system shall<br>manage system user privileges according<br>to the_Clarus_ data sharing agreements.”|H|
|I-032C1|The CAUI shall enable<br>administrators to manage<br>contributor data sharing<br>agreements.|||||
|I-032C2|The CAUI shall enable<br>administrators to assign system<br>privileges.|||||



_04037-rq301srs0100_

_Page 35_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_

###### **_4.3 Collector Services (CS)_**

The requirements in this section specify the collection of environmental data. The Collector Services shall receive environmental
data, convert the environmental data into a standard format, and store the environmental data in the Qualified Environmental
Data Cache.












|ID|Requirement|Source|Allocation -<br>CS|Comment|Criticality|
|---|---|---|---|---|---|
|F-100|The_Clarus_ system shall collect,<br>quality check, and disseminate<br>environmental data.|ConOps §1|CS, QChS,<br>QEDS,<br>CAUI|Environmental data includes all NTCIP<br>1204 data (summarized in Table 1).|H|
|F-100D1|CS shall collect environmental<br>data based on its configured<br>schedule.|||||
|F-100D2|CS shall be able to transform<br>extracted environmental data into<br>the internal storage format.|||||
|F-100D3|CS shall be able to store<br>transformed environmental data in<br>the QEDC.|||||
|F-100D4|CS shall be able to convert<br>observation units into the_Clarus_ <br>standard unit specification.|||||
|F-100D5|CS shall be able to be initiated on<br>a schedule.|||||
|F-100D6|CS shall be able to be initiated on<br>demand.|||||
|F-200|The_Clarus_ system shall be able to<br>detect data submission errors.|MHI|CS||H|
|F-200D1|CS shall log when a data<br>submission error occurs.|||||



_04037-rq301srs0100_

_Page 36_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_





|ID|Requirement|Source|Allocation -<br>CS|Comment|Criticality|
|---|---|---|---|---|---|
|F-201|The_Clarus_ system shall be able to<br>access in-situ environmental<br>observations from data collectors.|OCS|CS|Access to data may be conditional based<br>on data sharing agreements to be reached<br>with individual data collector<br>organizations.|H|
|F-201D1|CS shall be able to collect in-situ<br>environmental observations from<br>data collectors.|||||
|F-205|The_Clarus_ system shall be able to<br>access remotely sensed<br>environmental observations from<br>data collectors.|OCS|CS||M|
|F-205D1|CS shall be able to retrieve<br>remotely sensed environmental<br>observations from data collectors.|||||
|F-211|The_Clarus_ system shall be able to<br>receive roadway weather<br>measurements derived from VII<br>data.|OCS|CS||M|
|F-211D1|CS shall be able to retrieve<br>roadway weather measurements<br>derived from VII data.|||||
|F-213|The_Clarus_ system shall allow<br>access to new surface<br>transportation-related observed<br>environmental data.|ConOps §1,<br>2.4, 3.1|CS, QChS,<br>QEDC,<br>QEDS,<br>CAS, EMC,<br>EMS, DOG|Access could only be provided when new<br>data sources are established and available.|L|
|F-213D1|CS shall be able to be<br>implemented to collect new<br>observation types as they become<br>available.|||||


_04037-rq301srs0100_

_Page 37_









_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_




















|ID|Requirement|Source|Allocation -<br>CS|Comment|Criticality|
|---|---|---|---|---|---|
|F-214|The_Clarus_ system shall accept<br>environmental data derived from<br>images.|MHI|CS|Images would include CCTV and still<br>images.|H|
|F-214D1|CS shall accept surface condition<br>data derived from surface images.|Task Force<br>review||Surface condition data may include, for<br>example, "dry", "wet", "icy", "snow-<br>covered", or "flooded". Used to be F-216.|H|
|F-214D2|CS shall accept atmospheric<br>condition data derived from<br>atmospheric images.|Task Force<br>review||Used to be F-217.|H|
|F-221|The_Clarus_ system shall be able to<br>retrieve environmental data<br>directly from environmental sensor<br>station collectors.|Task Force<br>review|CS|Changed from "The_Clarus_ system shall<br>be able to retrieve environmental data<br>directly from environmental sensor<br>stations."|L|
|F-221D1|CS shall be able to retrieve<br>environmental data directly from<br>environmental sensor station<br>collectors.|||||
|F-222|The_Clarus_system shall minimize<br>the time for data acquisition.|OCS|||H|
|F-222D1|CS shall be able to dynamically<br>adjust its retrieval schedules when<br>environmental data is expected to<br>be ready but is temporarily<br>delayed.|||||
|F-223|The_Clarus_ system shall process<br>data as they are received.|ConOps<br>§3.4.3|CS, QChS||H|
|F-223D1|CS shall process environmental<br>data as they are received.|||||



_04037-rq301srs0100_

_Page 38_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_














|ID|Requirement|Source|Allocation -<br>CS|Comment|Criticality|
|---|---|---|---|---|---|
|F-231|The_Clarus_ system shall collect<br>pavement-related observations.|ConOps §2.5|CS|Pavement-related observations could<br>include precipitation accumulation,<br>flooding or treatments.|H|
|F-231D1|CS shall be able to collect<br>pavement-related observations.|||||
|F-241|The_Clarus_ system shall accept<br>environmental data from railway<br>systems or in-situ ESS along<br>tracks.|ConOps<br>§2.5.7|CS||H|
|F-241D1|CS shall be able to collect<br>environmental data from railway<br>systems from railway collectors.|||||
|F-241D2|CS shall be able to collect<br>environmental data from in-situ<br>ESS along tracks from railway<br>collectors.|||||
|F-245|The_Clarus_ system shall accept<br>environmental data from railroad<br>vehicles.|ConOps<br>§2.5.7|CS||H|
|F-245D1|CS shall accept environmental<br>data derived from railroad vehicle<br>data.|||||
|F-251|The_Clarus_ system shall accept<br>environmental data from<br>(roadway) vehicles.|Inferred from<br>ConOps<br>§2.5.x|CS||H|
|F-251D1|CS shall accept environmental<br>data collected from (roadway)<br>vehicles.|||||



_04037-rq301srs0100_

_Page 39_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_






|ID|Requirement|Source|Allocation -<br>CS|Comment|Criticality|
|---|---|---|---|---|---|
|F-255|The_Clarus_ system shall accept<br>environmental data from<br>maintenance and construction<br>vehicles.|ConOps<br>§2.5.2|CS||H|
|F-255D1|CS shall accept environmental<br>data collected from maintenance<br>and construction vehicles.|||||
|F-261|The_Clarus_ system shall accept<br>environmental data from service<br>patrol vehicles.|ConOps<br>§2.5.3|CS||H|
|F-261D1|CS shall accept environmental<br>data collected from service patrol<br>vehicles.|||||
|F-271|The_Clarus_ system shall accept<br>environmental data from transit<br>vehicles.|ConOps<br>§2.5.5|CS|Transit vehicles include watercraft<br>(ferries) and buses.|H|
|F-271D1|CS shall accept environmental<br>data collected from transit<br>vehicles.|||||
|F-275|The_Clarus_ system shall accept<br>environmental data from<br>emergency vehicles.|ConOps<br>§2.5.6|CS||H|
|F-275D1|CS shall accept environmental<br>data collected from emergency<br>vehicles.|||||
|F-281|The_Clarus_ system shall be able to<br>receive weather data from weather<br>service providers.|ConOps<br>§3.5.1.4|CS||H|



_04037-rq301srs0100_

_Page 40_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_












|ID|Requirement|Source|Allocation -<br>CS|Comment|Criticality|
|---|---|---|---|---|---|
|F-281D1|CS shall be able to receive weather<br>data from weather service<br>providers.|||For example, ASOS/AWOS.||
|F-905|The_Clarus_ system shall log data<br>transactions.|MHI|CS, QEDS,<br>EMS,<br>QChS,<br>CAS, SS,<br>DOG||H|
|F-905D1|CS shall create a log entry when a<br>data set is invalid.|||An “invalid” data set is one that cannot be<br>understood as received.||
|H-011|The_Clarus_ system baseline data<br>types shall be defined by the<br>NTCIP ESS 1204 standard.|ConOps §3.3<br>(Table 2)|CS, QEDC,<br>QEDS|Version 02.20 was accepted as a<br>recommended standard by the NTCIP<br>Joint Committee in March 2005.  See<br>www.ntcip.org/library/documents.|H|
|H-<br>011D1|CS shall accept data types defined<br>by NTCIP 1204.|||||
|H-012|The_Clarus_ system data definitions<br>shall be consistent with the ITE<br>TM 1.03 standard, Functional<br>Level Traffic Management Data<br>Dictionary (TMDD).|Task Force<br>review|CS, QEDS||H|
|H-<br>012D1|CS shall accept environmental<br>data described by definitions<br>defined by the TMDD.|||||
|H-<br>012D2|CS shall accept environmental<br>data described by definitions<br>defined by CMML version 2.|||||
|H-020|The_Clarus_ system shall acquire,<br>process, and disseminate<br>environmental data.|ConOps §2.1|CS, QChS,<br>QEDS|Roll up of H-021, H-022, H-023, which<br>were deprecated.|H|



_04037-rq301srs0100_

_Page 41_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


















|ID|Requirement|Source|Allocation -<br>CS|Comment|Criticality|
|---|---|---|---|---|---|
|H-151|The_Clarus_ system shall accept<br>only observations that include<br>location, timestamp, and source<br>metadata.|Implied<br>throughout<br>ConOps|CS|Appendix A includes a discussion of<br>"metadata" in this context.|H|
|H-<br>151D1|CS shall accept only observations<br>that include location, timestamp,<br>and source metadata.|||||
|H-155|The_Clarus_ system shall accept<br>only observations of identified<br>measurement types and units.|OCS|CS||H|
|H-<br>155D1|CS shall accept only observation<br>of identified measurement types<br>and units.|||Incoming units will be converted to<br>NTCIP 1204 units.||
|H-301|The_Clarus_ system shall be able to<br>acquire, process, and disseminate<br>environmental data from across<br>North America.|ConOps<br>§3.4.2,<br>amended in<br>Task Force<br>review|CS, QChS,<br>QEDS|North America in this context includes the<br>United States, it territories, Canada, and<br>Mexico|H|
|H-<br>301D1|CS shall be able to acquire<br>environmental data from across<br>North America.|||||
|I-011|The_Clarus_ system shall accept<br>data through a_Clarus_ standard<br>interface.|OCS|CS|Standard to be determined during design<br>phase of this project.|H|
|I-011D1|CS shall implement the_Clarus_ <br>standard interface.|||||



_04037-rq301srs0100_

_Page 42_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_












|ID|Requirement|Source|Allocation -<br>CS|Comment|Criticality|
|---|---|---|---|---|---|
|I-012|The_Clarus_ system shall be able to<br>communicate with environmental<br>sensor stations through its<br>collector using the NTCIP ESS<br>1204.|ConOps §3.3|CS|Version 02.20 was accepted as a<br>recommended standard by the NTCIP<br>Joint Committee in March 2005.  See<br>www.ntcip.org/library/documents. The<br>ending phrase "for data collection" was<br>removed.|L|
|I-012D1|CS shall be able to process NTCIP<br>ESS 1204 data.|||||
|I-013|The_Clarus_ system shall be able to<br>communicate with RWIS<br>databases through their native<br>interfaces.|ConOps<br>§3.4.2|CS||L|
|I-013D1|CS shall be able to accept data<br>from an RWIS database in its<br>native output format.|||At such time as this requirement may be<br>implemented RWIS databases will be<br>treated as a collector.||
|I-014|The_Clarus_ system shall be able to<br>communicate with an individual<br>ESS through its native interface.|ConOps<br>§3.4.2|CS|Deprecated. F-221 covers this.|L|
|I-016|The_Clarus_ system shall transfer<br>data as efficiently as possible.|Inferred from<br>ConOps §3.2|CS, EMS,<br>QEDS, SS|Related to F-501, F-222.|H|
|I-016D1|CS shall transfer data<br>concurrently.|||||
|I-016D2|CS shall be able to request<br>collector environmental data on<br>demand.|||||
|I-016D3|CS shall be able to accept<br>environmental data pushed from<br>collectors.|||||



_04037-rq301srs0100_

_Page 43_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_








|ID|Requirement|Source|Allocation -<br>CS|Comment|Criticality|
|---|---|---|---|---|---|
|I-017|The_Clarus_ system shall employ<br>industry standards to minimize<br>implementation impact to users<br>and providers.|Inferred from<br>ConOps §4.1|CS, QEDS,<br>EMC, EMS|Standards in this context refer to the<br>environmental data standards in common<br>use among_Clarus_ stakeholders.|H|
|I-017D1|CS shall be able to extract<br>environmental data from an XML<br>message that conforms to the<br>_Clarus_ standard XML message<br>specification.|||||
|I-017D2|CS shall be able to extract<br>environmental data from comma<br>separated value messages.|||||
|I-017D3|CS that process comma separated<br>value ASCII text shall be able to<br>dynamically parse environmental<br>data that includes a descriptive<br>header row conforming to the<br>_Clarus_ collector standard message<br>specification.|||||
|I-017D4|CS that process comma separated<br>value ASCII text shall be able to<br>dynamically parse environmental<br>data described by a stored<br>collector configuration.|||||
|I-017D5|CS shall be able to extract<br>environmental data from CMML<br>version 2 messages.|||||
|I-017D6|CS shall be able to extract<br>environmental data from netCDF<br>version 3.6 messages.|||||



_04037-rq301srs0100_

_Page 44_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_

###### **_4.4 Watchdog (DOG)_**

The requirements in this section specify the operation of the watchdog to keep the system running. The watchdog is an
automated system management service that will monitor the overall _Clarus_ system, restart unresponsive services, notify the CAS
of failures, and log data transactions.




















|ID|Requirement|Source|Allocation -<br>DOG|Comment|Criticality|
|---|---|---|---|---|---|
|F-213|The_Clarus_ system shall allow<br>access to new surface<br>transportation related observed<br>environmental data.|ConOps §1, 2.4,<br>3.1|CS, QChS,<br>QEDC,<br>QEDS,<br>CAS, EMC,<br>EMS, DOG|Access could only be provided when<br>new data sources are established and<br>available.|L|
|F-<br>213G1|The DOG shall be able to<br>monitor new environmental data<br>services as they are added.|||||
|F-905|The_Clarus_ system shall log data<br>transactions.|MHI|CS, QEDS,<br>EMS,<br>QChS,<br>CAS, SS,<br>DOG||H|
|F-<br>905G1|The DOG shall be able to record<br>its activities.|||||
|Q-012|The_Clarus_ system shall be able<br>to automatically recover from an<br>unexpected shutdown.|MHI|DOG||H|
|Q-<br>012G1|The watchdog service shall<br>monitor the overall_Clarus_ <br>system state.|||||
|Q-<br>012G2|The watchdog service shall be<br>able to restart unresponsive<br>_Clarus_ system services.|||||



_04037-rq301srs0100_

_Page 45_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_

###### **_4.5 Environmental Metadata Cache (EMC)_**

The requirements in this section specify the storage of environmental metadata. The EMC will store environmental metadata
about the contributors and collectors from the Configuration & Administration Services and send environmental metadata to the
Environmental Metadata Services upon request.









|ID|Requirement|Source|Allocation<br>- EMC|Comment|Criticality|
|---|---|---|---|---|---|
|F-213|The_Clarus_ system shall allow<br>access to new surface<br>transportation related observed<br>environmental data.|ConOps §1, 2.4, 3.1|CS, QChS,<br>QEDC,<br>QEDS,<br>CAS,<br>EMC,<br>EMS,<br>DOG|Access could only be provided when<br>new data sources are established and<br>available.|L|
|F-<br>213E1|The EMC shall be configurable<br>to allow new observation types<br>to be implemented as they<br>become available.|||||
|H-120|The_Clarus_ system shall<br>acquire, process, and<br>disseminate environmental<br>metadata.|ConOps §3.3|CAS,<br>EMC,<br>EMS,<br>CAUI|Roll up of H-121, H-122, H-123, H-<br>201, which have been deprecated.||
|H-<br>120E1|The EMC shall be able to<br>process environmental<br>metadata.|||||
|H-<br>120E2|The EMC shall be able to<br>uniquely identify each<br>contributor, collector, and<br>station sensor.|||||


_04037-rq301srs0100_

_Page 46_







_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_







|ID|Requirement|Source|Allocation<br>- EMC|Comment|Criticality|
|---|---|---|---|---|---|
|H-<br>120E3|The EMC shall be able to<br>maintain contact info for each<br>contributor, collector, and<br>station sensor.|||||
|H-<br>120E4|The EMC shall be able to<br>maintain backup contact info<br>for each contributor, collector,<br>and station sensor.|||||
|H-<br>120E5|The EMC shall be able to<br>maintain owner names for each<br>contributor, collector, and<br>station sensor.|||||
|H-<br>120E6|The EMC shall be able to<br>maintain an equipment list for<br>each station.|||||
|H-<br>120E7|The EMC shall be able to<br>maintain pavement types for<br>stations with corresponding<br>instrumentation.|||||
|H-<br>120E8|The EMC shall be able to<br>maintain latitude, longitude,<br>and elevation for stations.|||||
|H-<br>120E9|The EMC shall be able to<br>maintain a reference to<br>additional metadata.|Task Force||An example would be a URL to a<br>picture of the ESS.||
|I-017|The_Clarus_ system shall<br>employ industry standards to<br>minimize implementation<br>impact to users and providers.|Inferred from ConOps<br>§4.1|CS, QEDS,<br>EMC,<br>EMS|Standards in this context refer to the<br>environmental data standards in<br>common use among_Clarus_ <br>stakeholders.|H|


_04037-rq301srs0100_

_Page 47_







_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


|ID|Requirement|Source|Allocation<br>- EMC|Comment|Criticality|
|---|---|---|---|---|---|
|I-017E1|The EMC shall store collector<br>metadata that consists of<br>information based on TMDD &<br>MS/ETMCC.|||||


_04037-rq301srs0100_

_Page 48_



_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_

###### **_4.6 Environmental Metadata Services (EMS)_**

The requirements in this section specify the services for the retrieval of environmental metadata. The EMS receives request, gets
environmental metadata from cache, formats environmental metadata to fulfill requests and subscriptions, and sends formatted
metadata back to requester.











|ID<br>D-062|Requirement<br>The Clarus system shall<br>disseminate environmental<br>metadata in response to<br>polling.|Source<br>OCS|Allocation<br>- EMS<br>EMS|Comment|Criticality<br>H|
|---|---|---|---|---|---|
|D-<br>062F1|EMS shall disseminate<br>metadata in response to<br>polling.|||||
|D-091|The_Clarus_ system shall<br>disseminate data using<br>standard Internet protocols.|OCS|QEDS,<br>EMS||H|
|D-<br>091F1|EMS shall disseminate<br>metadata using standard<br>Internet protocols.|||||
|F-213|The_Clarus_ system shall allow<br>access to new surface<br>transportation related observed<br>environmental data.|ConOps §1, 2.4, 3.1|CS, QChS,<br>QEDC,<br>QEDS,<br>CAS,<br>EMC,<br>EMS,<br>DOG|Access could only be provided when<br>new data sources are established and<br>available.|L|
|F-213F1|The_Clarus_ system shall allow<br>new EMS to be implemented<br>that disseminate new<br>observation types to be<br>implemented as they become<br>available.|||||


_04037-rq301srs0100_

_Page 49_







_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_









|ID<br>F-401|Requirement<br>The Clarus system shall be<br>able to provide sensor<br>equipment metadata in<br>response to a request.|Source<br>OCS|Allocation<br>- EMS<br>EMS|Comment<br>Subject to data sharing agreements.|Criticality<br>H|
|---|---|---|---|---|---|
|F-401F1|EMS shall be able to provide<br>sensor equipment metadata in<br>response to a request.|||||
|F-501|The_Clarus_ system shall<br>minimize the time for data<br>dissemination.|MHI|QEDS,<br>EMS||H|
|F-501F1|EMS shall respond to queries<br>for metadata within five<br>minutes.|||Related to I-016, F-222.||
|F-905|The_Clarus_ system shall log<br>data transactions.|MHI|CS, QEDS,<br>EMS,<br>QChS,<br>CAS, SS,<br>DOG||H|
|F-905F1|EMS shall log metadata<br>transactions.|||||
|H-120|The_Clarus_ system shall<br>acquire, process, and<br>disseminate environmental<br>metadata.|ConOps §3.3|CAS,<br>EMC,<br>EMS,<br>CAUI|Roll up of H-121, H-122, H-123, H-<br>201, which have been deprecated.||
|H-<br>120F1|The EMS shall accept source<br>queries that consist of a list of<br>_Clarus_ contributors.|||||
|H-<br>120F2|The EMS shall accept source<br>queries that consist of a list of<br>_Clarus_ contributors including<br>station identifier.|||||


_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._





_04037-rq301srs0100_

_Page 50_


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_












|ID<br>H-<br>120F3|Requirement<br>The EMS shall accept location<br>queries based on a bounding<br>latitude/longitude coordinate<br>pair.|Source|Allocation<br>- EMS|Comment|Criticality|
|---|---|---|---|---|---|
|H-<br>120F4|The EMS shall accept location<br>queries based on<br>latitude/longitude location and<br>radius.|Task Force||||
|I-016|The_Clarus_ system shall<br>transfer data as efficiently as<br>possible.|Inferred from ConOps<br>§3.2|CS, EMS,<br>QEDS, SS|Related to F-501, F-222.|H|
|I-016F1|EMS shall transfer data<br>concurrently.|||||
|I-017|The_Clarus_ system shall<br>employ industry standards to<br>minimize implementation<br>impact to users and providers.|Inferred from ConOps<br>§4.1|CS, QEDS,<br>EMS|“Standards” in this context refer to<br>the environmental data standards in<br>common use among_Clarus_ <br>stakeholders.|H|
|I-017F1|EMS shall be able to distribute<br>metadata in a comma<br>separated value ASCII format.|||||
|I-023|The_Clarus_ system shall<br>respond to queries for<br>environmental metadata from<br>the available metadata.|MHI|||H|
|I-023F1|EMS responses shall include<br>metadata that meets the<br>requested metadata query<br>filtering specifications.|||||



_04037-rq301srs0100_

_Page 51_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_






|ID<br>I-023F2|Requirement<br>EMS shall respond to queries<br>returning no results with a<br>message stating that no results<br>matching that query are<br>available.|Source<br>Task Force|Allocation<br>- EMS|Comment|Criticality|
|---|---|---|---|---|---|
|P-025|The_Clarus_ system shall<br>respond to a request for<br>information within five<br>minutes.|MHI|QEDS,<br>EMS|Related to F-501.|H|
|P-025F1|The EMS shall respond to a<br>request for metadata within<br>five minutes.|||||



_04037-rq301srs0100_

_Page 52_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_

###### **_4.7  Qualified Environmental Data (QEDC)_**

The requirements in this section specify the storage of qualified environmental data. The QEDC receives environmental data
from the Collector Services (CS), stores qualified environmental data, sends environmental data to Quality Checking Services
(QCS), receives quality checked environmental data from QCS, receives requests from the Qualified Environmental Data
Services (QEDS), and sends qualified environmental data in response to Qualified Environmental Data Services’ request.












|ID|Requirement|Source|Allocation<br>- QEDC|Comment|Criticality|
|---|---|---|---|---|---|
|F-111|The_Clarus_ system shall<br>provide environmental data<br>quality flags.|OCS|QChS,<br>CAUI,<br>QEDC||H|
|F-111I1|The QEDC shall keep the<br>results of each quality test for<br>each observation for the life<br>of the observation.|||||
|F-213|The_Clarus_ system shall<br>allow access to new surface<br>transportation related<br>observed environmental data.|ConOps §1, 2.4, 3.1|CS, QChS,<br>QEDC,<br>QEDS,<br>CAS,<br>EMC,<br>EMS,<br>DOG|Access could only be provided when new<br>data sources are established and available.|L|
|F-213I1|The QEDC shall be<br>configurable to allow new<br>observation types to be<br>implemented as they become<br>available.|||||
|F-521|The_Clarus_ system shall<br>maintain a dynamic library of<br>data for at least seven days.|Task Force review|QEDC||H|



_04037-rq301srs0100_

_Page 53_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_














|ID<br>F-521I1|Requirement<br>The QEDC shall maintain<br>observations and their<br>associated quality flags for<br>seven days.|Source|Allocation<br>- QEDC|Comment|Criticality|
|---|---|---|---|---|---|
|H-011|The_Clarus_ system baseline<br>data types shall be defined by<br>the NTCIP ESS 1204<br>standard.|ConOps §3.3 (Table<br>2)|CS, QEDC,<br>QEDS|Version 02.20 was accepted as a<br>recommended standard by the NTCIP<br>Joint Committee in March 2005.  See<br>www.ntcip.org/library/documents.|H|
|H-011I1|The QEDC observation types<br>shall be defined by NTCIP<br>ESS 1204.|||||
|I-021|The_Clarus_ system shall<br>allow service providers to<br>select specific desired data<br>sets.|ConOps §3.5.1.4|QEDS,<br>QEDC||H|
|I-021I1|The QEDC shall support<br>queries for its observations.|||||
|I-022|The_Clarus_ system shall<br>respond to queries for<br>environmental data from the<br>available data.|MHI|QEDS,<br>QEDC||H|
|I-022I1|The QEDC shall support<br>queries against all of its<br>available observation<br>datasets.|||||
|P-013|The_Clarus_ system shall<br>support 470 million current<br>observations.|MHI|QEDC|4.7 million road miles in North America;<br>approximately 100 environmental<br>parameters for a reporting location (based<br>on NTCIP 1204).|M|



_04037-rq301srs0100_

_Page 54_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_04037-rq301srs0100_

_Page 55_



_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_

###### **_4.8 Qualified Environmental Data Services (QEDS)_**

The requirements in this section specify the means of disseminating qualified environmental data. In all requirements where it
applies, data is to be disseminated only in accordance with the data sharing agreements. The QEDS receive requests, get quality
checked environmental data from cache, format quality checked environmental data to fulfill requests and subscriptions, and
sends formatted environmental data back to requester.










|ID|Requirement|Source|Allocation -<br>QEDS|Comment|Criticality|
|---|---|---|---|---|---|
|D-051|The_Clarus_ system shall<br>disseminate data in<br>response to a scheduled<br>request.|OCS|QEDS, SS||H|
|D-051J1|QEDS shall disseminate<br>data in response to a<br>scheduled environmental<br>data request.|||||
|D-061|The_Clarus_ system shall<br>disseminate environmental<br>data in response to polling.|OCS|QEDS||H|
|D-061J1|QEDS shall disseminate<br>data in response to an<br>immediate environmental<br>data request.|||||
|D-071|The_Clarus_ system shall<br>disseminate data in<br>response to a change<br>notification request.|OCS|QEDS||H|
|D-071J1|QEDS shall disseminate<br>data in response to a<br>change notification request.|||||
|D-081|The_Clarus_ system shall be<br>able to notify subscribers<br>when data sets become<br>available.|OCS|QEDS||H|



_04037-rq301srs0100_

_Page 56_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_







|ID<br>D-081J1|Requirement<br>QEDS shall disseminate<br>environmental data to<br>subscribers when datasets<br>fulfilling a subscription<br>query become available.|Source|Allocation -<br>QEDS|Comment|Criticality|
|---|---|---|---|---|---|
|D-081J2|QEDS shall be able to<br>disseminate environmental<br>data to contributor<br>subscribers when datasets<br>fulfilling a subscription<br>query applying threshold<br>filters become available.|||||
|D-091|The_Clarus_ system shall<br>disseminate data using<br>standard Internet protocols.|OCS|QEDS,<br>EMS||H|
|D-091J1|QEDS system shall<br>disseminate environmental<br>data using standard Internet<br>protocols.|||||
|F-100|The_Clarus_ system shall<br>collect, quality check, and<br>disseminate environmental<br>data.|ConOps §1|CS, QChS,<br>QEDS,<br>CAUI|“Environmental data” includes all NTCIP<br>1204 data (summarized in Table 1).|H|
|F-100J1|QEDS shall disseminate<br>environmental data.|||||
|F-100J2|QEDS shall be able to<br>disseminate environmental<br>data in English units.|||||


_04037-rq301srs0100_

_Page 57_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_
















|ID<br>F-115|Requirement<br>The Clarus system shall<br>provide notification of data<br>quality conditions to data<br>contributors.|Source<br>ConOps §2.4|Allocation -<br>QEDS<br>QChS,<br>QEDS|Comment<br>A “data contributor” in this context could<br>ultimately be a State DOT maintenance<br>engineer or traffic manager.|Criticality<br>H|
|---|---|---|---|---|---|
|F-115J1|The observation quality<br>flags shall be used to<br>determine data quality<br>condition notifications.|||||
|F-115J2|QEDS shall provide quality<br>checking statistics to data<br>contributors.|Task Force||Functionality may be similar to that provided<br>by MADIS and MesoWest.||
|F-140|The_Clarus_ system shall<br>enable quality managers to<br>review which quality<br>checks passed or failed.|OCS||New high-level requirement.|H|
|F-140J1|QEDS shall enable quality<br>managers to review which<br>quality checks passed or<br>failed.|||||
|F-213|The_Clarus_ system shall<br>allow access to new surface<br>transportation related<br>observed environmental<br>data.|ConOps §1, 2.4, 3.1|CS, QChS,<br>QEDC,<br>QEDS,<br>CAS, EMC,<br>EMS, DOG|Access could only be provided when new data<br>sources are established and available.|L|
|F-213J1|QEDS shall be able to<br>disseminate new<br>observation types as they<br>become available.|||||
|F-219|The_Clarus_ system shall<br>disseminate NWS watches,<br>warnings, and advisories.|Task Force review|QEDS|New. Split from F-218.|M|



_04037-rq301srs0100_

_Page 58_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_







|ID<br>F-219J1|Requirement<br>QEDS shall be able to<br>disseminate NWS watches,<br>warnings, and advisories.|Source|Allocation -<br>QEDS|Comment|Criticality|
|---|---|---|---|---|---|
|F-501|The_Clarus_ system shall<br>minimize the time for data<br>dissemination.|MHI|QEDS,<br>EMS||H|
|F-501J1|QEDS shall respond to<br>environmental data queries<br>within one minute.|||Related to I-016, F-222.||
|F-505|The_Clarus_ system shall be<br>able to disseminate data<br>based on spatial queries.|ConOps §3.4.2|QEDS|Defining this as "spatial" allows coverage of<br>custom regions.|H|
|F-505J1|QEDS shall be able to<br>disseminate data based on<br>spatial queries.|||||
|F-811|The_Clarus_ system shall be<br>able to restrict<br>environmental data<br>publication based on<br>source.|MHI & ConOps<br>§4.5|QEDS,<br>CAS|Use MADIS as a template (ConOps §3.6).|H|
|F-811J1|QEDS shall be able to<br>determine if an observation<br>can be disseminated.|||||
|F-905|The_Clarus_ system shall log<br>data transactions.|MHI|CS, QEDS,<br>EMS,<br>QChS,<br>CAS, SS,<br>DOG||H|
|F-905J1|QEDS shall log their<br>activities.|||||


_04037-rq301srs0100_

_Page 59_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


















|ID<br>H-011|Requirement<br>The Clarus system baseline<br>data types shall be defined<br>by the NTCIP ESS 1204<br>standard.|Source<br>ConOps §3.3<br>(Table 2)|Allocation -<br>QEDS<br>CS, QEDC,<br>QEDS|Comment<br>Version 02.20 was accepted as a<br>recommended standard by the NTCIP Joint<br>Committee in March 2005. See<br>www.ntcip.org/library/documents.|Criticality<br>H|
|---|---|---|---|---|---|
|H-011J1|QEDS shall disseminate<br>environmental data types<br>defined by NTCIP 1204.|||||
|H-012|The_Clarus_ system data<br>definitions shall be<br>consistent with the ITE TM<br>1.03 standard, Functional<br>Level Traffic Management<br>Data Dictionary (TMDD).|Task Force review|CS, QEDS||H|
|H-012J1|QEDS shall disseminate<br>data with descriptions that<br>conform to the TMDD.|||||
|H-020|The_Clarus_ system shall<br>acquire, process, and<br>disseminate environmental<br>data.|ConOps §2.1|CS, QChS,<br>QEDS|Roll up of H-021, H-022, H-023, which were<br>deprecated.|H|
|H-301|The_Clarus_ system shall be<br>able to acquire, process,<br>and disseminate<br>environmental data from<br>across North America.|ConOps §3.4.2,<br>amended in Task<br>Force review|CS, QChS,<br>QEDS|North America in this context includes the<br>United States, it territories, Canada, and<br>Mexico|H|
|H-301J1|QEDS shall be able to<br>disseminate environmental<br>data collected from across<br>North America.|||||
|I-016|The_Clarus_ system shall<br>transfer data as efficiently<br>as possible.|Inferred from<br>ConOps §3.2|CS, EMS,<br>QEDS, SS|Related to F-501, F-222.|H|



_04037-rq301srs0100_

_Page 60_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_










|ID<br>I-016J1|Requirement<br>QEDS shall transfer data<br>concurrently.|Source|Allocation -<br>QEDS|Comment|Criticality|
|---|---|---|---|---|---|
|I-017|The_Clarus_ system shall<br>employ industry standards<br>to minimize<br>implementation impact to<br>users and providers.|Inferred from<br>ConOps §4.1|CS, QEDS,<br>EMS|“Standards” in this context refer to the<br>environmental data standards in common use<br>among_Clarus_ stakeholders.|H|
|I-017J1|QEDS shall be able to<br>disseminate environmental<br>data in netCDF version 3.6<br>format.|||||
|I-017J2|QEDS shall be able to<br>disseminate environmental<br>data in HDF version 5<br>format.|||||
|I-017J3|QEDS shall be able to<br>disseminate environmental<br>data in CMML version 2<br>format.|||||
|I-017J4|QEDS shall be able to<br>disseminate environmental<br>data in comma separated<br>value ASCII format.|||||
|I-021|The_Clarus_ system shall<br>allow service providers to<br>select specific desired<br>datasets.|ConOps §3.5.1.4|QEDS,<br>QEDC||H|



_04037-rq301srs0100_

_Page 61_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_






|ID<br>I-021J1|Requirement<br>QEDS shall respond to<br>environmental data queries<br>selecting specific desired<br>datasets.|Source|Allocation -<br>QEDS|Comment|Criticality|
|---|---|---|---|---|---|
|I-022|The_Clarus_ system shall<br>respond to queries for<br>environmental data from<br>the available data.|MHI|QEDS,<br>QEDC||H|
|I-022J1|QEDS shall enable users to<br>request environmental data<br>from among the available<br>output formats.|||||
|I-022J2|QEDS shall respond to<br>queries returning no results<br>with a message stating that<br>no results matching that<br>query are available.|Task Force||||
|I-025|The_Clarus_ system shall<br>enable environmental data<br>queries by timestamp.|ConOps §3.5.1.4|||H|
|I-025J1|QEDS shall accept<br>timestamp queries based on<br>a single timestamp range.|||||
|I-026|The_Clarus_ system shall<br>enable environmental data<br>queries by location<br>reference.|ConOps §3.5.1.4|||H|
|I-026J1|QEDS shall accept location<br>queries based on a<br>bounding latitude/longitude<br>coordinate pair.|||||



_04037-rq301srs0100_

_Page 62_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_






|ID<br>I-026J2|Requirement<br>QEDS shall accept location<br>queries based on a<br>latitude/longitude location<br>and radius.|Source|Allocation -<br>QEDS|Comment|Criticality|
|---|---|---|---|---|---|
|I-027|The_Clarus_ system shall<br>enable environmental data<br>queries by quality.|ConOps §3.5.1.4|||H|
|I-027J1|QEDS shall accept quality<br>flag queries based on a<br>range of quality flag values.|||||
|I-028|The_Clarus_ system shall<br>enable environmental data<br>queries by source.|MHI|||H|
|I-028J1|QEDS shall accept source<br>queries that consist of a list<br>of_Clarus_ contributors.|||||
|I-028J2|QEDS shall accept source<br>queries that are a list of<br>_Clarus_ contributors<br>combined with a station<br>identifier.|||||
|I-033|The_Clarus_ system shall<br>allow users to create a data<br>subscription request.|ConOps §4.5|||H|
|I-033J1|QEDS shall be able to<br>accept a subscription<br>request.|||||



_04037-rq301srs0100_

_Page 63_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_






|ID<br>I-033J2|Requirement<br>QEDS shall accept data<br>subscriptions that include<br>an environmental data<br>request and the publishing<br>trigger.|Source|Allocation -<br>QEDS|Comment|Criticality|
|---|---|---|---|---|---|
|I-033J3|QEDS shall be able to<br>accept subscription requests<br>with triggers based on a<br>schedule.|||||
|I-033J4|QEDS shall be able to<br>accept subscription requests<br>with triggers based on<br>quality flag state changes.|||||
|I-033J5|QEDS shall disseminate<br>subscription responses to<br>the originating request<br>address by default.|||||
|I-033J6|QEDS shall disseminate<br>subscription responses to a<br>specified return address.|||||
|I-033J7|QEDS shall uniquely<br>identify environmental data<br>subscriptions.|||||
|I-033J8|QEDS shall automatically<br>delete a subscription when<br>the triggering event will not<br>occur again and no more<br>responses are possible.|||||
|P-024|The_Clarus_ system shall be<br>able to publish new data<br>within twenty minutes of<br>data receipt.|ConOps §3.2 (Fig.<br>7)|QChS,<br>QEDS||H|



_04037-rq301srs0100_

_Page 64_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_






|ID<br>P-024J1|Requirement<br>QEDS shall disseminate<br>subscription responses<br>within twenty minutes of<br>new data becoming<br>available.|Source|Allocation -<br>QEDS|Comment|Criticality|
|---|---|---|---|---|---|
|P-025|The_Clarus_ system shall<br>respond to a request for<br>information within one<br>minute.|MHI|QEDS,<br>EMS|Related to F-501.|H|
|P-025J1|QEDS shall respond to an<br>environmental data request<br>within one minute.|||||
|P-031|The_Clarus_ system shall be<br>able to handle three<br>hundred simultaneous<br>requests for environmental<br>data.|MHI|QEDS|Estimated that half of the concurrent users<br>may be requesting data at any one time.|H|
|P-031J1|QEDS shall be able to<br>respond to three hundred<br>simultaneous queries.|||||



_04037-rq301srs0100_

_Page 65_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_

###### **_4.9 Quality Checking Services (QChS)_**

The requirements in this section specify the services needed for quality checking. The QChS receive environmental data from
qualified environmental data cache, execute multiple methods to quality check the environmental data, apply quality flags, and
send quality checked environmental data to the Qualified Environmental Data Cache (QEDC) with its associated quality flags.









|ID|Requirement|Source|Allocation -<br>QChS|Comment|Criticality|
|---|---|---|---|---|---|
|F-100|The_Clarus_ system shall<br>collect, quality check, and<br>disseminate environmental<br>data.|ConOps §1|CS, QChS,<br>QEDS,<br>CAUI|“Environmental data” includes all NTCIP<br>1204 data (summarized in Table 1).|H|
|F-100H1|The QChS shall quality<br>check environmental data.|||||
|F-101|The_Clarus_ system shall<br>implement quality<br>checking processes as soon<br>as data become available.|ConOps §2.4|QChS, SS,<br>CAS||H|
|F-101H1|QChS shall be able to be<br>configured individually.|||||
|F-101H2|QChS processing order<br>shall be able to be<br>configured.|||||
|F-101H3|QChS processing shall<br>commence when new data<br>arrives but no less<br>frequently than the<br>scheduled interval.|||||
|F-111|The_Clarus_ system shall<br>provide environmental data<br>quality flags.|OCS|QChS,<br>CAUI,<br>QEDC||H|
|F-111H1|Each QChS shall produce a<br>unique quality flag value.|||||


_04037-rq301srs0100_

_Page 66_







_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_
















|ID<br>F-111H2|Requirement<br>The QChS shall be able to<br>indicate a numeric<br>confidence value.|Source|Allocation -<br>QChS|Comment|Criticality|
|---|---|---|---|---|---|
|F-115|The_Clarus_ system shall<br>provide notification of data<br>quality conditions to data<br>contributors.|ConOps §2.4|QChS,<br>QEDS|A “data contributor” could be a State DOT<br>maintenance engineer or traffic manager.|H|
|F-115H1|A QChS shall evaluate data<br>quality conditions.|||||
|F-121|The_Clarus_ system shall<br>detect out of range values.|ConOps §3.5.1.4|QChS|Examples – sensor range tests and climates<br>tests.|H|
|F-121H1|QChS algorithms shall use<br>sensor range metadata for<br>range checking bounds.|||||
|F-121H2|QChS algorithms shall use<br>climate records for range<br>checking bounds.|||||
|F-121H3|QChS algorithms shall be<br>able to use monthly climate<br>extremes for range<br>checking bounds.|||||
|F-125|The_Clarus_ system shall<br>not modify original<br>observations.|OCS|QChS||H|
|F-125H1|QChS shall apply separate,<br>independent quality flags<br>that do not modify the<br>observation.|||||
|F-141|The_Clarus_ system shall<br>allow human quality<br>checks of observations.|OCS|CAUI,<br>QChS|Changed from “The_Clarus_ system shall<br>allow human intervention to override<br>automatically applied quality assessment.”<br>Example – manual quality test.|M|



_04037-rq301srs0100_

_Page 67_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_










|ID<br>F-141H1|Requirement<br>QChS shall implement a<br>manual override to set<br>quality flags.|Source|Allocation -<br>QChS|Comment|Criticality|
|---|---|---|---|---|---|
|F-151|The_Clarus_ system shall<br>record the methods applied<br>when deriving quality<br>checking information.|MHI|QChS, CAS||H|
|F-151H1|QChS shall indicate when<br>a quality check has been<br>performed.|||||
|F-155|The_Clarus_ system shall be<br>able to implement quality<br>checking rules for each<br>environmental parameter.|ConOps §3.5.1.4|QChS,<br>CAS, CAUI|Example – variable-specific tests.|H|
|F-155H1|QChS shall be able to<br>implement quality<br>checking rules for a<br>specific environmental<br>parameter.|||||
|F-161|The_Clarus_ system shall be<br>able to implement quality<br>checking rules for specific<br>environmental situations.|ConOps §3.5.1.4|QChS, CAS|The rules for setting quality flags on<br>environmental data elements may<br>themselves depend on other environmental<br>data. For example, stormy conditions may<br>allow more spatial and temporal variability<br>in wind speed observations than under fair<br>weather conditions.|H|
|F-161H1|QChS shall be able to<br>implement quality<br>checking rules for specific<br>environmental situations.|||||



_04037-rq301srs0100_

_Page 68_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_










|ID<br>F-162|Requirement<br>The Clarus system shall be<br>able to implement quality<br>checking spatial tests using<br>available data.|Source<br>OCS|Allocation -<br>QChS|Comment<br>New requirement. Available data could be<br>from adjacent environmental sensor stations<br>and ASOS. Examples – Barnes spatial test<br>and optimal interpolation spatial test.|Criticality<br>H|
|---|---|---|---|---|---|
|F-162H1|QChS shall be able to<br>implement quality<br>checking spatial tests using<br>available data.|||Available data could be from adjacent<br>environmental sensor stations and ASOS.||
|F-163|The_Clarus_ system shall be<br>able to implement quality<br>checking rules specific to<br>observation locations.|Task Force review|QChS, CAS|Quality checking rules may vary from<br>region to region.|H|
|F-163H1|QChS shall be able to<br>implement different quality<br>checking rules specific to<br>regional weather.|||||
|F-165|The_Clarus_ system shall be<br>able to base its quality<br>checking process on values<br>from multiple observations.|ConOps §3.5.1.4||Example – variable-specific and like<br>instrument tests.|H|
|F-165H1|QChS shall be able to flag<br>observations based on<br>more than one observation<br>type.|||||
|F-166|The_Clarus_ system shall be<br>able to base its quality<br>checking process on values<br>distributed in time.|OCS||New high-level requirement. Example –<br>step tests and persistence tests.|H|
|F-166H1|QChS shall be able to base<br>its quality checking process<br>on values distributed in<br>time.|||||



_04037-rq301srs0100_

_Page 69_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_












|ID<br>F-171|Requirement<br>The Clarus system shall be<br>able to base its quality<br>checking process on<br>historical environmental<br>data.|Source<br>Inferred from<br>ConOps §3.5.1.4|Allocation -<br>QChS<br>QChS, CAS|Comment<br>See F-121.|Criticality<br>H|
|---|---|---|---|---|---|
|F-171H1|QChS shall be able to use<br>historical environmental<br>data in their quality<br>checking algorithms.|||||
|F-175|The_Clarus_ system shall be<br>able to use multiple<br>algorithms for its quality<br>checking process.|Inferred from<br>ConOps §4.3|QChS, CAS|Multiple methods or comparisons may be<br>needed for a given observation.|M|
|F-175H1|QChS shall be<br>implemented for each<br>defined standard quality<br>checking algorithm.|||||
|F-213|The_Clarus_ system shall<br>allow access to new<br>surface transportation<br>related observed<br>environmental data.|ConOps §1, 2.4, 3.1|CS, QChS,<br>QEDC,<br>QEDS,<br>CAS, EMC,<br>EMS, DOG|Access could only be provided when new<br>data sources are established and available.|L|
|F-213H1|QChS shall be<br>implemented to quality<br>check new observation<br>types as they become<br>available.|||||
|F-223|The_Clarus_ system shall<br>process data as they are<br>received.|ConOps §3.4.3|CS,QChS||H|



_04037-rq301srs0100_

_Page 70_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_














|ID<br>F-223H1|Requirement<br>QChS shall apply quality<br>flags to data as they are<br>received.|Source|Allocation -<br>QChS|Comment|Criticality|
|---|---|---|---|---|---|
|F-905|The_Clarus_ system shall<br>log data transactions.|MHI|CS, QEDS,<br>EMS,<br>QChS,<br>CAS, SS,<br>DOG||H|
|F-905H1|QChS shall log quality<br>checking activity.|||||
|H-020|The_Clarus_ system shall<br>acquire, process, and<br>disseminate environmental<br>data.|ConOps §2.1|CS, QChS,<br>QEDS|Roll up of H-021, H-022, H-023, which<br>were deprecated.|H|
|H-301|The_Clarus_ system shall be<br>able to acquire, process,<br>and disseminate<br>environmental data from<br>across North America.|ConOps §3.4.2,<br>amended in Task<br>Force review|CS, QChS,<br>QEDS|North America in this context includes the<br>United States, it territories, Canada, and<br>Mexico|H|
|H-<br>301H1|QChS shall process<br>environmental data from<br>across North America.|||||
|P-023|The_Clarus_ system shall be<br>able to complete an<br>automated quality checking<br>check of environmental<br>data within ten seconds of<br>data receipt.|OCS|QChS||H|



_04037-rq301srs0100_

_Page 71_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_






|ID<br>P-023H1|Requirement<br>A QChS shall be able to<br>complete an automated<br>quality check within ten<br>seconds of when data is<br>available for checking.|Source|Allocation -<br>QChS|Comment|Criticality|
|---|---|---|---|---|---|
|P-024|The_Clarus_ system shall be<br>able to publish new data<br>within twenty minutes of<br>data receipt.|ConOps §3.2 (Fig.<br>7)|QChS,<br>QEDS||H|
|P-024H1|All QChS shall be<br>completed within twenty<br>minutes of data being<br>available for checking.|||A goal of 5 minutes was established at the<br>task force review.||



_04037-rq301srs0100_

_Page 72_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_

###### **_4.10 Schedule Service (SS)_**

The requirements in this section specify the scheduling of the collector services and quality checking services. The SS schedules
input for environmental data from collectors and contributors, schedules Quality Checking Services (QCS), and schedules
dissemination of qualified environmental data and metadata based on subscriptions.


















|ID|Requirement|Source|Allocation<br>- SS|Comment|Criticality|
|---|---|---|---|---|---|
|D-051|The_Clarus_ system shall<br>disseminate data in response to<br>a scheduled request.|OCS|QEDS, SS||H|
|D-<br>051K1|The SS shall be able to initiate<br>a QEDS response.|||||
|F-101|The_Clarus_ system shall<br>implement quality checking<br>processes as soon as data<br>become available.|ConOps §2.4|QChS, SS,<br>CAS||H|
|F-<br>101K1|The SS shall be able to initiate<br>QChS.|||||
|F-905|The_Clarus_ system shall log<br>data transactions.|MHI|CS, QEDS,<br>EMS,<br>QChS,<br>CAS, SS,<br>DOG||H|
|F-<br>905K1|The SS shall record when it<br>initiates actions.|||||
|I-016|The_Clarus_ system shall<br>transfer data as efficiently as<br>possible.|Inferred from ConOps<br>§3.2|CS, EMS,<br>QEDS, SS|Related to F-501, F-222.|H|
|I-016K1|The SS shall be able to store<br>event schedules.|||||
|I-016K2|The SS shall be able to initiate<br>CS.|||||



_04037-rq301srs0100_

_Page 73_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_

###### **_4.11 Program Requirements_**

The requirements in this section specify the distribution, performance, and organizational requirements.






|ID|Requirement|Source|Allocation|Comment|Criticality|
|---|---|---|---|---|---|
|D-011|The_Clarus_ system shall be<br>able to be hosted at one or<br>more physical locations.|MHI|||H|
|D-<br>011A1|The_Clarus_ system shall<br>track its constituent hosts.|||||
|D-<br>011A2|The_Clarus_ system shall<br>allocate each collector to a<br>specific host.|||||
|D-<br>011A3|The_Clarus_ system shall<br>allocate each contributor to a<br>specific host.|||||
|D-<br>011A4|_Clarus_ hosts shall be able to<br>aggregate environmental<br>data from other_Clarus_ <br>hosts.|||||
|D-<br>011A5|_Clarus_ hosts shall be able to<br>distribute queries to other<br>_Clarus_ hosts.|||||
|D-021|The_Clarus_ system shall use<br>hardware that implements<br>industry accepted standard<br>interfaces.|MHI|||H|
|D-031|The_Clarus_ system shall use<br>software that implements<br>industry accepted standard<br>interfaces.|MHI|||H|
|D-041|The_Clarus_ system shall be<br>able to operate on redundant<br>hardware.|ConOps §3.4.2|||H|



_04037-rq301srs0100_

_Page 74_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_
















|ID|Requirement|Source|Allocation|Comment|Criticality|
|---|---|---|---|---|---|
|D-101|All HTML coding shall<br>meet FHWA requirements<br>for web sites.|Contract||FHWA requirements for HTML<br>coding can be found at<br>http://www.tfhrc.gov/qkref/qrg08.htm|H|
|D-111|The_Clarus_ system shall<br>support modular<br>components.|OCS|||H|
|D-121|The_Clarus_ system shall be<br>able to use latitude,<br>longitude, and elevation<br>coordinates to specify<br>location to the nearest three<br>feet.|MHI|||H|
|D-126|The_Clarus_ system shall use<br>Coordinated Universal Time<br>(UTC) for all timestamps.|OCS|||H|
|X-801|The_Clarus_ program shall<br>alert users to system<br>modifications.|OCS||Changed from F-801.|H|
|P-011|The_Clarus_ system shall be<br>able to publish<br>environmental data at three<br>times the volume rate that it<br>collects it.|MHI|||M|
|P-041|The_Clarus_ system shall be<br>able to support six hundred<br>concurrent users.|MHI||An estimate of the number of<br>concurrent potential users of the<br>_Clarus_ system: one tenth of the<br>registered users at any one time.|H|
|P-042|The_Clarus_ system shall be<br>able to support six thousand<br>registered users.|MHI||An estimate of the number of<br>individual users: a pool of 250<br>weather service providers, ten per<br>provider; 100 governmental agencies,<br>25 per agency; and 1000 other users.|H|



_04037-rq301srs0100_

_Page 75_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_






|ID|Requirement|Source|Allocation|Comment|Criticality|
|---|---|---|---|---|---|
|Q-011|The_Clarus_ system shall be<br>able to mitigate<br>communication denial-of-<br>service attacks.|MHI|||H|
|Q-013|The_Clarus_ system shall be<br>able to respond to 95% of all<br>requests for environmental<br>data 95% of the time.|MHI|||H|
|X-201|The_Clarus_ program shall<br>establish data sharing<br>agreements with all<br>participating sources of<br>environmental data.|Task Force review|||H|
|X-<br>20110|The_Clarus_ program shall<br>identify categories of<br>recipients for dissemination<br>of data.|Task Force||||
|X-<br>20111|The_Clarus_ program shall<br>determine the need for<br>bilateral_Clarus_ Data<br>Sharing Agreements with<br>countries, agencies, states,<br>and regions.|||The U.S. Department of State will<br>facilitate the review of international<br>agreements if it is determined that a<br>Circular 175 process is required.<br>[See Case-Zablocki Act of 1977]||
|X-<br>20112|The authorized<br>representative(s) of the<br>contributors shall be<br>identified.|||Both the signatories of the_Clarus_ <br>Data Sharing Agreement and the<br>positions/organizations responsible<br>for Quality Control (QC)/Quality<br>Assurance (QA) shall be named.||



_04037-rq301srs0100_

_Page 76_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_






|ID|Requirement|Source|Allocation|Comment|Criticality|
|---|---|---|---|---|---|
|X-<br>20113|The contributors shall<br>identify and define the types<br>of data and information that<br>will be included in the<br>_Clarus_Data Sharing<br>Agreement.|||Examples of data and information<br>include surface condition data,<br>atmospheric condition data,weather<br>hazards reports and associated<br>metadata.||
|X-<br>20114|The contributors shall<br>identify the intended use of<br>their shared data and<br>information.|||||
|X-<br>20115|The contributors shall<br>identify the categories of<br>recipients of their shared<br>data and information.|||||
|X-<br>20116|The contributors shall define<br>the units of measurements of<br>their shared data and<br>information.|||Identification markers are needed for<br>qualitative data and information.||
|X-<br>20118|The_Clarus_ program shall<br>determine how it will<br>provide data and<br>information to contributors.|||||
|X-<br>20119|The_Clarus_ program shall<br>provide data and<br>information statistics on its<br>operation to contributors.|||||
|X-<br>20120|The contributors shall<br>inform the_Clarus_ program<br>of changes in authorized<br>personnel/offices.|Task Force||||



_04037-rq301srs0100_

_Page 77_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


|ID|Requirement|Source|Allocation|Comment|Criticality|
|---|---|---|---|---|---|
|X-<br>20121|The_Clarus_ program shall<br>inform contributors of the<br>"acceptance and use" of<br>their data and information.|||||
|X-<br>20123|The_Clarus_ Initiative<br>Management Team shall<br>undertake joint<br>communications activities<br>and products that will<br>enhance public<br>understanding and<br>dissemination of<br>contributions of the_Clarus_ <br>program.|||||
|X-<br>20124|The_Clarus_ Initiative<br>Management Team shall<br>agree upon the activities and<br>products that will enhance<br>public understanding/<br>communication of the<br>contribution of the_Clarus_ <br>program.|||||
|X-<br>20126|The contributors shall<br>inform the_Clarus_ program<br>of known error(s) and<br>modifications in its data and<br>information.|||||
|X-<br>20127|The_Clarus_ program shall<br>determine its redistribution<br>of shared data from<br>contributors based upon<br>_Clarus_ Data Sharing<br>Agreements.|||||



_04037-rq301srs0100_

_Page 78_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_




|ID|Requirement|Source|Allocation|Comment|Criticality|
|---|---|---|---|---|---|
|X-<br>20128|The_Clarus_ program shall<br>report successes and failures<br>in data and information<br>transmission to its<br>contributors.|||||
|X-<br>20129|The contributors shall report<br>periods of data and<br>information outages to the<br>_Clarus_ program.|||||
|X-<br>20131|The_Clarus_ program shall<br>maintain information about<br>requestors and their access<br>to data and information.|||||
|X-<br>20132|The_Clarus_ Initiative<br>Management Team shall<br>review and amend data and<br>information sharing and use<br>policies.|||Define policy advisement structure.||
|X-<br>20133|The_Clarus_ Initiative<br>Management Team shall<br>specify the general<br>frequency of policy<br>meetings.|||Define policy advisement structure.||
|X-<br>20134|The_Clarus_ Initiative<br>Coordinating Committee<br>shall nominate technical<br>expert(s) to participate on<br>technical working groups.|||Define technical advisement<br>structure.||



_04037-rq301srs0100_

_Page 79_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_






|ID|Requirement|Source|Allocation|Comment|Criticality|
|---|---|---|---|---|---|
|X-<br>20135|The requestors shall adhere<br>to the intellectual property<br>requirements of the_Clarus_ <br>User Agreement.|Task Force||||
|X-<br>20136|The contributors shall<br>adhere to the intellectual<br>property requirements of the<br>_Clarus_ Data Sharing<br>Agreement.|||||
|X-<br>20139|The contributors shall have<br>the right to use the_Clarus_ <br>system data and information<br>for purposes delineated<br>within the_Clarus_ Data<br>Sharing Agreement.|||||
|X-<br>20140|The requestors shall have<br>the right to use the_Clarus_ <br>system data and information<br>for purposes delineated<br>within the_Clarus_ User<br>Agreement.|Task Force||||
|X-<br>20141|The_Clarus_ program shall<br>have the right to reject the<br>use of data and information<br>provided by the contributors<br>when deemed appropriate.|||||
|X-<br>20142|The_Clarus_ program shall<br>inform contributors of the<br>policies, processes and<br>procedures employed to<br>reject data and information<br>provided by the contributors.|||||



_04037-rq301srs0100_

_Page 80_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_






|ID|Requirement|Source|Allocation|Comment|Criticality|
|---|---|---|---|---|---|
|X-<br>20149|The contributors shall<br>provide the_Clarus_ program<br>with a timely notice of their<br>intent to change, alter,<br>replace, or eliminate any<br>shared data and information<br>as specified within this<br>_Clarus_ Data Sharing<br>Agreement.|||||
|X-<br>20152|Any reference in the_Clarus_ <br>Data Sharing Agreement to<br>statutes, regulations and<br>rules shall be a reference to<br>the amended, substituted,<br>replaced or re-enacted<br>statute, regulations and<br>rules.|||||
|X-<br>20165|The_Clarus_ program shall<br>provide to contributors the<br>limitation of liability for<br>contributing environmental<br>data and metadata.|Task Force||||
|X-<br>20166|The_Clarus_ program shall<br>provide to requesters the<br>limitation of liability for<br>using environmental data<br>and metadata.|Task Force||||
|X-205|The_Clarus_ program shall<br>maintain continuous 24x7<br>operations.|OCS|||H|



_04037-rq301srs0100_

_Page 81_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_






















|ID|Requirement|Source|Allocation|Comment|Criticality|
|---|---|---|---|---|---|
|X-207|The_Clarus_ program shall<br>provide an environment that<br>has uninterruptible power<br>for the_Clarus_ system.|MHI|||H|
|X-209|The_Clarus_ program shall<br>provide an environment that<br>has redundant<br>communication for the<br>_Clarus_ system.|MHI|||H|
|X-211|The_Clarus_ program shall<br>provide network<br>management tools.|OCS||Network management tools can be<br>used to determine latency.|H|
|X-215|The_Clarus_ program shall<br>provide setup support.|ConOps §3.3.1 (Fig. 9)|||H|
|X-221|The_Clarus_ program shall<br>provide for customer<br>service.|OCS|||H|
|X-225|The_Clarus_ program shall<br>provide a trained support<br>staff.|ConOps §3.3.1|||H|
|X-232|The_Clarus_ program shall<br>define quality checking rules<br>for environmental<br>observations.|MHI||Specifies the rules to be implemented<br>according to F-155, F-161, F-165, F-<br>171, and F-175.|H|
|X-233|The_Clarus_ program shall<br>define data retention<br>standards.|MHI|||H|
|X-235|The_Clarus_ program shall<br>provide documentation of <br>_Clarus_ standards.|OCS||That is, the_Clarus_ program needs to<br>provide documentation of whatever<br>standards it creates for its own<br>development, deployment,<br>management, and operations.|H|



_04037-rq301srs0100_

_Page 82_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_






|ID|Requirement|Source|Allocation|Comment|Criticality|
|---|---|---|---|---|---|
|X-237|The_Clarus_ program<br>standards shall<br>accommodate contributions<br>of new sensor technologies<br>to the_Clarus_ system.|Inferred from ConOps §1|||M|
|X-239|The_Clarus_ program<br>standards shall support<br>multiple methods of data<br>delivery to users.|Inferred from ConOps<br>§4.3|||M|
|X-305|The_Clarus_ program shall<br>maintain a comprehensive<br>_Clarus_ system test<br>environment.|OCS|||H|
|X-311|The_Clarus_ program shall<br>test all software changes in<br>the designated test<br>environment before<br>deployment to production.|OCS|||H|
|X-315|The_Clarus_ program shall<br>test all hardware changes in<br>the designated test<br>environment before<br>deployment to production.|OCS|||H|
|X-601|The_Clarus_ program shall<br>operate the_Clarus_ system<br>according to its published IT<br>Security Plan.|Contract|||H|



_04037-rq301srs0100_

_Page 83_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_






|ID|Requirement|Source|Allocation|Comment|Criticality|
|---|---|---|---|---|---|
|X-605|The_Clarus_ program shall<br>operate according to<br>Government IT security<br>requirements as outlined in<br>OMB Circular A-130,<br>Management of Federal<br>Information Resources,<br>Appendix III, Security of<br>Federal Automated<br>Information Resources.|Contract|||H|
|X-611|The_Clarus_ program shall<br>operate according to<br>Government IT security<br>requirements as outlined in<br>the National Institute of<br>Standards and Technology<br>(NIST) Guidelines,<br>Departmental Information<br>Resource Management<br>Manual, and associated<br>guidelines.|Contract|||H|
|X-615|The_Clarus_ program shall<br>operate according to<br>Government IT security<br>requirements as outlined in<br>U.S. DOT Order 1630.2B,<br>Personnel Security<br>Management.|Contract|||H|
|X-805|Weather service providers<br>shall be able to use_Clarus_ <br>data to provide localized<br>special weather products.|ConOps §3.4.2|||L|



_04037-rq301srs0100_

_Page 84_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_






|ID|Requirement|Source|Allocation|Comment|Criticality|
|---|---|---|---|---|---|
|X-811|Public agency maintenance<br>and construction personnel<br>shall be able to use the<br>_Clarus_ system to obtain<br>environmental conditions.|ConOps §2.5.2|||L|
|X-815|Rail system personnel shall<br>be able to use the_Clarus_ <br>system to obtain<br>environmental conditions.|Inferred from ConOps<br>§2.5.7|||L|
|X-821|Traffic management<br>personnel shall be able to<br>use the_Clarus_ system to<br>obtain environmental<br>conditions.|Inferred from ConOps<br>§2.5.3|||L|
|X-823|Transit personnel shall be<br>able to use the_Clarus_ <br>system to obtain<br>environmental conditions.|Inferred from ConOps<br>§2.5.5|||L|
|X-825|The freight community shall<br>be able to use the_Clarus_ <br>system to obtain<br>environmental conditions.|Inferred from ConOps<br>§2.5.8|||L|
|X-827|Emergency management and<br>public safety personnel shall<br>be able to use the_Clarus_ <br>system to obtain<br>environmental conditions.|Inferred from ConOps<br>§2.5.6|||L|
|X-905|The_Clarus_ program shall<br>maintain information about<br>data providers.|OCS|||H|



_04037-rq301srs0100_

_Page 85_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_





|ID|Requirement|Source|Allocation|Comment|Criticality|
|---|---|---|---|---|---|
|X-910|The_Clarus_ program shall<br>maintain metadata about<br>each data provider's<br>network.|OCS|||H|
|X-915|The_Clarus_ program shall<br>maintain information about<br>data provider redistribution<br>restrictions.|OCS|||H|
|X-921|The_Clarus_ program shall<br>maintain information about<br>service providers.|OCS|||H|
|X-925|The_Clarus_ program shall<br>maintain information about<br>service provider<br>communications.|OCS|||M|
|X-931|The_Clarus_ program shall<br>maintain information about<br>service provider access to<br>data.|OCS|||H|
|X-935|The_Clarus_ program shall<br>allow potential weather<br>element data providers to<br>request permission to submit<br>weather information.|MHI|||H|
|X-101|The_Clarus_ system shall<br>accept data only from<br>sources which data sharing<br>agreements have been<br>established.|MHI|(The<br>_Clarus_ <br>program<br>shall<br>approve<br>sources.)|“Approved sources” are anticipated<br>to be those with whom a data sharing<br>agreement has been established.|H|


_04037-rq301srs0100_

_Page 86_









_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_

##### **APPENDIX A - DEFINITIONS, ACRONYMS, AND** **ABBREVIATIONS**

The following table provides definitions of terms, acronyms, and abbreviations to
assist interpretation of this document.


|Term|Definition|
|---|---|
|ADAS<br>ARPS<br>ASCII<br>CAS<br>CAUI<br>CCTV<br>Clarus Initiative<br>Clarus Program<br>Clarus System<br>CMML<br>Collector<br>ConOps<br>Contributor<br>COTS<br>CS<br>DOG<br>DOT<br>DRS<br>DSS<br>DST<br>EMC<br>EMS<br>Environmental data|ARPS Data Analysis System<br>Advanced Regional Prediction System<br>A code that represents letters, numerals, punctuation marks and control signals<br>as seven bit groups.<br>Configuration and Administration Service<br>Configuration and Administration User Interface<br>Closed Circuit Television<br>• <br>Development of tools, models, decision support that leverage the_Clarus_ <br>System<br>• <br>End-to-End processes spanning data gathering to road weather<br>information products & services<br>• <br>Research activities that support creation of road weather information<br>products & services <br>Operations and maintenance functions and personnel needed to sustain the<br>_Clarus_ System<br>Tools for sharing surface weather observations and relevant surface<br>transportation conditions<br>Canadian Meteorological Markup Language<br>An electronic device used to convert environmental sensor electrical signals<br>into environmental condition measured values and store them for retrieval.<br>Concept of Operations<br>A managing agency or organization that owns and/or operates a set of<br>environmental sensor collectors.<br>Commercial Off-the-Shelf<br>Collector Services<br>Watchdog<br>Department of Transportation<br>Detailed Systems Requirements Specification<br>Decision Support System<br>Daylight Savings Time<br>Environmental Metadata Cache<br>Environmental Metadata Services<br>In the_Clarus_ context, includes atmospheric, surface, and hydrologic data;<br>more specifically, it includes all data defined in NTCIP 1204 (Ref. 8).|



_04037-rq301srs0100_

_Page 87_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


|Term|Definition|
|---|---|
|Environmental metadata<br>ESS<br>External data<br>FHWA<br>GPS<br>HDF<br>hPa<br>HTML<br>ICC<br>IEEE<br>in-situ<br>IT<br>ITE<br>ITS<br>ITS America<br>MADIS<br>MDSS<br>metadata<br>MHI<br>MS/ETMCC<br>NCSA<br>netCDF<br>NIST<br>NOAA<br>NTCIP<br>NWS<br>OCS<br>OMB<br>Open<br>PMP|In the_Clarus_ context, includes all contributor, collector, ESS, and sensor data<br>relating to environmental data.<br>Environmental Sensor Station<br>Weather data used to assist in quality checking such as ASOS and climate<br>records<br>Federal Highway Administration<br>Global Positioning System<br>Hierarchical Data Format; a data file format developed at the National Center<br>for Supercomputing Applications (NCSA) (http://hdf.ncsa.uiuc.edu/)<br>hectopascal = 100 Pascals = 1 millibar<br>Hypertext Markup Language<br>(_Clarus_) Initiative Coordinating Committee<br>Institute of Electrical and Electronic Engineers, Inc.<br>From Latin, “in-situ” means “in place.” As applied to meteorological data, it<br>refers to data specific to a (fixed) point of observation.<br>Information Technology<br>Institute of Transportation Engineers<br>Intelligent Transportation Systems<br>Intelligent Transportation Society of America<br>Meteorological Assimilation Data Ingest System<br>Maintenance Decision Support System<br>In common information systems use, “metadata” is “data about data.” Within<br>the meteorological community, this use has been extended to include data<br>about objects related to weather observations. For example, location data for<br>an ESS becomes metadata for the observation data.<br>Mixon/Hill, Inc.<br>Message Set for External Traffic Management Center Communication.<br>National Cener for Supercomputing Applications<br>Network Common Data Form is a binary data format standard for exchanging<br>scientific data<br>National Institute of Standards and Technology<br>National Oceanic and Atmospheric Administration<br>National Transportation Communications for ITS Protocol<br>National Weather Service<br>Oklahoma Climatological Survey<br>Office of Management and Budget<br>Using interfaces that are non-proprietary and broadly supported within the<br>information technology industry.<br>Project Management Plan|



_04037-rq301srs0100_

_Page 88_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


|Term|Definition|
|---|---|
|Polling<br>QA<br>QC<br>QCh<br>QChS<br>QEDC<br>QEDS<br>Quality checking<br>Quality flag<br>Quality manager<br>Requestor<br>RUC<br>RWIS<br>Security groups<br>SHEF<br>SS<br>STWDSR<br>STWSP<br>TMC<br>TMDD<br>TOC<br>TRB<br>U.S. DOT<br>UTC<br>VII<br>WIST|Asking for information<br>Quality Assurance<br>Quality Control<br>Quality Check or Quality Checking<br>Quality Checking Services<br>Qualified Environmental Data Cache<br>Qualified Environmental Data Services<br>The operational activities and techniques required to ensure that quality<br>requirements have been fulfilled.<br>An indicator of the degree to which quality requirements have been fulfilled; in<br>the_Clarus_ context, an indicator of the reliability or usefulness of a data<br>element or dataset.<br>Personnel charged with reviewing the quality of the environmental data.<br>The person or group requesting information from the Clarus system.<br>Rapid Update Cycle<br>Road Weather Information System<br>A method of grouping users and their privileges.<br>Standard Hydrological Encoding Format<br>Schedule Service<br>Surface Transportation Weather Decision Support Requirements<br>Surface Transportation Weather Service Provider<br>Transportation Management Center<br>Traffic Management Data Dictionary<br>Transportation (Traffic) Operations Center<br>Transportation Research Board<br>U.S. Department of Transportation<br>Coordinated Universal Time<br>Vehicle Infrastructure Integration<br>Weather Information for Surface Transportation|



_04037-rq301srs0100_

_Page 89_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_

##### **APPENDIX B - SUPPLEMENTAL DESCRIPTION OF** **CLARUS QC TESTS**


The _Clarus_ detailed requirements describe QC tests to be implemented as _Clarus_
standard tests. This appendix provides descriptions of these QC test methods as a
means of clarifying the intended implementations. These descriptions should not
be interpreted, however, as further elaborations of requirements or as design
specifications. The _Clarus_ system design descriptions will provide the final
specifications and will be subject to formal design review.

**Manual Quality Test**

The _Clarus_ manual quality test allows authorized _Clarus_ personnel to flag
particular observations as “passed” or “failed” independent of the automated
analysis. For instance, if a network manager communicates to _Clarus_ that one of
its stations has a temperature bias, then that station’s temperature data can be
manually flagged as “failed” until the network corrects the problem. If a _Clarus_
QA meteorologist determines that suspicious-looking snow depth data are from a
real, meteorological event, that station’s snow depth can be manually flagged as
“passed” until the event ends. Observations that have received manual quality
checks need not be run through the automated quality checks (Fiebrich and
Crawford 2001).

**Sensor Range Test**

The _Clarus_ range test will flag any observation that lies outside of the predetermined range threshold values as “failed”. The threshold values will usually
be determined via sensor specifications or theoretical limits (Meek and Hatfield
1994). For instance, the range for relative humidity would likely be 0 to 100%.
Observations that have received range filter flags of “failed” need not be run
through the automated quality checks.

**Climate Test**

The _Clarus_ climate test will flag any observation that exceeds defined, variablespecific climatological ranges as “failed” (Reek et al., 1992). Otherwise, the
observation will be flagged as “passed”. The _Clarus_ climatological threshold
values will be station-specific and will be based on either regional extremes or
individual station extremes (if they are available).

**Barnes Spatial Test**

The _Clarus_ Barnes spatial test will calculate an estimate for each observation
using a one-pass Barnes objective analysis routine (Barnes 1964, Shafer et al.
2000). Neighboring observations will be weighted according to their distance
from the station that is being estimated:


#### ∑ w ( ri ) zi

_Ze_ =
#### ∑ w ( ri )



,



_04037-rq301srs0100_

_Page 90_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


where _Ze_ is the estimated value, _zi_ are the neighboring observations, and _w_ is the
weighting, based on the neighboring site’s distance to the site in question. The
weighting decreases exponentially with distance from the station:



_W_ ( _ri_ ) = _e_




- _ri_ 2

_ko_ .



The weight function, _ko_, is determined by the Barnes analysis based upon the
mean station spacing. The standard deviation, σ, of the observations within the
radius of influence is calculated. The ratio of the difference between the observed
( _Zo_ ) and estimated ( _Ze_ ) values to the analysis’ standard deviation is defined as:

∆= _[Z][e]_ [ −] _[Z][o]_ .

σ

The _Clarus_ Barnes spatial test will fail any observation whose value differs by
more than three standard deviations from its estimated value (i.e., ∆ - 3).
Otherwise, the _Clarus_ Barnes spatial test will pass the observation, and list the ∆
value with the QC flag to indicate the confidence in the observation. For instance,
a ∆ value of 1.5 would indicate that the observation was within 1.5 standard
deviations of its expected value. Further analysis may indicate that the Barnes
spatial test should have the ability to incorporate background fields (e.g., ADAS
or RUC analysis from the previous hour) into the analysis to compensate for
regions that have inadequate spatial or temporal coverage.

**Optimal Interpolation Spatial Test**

The _Clarus_ Optimal Interpolation spatial test will calculate an estimate for each
observation using a univariate optimal-interpolation technique (Belousov et al.,
1968). Specifically, the test will use the nearest observation in each of eight
directional sectors distributed around the observation (Miller and Benjamin,
1992). If the difference between the observation and estimate is “small”, the
observation is flagged as “passed”, and the difference between the observation
and the estimate is listed to indicate the confidence in the observation. The
threshold for “small” is a function of the expected analysis error, which is
dependent on location and density of the neighboring observations (Gandin, 1963,
and Miller and Benjamin, 1991). If the difference is large, then neighboring
observations are successively eliminated from the analysis to determine whether
the discrepancy was caused by an erroneous observation from a neighboring site.
If successively eliminating a neighboring station from the analysis results in a
value that agrees with the observation, then the observation is flagged as
“passed”. The difference between the observation and the estimate indicates the
confidence in the observation. In addition, the suspicious neighboring observation
is not used in the analysis of other stations. If successive eliminations of
neighboring stations does not result in an estimated value that agrees with the
observation, the observation is flagged as “failed”.

The _Clarus_ Optimal Interpolation spatial check will incorporate a background
field (e.g., ADAS or RUC analysis from the previous hour) into the analysis to
compensate for regions that have inadequate spatial or temporal coverage. Miller



_04037-rq301srs0100_

_Page 91_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


and Benjamin (1992) found that subtracting the background field before
performing the analysis improved error detection.

**Step Test**

The _Clarus_ step test will flag all observations whose consecutive values in time
exceed predefined variable-specific step threshold values as “failed” (Fiebrich and
Crawford 2001). For instance, if a pressure observation changes by greater than
10 hPa in five minutes, the observation is flagged as “failed”. As another
example, if a temperature observation changes by greater than 10 °C in five
minutes, the observation would be flagged as “failed”.

**Persistence Test**

The _Clarus_ persistence test will flag all observations whose consecutive values in
time remain the same for a predefined variable-specific persistence threshold
value during a defined time interval as “failed” (Oklahoma Climatological
Survey). For instance, if a pressure observation remains unchanged (to the nearest
pascal) for more than 30 minutes, the observation would be flagged as “failed”.
As another example, if a temperature observation remains unchanged (to the
nearest tenth of a °C) for more than 120 minutes, the observation would be
flagged as “failed”.

**Like Instrument Test**

The _Clarus_ like instrument test will flag all observations that differ from the
corresponding like-instrument observations by more than a predefined variablespecific threshold value as “failed” (Fiebrich and Crawford 2001). For instance, if
the wind speed at 10 m differs from the wind speed at 2 m by more than 5 ms [-1],
then the observation would be flagged as “failed”.

**Potential Temperature Test**

The _Clarus_ potential temperature test will flag all temperature observations whose
potential temperatures fail the _Clarus_ Optimal Interpolation spatial test as
“failed”. Elevation differences will be incorporated to help model the horizontal
correlation between mountain stations (Miller and Benjamin 1992).

**Dew Point Temperature Test**

The _Clarus_ dew point temperature test will flag all temperature and relative
humidity observations whose resulting dew point values fail the _Clarus_ Barnes
spatial test or the _Clarus_ Optimal Interpolation spatial test as “failed” (Oklahoma
Climatological Survey).

**Sea Level Pressure Test**

The _Clarus_ sea level pressure test will flag all pressure observations whose
computed sea level pressure values fail the _Clarus_ Barnes spatial test or the
_Clarus_ Optimal Interpolation spatial test as “failed” (Oklahoma Climatological
Survey).



_04037-rq301srs0100_

_Page 92_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


**Theoretical Solar Radiation Test**

The _Clarus_ theoretical solar radiation test will flag all downwelling short wave
radiation observations whose values exceed the theoretical solar radiation for the
site’s latitude, longitude, and day of year as “failed” (Oklahoma Climatological
Survey).

**Precipitation Amount Test**

The _Clarus_ precipitation amount test would flag all precipitation amount
observations whose values differ from the radar-estimated precipitation amount
by more than a pre-determined threshold as “failed”. The nearest or best radar to
use for each location would be configurable. This technique is still being
researched and is not recommended for _Clarus_ proof-of-concept implementation
(Oklahoma Climatological Survey).

**Wind Direction Test**

The _Clarus_ wind direction test will function the same way as the Barnes and
Optimal Interpolation spatial tests do, with the exception that wind direction
estimates will be calculated from directional means (rather than arithmetic
means). In addition, the wind direction observation will be subject to this test only
if its associated wind speed observations are greater than 3 ms [-1] (Oklahoma
Climatological Survey). For instance, wind directions with associated wind
speeds of 0-3 ms [-1] will not be tested, because wind direction is highly variable
during calm/light winds.

**Soil Moisture Change Test**

The _Clarus_ soil moisture change test will function similarly to the step test except
that different thresholds will be set for changes in moistening versus drying. For
instance, the observations will be allowed to moisten more rapidly than they will
be allowed to dry (Oklahoma Climatological Survey 2005).

**Soil Moisture Freeze Test**

The _Clarus_ soil moisture freeze test will flag all observations whose associated
subsurface temperatures are below freezing as “failed”. Most soil moisture
sensors do not operate correctly when the soil is frozen (Oklahoma Climatological
Survey 2005).



_04037-rq301srs0100_

_Page 93_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_




















|Variable|Manual<br>Flag|Sensor<br>Range|Climate<br>Check|Barnes<br>Spatial|OI<br>Spatial|Persistence|Step|Like<br>Instrument|Variable<br>Specific|
|---|---|---|---|---|---|---|---|---|---|
|Air Temperature|X|X|X|X|X|X|X|X|X|
|Atmospheric Pressure|X|X|X|||X|X||X|
|Humidity|X|X|X|X|X|X|X||X|
|Long Wave Radiation|X|X|X|X||X|X|||
|Short Wave Radiation|X|X|X|X||X|X||X|
|Precipitation Occurrence|X|X||||X||X||
|Precipitation Type|X|X|X|||||X||
|Precipitation Rate|X|X|X|||X|X|X||
|Precipitation Amount|X|X|X||||X|X||
|Visibility|X|X|X|X||X|X|||
|Wind Speed|X|X|X|X|X|X|X|X||
|Wind Direction|X|X|X|||X|X||X|
|Wind Gust|X|X|X|X||X|X|X||
|Pavement Condition|X|X|X|X||||||
|Pavement Temperature|X|X|X|X||X|X|X||
|Pavement Chem Soln Freeze Pt|X|X|X|X||||||
|Pavement Ice Thickness|X|X|X|X||X|X|||
|Snow Depth|X|X|X|||X|X|||
|Water Depth, Road|X|X|X|||X|X|||
|Water Depth, Stream|X|X|X|||X|X|||
|Subsurface Temperature|X|X|X|X||X|X|X||
|Subsurface Moisture|X|X|X||||||X|
|Air Quality Condition|X|X|X|||||||
|Bio-Hazards|X|X|X|||||||
|Camera Imagery|X|X||||||||



_04037-rq301srs0100_

_Page 94_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


**Notes**














|Variable|Comments|
|---|---|
|Air Temperature|Like Instrument only if air temperature at another level is available.<br>Variable specific tests include potential temperature and dew point tests.|
|Atmospheric Pressure|Variable specific test includes sea level pressure test.|
|Humidity|Variable specific test includes dew point test.|
|Long Wave Radiation|Spatial would be possible only for net and/or LW down|
|Short Wave Radiation|Variable specific test includes theoretical solar radiation test.|
|Precipitation Occurrence|Like instrument test with precipitation rate observations.|
|Precipitation Type|Like instrument test with precipitation occurrence observations.|
|Precipitation Rate|Like instrument test with precipitation occurrence observations.|
|Precipitation Amount|Like instrument test with precipitation occurrence observations.|
|Visibility||
|Wind Speed|Like instrument only if wind speed at another level is available.|
|Wind Direction|Variable specific test includes the wind direction test.|
|Wind Gust|Like instrument with wind speed observations.|
|Pavement Condition||
|Pavement Temperature|Like instrument tests with air temperature and subsurface temperature (if available)|
|Pavement Chem Soln Freeze Pt||
|Pavement Ice Thickness||
|Snow Depth||
|Water Depth, Road||
|Water Depth, Stream||
|Subsurface Temperature|Intercomparison tests with air temperature and other subsurface<br>temperatures (if available)|
|Subsurface Moisture|Variable specific tests include soil moisture change and soil moisture freeze tests.|
|Air Quality Condition||
|Bio-Hazards||
|Camera Imagery||



_04037-rq301srs0100_

_Page 95_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


_Clarus Weather System Design_
_**Detailed System Requirements Specification**_


**Appendix B References**

Barnes, S. L., 1964: A technique for maximizing details in numerical weather
map analysis. _J. Appl. Meteor_ ., **3**, 396-409.

Belousov, S. L., L. S. Gandin, and S. A. Mashkovich, 1968 _: Computer Processing_
_of Current Meteorological Data_ . Ed. V. Bugaev. Meteorological
Translation No. 18, 1972, Atmospheric Environment Service, Downsview,
Ontario, Canada, 227 pp.

Fiebrich, C. A., and K. C. Crawford, 2001: The impact of unique meteorological
phenomena detected by the Oklahoma Mesonet and ARS Micronet on
automated quality checking. _Bull. Amer. Meteor. Soc_ ., **82**, 2173-2187.

Gandin, L. S., 1963: Objective Analysis of Meteorological Fields.
Gidrometeorologicheskoe Izdatel’stvo. Translated from Russian, 1965,
Israel Program for Scientific Translations, 242 pp.

Meek, D. W., and J. L. Hatfield, 1994: Data quality checking for single station
meteorological databases. _Agric. Forest Meteor_ ., **69**, 85-109.

Miller, P. A., and S. G. Benjamin, 1991: Horizontal quality checking for a realtime three-hourly assimilation system configured in isentropic coordinates.
_Preprints, Ninth Conf. Numerical Weather Prediction,_ Denver, Amer.
Meteor. Soc., 32-36.

Miller, P. A., and S. G. Benjamin, 1992: A system for the hourly assimilation of
surface observations in mountainous and flat terrain. _Mon. Wea. Rev_ ., **120**,
2342-2359.

Oklahoma Climatological Survey, 2005: Estimates of soil moisture from the
Oklahoma Mesonet, Version 3.0, 19 pp.

Reek, T., S. R. Doty, and T. W. Owen, 1992: A deterministic approach to the
validation of historical daily temperature and precipitation data from the
cooperative network. _Bull. Amer. Meteor. Soc.,_ **73**, 753-762.

Shafer, M. A., C. A. Fiebrich, D. S. Arndt, S. E. Fredrickson, and T. W. Hughes,
2000: Quality assurance procedures in the Oklahoma Mesonetwork. _J._
_Atmos. Oceanic Technol_ ., 17, 474-494.



_04037-rq301srs0100_

_Page 96_



_Copyright © 2005 Mixon/Hill, Inc._
_All rights reserved._


