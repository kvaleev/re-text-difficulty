---
consensus_grade_level: 12.4
headings_per_sentence: 0.02
lists_per_sentence: 0.0
smao_sentences_pct: 3.5
vague_words_per_sentence: 0.1
anaphora_per_sentence: 0.25
sentence_cv: 1.11
cpre_terms_per_sentence: 0.64
---
\

\

\

\

\

\

\

**Clarus Weather System Design**

**HIGH LEVEL**

**SYSTEM REQUIREMENTS SPECIFICATION**

\

\

July 2005

\

\

**Prepared By:**

\

\

Mixon/Hill, Inc.

12980 Metcalf Ave, Suite 470

Overland Park, Kansas 66213

**Table of Contents**

**[ ]{.Apple-converted-space}TOC \\O \"1-4\" \\H \\Z
\\U[ ]{.Apple-converted-space}**[ ]{.s1}**HYPERLINK \\L
\"\_TOC108576511\"**[ 1]{.s1}[ ]{.Apple-tab-span}[Introduction]{.s1}**[
]{.Apple-tab-span} PAGEREF \_TOC108576511 \\H 1**

[[ ]{.Apple-converted-space}]{.s2}**HYPERLINK \\l \"\_Toc108576512\"**[
1.1]{.s2}[[ ]{.Apple-tab-span}]{.s3}[Purpose]{.s2}**[ ]{.Apple-tab-span}
PAGEREF \_Toc108576512 \\h 1**

[[ ]{.Apple-converted-space}]{.s2}**HYPERLINK \\l \"\_Toc108576513\"**[
1.2]{.s2}[[ ]{.Apple-tab-span}]{.s3}[Scope]{.s2}**[ ]{.Apple-tab-span}
PAGEREF \_Toc108576513 \\h 1**

[[ ]{.Apple-converted-space}]{.s2}**HYPERLINK \\l \"\_Toc108576514\"**[
1.3]{.s2}[[ ]{.Apple-tab-span}]{.s3}[Definitions, Acronyms, and
Abbreviations]{.s2}**[ ]{.Apple-tab-span} PAGEREF \_Toc108576514 \\h 3**

[[ ]{.Apple-converted-space}]{.s2}**HYPERLINK \\l \"\_Toc108576515\"**[
1.4]{.s2}[[ ]{.Apple-tab-span}]{.s3}[References]{.s2}**[
]{.Apple-tab-span} PAGEREF \_Toc108576515 \\h 3**

[[ ]{.Apple-converted-space}]{.s2}**HYPERLINK \\l \"\_Toc108576516\"**[
1.5]{.s2}[[ ]{.Apple-tab-span}]{.s3}[Overview]{.s2}**[
]{.Apple-tab-span} PAGEREF \_Toc108576516 \\h 4**

[[ ]{.Apple-converted-space}]{.s1}**HYPERLINK \\L \"\_TOC108576517\"**[
2]{.s1}[ ]{.Apple-tab-span}[General Description]{.s1}**[
]{.Apple-tab-span} PAGEREF \_TOC108576517 \\H 5**

[[ ]{.Apple-converted-space}]{.s2}**HYPERLINK \\l \"\_Toc108576518\"**[
2.1]{.s2}[[ ]{.Apple-tab-span}]{.s3}[System Perspective]{.s2}**[
]{.Apple-tab-span} PAGEREF \_Toc108576518 \\h 5**

[[ ]{.Apple-converted-space}]{.s2}**HYPERLINK \\l \"\_Toc108576519\"**[
2.2]{.s2}[[ ]{.Apple-tab-span}]{.s3}[System Functions]{.s2}**[
]{.Apple-tab-span} PAGEREF \_Toc108576519 \\h 6**

[[ ]{.Apple-converted-space}]{.s2}**HYPERLINK \\l \"\_Toc108576520\"**[
2.3]{.s2}[[ ]{.Apple-tab-span}]{.s3}[User Characteristics]{.s2}**[
]{.Apple-tab-span} PAGEREF \_Toc108576520 \\h 10**

[[ ]{.Apple-converted-space}]{.s2}**HYPERLINK \\l \"\_Toc108576521\"**[
2.4]{.s2}[[ ]{.Apple-tab-span}]{.s3}[General Constraints]{.s2}**[
]{.Apple-tab-span} PAGEREF \_Toc108576521 \\h 14**

[[ ]{.Apple-converted-space}]{.s2}**HYPERLINK \\l \"\_Toc108576522\"**[
2.5]{.s2}[[ ]{.Apple-tab-span}]{.s3}[Assumptions and
Dependencies]{.s2}**[ ]{.Apple-tab-span} PAGEREF \_Toc108576522 \\h 15**

[[ ]{.Apple-converted-space}]{.s1}**HYPERLINK \\L \"\_TOC108576523\"**[
3]{.s1}[ ]{.Apple-tab-span}[Specific Requirements]{.s1}**[
]{.Apple-tab-span} PAGEREF \_TOC108576523 \\H 16**

[[ ]{.Apple-converted-space}]{.s2}**HYPERLINK \\l \"\_Toc108576524\"**[
3.1]{.s2}[[ ]{.Apple-tab-span}]{.s3}[Functional Requirements]{.s2}**[
]{.Apple-tab-span} PAGEREF \_Toc108576524 \\h 19**

[[ ]{.Apple-converted-space}]{.s2}HYPERLINK \\l \"\_Toc108576525\"[
3.1.1]{.s2}[[ ]{.Apple-tab-span}]{.s3}[General Functional
Requirements]{.s2}[ ]{.Apple-tab-span} PAGEREF \_Toc108576525 \\h 19

[[ ]{.Apple-converted-space}]{.s2}HYPERLINK \\l \"\_Toc108576526\"[
3.1.2]{.s2}[[ ]{.Apple-tab-span}]{.s3}[Functional Data
Requirements]{.s2}[ ]{.Apple-tab-span} PAGEREF \_Toc108576526 \\h 23

[[ ]{.Apple-converted-space}]{.s2}HYPERLINK \\l \"\_Toc108576527\"[
3.1.3]{.s2}[[ ]{.Apple-tab-span}]{.s3}[Functional Interface
Requirements]{.s2}[ ]{.Apple-tab-span} PAGEREF \_Toc108576527 \\h 25

[[ ]{.Apple-converted-space}]{.s2}**HYPERLINK \\l \"\_Toc108576528\"**[
3.2]{.s2}[[ ]{.Apple-tab-span}]{.s3}[Performance Requirements]{.s2}**[
]{.Apple-tab-span} PAGEREF \_Toc108576528 \\h 27**

[[ ]{.Apple-converted-space}]{.s2}HYPERLINK \\l \"\_Toc108576529\"[
3.2.1]{.s2}[[ ]{.Apple-tab-span}]{.s3}[Design Constraints]{.s2}[
]{.Apple-tab-span} PAGEREF \_Toc108576529 \\h 27

[[ ]{.Apple-converted-space}]{.s2}HYPERLINK \\l \"\_Toc108576530\"[
3.2.2]{.s2}[[ ]{.Apple-tab-span}]{.s3}[Quality Requirements]{.s2}[
]{.Apple-tab-span} PAGEREF \_Toc108576530 \\h 28

[[ ]{.Apple-converted-space}]{.s2}HYPERLINK \\l \"\_Toc108576531\"[
3.2.3]{.s2}[[ ]{.Apple-tab-span}]{.s3}[System Performance
Requirements]{.s2}[ ]{.Apple-tab-span} PAGEREF \_Toc108576531 \\h 29

[[ ]{.Apple-converted-space}]{.s2}**HYPERLINK \\l \"\_Toc108576532\"**[
3.3]{.s2}[[ ]{.Apple-tab-span}]{.s3}[Organizational
Requirements]{.s2}**[ ]{.Apple-tab-span} PAGEREF \_Toc108576532 \\h 30**

[[ ]{.Apple-converted-space}]{.s1}**HYPERLINK \\L \"\_TOC108576533\"**[
APPENDIX A -]{.s1}[ ]{.Apple-tab-span}[definitions, acronyms, and
abbreviations]{.s1}**[ ]{.Apple-tab-span} PAGEREF \_TOC108576533 \\H
35**

\

**Table of Figures**

[ ]{.Apple-converted-space}TOC \\T \"HEADER,1\" \\C \"FIGURE\" FIGURE 1
-- *CLARUS* DATA ACQUISITION, PROCESSING AND PUBLICATION[
]{.Apple-tab-span} PAGEREF \_TOC108576487 \\H 6

FIGURE 2 -- BASIC *CLARUS* SYSTEM OBJECTS AND FUNCTIONS[
]{.Apple-tab-span} PAGEREF \_TOC108576488 \\H 7

FIGURE 3 -- TIME HORIZONS FOR WEATHER DATA[ ]{.Apple-tab-span} PAGEREF
\_TOC108576489 \\H 9

FIGURE 4 -- *CLARUS* USER LAYERS AND TIME HORIZON RELATIONSHIPS[
]{.Apple-tab-span} PAGEREF \_TOC108576490 \\H 11

FIGURE 5 -- CONTEXT DIAGRAM OF *CLARUS* USER NEEDS[ ]{.Apple-tab-span}
PAGEREF \_TOC108576491 \\H 12

FIGURE 6 -- HIGH-LEVEL REQUIREMENTS CONTEXT[ ]{.Apple-tab-span} PAGEREF
\_TOC108576492 \\H 16

\

**Table of Tables**

[ ]{.Apple-converted-space}TOC \\t \"Header,1\" \\c \"Table\" TABLE 1 --
POTENTIAL *CLARUS* ENVIRONMENTAL DATA ELEMENTS[ ]{.Apple-tab-span}
PAGEREF \_TOC108576465 \\H 8

TABLE 2 - EXPLANATION OF THE REQUIREMENTS TABLES[ ]{.Apple-tab-span}
PAGEREF \_TOC108576466 \\H 18

TABLE 3 -- HIGH-LEVEL REQUIREMENT ID FORMAT[ ]{.Apple-tab-span} PAGEREF
\_TOC108576467 \\H 18

\

\

\

**Revision History**

  -------------- ------------------------------------------- ------------ ------------------------------------------ -----------------------------------------
  **Revision**   **Issue Date**[ ]{.Apple-converted-space}   **Status**   **Authority**[ ]{.Apple-converted-space}   **Comments**[ ]{.Apple-converted-space}
  00.05          June 2005                                   Draft        PMP                                        For Task Force review
  01.00          July 2005                                   Final        PMP                                        Incorporating Task Force comments
  -------------- ------------------------------------------- ------------ ------------------------------------------ -----------------------------------------

**Electronic File**

[    ]{.Apple-converted-space}Saved As:[ ]{.Apple-converted-space}
**FILENAME [  ]{.Apple-converted-space}\\\* MERGEFORMAT
04037-rq201hrs0100_Clarus_HRS_Final.doc**

[]{.s3}**INTRODUCTION**

***Purpose***

The purpose of this requirements specification is to provide a
repository for the high level requirements governing the design of the
*Clarus* system. These requirements capture the expression of general
needs in the *Clarus* Concept of Operations and in meetings with
potential users and participants. These requirements will be further
refined and expanded as the project progresses and will form the basis
for the design verification and validation of the system. The intended
audience for this document includes decision makers, stakeholders,
designers, and testers.

This document may be updated periodically to reflect changes in the
system requirements, including changes reflected in subsequent versions
of the system.

***Scope[ ]{.Apple-converted-space}***

*Clarus* is an initiative sponsored by the Federal Highway
Administration (FHWA) to organize and make more effective environmental
and road condition observation capabilities in support of four primary
motivations.

Provide a North American resource to collect, quality control, and make
available surface transportation weather and road condition observations
so that State Departments of Transportation (DOTs) can be more
productive in maintaining safety and mobility on all roads.

Surface transportation-based weather observations will enhance and
extend the existing weather data sources that support general purpose
weather forecasting for the protection of life and property.

Collection of real-time surface transportation-based weather
observations will support real-time operational responses to weather.

Surface transportation-based weather observations integrated with
existing observation data will permit broader support for the
enhancement and creation of models that make better predictions in the
atmospheric boundary layer and near the Earth's surface to support more
accurate forecasts.

The intent of the *Clarus* Initiative is to demonstrate how an open and
integrated approach to observational data management can be used to
collect, control the quality of, and consolidate surface transportation
environmental data. The *Clarus* Initiative will address the necessary
infrastructure to consolidate the data from a multitude of independent
data collection systems. This process offers the prospect of enhancing
data coverage, improving the performance of meteorological support
services, and providing guidance to owners of these data sources
regarding the quality of their data and performance of their data
collection systems.

*Clarus* represents the next step in bringing together surface
transportation best practices and the greater weather community. Surface
transportation environmental data collected by the *Clarus* system will
include atmospheric data, pavement data, and hydrologic (water level)
data.

The *Clarus* Initiative consists of two development
components.[ ]{.Apple-converted-space}

The first component is the development of the *Clarus* system -- a
network for sharing, quality controlling, and exchanging surface
environmental data and relevant surface transportation
conditions.[ ]{.Apple-converted-space}

The second component is the development of tools (such as decision
support systems) that make effective use of the *Clarus*
system.[ ]{.Apple-converted-space}

The addition of *Clarus* system data to national weather observations
will further enhance general purpose weather forecasting, providing a
wider range of benefits to the protection of life and property.

Data from the *Clarus* system will have a wide variety of direct and
indirect uses. Users having the most immediate contact with the *Clarus*
system will include the owners and operators of the observing systems
that are providing information to the *Clarus* system, as well as the
users directly accessing the data contained within the *Clarus* system.
The following is an initial list --- which will likely grow as the
initiative progresses --- of these stakeholders:

Observation system owners including federal, state, local, and private
institutions;

Instrument and observation platform suppliers;

Direct data users including system owners and their contractors;

Surface transportation weather service providers (which may include the
observation system owners);

The National Oceanic and Atmospheric Administration (NOAA);

General weather service providers;

Research community; and

Climate data warehouse and other non-surface weather interests.

The deployed *Clarus* system is envisioned to include:

A one-stop Internet portal for all surface transportation environmental
observations;

Data provided without post-processing, ready to be incorporated into
value-added products including weather and traffic models as well as
decision support systems;

Continuous quality control of data with feedback to operators of the
originating sensor stations;

Data transferred in one common protocol with full metadata;

Management of user's rights to input or extract specific data
components;

Data retrieval tools; and

Support for the inclusion of new technologies such as vehicle-based
sensors, surface visibility information from traffic cameras, and remote
sensing technologies.

***Definitions, Acronyms, and
Abbreviations[ ]{.Apple-converted-space}***

This document may contain terms, acronyms, and abbreviations that are
unfamiliar to the reader. A dictionary of these terms, acronyms, and
abbreviations can be found in Appendix A.

***References[ ]{.Apple-converted-space}***

The following documents contain additional information pertaining to
this project or have been referenced within this document:

*Clarus -- The Nationwide Surface Transportation Weather Observing and
Forecast System*; Pisano, Pol, Stern, and Goodwin; TRB 2005.

*National ITS Architecture, Version 5.0*; FHWA, U.S. DOT; October 2003.

*Weather Information in the National ITS Architecture Version* 5.0;
Meridian Environmental Technology, Inc.; August 2004.

*Clarus Initiative Coordinating Committee (ICC) Management Plan*
(Revision 1); James Pol, U.S. DOT; September 2004.

*Surface Transportation Decision Support Requirements,* *Version 1.0*;
Mitretek Systems, Inc.; January 2000.

*Weather Information for Surface Transportation: National Needs
Assessment Report*; Office of the Federal Coordinator for Meteorology;
FCM-R18-2002; December 2002.

*Weather and Environmental Content on 511 Services*; 511 Deployment
Coalition; June 2003.

*NTCIP 1204:1998 NTCIP Object Definitions for Environmental Sensor
Stations*; National Electrical Manufacturers' Association, American
Association of State Highway and Transportation Officials, and Institute
of Transportation Engineers; 1998.

*Where the Weather Meets the Road: A Research Agenda for Improving Road
Weather*; The National Academies; BASC-U-02-06-A; 2004.

*Road Weather Information Systems (RWIS) Data Integration Guidelines*;
Castle Rock Consultants; October 2002.

*Draft Report: Joint TMC/TOC System Integration Study for Emergency
Transportation Operations and Weather: Baseline Conditions*; Battelle;
2004 (in review).

*Clarus Final Draft Concept of Operations;* Iteris and Meridian
Environmental Technology, Inc.; May 16, 2005.

*IEEE Recommended Practice for Software Requirements Specifications*;
Software Engineering Standards Committee of the IEEE Computer Society;
IEEE Std 830-1998, 25 June 1998.

*Security of Federal Automated Information Resources*; Appendix III to
OMB Circular No. A‑130; Office of Management and Budget; February 8,
1996.

Some portions of the *Clarus* Concept of Operations (Ref. 12) have been
incorporated in this document, both for continuity of concept, and to
help identify the basis for the high level requirements. Specific
attributions of this content are only included where they enhance the
context of the requirements.

***Overview[ ]{.Apple-converted-space}***

The organization and content of this document is generally based on the
IEEE standards for System Requirements Specifications (Ref. 13). The
requirements presented in this document represent the high level
objectives, constraints, and desires for the *Clarus* system.

Each requirement is identified by a unique *Clarus*-specific identifier
to allow the requirement to be referenced in future documents, providing
traceability throughout the development
process.[ ]{.Apple-converted-space}

A requirements document states what must be accomplished to fulfill the
vision described in a concept of operations. It does not state how it is
to be accomplished. This document describes each requirement and the
basis for inclusion of that requirement.[ ]{.Apple-converted-space}

The remaining sections of the document contain the requirements for the
system. The sections and their content are as
follows:[ ]{.Apple-converted-space}

**Section 2 -- General Description** provides a general overview of the
entire system. This section describes the general factors that affect
the system and its requirements.

**Section 3 -- Specific Requirements** contains the requirements
developed from reference documentation and stakeholder communications.
This section organizes the requirements into categories that facilitate
the system development process. The categories in this document are:
Functional Requirements, Performance Requirements, and Organizational
Requirements.

**GENERAL DESCRIPTION**

This section provides an overview of the entire system and describes the
general factors that affect the system and its requirements. This
section does not state specific requirements, but instead is intended to
make the requirements easier to understand by giving them context. That
context and the overall intent of the *Clarus* program are described in
detail in the *Clarus* Concept of Operations (Ref. 12), from which much
of the description in this section was derived. Descriptions of specific
terms and acronyms used in this section may be found in Appendix A.

***System Perspective[ ]{.Apple-converted-space}***

The *Clarus* Initiative is essentially a plan to create a "network of
networks" --- much like the Internet --- for surface transportation
environmental data. While the Internet is an interconnection of computer
networks, *Clarus* will be an interconnection of environmental (weather,
pavement, and water level condition) data collection networks. Each of
the weather networks will function autonomously; they will collect
information and disseminate it internally without direction or
dependence on *Clarus*.

Each participating weather network's connection to *Clarus* will add two
new possible modes of functionality. First, the participant will be able
to *share collected environmental data* with *Clarus*. Second,
participants will be able to *receive environmental data* collected by
*Clarus*. The primary recipients of this data will be weather service
providers, but any *Clarus* participants would be able to receive data
if they so chose. This concept of autonomous data sharing is comparable
to the World Wide Web layer of the Internet, where organizations can
publish information on web pages, or browse and download information
published by other organizations on the web. Ownership of the data is
retained by the organization that provided the data to *Clarus*, and the
provider organization can restrict the dissemination of the data through
data sharing agreements with the *Clarus* program.

The *Clarus* system will add a third mode of functionality, which might
be called "meta-librarian." The *Clarus* system will collect, organize,
and qualify the environmental data to be published by the system. The
data will be collected from the participants, organized by location and
type of data, and quality flags will be added. When this is done, the
data will be published to the Service Providers and other
participant/consumers in *Clarus*.[  ]{.Apple-converted-space}REF
\_Ref104179486 \\h Figure 1 shows the general process as data progresses
from collection through publication to service providers.

\

**Figure[  ]{.Apple-converted-space}SEQ Figure \\\* ARABIC 1 --**
***Clarus*** **Data Acquisition, Processing, and Publication**

The principal interfaces that will be critical to *Clarus* are the
interface between *Clarus* and the participating collectors, and the
interface between *Clarus* and the participating service providers.
While the service provider interface is completely within the control of
the *Clarus* Initiative, the interface(s) to the collectors may be
influenced by what interfaces these systems can support.

While the participants want to access the network through "a one-stop
internet portal for all surface transportation weather and pavement
related observations" (Ref. 12), there is no requirement that the system
be a single centralized system. Designers are free to explore
centralized and de-centralized architectures so long as the interfaces
with participants give the appearance of a "one-stop" portal.

The issues of data retention and archive are also not explicitly
addressed. While some data retention is likely to be necessary to
support the quality control function and the publication function, there
is a clear recognition that as the data age, they lose value to all but
climatological investigators and other researchers. This phase of
development does not include directly archiving the large volume of
environmental data in *Clarus*. Considering the technical scope of such
an effort, archiving may be externalized or be deferred until the
*Clarus* network is operational and proven.

***System Functions[ ]{.Apple-converted-space}***

The *Clarus* system will collect data from contributing members,
organize and qualify the data, and then publish the data for use by
service providers and other members of the network. These basic
processes are shown in[  ]{.Apple-converted-space}REF \_Ref103679167 \\h
Figure 2 in terms of *Clarus* system objects and their interactions. The
ellipses represent specific types of data, user roles, or equipment, and
the arrows represent the interactions between them. For example, a
"Collector" administers a "Sensor", collects "Observation Data",
provides "Sensor Metadata", and receives "Quality Feedback".

\

\

**Figure[  ]{.Apple-converted-space}SEQ Figure \\\* ARABIC 2 -- Basic**
***Clarus*** **System Objects and Functions**

The volume of data involved in this process has the potential to become
very large, which leads to a significant challenge in developing a
system that can effectively gather, organize, and disseminate the data.
The *Clarus* system should be a data collection system capable of
handling a vast range of data in a flexible manner that permits new data
types to be added.[ ]{.Apple-converted-space}

Determining data types will be a significant challenge. Proper
understanding of the available data versus the required information will
dictate how the data gathering processes and the database itself should
be designed for greatest efficiency.

While there are many types of environmental data that could be
collected, the *Clarus* emphasis on surface weather and transportation
puts the focus on those weather elements that have a direct bearing on
surface transportation systems. These environmental data elements are
described in the NTCIP standard for Environmental Sensor Station (ESS)
interfaces (Ref. 8) and summarized in[  ]{.Apple-converted-space}REF
\_Ref103676029 \\h Table 1.

**Table[  ]{.Apple-converted-space}SEQ Table \\\* ARABIC 1 --
Potential** ***Clarus*** **Environmental Data Elements**

  ------------------------- -------------------------------------------------
  **Feature**               **Data Type**
  Fixed ESS Data            Station Category
                            Type of Station
                            Location of ESS
                            Location of Sensors
                            Sensor Configuration[ ]{.Apple-converted-space}
                            Pavement Treatment Information
                            Time of Observations
  Mobile ESS Data           Location of ESS
                            Sensor Configuration[ ]{.Apple-converted-space}
                            Speed of Platform
                            Direction of Platform
                            Pavement Treatment Information
                            Time of Observations
  Atmospheric Sensor Data   Sensor Data
                            Air Temperature
                            Atmospheric Pressure
                            Humidity
                            Long and Short Wave Radiation
                            Precipitation Occurrence, Type, Rate, Amount
                            Visibility
                            Wind Speed and Direction
                            Wind Gust
  Pavement Sensor Data      Sensor Data
                            Pavement Condition
                            Pavement Temperature
                            Pavement Chemical Solution Freeze Point
                            Pavement Ice Thickness
                            Snow Depth
                            Water Depth, Road & Stream
  Subsurface Sensor Data    Sensor Data
                            Subsurface Temperature
                            Subsurface Moisture
  Air Quality Sensor Data   Sensor Data
                            Air Quality Condition
  Bio-Hazards               Bio-Hazards
  Camera Imagery            Camera Imagery
  ------------------------- -------------------------------------------------

\

There are basic temporal limits for the data collection, quality
control, processing, and publication of the environmental data. There is
also a period for which the Service Provider Customers have
temporal-driven requirements. The design of *Clarus* will need to
consider these time horizons when planning the technical limitations of
the system architecture. These data time horizons are illustrated in[ 
]{.Apple-converted-space}REF \_Ref103672360 \\h Figure 3.

\

**Figure[  ]{.Apple-converted-space}SEQ Figure \\\* ARABIC 3 -- Time
Horizons for Weather Data**

The average elapsed time for the Autonomous Layer varies as a result of
configuration and communications latencies that are inherent within the
operation of the system to collect the data. The *Clarus* component
includes the time required to communicate data from the Autonomous Layer
to the *Clarus* system import process as well as the time required to
process the input data into storage structures. Further, the variation
in the Service Provider component includes the time required to add
other data to the *Clarus* data and to perform the required human- and
machine-based product generation. The average data age grows as a result
of the aggregated times required to move through the various layers and
eventually to the Service Provider Customers. The *Clarus* system design
must address how best to minimize these times to optimize the flow of
data in a timely manner.

For the purposes of defining the boundaries of these time horizons, the
following definitions apply:

**Average Elapsed Time** is the estimated time for the process within a
given layer or layer sub-division to take place. The age of observed and
recorded values can vary widely within these bands.

**Average Data Age** is the estimated average age of an ESS observation
as it is transferred from the ESS to the end user.

***User Characteristics[ ]{.Apple-converted-space}***

Direct and indirect use of the *Clarus* system can be applied to a wide
audience. Because a variety of users can derive benefit from the
*Clarus* system, it is necessary to focus upon those users who have the
most immediate contact with the system components.

The primary user classes include the owners and operators of the
observing systems collecting and sending information to *Clarus*, and
the users directly accessing the data published by the *Clarus*
system.[ ]{.Apple-converted-space}

The following is an initial list of stakeholders whose user needs are
considered:

Observation system owners including federal, state, local, and private
institutions;

Instrument and observation platform suppliers;

Direct data users including system owners and their contractors;

Surface transportation weather service providers (which may include the
observation system owners);

NOAA;

General weather service providers;

Research community; and

Climate data warehouse and other non-surface weather interests.

This list of direct users of data from the *Clarus* system is a subset
of the entire population of stakeholders interested in the *Clarus*
Initiative. The requirements of the broader stakeholder community are
essential to the *Clarus* Initiative and these interests must serve as a
framework for the core *Clarus* system. From information in the *Surface
Transportation Weather Decision Support Requirements* (STWDSR) (Ref. 5),
*Weather Information for Surface Transportation* (WIST) (Ref. 6), and
511 Deployment Coalition (Ref. 7) documents, it is possible to separate
stakeholder groups into a condensed list based upon the user's interface
or interaction with *Clarus* data.[ ]{.Apple-converted-space}

The users are viewed as defining layers in the process of transferring
data from raw field observations to various levels of data use. This is
illustrated in[  ]{.Apple-converted-space}REF \_Ref103672490 \\h Figure
4.

\

\

\

**Figure[  ]{.Apple-converted-space}SEQ Figure \\\* ARABIC 4 --**
***Clarus*** **User Layers and Time Horizon Relationships**

The **Autonomous Layer** is comprised of operational entities who
utilize weather and transportation data to make plans, decisions, and/or
take action based upon sensor data within their control. These data
include observations collected by ESS, mobile data acquisition
platforms, cameras, and other transportation-related measurement
devices. The Autonomous Layer data comprises the vast majority of the
raw input data to the *Clarus* system.

The ***Clarus*** **Layer** lies between the Autonomous and Service
Providers Layers and represents the nationwide system and architecture
to accomplish the previously outlined goals of surface transportation
environmental data collection and management.[ ]{.Apple-converted-space}

The **Service Providers Layer** is composed of both public and private
entities that provide basic and value-added weather support services to
support the weather information needs of the broader surface
transportation community. These support services rely on *Clarus* data
(raw and processed) combined with other environmental, road condition,
or traffic information products to develop or provide road weather
information and enhanced products.[ ]{.Apple-converted-space}

The **Service Provider Customer Layer** includes those groups who are
direct consumers of products generated by Service Providers and are
generally not a direct user of *Clarus* data. The members of this group
could be anyone using weather information, but are largely found within
the surface transportation community. The weather products received by
these end users are built from a combination of *Clarus* and
non-*Clarus* data. In some instances, the Service Provider Customer
Layer includes entities and agencies also found within the Autonomous
Layer who receive quality control information on the data they
originally provided to *Clarus*.

[ ]{.Apple-converted-space}REF \_Ref103672490 \\h Figure 4 can also be
viewed as a depiction of the time horizons that separate the stakeholder
groups. There is an inherent time scale, similar to[ 
]{.Apple-converted-space}REF \_Ref103672360 \\h Figure 3, emanating from
the center of the diagram outward, representing the flow and processing
of data through the *Clarus* system and between the
layers.[ ]{.Apple-converted-space}

The context diagram in[  ]{.Apple-converted-space}REF \_Ref103673321 \\h
Figure 5 illustrates the relationship of the entities interfacing with
*Clarus*. The diagram also describes the flow of data between the
entities and the *Clarus* system. The data provider organizations
maintain data collection systems. These organizations make up the
Autonomous Layer --- the primary contributors of surface transportation
data to the *Clarus* system. These stakeholders can benefit from
*Clarus* by receiving quality-controlled data from the *Clarus* system.
This quality-controlled data are not value-added data, but data with
flags indicating that elements do not meet quality control
thresholds.[ ]{.Apple-converted-space}

INCLUDEPICTURE
\"../../../../../../../../../../../../../../New%20Folder/Moe/FHWA%20Clarus/UserNeedsContextDiagram-mod-12-6-04.gif\"
\\\* MERGEFORMATINET[ ]{.Apple-converted-space}

**Figure[  ]{.Apple-converted-space}SEQ Figure \\\* ARABIC 5 -- Context
Diagram of** ***Clarus*** **User Needs**

The private and public sector Service Providers are the principal
*Clarus* users. These Service Providers generate value-added road and
rail weather information services for the transportation community.
Additional Service Providers having direct access to *Clarus* data
resources include research organizations, external agencies that may
choose to archive *Clarus* data, and other related weather service
providers.[ ]{.Apple-converted-space}

Within the context of[  ]{.Apple-converted-space}REF \_Ref103673321 \\h
Figure 5, the following roles can be assigned to each group of users:

**Federal, State, and Local Agencies --** These are the transportation
system and road weather information system (RWIS) operators and owners
who directly provide the *Clarus* data. This group places considerable
emphasis on the pavement-specific component of the data at the
observational level to make immediate decisions. These users, primarily
maintenance and operations personnel, are the principal consumers of
information provided by surface transportation weather service
providers. Additional data from this group may include closed circuit
television (CCTV) images, road condition information, and records of
treatment activities such as plowing and chemical application.

**Transit --** These are the owners and operators of transit systems who
contribute raw data to the *Clarus* system and may receive
quality-controlled data from it. This group places considerable emphasis
on understanding weather conditions along designated routes.

**Rail --** These are the owners and operators of rail systems who
contribute raw data to the *Clarus* system and may receive
quality-controlled data from it. This group places considerable emphasis
on understanding weather conditions along designated routes plus
weather-induced specifics such as rail temperatures, frozen switches,
and drifting snow.

**Vehicle --** Emerging technologies are developing that will encourage
a greater level of data collection from vehicles for the purpose of
understanding the nature of the transportation system state including
the impacts of weather. As this method of data collection matures, the
information obtained on weather and pavement conditions from
instrumentation on-board vehicles will be important *Clarus* data.

**Surface Transportation Weather Service Providers (STWSP) --** These
surface transportation weather service providers are the private and
public weather service providers who assimilate the *Clarus* data with
other available data to generate value-added products and services used
by the surface transportation decision-makers at state and local
transportation agencies.

**Weather Service Providers --** These include the weather support
services that are primarily interested in the meteorological and
hydrologic components of the *Clarus* data. This group includes the
efforts in public forecasting by NOAA and the National Weather Service
(NWS) along with private sector weather services and their value-added
support to markets such as agriculture, power utilities, and
construction.

**Research --** This category incorporates federal, academic, and
private sector researchers who are working to improve the state of
knowledge and practice through the research of surface transportation
weather.

**Archives --** This category includes operational and non-operational
interests who choose to include the *Clarus* data in their endeavors.
The archiving of *Clarus* data will be most effective when combined with
other meteorological archives beyond the scope of *Clarus*, but is not
restricted to such efforts.

***General Constraints***

Timeliness of information and reliability of the system are major
constraints on the design. Both of these factors can be addressed
through appropriate system architecture and
implementation.[ ]{.Apple-converted-space}

To address the timeliness factor, the system should be designed such
that it can both retrieve and disseminate large volumes of data from a
variety of sources and at potentially high rates. An architecture that
spreads its data collection and dissemination processes across multiple
servers and communication channels may address this issue. The inherent
scalability of such a design may also enable the system to expand and
add new data sources and end-users.

Reliability can be achieved through a variety of design and deployment
considerations. Hardware, operating system, and development environment
have significant impacts on the inherent reliability of the system. To
maximize system uptime, redundancies may be required at both the
hardware and software levels of the system. The primary challenge here
will be the trade-off between the desire for reliability and the cost of
redundancies.

While the availability of the system is covered in the Concept of
Operations, the criticality of the system is not explicitly addressed.
Since *Clarus* is not replacing any existing application, the system is
not currently critical to any operation or transportation function;
neither is it intended to support any "critical national security
missions".

The system shall be "open," using an architecture and communications
interfaces that are non-proprietary and broadly supported within the
information technology industry. The system should be standards based,
where national standards are applicable. Special consideration should be
given to the national intelligent transportation system (ITS) standards.

***Assumptions and Dependencies[ ]{.Apple-converted-space}***

The usefulness of the *Clarus* system is dependent on participation by
multiple environmental data providers and multiple environmental data
consumers. While the system could be placed in operation with data from
only a single contributing network, there is no added value without the
participation of other weather data sources. Likewise, participation by
a small number of data consumers would not justify the cost of operating
the system.

Several assumptions have been made about how long it will take
environmental data contributors to collect, process, and publish their
data. Data not collected in a timely manner may be of limited use to the
data consumers. Assumptions have also been made about the accuracy of
the data, and the ability of the contributing systems to provide
adequate location, time/date, and data qualification tags. Accepting
data from contributors who cannot provide these tags with the data could
seriously complicate the design of the data acquisition interfaces.

Even though the system will check the data and apply quality flags,
consumers of *Clarus*-provided data will need to understand that neither
FHWA nor the contributing data providers will accept responsibility for
the accuracy of any of the data. The particular limitations and
conditions will be defined in data sharing agreements to be established
with data providers, and disclaimer information will be made available
to data consumers by whatever means the data are published.

Several requirements deal with "regional" needs, without specifying
regional boundaries. It is unlikely that the regional boundaries from
contributing systems will correspond with the regional boundaries
defined within data consumer systems. It is even likely that
participating data contributors will have different (though possibly
overlapping) coverage areas for their networks. Data consumers will need
to understand that data will be presented by geographic coordinates, not
by regional boundaries. Consumers will also need to understand that
coverage will not be uniform and will depend on sensor placement by the
contributing organizations.

The availability, format, and precision of geo-reference coordinates for
data collection points could present unusual problems for the data
acquisition system. Data in the system database and in published data
sets will likely include geo-reference coordinates in decimal longitude,
latitude, and elevation.

The availability, format, and precision of time/date stamps could also
present unusual problems for the data acquisition system, particularly
if contributing systems cannot manage Daylight Savings Time (DST), span
time zones, or span areas that do and do not participate in DST.
*Clarus* timestamps for data in the database and in published data sets
need to be referenced to a standard time reference such as Coordinated
Universal Time (UTC).

The base assumption regarding "database tools" is that the selected data
storage software will include appropriate programming interfaces, query
tools, and configuration and management tools. No special database tools
will be developed as a part of the *Clarus* project.

**SPECIFIC REQUIREMENTS**

This section presents the high-level requirements for the *Clarus*
system and the associated institutional program necessary to achieve the
needs and goals described by the Concept of Operations. These
requirements describe the expected attributes and capabilities of the
system as a whole and do not attempt to allocate capabilities to
specific modules or subsystems within *Clarus*. This approach limits the
high-level requirements in this document to those that can be derived
from a context diagram ( REF \_Ref108314816 \\h[ 
]{.Apple-converted-space}\\\* MERGEFORMAT Figure 6) that pictures the
*Clarus* system as a single functional block with its interfaces. The
types of requirements described in this section correspond roughly to
these functions and interfaces. Functional requirements describe what
happens inside the *Clarus* system itself: quality control, development,
and packaging of environmental data. Each interface to the *Clarus*
system has its own requirements: on collection of data from providers as
input; on the dissemination of data for output; on the controlling rules
and constraints under which the system operates; and on the means
(primarily data management) by which it works.

\

**Figure[  ]{.Apple-converted-space}SEQ Figure \\\* ARABIC 6 --
High-Level Requirements Context**

The high-level perspective assumed for these requirements has
implications for downstream development activities. The high-level
requirements provide a basis for components in system elaboration, and
detailed requirements are subsequently tied to specific components.
Conformance to high-level requirements is shown through testing based on
plans derived from the detailed requirements. The entire development
process is tied together by lines of traceability anchored in the
high-level requirements.

In this section, the requirements are divided into the following
categories.

Functional Requirements -- Lists the characteristics that the system
must support for each interface. Identifies what is to be done by the
system, what inputs should be transformed to what outputs, and what
specific operations are required. The functional requirements further
include:

Functional Data Requirements, which describe requirements specific to
the definition and management of data used and provided by the system;
and

Functional Interface Requirements, which describe the functional
interfaces to the *Clarus* system from information providers and
consumers.

Performance Requirements -- Specifies static and dynamic capacity for
the number of users, connections, and other performance related factors.
Performance requirements further include:

Design Constraints, which identify constraints imposed by standards,
regulations, software or hardware limitations; and

Quality Requirements, which provide requirements which address the
general quality, usability, extensibility, flexibility, and
maintainability of the system.

Organizational Requirements -- Includes requirements for policies and
procedures to support the implementation, operations, training, and
institutional requirements to support the system. This category
also:[ ]{.Apple-converted-space}

Details logical characteristics between the system and external data
sources;

Specifies level of integration with external systems and defines the
interfaces with each user class; and

Specifies any communications interfaces and protocols that should be
supported.

[ ]{.Apple-converted-space}REF \_Ref94517055 \\h Table 2 shows the
general layout of the requirements tables, and explains the purpose or
content of each column of the requirements table. The requirements in
this document are a subset of the requirements information that will be
tracked in the system "Requirements Matrix." While this document is
intended to record the requirements that apply to a particular
implementation of the system, the Requirements Matrix tracks all
proposed requirements for the system. The Matrix includes requirements
that may apply to future versions of the system or which have been
deferred due to cost or complexity.

[ ]{.Apple-converted-space}REF \_Ref94517064 \\h Table 3 provides an
explanation of the requirement identification numbering system.

[]{.s3}**Table[  ]{.Apple-converted-space}SEQ Table \\\* ARABIC 2 -
Explanation of the Requirements Tables**

+-------------+-------------+-------------+-------------+-------------+
| **ID**      | **Require   | **Source**  | **Comment** | **Cr        |
|             | ment[ ]{.Ap |             |             | iticality** |
|             | ple-convert |             |             |             |
|             | ed-space}** |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| A unique    | The text of | Source(s)   | Supporting  | H =         |
| identifier  | the actual  | for the     | text that   | High[ ]{.   |
| used to     | r           | r           | may help    | Apple-conve |
| trace       | equirement. | equirement; | explain the | rted-space} |
| r           | R           | could be a  | r           |             |
| equirements | equirements | reference   | equirement, | M = Medium  |
| from        | formulated  | document or | its         |             |
| beginning   | with "...   | a "parent"  | priority,   | L =         |
| to end in a | shall..."   | r           | or the      | Low[ ]{.    |
| system      | are direct  | equirement. | risks       | Apple-conve |
| development | re          |             | associated  | rted-space} |
| process.    | quirements; |             | with        |             |
|             | those using |             | i           |             |
|             | "... shall  |             | mplementing |             |
|             | be able     |             | the         |             |
|             | to..." are  |             | r           |             |
|             | conditioned |             | equirement. |             |
|             | on other    |             |             |             |
|             | r           |             |             |             |
|             | equirements |             |             |             |
|             | being       |             |             |             |
|             | fulfilled   |             |             |             |
|             | or on       |             |             |             |
|             | factors     |             |             |             |
|             | outside the |             |             |             |
|             | control of  |             |             |             |
|             | the         |             |             |             |
|             | re          |             |             |             |
|             | quirement's |             |             |             |
|             | su          |             |             |             |
|             | bject.[ ]{. |             |             |             |
|             | Apple-conve |             |             |             |
|             | rted-space} |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

\

**Table[  ]{.Apple-converted-space}SEQ Table \\\* ARABIC 3 -- High-Level
Requirement ID Format**

+-----------------------------------+-----------------------------------+
| **High-Level Requirement ID       | **Explanation of                  |
| Format**                          | Fo                                |
|                                   | rmat[ ]{.Apple-converted-space}** |
+-----------------------------------+-----------------------------------+
| A-NNN                             | A[ ]{.Apple-tab-span}Represents   |
|                                   | the classification of the         |
|                                   | requirements within the           |
|                                   | requirements document. The        |
|                                   | following classifications have    |
|                                   | been used in this requirements    |
|                                   | specific                          |
|                                   | ation:[ ]{.Apple-converted-space} |
|                                   |                                   |
|                                   | D[ ]{.Apple-tab-span}Design       |
|                                   | Constraints (Section 3.2.1)       |
|                                   |                                   |
|                                   | F[ ]{.Apple-tab-span}General      |
|                                   | Functional Requirements (Section  |
|                                   | 3.1.1)                            |
|                                   |                                   |
|                                   | H[ ]{.Apple-tab-span}Functional   |
|                                   | Data Requirements (Section 3.1.2) |
|                                   |                                   |
|                                   | I[ ]{.Apple-tab-span}Functional   |
|                                   | Interface Requirements (Section   |
|                                   | 3.1.3)                            |
|                                   |                                   |
|                                   | P[ ]{.Apple-tab-span}System       |
|                                   | Performance Requirements (Section |
|                                   | 3.2.3)                            |
|                                   |                                   |
|                                   | Q[ ]{.Apple-tab-span}Quality      |
|                                   | Requirements (Section 3.2.2)      |
|                                   |                                   |
|                                   | X[                                |
|                                   | ]{.Apple-tab-span}Organizational  |
|                                   | Requirements (Section 3.3)        |
|                                   |                                   |
|                                   | NNN[ ]{.Apple-tab-span}Provides   |
|                                   | unique identification. Numbering  |
|                                   | is not necessarily sequential;    |
|                                   | gaps in the sequence leave room   |
|                                   | to add additional related         |
|                                   | requirements when they are        |
|                                   | discovered.                       |
+-----------------------------------+-----------------------------------+

\

***Functional Requirements[ ]{.Apple-converted-space}***

This section lists the functional characteristics that the system must
support. It also identifies what is to be done by the system, what
inputs should be transformed to what outputs, and what specific
operations are required. The functional requirements are broken into
subsections by general functions, data functions, and interface
functions.

**General Functional Requirements**

The general functional requirements apply to the system as a whole,
without respect to specific functions or processes.

+-------------+-------------+-------------+-------------+-------------+
| **ID**      | **Require   | **Source**  | **Comment** | **Cr        |
|             | ment[ ]{.Ap |             |             | iticality** |
|             | ple-convert |             |             |             |
|             | ed-space}** |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| F-100       | The         | ConOps §1   | "En         | **H**       |
|             | *Clarus*    |             | vironmental |             |
|             | system      |             | data"       |             |
|             | shall       |             | includes    |             |
|             | collect,    |             | all NTCIP   |             |
|             | quality     |             | 1204 data   |             |
|             | control,    |             | (summarized |             |
|             | and         |             | in Table    |             |
|             | disseminate |             | 1).         |             |
|             | en          |             |             |             |
|             | vironmental |             |             |             |
|             | data.       |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| F-201       | The         | OCS         | Access to   | **H**       |
|             | *Clarus*    |             | data may be |             |
|             | system      |             | conditional |             |
|             | shall be    |             | based on    |             |
|             | able to     |             | data        |             |
|             | access      |             | sharing     |             |
|             | in-situ     |             | agreements  |             |
|             | en          |             | to be       |             |
|             | vironmental |             | reached     |             |
|             | o           |             | with        |             |
|             | bservations |             | individual  |             |
|             | from data   |             | data        |             |
|             | collectors. |             | collector   |             |
|             |             |             | org         |             |
|             |             |             | anizations. |             |
+-------------+-------------+-------------+-------------+-------------+
| F-205       | The         | OCS         | \           | **M**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall be    |             |             |             |
|             | able to     |             |             |             |
|             | access      |             |             |             |
|             | remotely    |             |             |             |
|             | sensed      |             |             |             |
|             | en          |             |             |             |
|             | vironmental |             |             |             |
|             | o           |             |             |             |
|             | bservations |             |             |             |
|             | from data   |             |             |             |
|             | collectors. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| F-207       | The         | OCS         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall       |             |             |             |
|             | calculate   |             |             |             |
|             | derived     |             |             |             |
|             | en          |             |             |             |
|             | vironmental |             |             |             |
|             | data from   |             |             |             |
|             | ob          |             |             |             |
|             | servations. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| F-211       | The         | OCS         | \           | **M**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall be    |             |             |             |
|             | able to     |             |             |             |
|             | receive     |             |             |             |
|             | roadway     |             |             |             |
|             | weather     |             |             |             |
|             | m           |             |             |             |
|             | easurements |             |             |             |
|             | derived     |             |             |             |
|             | from VII    |             |             |             |
|             | data.       |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| F-213       | The         | ConOps §1,  | Access      | **L**       |
|             | *Clarus*    | 2.4, 3.1    | could only  |             |
|             | system      |             | be provided |             |
|             | shall allow |             | when new    |             |
|             | access to   |             | data        |             |
|             | new surface |             | sources are |             |
|             | tra         |             | established |             |
|             | nsportation |             | and         |             |
|             | related     |             | available.  |             |
|             | observed    |             |             |             |
|             | en          |             |             |             |
|             | vironmental |             |             |             |
|             | data.       |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| F-214       | The         | MHI         | "Images"    | **H**       |
|             | *Clarus*    |             | would       |             |
|             | system      |             | include     |             |
|             | shall       |             | CCTV and    |             |
|             | accept      |             | still       |             |
|             | en          |             | images.     |             |
|             | vironmental |             |             |             |
|             | data        |             |             |             |
|             | derived     |             |             |             |
|             | from        |             |             |             |
|             | images.     |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| F-216       | [           | Task Force  | "Surface    | **H**       |
|             | ]{.Apple-co | review      | condition   |             |
|             | nverted-spa |             | data" may   |             |
|             | ce}*Clarus* |             | include,    |             |
|             | system      |             | for         |             |
|             | shall       |             | example,    |             |
|             | accept      |             | "dry",      |             |
|             | surface     |             | "wet",      |             |
|             | condition   |             | "icy",      |             |
|             | data        |             | "sno        |             |
|             | derived     |             | w-covered", |             |
|             | from        |             | or          |             |
|             | surface     |             | "flooded".  |             |
|             | images.     |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

F-217The *Clarus* system shall accept atmospheric condition data derived
from atmospheric images.Task Force review

\

**H**

F-215

The *Clarus* system shall accept weather hazard reports containing the
hazard type, location, and timeframe.

ConOps §3.5.6.2

\

**H**

F-218

The *Clarus* system shall acquire and disseminate National Weather
Service (NWS) watches, warnings, and advisories.

Task Force review

\

**M**

F-221

The *Clarus* system shall be able to retrieve environmental data
directly from environmental sensor stations.

Task Force review

The system may have to have its own "collector" component (as shown in
Figures 1 and 2) to implement this requirement.

**L**

F-222

The *Clarus* system shall minimize the time for data acquisition.

OCS

\

**H**

F-223

The *Clarus* system shall process data as they are received.

ConOps §3.4.3

\

**H**

F-231

The *Clarus* system shall collect pavement-related observations.

ConOps §2.5

"Pavement-related" observations could include precipitation
accumulation, flooding or treatments.

**H**

F-241

The *Clarus* system shall accept environmental data from railway systems
or in situ ESS along tracks.

ConOps §2.5.7

\

**H**

F-245

The *Clarus* system shall accept environmental data from railroad
vehicles.

ConOps §2.5.7

\

**H**

F-251

The *Clarus* system shall accept environmental data from (roadway)
vehicles.

Inferred from ConOps §2.5.x

\

**H**

F-255

The *Clarus* system shall accept environmental data from maintenance and
construction vehicles.

ConOps §2.5.2

\

**H**

F-261

The *Clarus* system shall accept environmental data from service patrol
vehicles.

ConOps §2.5.3

\

**H**

F-271

The *Clarus* system shall accept environmental data from transit
vehicles.

ConOps §2.5.5

"Transit vehicles" include watercraft (ferries) and buses.

**H**

F-275

The *Clarus* system shall accept environmental data from emergency
vehicles.

ConOps §2.5.6

\

**H**

F-281

The *Clarus* system shall be able to receive weather data from weather
service providers.

ConOps §3.5.1.4

\

**M**

F-101

The *Clarus* system shall implement continuous quality control
processes.

ConOps §2.4

\

**H**

F-111

The *Clarus* system shall provide environmental data quality flags.

OCS

\

**H**

F-115

The *Clarus* system shall provide notification of data quality
conditions to data collectors.

ConOps §2.4

A "data collector" could be a State DOT maintenance engineer or traffic
manager.

**H**

F-121

The *Clarus* system shall detect out of range values.

ConOps §3.5.1.4

\

**H**

F-125

The *Clarus* system shall not modify original observations.

OCS

\

**H**

F-135

The *Clarus* system shall apply appropriate quality checks based on the
completeness of received sensor station metadata.

OCS

\

**H**

F-141

The *Clarus* system shall allow human intervention to override
automatically applied quality assessment.

OCS

\

**M**

F-151

The *Clarus* system shall record the methods applied when deriving
quality control information.

MHI

\

**H**

F-155

The *Clarus* system shall be able to implement quality control rules for
each environmental parameter.

ConOps §3.5.1.4

\

**H**

F-161The *Clarus* system shall be able to implement quality control
rules for specific environmental situations.ConOps §3.5.1.4The rules for
setting quality flags on environmental data elements may themselves
depend on other environmental data. For example, stormy conditions may
allow more spatial and temporal variability in wind speed observations
than under fair weather conditions.

**H**

F-163

The *Clarus* system shall be able to implement quality control rules
specific to observation locations.

Task Force review

Quality control rules may vary from region to region.

**H**

F-165

The *Clarus* system shall be able to base its quality control process on
values from multiple observations.

ConOps §3.5.1.4

Observations could be distributed in space or time.

**H**

F-171

The *Clarus* system shall be able to base its quality control process on
historical environmental data.

Inferred from ConOps §3.5.1.4

\

**H**

F-175

The *Clarus* system shall be able to use multiple algorithms for its
quality control process.

Inferred from ConOps §4.3

Multiple methods or comparisons may be needed for a given observation.

**M**

F-200

The *Clarus* system shall be able to detect data submission errors.

MHI

 

**H**

F-401

The *Clarus* system shall be able to provide sensor equipment data in
response to a request.

OCS

Subject to data sharing agreements.

**H**

F-501

The *Clarus* system shall minimize the time for data dissemination.

MHI

\

**H**

F-505

The *Clarus* system shall be able to disseminate data based on spatial
queries.

ConOps §3.4.2

Defining this as \"spatial\" allows coverage of custom regions.

**H**

F-521

The *Clarus* system shall maintain a dynamic library of data for at
least seven days.

Task Force review

\

**H**

F-801

The *Clarus* program shall alert users to system modifications.

OCS

\

**H**

F-805

The *Clarus* system shall not require approval to request environmental
data.

MHI

\

**M**

F-806

The *Clarus* system shall enable system administrators to manage
security groups.

MHI

\

**H**

F-811

The *Clarus* system shall be able to restrict environmental data
publication based on source.

MHI & ConOps §4.5

Use MADIS as a template (ConOps §3.6).

**H**

F-901

The *Clarus* system shall record statistics about its operation.

OCS

\

**H**

F-905

The *Clarus* system shall log data transactions.

MHI

\

**H**

\

**Functional Data Requirements**

The data requirements identify and describe the management of
information to be acquired, processed, and disseminated.

+-------------+-------------+-------------+-------------+-------------+
| **ID**      | **Require   | **Source**  | **Comment** | **Cr        |
|             | ment[ ]{.Ap |             |             | iticality** |
|             | ple-convert |             |             |             |
|             | ed-space}** |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| H-011       | The         | ConOps §3.3 | Version     | **H**       |
|             | *Clarus*    | (Table 2)   | 02.20 was   |             |
|             | system      |             | accepted as |             |
|             | baseline    |             | a           |             |
|             | data types  |             | recommended |             |
|             | shall be    |             | standard by |             |
|             | defined by  |             | the NTCIP   |             |
|             | the NTCIP   |             | Joint       |             |
|             | ESS 1204    |             | Committee   |             |
|             | standard    |             | in March    |             |
|             | for data    |             | 2005.  See  |             |
|             | collection. |             | www.ntcip.  |             |
|             |             |             | org/library |             |
|             |             |             | /documents. |             |
+-------------+-------------+-------------+-------------+-------------+
| H-012       | The         | Task Force  | \           | **H**       |
|             | *Clarus*    | review      |             |             |
|             | system data |             |             |             |
|             | definitions |             |             |             |
|             | shall be    |             |             |             |
|             | consistent  |             |             |             |
|             | with the    |             |             |             |
|             | ITE TM 1.03 |             |             |             |
|             | standard,   |             |             |             |
|             | Functional  |             |             |             |
|             | Level       |             |             |             |
|             | Traffic     |             |             |             |
|             | Management  |             |             |             |
|             | Data        |             |             |             |
|             | Dictionary  |             |             |             |
|             | (TMDD).     |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| H-021       | The         | ConOps §2.1 | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall       |             |             |             |
|             | acquire,    |             |             |             |
|             | process,    |             |             |             |
|             | and         |             |             |             |
|             | disseminate |             |             |             |
|             | atmospheric |             |             |             |
|             | data.       |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| H-022       | The         | ConOps §2.1 | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall       |             |             |             |
|             | acquire,    |             |             |             |
|             | process,    |             |             |             |
|             | and         |             |             |             |
|             | disseminate |             |             |             |
|             | surface     |             |             |             |
|             | data.       |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| H-023       | The         | ConOps §2.1 | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall       |             |             |             |
|             | acquire,    |             |             |             |
|             | process,    |             |             |             |
|             | and         |             |             |             |
|             | disseminate |             |             |             |
|             | hydrologic  |             |             |             |
|             | data.       |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| H-121       | The         | ConOps §3.3 | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall       |             |             |             |
|             | acquire,    |             |             |             |
|             | process,    |             |             |             |
|             | and         |             |             |             |
|             | disseminate |             |             |             |
|             | atmospheric |             |             |             |
|             | metadata.   |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| H-122       | The         | ConOps §3.3 | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall       |             |             |             |
|             | acquire,    |             |             |             |
|             | process,    |             |             |             |
|             | and         |             |             |             |
|             | disseminate |             |             |             |
|             | surface     |             |             |             |
|             | metadata.   |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| H-123       | The         | ConOps §3.3 | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall       |             |             |             |
|             | acquire,    |             |             |             |
|             | process,    |             |             |             |
|             | and         |             |             |             |
|             | disseminate |             |             |             |
|             | hydrologic  |             |             |             |
|             | metadata.   |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| H-151       | The         | Implied     | Appendix A  | **H**       |
|             | *Clarus*    | throughout  | includes a  |             |
|             | system      | ConOps      | discussion  |             |
|             | shall       |             | of          |             |
|             | accept only |             | "metadata"  |             |
|             | o           |             | in this     |             |
|             | bservations |             | context.    |             |
|             | that        |             |             |             |
|             | include     |             |             |             |
|             | location,   |             |             |             |
|             | timeframe,  |             |             |             |
|             | and source  |             |             |             |
|             | metadata.   |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| H-155       | The         | OCS         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall       |             |             |             |
|             | accept only |             |             |             |
|             | o           |             |             |             |
|             | bservations |             |             |             |
|             | of known    |             |             |             |
|             | measurement |             |             |             |
|             | types and   |             |             |             |
|             | units.      |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| H-201       | The         | ConOps §3.1 | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall       |             |             |             |
|             | acquire,    |             |             |             |
|             | process,    |             |             |             |
|             | and         |             |             |             |
|             | disseminate |             |             |             |
|             | en          |             |             |             |
|             | vironmental |             |             |             |
|             | sensor      |             |             |             |
|             | station     |             |             |             |
|             | metadata.   |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| H-301       | The         | ConOps      | \           | **H**       |
|             | *Clarus*    | §3.4.2,     |             |             |
|             | system      | amended in  |             |             |
|             | shall be    | Task Force  |             |             |
|             | able to     | review      |             |             |
|             | acquire,    |             |             |             |
|             | process,    |             |             |             |
|             | and         |             |             |             |
|             | disseminate |             |             |             |
|             | en          |             |             |             |
|             | vironmental |             |             |             |
|             | data from   |             |             |             |
|             | across      |             |             |             |
|             | North       |             |             |             |
|             | America.    |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

\

**Functional Interface Requirements**

The functional interface requirements describe the functional interfaces
to the *Clarus* system from information providers and consumers.

+-------------+-------------+-------------+-------------+-------------+
| **ID**      | **Require   | **Source**  | **Comment** | **Cr        |
|             | ment[ ]{.Ap |             |             | iticality** |
|             | ple-convert |             |             |             |
|             | ed-space}** |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| I-011       | The         | OCS         | Standard to | **H**       |
|             | *Clarus*    |             | be          |             |
|             | system      |             | determined  |             |
|             | shall       |             | during      |             |
|             | accept data |             | design      |             |
|             | through a   |             | phase of    |             |
|             | *Clarus*    |             | this        |             |
|             | standard    |             | project.    |             |
|             | interface.  |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| I-012       | The         | ConOps §3.3 | Version     | **L**       |
|             | *Clarus*    |             | 02.20 was   |             |
|             | system      |             | accepted as |             |
|             | shall be    |             | a           |             |
|             | able to     |             | recommended |             |
|             | communicate |             | standard by |             |
|             | with        |             | the NTCIP   |             |
|             | en          |             | Joint       |             |
|             | vironmental |             | Committee   |             |
|             | sensor      |             | in March    |             |
|             | stations    |             | 2005.  See  |             |
|             | using the   |             | www.ntcip.  |             |
|             | NTCIP ESS   |             | org/library |             |
|             | 1204        |             | /documents. |             |
|             | standard    |             |             |             |
|             | for data    |             |             |             |
|             | collection. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| I-013       | The         | ConOps      | \           | **L**       |
|             | *Clarus*    | §3.4.2      |             |             |
|             | system      |             |             |             |
|             | shall be    |             |             |             |
|             | able to     |             |             |             |
|             | communicate |             |             |             |
|             | with RWIS   |             |             |             |
|             | databases   |             |             |             |
|             | through     |             |             |             |
|             | their       |             |             |             |
|             | native      |             |             |             |
|             | interfaces. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| I-014       | The         | ConOps      | The system  | **L**       |
|             | *Clarus*    | §3.4.2      | may have to |             |
|             | system      |             | have its    |             |
|             | shall be    |             | own         |             |
|             | able to     |             | "collector" |             |
|             | communicate |             | component   |             |
|             | with an     |             | (as shown   |             |
|             | individual  |             | in Figures  |             |
|             | ESS through |             | 1 and 2) to |             |
|             | its native  |             | implement   |             |
|             | interface.  |             | this        |             |
|             |             |             | r           |             |
|             |             |             | equirement. |             |
+-------------+-------------+-------------+-------------+-------------+
| I-015       | The         | ConOps      | \           | **M**       |
|             | *Clarus*    | §3.5.1.4    |             |             |
|             | system      |             |             |             |
|             | shall be    |             |             |             |
|             | able to     |             |             |             |
|             | collect     |             |             |             |
|             | en          |             |             |             |
|             | vironmental |             |             |             |
|             | data that   |             |             |             |
|             | are         |             |             |             |
|             | manually    |             |             |             |
|             | entered.    |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| I-016       | The         | Inferred    | \           | **H**       |
|             | *Clarus*    | from ConOps |             |             |
|             | system      | §3.2        |             |             |
|             | shall       |             |             |             |
|             | transfer    |             |             |             |
|             | data as     |             |             |             |
|             | efficiently |             |             |             |
|             | as          |             |             |             |
|             | possible.   |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| I-017       | The         | Inferred    | "Standards" | **H**       |
|             | *Clarus*    | from ConOps | in this     |             |
|             | system      | §4.1        | context     |             |
|             | shall       |             | refer to    |             |
|             | employ      |             | the         |             |
|             | industry    |             | en          |             |
|             | standards   |             | vironmental |             |
|             | to minimize |             | data        |             |
|             | imp         |             | standards   |             |
|             | lementation |             | in common   |             |
|             | impact to   |             | use among   |             |
|             | users and   |             | *Clarus*    |             |
|             | providers.  |             | st          |             |
|             |             |             | akeholders. |             |
|             |             |             | Other       |             |
|             |             |             | *Clarus*    |             |
|             |             |             | design      |             |
|             |             |             | tasks are   |             |
|             |             |             | in          |             |
|             |             |             | vestigating |             |
|             |             |             | what        |             |
|             |             |             | standards   |             |
|             |             |             | are in use; |             |
|             |             |             | detailed    |             |
|             |             |             | r           |             |
|             |             |             | equirements |             |
|             |             |             | will        |             |
|             |             |             | reflect the |             |
|             |             |             | results of  |             |
|             |             |             | that        |             |
|             |             |             | research.   |             |
+-------------+-------------+-------------+-------------+-------------+
| I-021       | The         | ConOps      | \           | **H**       |
|             | *Clarus*    | §3.5.1.4    |             |             |
|             | system      |             |             |             |
|             | shall allow |             |             |             |
|             | service     |             |             |             |
|             | providers   |             |             |             |
|             | to select   |             |             |             |
|             | specific    |             |             |             |
|             | desired     |             |             |             |
|             | data sets.  |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| I-022       | The         | MHI         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall       |             |             |             |
|             | respond to  |             |             |             |
|             | queries for |             |             |             |
|             | en          |             |             |             |
|             | vironmental |             |             |             |
|             | data from   |             |             |             |
|             | the         |             |             |             |
|             | available   |             |             |             |
|             | data.       |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| I-025       | The         | ConOps      | \           | **H**       |
|             | *Clarus*    | §3.5.1.4    |             |             |
|             | system      |             |             |             |
|             | shall       |             |             |             |
|             | enable      |             |             |             |
|             | en          |             |             |             |
|             | vironmental |             |             |             |
|             | data        |             |             |             |
|             | queries by  |             |             |             |
|             | timestamp.  |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| I-026       | The         | ConOps      | \           | **H**       |
|             | *Clarus*    | §3.5.1.4    |             |             |
|             | system      |             |             |             |
|             | shall       |             |             |             |
|             | enable      |             |             |             |
|             | en          |             |             |             |
|             | vironmental |             |             |             |
|             | data        |             |             |             |
|             | queries by  |             |             |             |
|             | location    |             |             |             |
|             | reference.  |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| I-027       | The         | ConOps      | \           | **H**       |
|             | *Clarus*    | §3.5.1.4    |             |             |
|             | system      |             |             |             |
|             | shall       |             |             |             |
|             | enable      |             |             |             |
|             | en          |             |             |             |
|             | vironmental |             |             |             |
|             | data        |             |             |             |
|             | queries by  |             |             |             |
|             | quality.    |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| I-028       | The         | MHI         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall       |             |             |             |
|             | enable      |             |             |             |
|             | en          |             |             |             |
|             | vironmental |             |             |             |
|             | data        |             |             |             |
|             | queries by  |             |             |             |
|             | source.     |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| I-031       | The         | MHI         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall       |             |             |             |
|             | provide a   |             |             |             |
|             | user        |             |             |             |
|             | interface   |             |             |             |
|             | for system  |             |             |             |
|             | admi        |             |             |             |
|             | nistration. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

I-032The *Clarus* system shall manage system user privileges according
to the *Clarus* data sharing agreements.MHIA "user" in this context is
anyone who directly touches the system (for example, a collector
providing data or a service provider retrieving data).

**H**

I-033

The *Clarus* system shall allow users to create a data subscription
request.

ConOps §4.5

\

**H**

\

***Performance Requirements***

The requirements in this section specify static and dynamic capacity for
the number of users, connections, and other performance related factors.
The performance requirements are divided into subsections and are
provided in the form of design constraints, quality requirements, and
system performance requirements.

**Design Constraints**

Design constraints apply existing rules or external conditions to the
system. Examples of design constraints are communication standards,
requirements for standardized hardware or software, and minimum needs
for a system to be useful.

+-------------+-------------+-------------+-------------+-------------+
| **ID**      | **Require   | **Source**  | **Comment** | **Cr        |
|             | ment[ ]{.Ap |             |             | iticality** |
|             | ple-convert |             |             |             |
|             | ed-space}** |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| D-011       | The         | MHI         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall be    |             |             |             |
|             | able to be  |             |             |             |
|             | hosted at   |             |             |             |
|             | one or more |             |             |             |
|             | physical    |             |             |             |
|             | locations.  |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| D-021       | The         | MHI         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall use   |             |             |             |
|             | hardware    |             |             |             |
|             | that        |             |             |             |
|             | implements  |             |             |             |
|             | industry    |             |             |             |
|             | accepted    |             |             |             |
|             | standard    |             |             |             |
|             | interfaces. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| D-031       | The         | MHI         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall use   |             |             |             |
|             | software    |             |             |             |
|             | that        |             |             |             |
|             | implements  |             |             |             |
|             | industry    |             |             |             |
|             | accepted    |             |             |             |
|             | standard    |             |             |             |
|             | interfaces. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| D-041       | The         | ConOps      | \           | **H**       |
|             | *Clarus*    | §3.4.2      |             |             |
|             | system      |             |             |             |
|             | shall be    |             |             |             |
|             | able to     |             |             |             |
|             | operate on  |             |             |             |
|             | redundant   |             |             |             |
|             | hardware.   |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| D-051       | The         | OCS         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall       |             |             |             |
|             | disseminate |             |             |             |
|             | data in     |             |             |             |
|             | response to |             |             |             |
|             | a scheduled |             |             |             |
|             | request.    |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| D-061       | The         | OCS         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall       |             |             |             |
|             | disseminate |             |             |             |
|             | data in     |             |             |             |
|             | response to |             |             |             |
|             | polling.    |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| D-071       | The         | OCS         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall       |             |             |             |
|             | disseminate |             |             |             |
|             | data in     |             |             |             |
|             | response to |             |             |             |
|             | a change    |             |             |             |
|             | n           |             |             |             |
|             | otification |             |             |             |
|             | request.    |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| D-081       | The         | OCS         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall be    |             |             |             |
|             | able to     |             |             |             |
|             | notify      |             |             |             |
|             | subscribers |             |             |             |
|             | when data   |             |             |             |
|             | sets become |             |             |             |
|             | available.  |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| D-091       | The         | OCS         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall       |             |             |             |
|             | disseminate |             |             |             |
|             | data using  |             |             |             |
|             | standard    |             |             |             |
|             | Internet    |             |             |             |
|             | protocols.  |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| D-101       | All HTML    | Contract    | \           | **H**       |
|             | coding      |             |             |             |
|             | shall meet  |             |             |             |
|             | FHWA        |             |             |             |
|             | r           |             |             |             |
|             | equirements |             |             |             |
|             | for web     |             |             |             |
|             | sites.      |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| D-111       | The         | OCS         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall       |             |             |             |
|             | support     |             |             |             |
|             | modular     |             |             |             |
|             | components. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| D-121       | The         | MHI         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall be    |             |             |             |
|             | able to use |             |             |             |
|             | latitude,   |             |             |             |
|             | longitude,  |             |             |             |
|             | and         |             |             |             |
|             | elevation   |             |             |             |
|             | (standard   |             |             |             |
|             | GPS)        |             |             |             |
|             | coordinates |             |             |             |
|             | to specify  |             |             |             |
|             | location to |             |             |             |
|             | the nearest |             |             |             |
|             | fifty feet. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| D-126       | The         | OCS         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall use   |             |             |             |
|             | Coordinated |             |             |             |
|             | Universal   |             |             |             |
|             | Time (UTC)  |             |             |             |
|             | for all     |             |             |             |
|             | timestamps. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| D-131       | The         | MHI         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall have  |             |             |             |
|             | a minimum   |             |             |             |
|             | of one      |             |             |             |
|             | system      |             |             |             |
|             | adm         |             |             |             |
|             | inistrator. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

\

**Quality Requirements**

These quality requirements pertain directly to maintaining a high level
of service quality.

+-------------+-------------+-------------+-------------+-------------+
| **ID**      | **Require   | **Source**  | **Comment** | **Cr        |
|             | ment[ ]{.Ap |             |             | iticality** |
|             | ple-convert |             |             |             |
|             | ed-space}** |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Q-011       | The         | MHI         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall be    |             |             |             |
|             | able to     |             |             |             |
|             | mitigate    |             |             |             |
|             | co          |             |             |             |
|             | mmunication |             |             |             |
|             | denial      |             |             |             |
|             | -of-service |             |             |             |
|             | attacks.    |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Q-012       | The         | MHI         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall be    |             |             |             |
|             | able to     |             |             |             |
|             | au          |             |             |             |
|             | tomatically |             |             |             |
|             | recover     |             |             |             |
|             | from an     |             |             |             |
|             | unexpected  |             |             |             |
|             | shutdown.   |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Q-013       | The         | MHI         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall be    |             |             |             |
|             | able to     |             |             |             |
|             | respond to  |             |             |             |
|             | 95% of all  |             |             |             |
|             | requests    |             |             |             |
|             | for         |             |             |             |
|             | en          |             |             |             |
|             | vironmental |             |             |             |
|             | data 95% of |             |             |             |
|             | the time.   |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

\

**System Performance Requirements**

System performance requirements specify quantitatively what the system
must do and in what timeframe.

+-------------+-------------+-------------+-------------+-------------+
| **ID**      | **Require   | **Source**  | **Comment** | **Cr        |
|             | ment[ ]{.Ap |             |             | iticality** |
|             | ple-convert |             |             |             |
|             | ed-space}** |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| P-011       | The         | MHI         | \           | **M**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall be    |             |             |             |
|             | able to     |             |             |             |
|             | publish     |             |             |             |
|             | en          |             |             |             |
|             | vironmental |             |             |             |
|             | data at     |             |             |             |
|             | three times |             |             |             |
|             | the volume  |             |             |             |
|             | rate that   |             |             |             |
|             | it collects |             |             |             |
|             | it.         |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| P-012       | The         | ConOps §4.5 | User demand | **L**       |
|             | *Clarus*    |             | for some    |             |
|             | system      |             | data may    |             |
|             | shall be    |             | necessitate |             |
|             | able to     |             | that it be  |             |
|             | prioritize  |             | more        |             |
|             | data        |             | readily     |             |
|             | handling    |             | available   |             |
|             | for         |             | than other  |             |
|             | ti          |             | data. If    |             |
|             | me-critical |             | this is the |             |
|             | data.       |             | case, the   |             |
|             |             |             | detailed    |             |
|             |             |             | system      |             |
|             |             |             | r           |             |
|             |             |             | equirements |             |
|             |             |             | will        |             |
|             |             |             | identify    |             |
|             |             |             | the         |             |
|             |             |             | specific    |             |
|             |             |             | data to be  |             |
|             |             |             | provided    |             |
|             |             |             | and the     |             |
|             |             |             | timeliness  |             |
|             |             |             | cri         |             |
|             |             |             | teria.[ ]{. |             |
|             |             |             | Apple-conve |             |
|             |             |             | rted-space} |             |
+-------------+-------------+-------------+-------------+-------------+
| P-013       | The         | MHI         | 4.7 million | **M**       |
|             | *Clarus*    |             | road miles  |             |
|             | system      |             | in North    |             |
|             | shall       |             | America;    |             |
|             | support 470 |             | ap          |             |
|             | million     |             | proximately |             |
|             | current     |             | 100         |             |
|             | ob          |             | en          |             |
|             | servations. |             | vironmental |             |
|             |             |             | parameters  |             |
|             |             |             | for a       |             |
|             |             |             | reporting   |             |
|             |             |             | location    |             |
|             |             |             | (based on   |             |
|             |             |             | NTCIP       |             |
|             |             |             | 1204).      |             |
+-------------+-------------+-------------+-------------+-------------+
| P-021       | The         | ConOps §3.2 | \           | **H**       |
|             | *Clarus*    | (Fig. 6)    |             |             |
|             | system      |             |             |             |
|             | shall be    |             |             |             |
|             | able to     |             |             |             |
|             | collect     |             |             |             |
|             | data from   |             |             |             |
|             | sources     |             |             |             |
|             | within 5    |             |             |             |
|             | minutes of  |             |             |             |
|             | them        |             |             |             |
|             | becoming    |             |             |             |
|             | available.  |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| P-022       | The         | MHI         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall be    |             |             |             |
|             | able to     |             |             |             |
|             | receive all |             |             |             |
|             | reported    |             |             |             |
|             | en          |             |             |             |
|             | vironmental |             |             |             |
|             | data during |             |             |             |
|             | a fifteen   |             |             |             |
|             | minute time |             |             |             |
|             | interval.   |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| P-023       | The         | OCS         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall be    |             |             |             |
|             | able to     |             |             |             |
|             | complete an |             |             |             |
|             | automated   |             |             |             |
|             | quality     |             |             |             |
|             | control     |             |             |             |
|             | check of    |             |             |             |
|             | en          |             |             |             |
|             | vironmental |             |             |             |
|             | data within |             |             |             |
|             | ten seconds |             |             |             |
|             | of data     |             |             |             |
|             | receipt.    |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| P-024       | The         | ConOps §3.2 | \           | **H**       |
|             | *Clarus*    | (Fig. 7)    |             |             |
|             | system      |             |             |             |
|             | shall be    |             |             |             |
|             | able to     |             |             |             |
|             | publish new |             |             |             |
|             | data within |             |             |             |
|             | twenty      |             |             |             |
|             | minutes of  |             |             |             |
|             | data        |             |             |             |
|             | receipt.    |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| P-025       | The         | MHI         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | shall       |             |             |             |
|             | respond to  |             |             |             |
|             | a request   |             |             |             |
|             | for         |             |             |             |
|             | information |             |             |             |
|             | within one  |             |             |             |
|             | minute.     |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| P-031       | The         | MHI         | Estimated   | **H**       |
|             | *Clarus*    |             | that half   |             |
|             | system      |             | of the      |             |
|             | shall be    |             | concurrent  |             |
|             | able to     |             | users may   |             |
|             | handle      |             | be          |             |
|             | three       |             | requesting  |             |
|             | hundred     |             | data at any |             |
|             | s           |             | one time.   |             |
|             | imultaneous |             |             |             |
|             | requests    |             |             |             |
|             | for         |             |             |             |
|             | en          |             |             |             |
|             | vironmental |             |             |             |
|             | element     |             |             |             |
|             | data.       |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| P-041       | The         | MHI         | An estimate | **H**       |
|             | *Clarus*    |             | of the      |             |
|             | system      |             | number of   |             |
|             | shall be    |             | concurrent  |             |
|             | able to     |             | potential   |             |
|             | support six |             | users of    |             |
|             | hundred     |             | the         |             |
|             | concurrent  |             | *Clarus*    |             |
|             | users.      |             | system: one |             |
|             |             |             | tenth of    |             |
|             |             |             | the         |             |
|             |             |             | registered  |             |
|             |             |             | users at    |             |
|             |             |             | any one     |             |
|             |             |             | time.       |             |
+-------------+-------------+-------------+-------------+-------------+
| P-042       | The         | MHI         | An estimate | **H**       |
|             | *Clarus*    |             | of the      |             |
|             | system      |             | number of   |             |
|             | shall be    |             | individual  |             |
|             | able to     |             | users: a    |             |
|             | support six |             | pool of 250 |             |
|             | thousand    |             | weather     |             |
|             | registered  |             | service     |             |
|             | users.      |             | providers,  |             |
|             |             |             | ten per     |             |
|             |             |             | provider;   |             |
|             |             |             | 100         |             |
|             |             |             | g           |             |
|             |             |             | overnmental |             |
|             |             |             | agencies,   |             |
|             |             |             | 25 per      |             |
|             |             |             | agency; and |             |
|             |             |             | 1000 other  |             |
|             |             |             | users.      |             |
+-------------+-------------+-------------+-------------+-------------+

***Organizational Requirements***

Organizational requirements deal with policies regarding external
parties involved with the system, personnel roles, training, and
security needs.[ ]{.Apple-converted-space}

+-------------+-------------+-------------+-------------+-------------+
| **ID**      | **Require   | **Source**  | **Comment** | **Cr        |
|             | ment[ ]{.Ap |             |             | iticality** |
|             | ple-convert |             |             |             |
|             | ed-space}** |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-101       | The         | MHI         | "Approved   | **H**       |
|             | *Clarus*    |             | sources"    |             |
|             | system      |             | are         |             |
|             | shall       |             | anticipated |             |
|             | accept data |             | to be those |             |
|             | only from   |             | with whom a |             |
|             | approved    |             | data        |             |
|             | sources.    |             | sharing     |             |
|             |             |             | agreement   |             |
|             |             |             | has been    |             |
|             |             |             | e           |             |
|             |             |             | stablished. |             |
+-------------+-------------+-------------+-------------+-------------+
| X-201       | The         | Task Force  | \           | **H**       |
|             | *Clarus*    | review      |             |             |
|             | program     |             |             |             |
|             | shall       |             |             |             |
|             | establish   |             |             |             |
|             | data        |             |             |             |
|             | sharing     |             |             |             |
|             | agreements  |             |             |             |
|             | with all    |             |             |             |
|             | pa          |             |             |             |
|             | rticipating |             |             |             |
|             | sources of  |             |             |             |
|             | en          |             |             |             |
|             | vironmental |             |             |             |
|             | data.       |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-205       | The         | OCS         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | program     |             |             |             |
|             | shall       |             |             |             |
|             | maintain    |             |             |             |
|             | continuous  |             |             |             |
|             | 24x7        |             |             |             |
|             | operations. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-207       | The         | MHI         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | program     |             |             |             |
|             | shall       |             |             |             |
|             | provide an  |             |             |             |
|             | environment |             |             |             |
|             | that has    |             |             |             |
|             | unin        |             |             |             |
|             | terruptible |             |             |             |
|             | power for   |             |             |             |
|             | the         |             |             |             |
|             | *Clarus*    |             |             |             |
|             | system.     |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-209       | The         | MHI         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | program     |             |             |             |
|             | shall       |             |             |             |
|             | provide an  |             |             |             |
|             | environment |             |             |             |
|             | that has    |             |             |             |
|             | redundant   |             |             |             |
|             | co          |             |             |             |
|             | mmunication |             |             |             |
|             | for the     |             |             |             |
|             | *Clarus*    |             |             |             |
|             | system.     |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-211       | The         | OCS         | Network     | **H**       |
|             | *Clarus*    |             | management  |             |
|             | program     |             | tools can   |             |
|             | shall       |             | be used to  |             |
|             | provide     |             | determine   |             |
|             | network     |             | latency.    |             |
|             | management  |             |             |             |
|             | tools.      |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-215       | The         | ConOps      | \           | **H**       |
|             | *Clarus*    | §3.3.1      |             |             |
|             | program     | (Fig. 9)    |             |             |
|             | shall       |             |             |             |
|             | provide     |             |             |             |
|             | setup       |             |             |             |
|             | support.    |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-221       | The         | OCS         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | program     |             |             |             |
|             | shall       |             |             |             |
|             | provide for |             |             |             |
|             | customer    |             |             |             |
|             | service.    |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-225       | The         | ConOps      | \           | **H**       |
|             | *Clarus*    | §3.3.1      |             |             |
|             | program     |             |             |             |
|             | shall       |             |             |             |
|             | provide a   |             |             |             |
|             | trained     |             |             |             |
|             | support     |             |             |             |
|             | staff.      |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-231       | The         | OCS         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | program     |             |             |             |
|             | shall       |             |             |             |
|             | define data |             |             |             |
|             | quality     |             |             |             |
|             | assurance   |             |             |             |
|             | methods and |             |             |             |
|             | criteria.   |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-232       | The         | MHI         | Specifies   | **H**       |
|             | *Clarus*    |             | the rules   |             |
|             | program     |             | to be       |             |
|             | shall       |             | implemented |             |
|             | define      |             | according   |             |
|             | quality     |             | to F-155,   |             |
|             | control     |             | F-161,      |             |
|             | rules for   |             | F-165,      |             |
|             | en          |             | F-171, and  |             |
|             | vironmental |             | F-175.      |             |
|             | ob          |             |             |             |
|             | servations. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-233       | The         | MHI         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | program     |             |             |             |
|             | shall       |             |             |             |
|             | define data |             |             |             |
|             | retention   |             |             |             |
|             | standards.  |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-235       | The         | OCS         | That is,    | **H**       |
|             | *Clarus*    |             | the         |             |
|             | program     |             | *Clarus*    |             |
|             | shall       |             | program     |             |
|             | provide     |             | needs to    |             |
|             | do          |             | provide     |             |
|             | cumentation |             | do          |             |
|             | of *Clarus* |             | cumentation |             |
|             | standards.  |             | of whatever |             |
|             |             |             | standards   |             |
|             |             |             | it creates  |             |
|             |             |             | for its own |             |
|             |             |             | d           |             |
|             |             |             | evelopment, |             |
|             |             |             | deployment, |             |
|             |             |             | management, |             |
|             |             |             | and         |             |
|             |             |             | operations. |             |
+-------------+-------------+-------------+-------------+-------------+
| X-237       | The         | Inferred    | \           | **M**       |
|             | *Clarus*    | from ConOps |             |             |
|             | program     | §1          |             |             |
|             | standards   |             |             |             |
|             | shall       |             |             |             |
|             | accommodate |             |             |             |
|             | co          |             |             |             |
|             | ntributions |             |             |             |
|             | of new      |             |             |             |
|             | sensor      |             |             |             |
|             | t           |             |             |             |
|             | echnologies |             |             |             |
|             | to the      |             |             |             |
|             | *Clarus*    |             |             |             |
|             | system.     |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-239       | The         | Inferred    | \           | **M**       |
|             | *Clarus*    | from ConOps |             |             |
|             | program     | §4.3        |             |             |
|             | standards   |             |             |             |
|             | shall       |             |             |             |
|             | support     |             |             |             |
|             | multiple    |             |             |             |
|             | methods of  |             |             |             |
|             | data        |             |             |             |
|             | delivery to |             |             |             |
|             | users.      |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-305       | The         | OCS         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | program     |             |             |             |
|             | shall       |             |             |             |
|             | maintain a  |             |             |             |
|             | co          |             |             |             |
|             | mprehensive |             |             |             |
|             | *Clarus*    |             |             |             |
|             | system test |             |             |             |
|             | e           |             |             |             |
|             | nvironment. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-311       | The         | OCS         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | program     |             |             |             |
|             | shall test  |             |             |             |
|             | all         |             |             |             |
|             | software    |             |             |             |
|             | changes in  |             |             |             |
|             | the         |             |             |             |
|             | designated  |             |             |             |
|             | test        |             |             |             |
|             | environment |             |             |             |
|             | before      |             |             |             |
|             | deployment  |             |             |             |
|             | to          |             |             |             |
|             | production. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-315       | The         | OCS         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | program     |             |             |             |
|             | shall test  |             |             |             |
|             | all         |             |             |             |
|             | hardware    |             |             |             |
|             | changes in  |             |             |             |
|             | the         |             |             |             |
|             | designated  |             |             |             |
|             | test        |             |             |             |
|             | environment |             |             |             |
|             | before      |             |             |             |
|             | deployment  |             |             |             |
|             | to          |             |             |             |
|             | production. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-601       | The         | Contract    | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | program     |             |             |             |
|             | shall       |             |             |             |
|             | operate the |             |             |             |
|             | *Clarus*    |             |             |             |
|             | system      |             |             |             |
|             | according   |             |             |             |
|             | to its      |             |             |             |
|             | published   |             |             |             |
|             | IT Security |             |             |             |
|             | Plan.       |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-605       | The         | Contract    | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | program     |             |             |             |
|             | shall       |             |             |             |
|             | operate     |             |             |             |
|             | according   |             |             |             |
|             | to          |             |             |             |
|             | Government  |             |             |             |
|             | IT security |             |             |             |
|             | r           |             |             |             |
|             | equirements |             |             |             |
|             | as outlined |             |             |             |
|             | in OMB      |             |             |             |
|             | Circular    |             |             |             |
|             | A-130,      |             |             |             |
|             | Management  |             |             |             |
|             | of Federal  |             |             |             |
|             | Information |             |             |             |
|             | Resources,  |             |             |             |
|             | Appendix    |             |             |             |
|             | III,        |             |             |             |
|             | Security of |             |             |             |
|             | Federal     |             |             |             |
|             | Automated   |             |             |             |
|             | Information |             |             |             |
|             | Resources.  |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-611       | The         | Contract    | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | program     |             |             |             |
|             | shall       |             |             |             |
|             | operate     |             |             |             |
|             | according   |             |             |             |
|             | to          |             |             |             |
|             | Government  |             |             |             |
|             | IT security |             |             |             |
|             | r           |             |             |             |
|             | equirements |             |             |             |
|             | as outlined |             |             |             |
|             | in the      |             |             |             |
|             | National    |             |             |             |
|             | Institute   |             |             |             |
|             | of          |             |             |             |
|             | Standards   |             |             |             |
|             | and         |             |             |             |
|             | Technology  |             |             |             |
|             | (NIST)      |             |             |             |
|             | Guidelines, |             |             |             |
|             | D           |             |             |             |
|             | epartmental |             |             |             |
|             | Information |             |             |             |
|             | Resource    |             |             |             |
|             | Management  |             |             |             |
|             | Manual, and |             |             |             |
|             | associated  |             |             |             |
|             | guidelines. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-615       | The         | Contract    | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | program     |             |             |             |
|             | shall       |             |             |             |
|             | operate     |             |             |             |
|             | according   |             |             |             |
|             | to          |             |             |             |
|             | Government  |             |             |             |
|             | IT security |             |             |             |
|             | r           |             |             |             |
|             | equirements |             |             |             |
|             | as outlined |             |             |             |
|             | in DOT      |             |             |             |
|             | Order       |             |             |             |
|             | 1630.2B,    |             |             |             |
|             | Personnel   |             |             |             |
|             | Security    |             |             |             |
|             | Management. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-805       | Weather     | ConOps      | \           | **L**       |
|             | service     | §3.4.2      |             |             |
|             | providers   |             |             |             |
|             | shall be    |             |             |             |
|             | able to use |             |             |             |
|             | *Clarus*    |             |             |             |
|             | data to     |             |             |             |
|             | provide     |             |             |             |
|             | localized   |             |             |             |
|             | special     |             |             |             |
|             | weather     |             |             |             |
|             | products.   |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-811       | Public      | ConOps      | \           | **L**       |
|             | agency      | §2.5.2      |             |             |
|             | maintenance |             |             |             |
|             | and         |             |             |             |
|             | c           |             |             |             |
|             | onstruction |             |             |             |
|             | personnel   |             |             |             |
|             | shall be    |             |             |             |
|             | able to use |             |             |             |
|             | the         |             |             |             |
|             | *Clarus*    |             |             |             |
|             | system to   |             |             |             |
|             | obtain      |             |             |             |
|             | en          |             |             |             |
|             | vironmental |             |             |             |
|             | conditions. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-815       | Rail system | Inferred    | \           | **L**       |
|             | personnel   | from ConOps |             |             |
|             | shall be    | §2.5.7      |             |             |
|             | able to use |             |             |             |
|             | the         |             |             |             |
|             | *Clarus*    |             |             |             |
|             | system to   |             |             |             |
|             | obtain      |             |             |             |
|             | en          |             |             |             |
|             | vironmental |             |             |             |
|             | conditions. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-821       | Traffic     | Inferred    | \           | **L**       |
|             | management  | from ConOps |             |             |
|             | personnel   | §2.5.3      |             |             |
|             | shall be    |             |             |             |
|             | able to use |             |             |             |
|             | the         |             |             |             |
|             | *Clarus*    |             |             |             |
|             | system to   |             |             |             |
|             | obtain      |             |             |             |
|             | en          |             |             |             |
|             | vironmental |             |             |             |
|             | conditions. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-823       | Transit     | Inferred    | \           | **L**       |
|             | personnel   | from ConOps |             |             |
|             | shall be    | §2.5.5      |             |             |
|             | able to use |             |             |             |
|             | the         |             |             |             |
|             | *Clarus*    |             |             |             |
|             | system to   |             |             |             |
|             | obtain      |             |             |             |
|             | en          |             |             |             |
|             | vironmental |             |             |             |
|             | conditions. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-825       | The freight | Inferred    | \           | **L**       |
|             | community   | from ConOps |             |             |
|             | shall be    | §2.5.8      |             |             |
|             | able to use |             |             |             |
|             | the         |             |             |             |
|             | *Clarus*    |             |             |             |
|             | system to   |             |             |             |
|             | obtain      |             |             |             |
|             | en          |             |             |             |
|             | vironmental |             |             |             |
|             | conditions. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-827       | Emergency   | Inferred    | \           | **L**       |
|             | management  | from ConOps |             |             |
|             | and public  | §2.5.6      |             |             |
|             | safety      |             |             |             |
|             | personnel   |             |             |             |
|             | shall be    |             |             |             |
|             | able to use |             |             |             |
|             | the         |             |             |             |
|             | *Clarus*    |             |             |             |
|             | system to   |             |             |             |
|             | obtain      |             |             |             |
|             | en          |             |             |             |
|             | vironmental |             |             |             |
|             | conditions. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-905       | The         | OCS         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | program     |             |             |             |
|             | shall       |             |             |             |
|             | maintain    |             |             |             |
|             | information |             |             |             |
|             | about data  |             |             |             |
|             | providers.  |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-910       | The         | OCS         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | program     |             |             |             |
|             | shall       |             |             |             |
|             | maintain    |             |             |             |
|             | metadata    |             |             |             |
|             | about each  |             |             |             |
|             | data        |             |             |             |
|             | provider\'s |             |             |             |
|             | network.    |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-915       | The         | OCS         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | program     |             |             |             |
|             | shall       |             |             |             |
|             | maintain    |             |             |             |
|             | information |             |             |             |
|             | about data  |             |             |             |
|             | provider    |             |             |             |
|             | red         |             |             |             |
|             | istribution |             |             |             |
|             | re          |             |             |             |
|             | strictions. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-921       | The         | OCS         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | program     |             |             |             |
|             | shall       |             |             |             |
|             | maintain    |             |             |             |
|             | information |             |             |             |
|             | about       |             |             |             |
|             | service     |             |             |             |
|             | providers.  |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-925       | The         | OCS         | \           | **M**       |
|             | *Clarus*    |             |             |             |
|             | program     |             |             |             |
|             | shall       |             |             |             |
|             | maintain    |             |             |             |
|             | information |             |             |             |
|             | about       |             |             |             |
|             | service     |             |             |             |
|             | provider    |             |             |             |
|             | comm        |             |             |             |
|             | unications. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-931       | The         | OCS         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | program     |             |             |             |
|             | shall       |             |             |             |
|             | maintain    |             |             |             |
|             | information |             |             |             |
|             | about       |             |             |             |
|             | service     |             |             |             |
|             | provider    |             |             |             |
|             | access to   |             |             |             |
|             | data.       |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| X-935       | The         | MHI         | \           | **H**       |
|             | *Clarus*    |             |             |             |
|             | program     |             |             |             |
|             | shall allow |             |             |             |
|             | potential   |             |             |             |
|             | weather     |             |             |             |
|             | element     |             |             |             |
|             | data        |             |             |             |
|             | providers   |             |             |             |
|             | to request  |             |             |             |
|             | permission  |             |             |             |
|             | to submit   |             |             |             |
|             | weather     |             |             |             |
|             | i           |             |             |             |
|             | nformation. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

\

**DEFINITIONS, ACRONYMS, AND ABBREVIATIONS**

The following table provides definitions of terms, acronyms, and
abbreviations to assist interpretation of this document.

  -------------------- ------------------------------------------------------------------------------------------------------------------------------------------
  **Term**             **Definition**
  CCTV                 Closed Circuit Television
  ConOps               Concept of Operations
  DOT                  Department of Transportation
  DSS                  Decision Support System
  DST                  Daylight Saving Time
  environmental data   In the *Clarus* context, includes all data defined in NTCIP 1204 (Ref. 8).
  ESS                  Environmental Sensor Station
  FHWA                 Federal Highway Administration
  GPS                  Global Positioning System
  HTML                 Hypertext Markup Language
  ICC                  (*Clarus*) Initiative Coordinating Committee
  IEEE                 Institute of Electrical and Electronic Engineers
  in situ              From Latin, "in situ" means "in place." As applied to meteorological data, it refers to data specific to a (fixed) point of observation.
  IT                   Information Technology
  ITE                  Institute of Transportation Engineers
  ITS                  Intelligent Transportation System
  ITS America          Intelligent Transportation Society of America
  MADIS                Meteorological Assimilation Data Ingest System
  MDSS                 Maintenance Decision Support System
  -------------------- ------------------------------------------------------------------------------------------------------------------------------------------

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  metadataIn common information systems use, "metadata" is "data about data[."]{.s3} Within the meteorological community, this use has been extended to include data about objects related to weather observations. For example, location data for an ESS becomes metadata for the observation data.   
  MHI                                                                                                                                                                                                                                                                                                  Mixon/Hill, Inc.
  NIST                                                                                                                                                                                                                                                                                                 National Institute of Standards and Technology
  NOAA                                                                                                                                                                                                                                                                                                 National Oceanic and Atmospheric Administration
  NTCIP                                                                                                                                                                                                                                                                                                National Transportation Communications for ITS Protocol
  NWS                                                                                                                                                                                                                                                                                                  National Weather Service
  OCS                                                                                                                                                                                                                                                                                                  Oklahoma Climatological Survey
  OMB                                                                                                                                                                                                                                                                                                  Office of Management and Budget
  PMP                                                                                                                                                                                                                                                                                                  Project Management Plan
  quality control                                                                                                                                                                                                                                                                                      The operational activities and techniques required to ensure that quality requirements have been fulfilled.
  quality flag                                                                                                                                                                                                                                                                                         An indicator of the degree to which quality requirements have been fulfilled; in the *Clarus* context, an indicator of the reliability or usefulness of a data element or dataset.
  RWIS                                                                                                                                                                                                                                                                                                 Road Weather Information System
  STWDSR                                                                                                                                                                                                                                                                                               Surface Transportation Weather Decision Support Requirements
  STWSP                                                                                                                                                                                                                                                                                                Surface Transportation Weather Service Provider
  TMDD                                                                                                                                                                                                                                                                                                 Traffic Management Data Dictionary
  UTC                                                                                                                                                                                                                                                                                                  Coordinated Universal Time
  VII                                                                                                                                                                                                                                                                                                  Vehicle Infrastructure Integration
  WIST                                                                                                                                                                                                                                                                                                 Weather Information for Surface Transportation
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\

[ ]{.Apple-converted-space}"Pavement data" in this context includes
surface and subsurface data specified in NTCIP 1204 (Ref. 8).

[ ]{.Apple-converted-space}The arrows in this diagram do *not* indicate
data flows; they show the subject-object orientation of the
relationship.

[ ]{.Apple-converted-space}"Pavement" in this context includes bridges.

[ ]{.Apple-converted-space}Security considerations for the *Clarus*
system fall under the guidance of Reference 14, OMB Circular No. A‑130,
which, by its own definition, does not apply to "critical national
security missions." Future applications of *Clarus* may necessitate
revisiting this classification.

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

PAGE[  ]{.Apple-converted-space}9

\

\

+-----------------------+-----------------------+-----------------------+
| \                     | All documentation,    | \                     |
|                       | software, and data    |                       |
|                       | related to this       |                       |
|                       | project are           |                       |
|                       | proprietary and       |                       |
|                       | copyrighted. Use is   |                       |
|                       | governed by the       |                       |
|                       | contract requirements |                       |
|                       | as defined in the U.  |                       |
|                       | S. Department of      |                       |
|                       | Transportation        |                       |
|                       | Federal Highway       |                       |
|                       | Administration[       |                       |
|                       | ]{.s4}Contract No.    |                       |
|                       | DTFH61-05-C-00022.    |                       |
|                       | Unauthorized use of   |                       |
|                       | this documentation is |                       |
|                       | a violation of law    |                       |
|                       | except as provided    |                       |
|                       | for in said contract. |                       |
+-----------------------+-----------------------+-----------------------+
|                       |                       | \                     |
+-----------------------+-----------------------+-----------------------+

Copyright © 2005 Mixon/Hill, Inc. All rights reserved.

\

\

\

*Clarus Weather System Design*

***[ ]{.Apple-tab-span}High Level System Requirements Specification***

\

[]{.s5}04037-rq201hrs0100

\

[*Page[ ]{.Apple-converted-space}*]{.s5} PAGE ii

*Copyright © 2005 Mixon/Hill, Inc.*

*All rights reserved.*

\

\

[]{.s5}04037-rq201hrs0100

\

[*Page[ ]{.Apple-converted-space}*]{.s5} PAGE 10

*Copyright © 2005 Mixon/Hill, Inc.*

*All rights reserved.*

\

\

*Clarus Weather System Design*

***[ ]{.Apple-tab-span}High Level System Requirements Specification***

\

[]{.s5}04037-rq201hrs0100

\

[*Page[ ]{.Apple-converted-space}*]{.s5} PAGE 18

*Copyright © 2005 Mixon/Hill, Inc.*

*All rights reserved.*

\

\

*Clarus Weather System Design*

***[ ]{.Apple-tab-span}High Level System Requirements Specification***

\

[]{.s5}04037-rq201hrs0100

\

[*Page[ ]{.Apple-converted-space}*]{.s5} PAGE 36

*Copyright © 2005 Mixon/Hill, Inc.*

*All rights reserved.*

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
