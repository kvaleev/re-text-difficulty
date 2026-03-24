---
consensus_grade_level: 10.4
headings_per_sentence: 0.01
lists_per_sentence: 0.01
smao_sentences_pct: 0.6
vague_words_per_sentence: 0.1
anaphora_per_sentence: 0.06
sentence_cv: 2.288
cpre_terms_per_sentence: 0.33
---
# **SOFTWARE REQUIREMENTS SPECIFICATION (SRS)** **FOR THE DALLAS / FT. WORTH REGIONAL** **CENTER-TO-CENTER COMMUNICATIONS NETWORK**

## **Version 3.0** December 5, 2001 Prepared for: Software Task Force **NORTH CENTRAL TEXAS COUNCIL OF GOVERNMENTS** 616 Six Flags Drive P.O. Box 5888 Arlington, TX 76005-5888 Prepared by: **SOUTHWEST RESEARCH INSTITUTE** Post Office Drawer 28510, 6220 Culebra Road San Antonio, Texas 78228-0510


## **TABLE OF CONTENTS**

**Page**


**1.0** **SCOPE...............................................................................................................................1**


1.1 Identification.......................................................................................................................1
1.2 System Overview................................................................................................................1
1.3 Operational Concept...........................................................................................................1
1.4 Goals and Objectives..........................................................................................................2
1.5 Constraints..........................................................................................................................3
1.6 Document Overview...........................................................................................................3
1.7 Related Documents.............................................................................................................3

**2.0** **REQUIREMENTS ...........................................................................................................4**


2.1 Interfaces ............................................................................................................................4
2.1.1 Roadway Network Interface Requirements........................................................................5
2.1.2 Traffic Conditions Interface Requirements........................................................................5
2.1.3 Incident Data Interface Requirements................................................................................6
2.1.4 Lane Closure Interface Requirements................................................................................6
2.1.5 Dynamic Message Sign Interface Requirements................................................................7
2.1.6 Lane Control Signal Interface Requirements.....................................................................8
2.1.7 Closed Circuit Television Interface Requirements.............................................................9
2.1.8 Ramp Meter Requirements...............................................................................................10
2.1.9 Highway Advisory Radio Requirements..........................................................................11
2.1.10 Traffic Signals Requirements...........................................................................................12
2.1.11 Environment Sensor Station Requirements......................................................................13
2.1.12 High Occupany Vehicle Requirements............................................................................13
2.1.13 Parking Lot Requirements................................................................................................14
2.1.14 School Zone Requirements...............................................................................................14
2.1.15 Railroad Crossing Requirements......................................................................................15
2.1.16 Reversible Lanes Requirements.......................................................................................15
2.1.17 Dynamic Lane Assignments Requirements......................................................................16
2.1.18 Transit Requirements........................................................................................................17
2.1.19 Network Device Status Interface Requirments ................................................................19
2.1.20 Command Timeframe Request / Response Interface Requirements................................20
2.2 Functional.........................................................................................................................21
2.2.1 Data Collector Requirements...........................................................................................21
2.2.2 Data Transmission Requirements.....................................................................................21
2.2.3 Web Map Requirements...................................................................................................22
2.2.4 Incident GUI Requirements..............................................................................................23
2.2.5 Remote Control GUI ........................................................................................................23
2.3 Design and Construction Standards..................................................................................25
2.4 Operational.......................................................................................................................26

**APPENDIX A – ACRONYMS**


**SOFTWARE REQUIREMENTS SPECIFICATION** ii


## **LIST OF TABLES**

**Page**

Table 1. Roadway Network Interface Requirements......................................................................5
Table 2. Traffic Conditions Interface Requirements ......................................................................6
Table 3. Incident Data Interface Requirements ..............................................................................6
Table 4. Lane Closure Interface Requirements...............................................................................7
Table 5. DMS Interface Requirements ...........................................................................................8
Table 6. LCS Interface Requirements.............................................................................................9
Table 7. CCTV Interface Requirements .......................................................................................10
Table 8. Ramp Meter Interface Requirements..............................................................................11
Table 9. HAR Interface Requirements..........................................................................................12
Table 10. Traffic Signals Interface Requirements........................................................................13
Table 11. ESS Interface Requirements.........................................................................................13
Table 12. HOV Interface Requirements .......................................................................................14
Table 13. Parking Lot Interface Requirements.............................................................................14
Table 14. School Zone Interface Requirements............................................................................15
Table 15. Railroad Crossing Interface Requirements...................................................................15
Table 16. Reversible Lanes Interface Requirements ....................................................................16
Table 17. Dynamic Lane Assignments Interface Requirements...................................................17
Table 18. Transit Interface Requirements.....................................................................................18
Table 19. Network Device Status Requirements..........................................................................20
Table 20. Command Timeframe Request / Response Interface Requirements ............................21
Table 21. Data Collector Requirements........................................................................................21
Table 22. Data Transmission Requirements.................................................................................21
Table 23. WWW Map Requirements............................................................................................22
Table 24. Incident GUI Requirements..........................................................................................23
Table 25. Remote Control GUI.....................................................................................................24
Table 26. Computer Resource Requirements ...............................................................................25
Table 27. Design and Implementation Requirements...................................................................26
Table 28. Required States and Modes Requirements ...................................................................26


**SOFTWARE REQUIREMENTS SPECIFICATION** iii


## **REVISION HISTORY**

|Revision|Date|Changes|
|---|---|---|
|1.0|September 4, 1999|Initial release|
|2.0|February 24, 2000|• Significantly modified the structure of the SRS<br>• Requirements from version 1.0 were reformatted to utilize<br>the new structure<br>• Expanded the requirements for device status<br>• Added requirements for device command/control<br>• Added requirements for remote control user interface|
|3.0|December 5, 2001|Added EO-22 to identification table.<br>Revised to reflect changes from SICD and CICD version 2.3.<br>Incorporated input from DFW Regional Software Task Force<br>into document. Major new additions included:<br>• Ramp Meters<br>• Highway Advisory Radio (HAR)<br>• Traffic Signals<br>• Environmental Sensor Stations (ESS)<br>• High Occupancy Vehicle (HOV) Lanes<br>• Parking Lots<br>• School Zones<br>• Railroad Crossings<br>• Reversible Lanes<br>• Dynamic Lanes<br>• Transit|



**SOFTWARE REQUIREMENTS SPECIFICATION** iv


## **1.0 SCOPE**

This Software Requirements Specification (SRS) provides the requirements for the Center-toCenter Communications (C2C) Communications project.

|Identification|Col2|
|---|---|
|**Project Title:**|Center-To-Center Communications|
|**Project Number:**|04594, EO 17<br>04594, EO 22|
|**Abbreviation:**|C2C|
|**Version Number:**|3.0|
|**Release Number:**|1|



**1.2** **System Overview**


This document describes the requirements for the Dallas/Ft. Worth (DFW) Regional “Center-toCenter (C2C) Communications Network” that is based on a Texas Department of Transportation
(TxDOT) C2C project. The TxDOT C2c project initially connected the DFW TxDOT Traffic
Management Centers (TMCs). This C2C infrastructure implements a repository for traffic data
and provides a mechanism to exchange device control information between TMCs.


The C2C project will be implemented using the evolving ITS Traffic Management Data
Dictionary (TMDD) standard, the message sets associated with TMDD, other ITS Data Elements
and Message Sets. The use of ITS standards will create a system that is reusable for other ITS
application areas and will provide the State of Texas with a baseline system that can be cost
effectively extended in the future.


**1.3** **Operational Concept**


The C2C infrastructure must interconnect several dissimilar traffic management systems. In
order to create the C2C infrastructure, interfaces to the existing systems will be created. The
data from these interfaces will communicate with the existing system in a “system specific”
format. The data being deposited into the C2C infrastructure will be converted to a standard
format (based on the ITS standards). The C2C infrastructure is being created using a series of
building blocks. These building blocks allow the software to be utilized in a number of
configurations (by simply altering the configuration parameters of the software).


In a region such as Dallas/Ft. Worth, multiple instances of the building blocks will be utilized.
The software is being designed so that multiple instances of a building block can be deployed by
simply “configuring” the building block of operation within a specific agency. Conceptually, the
C2C infrastructure would be deployed as depicted in the following diagram:


**SOFTWARE REQUIREMENTS SPECIFICATION** **1**


Any data that is passed into the “cloud” in the above figure will be based on the ITS standards.
Systems will interface to the “cloud” using a project defined protocol. New systems that are
deployed (based on the ITS standards) will not utilize the project defined protocol but will be
moved “into” the cloud (because they themselves would be based on the ITS standards.


**1.4** **Goals and Objectives**


The C2C project has the following goals:


  - To provide a common repository for traffic information for the DFW Metroplex.

  - To provide a World Wide Web based graphical map to display traffic conditions in the
DFW Metroplex.

  - To provide a Microsoft Windows application that will allow agencies without a formal
Traffic Management Center (TMC) to participate in the C2C infrastructure and
information sharing.

  - To provide a system which supports ITS center-to-center communications for
command/control/status of various ITS field devices including: Dynamic Message
Signs, Lane Control Signals and Closed Circuit Television Cameras (CCTVs), Ramp
Meters, and Highway Advisory Radios (HARs).

  - To utilize National ITS standards to implement the project.

  - To provide a software system that is extensible all local or regional partners. This
would allow a “local” common repository to be created by “linking” individual
partners, a “regional” common repository to be created by “linking” local common
repositories and a “statewide” common repository to be created by “linking” regional
common repositories.


**SOFTWARE REQUIREMENTS SPECIFICATION** **2**


**1.5** **Constraints**


None.


**1.6** **Document Overview**


Section 2 defines the requirements of the system. Acronyms are defined in Appendix A.


**1.7** **Related Documents**


 - _Concept Of Operations Framework For The Dallas/Ft. Worth Regional Center-to-Center_
_Communications Network_, Version 1.0, Southwest Research Institute, November 2001.


**SOFTWARE REQUIREMENTS SPECIFICATION** **3**


## **2.0 REQUIREMENTS**

The following sections define the requirements for the C2C project. Requirements are listed in
separate sections and in table format for each functional area. The C2C project mnemonic
uniquely identifies the C2C project to distinguish its requirements from the requirements of other
ITS systems. The mnemonic for the C2C project is _C2C_ . The Requirement Category Mnemonic
is a two-letter mnemonic for each functional area. The Requirement Numbers are a combination
of target Advanced Traffic Management System (ATMS) and sequential within a given
functional area.


The columns of the tables are structured as follows:


 - The first column of the table contains the requirement identifier. The requirement
identifier is a three-part number that is used to uniquely identify each requirement. The
number consists of the following fields: <C2C Project Mnemonic>-<Requirement
Category Mnemonic>-<Requirement Number>.

 - The second column of each table contains a description of the requirement.

 - The third column contains a rationale for the requirements. If the rationale is left blank
for a particular requirement, the requirement rationale is assumed obvious from the
description.


**2.1** **Interfaces**


The following tables list the interfaces that shall be developed.


**SOFTWARE REQUIREMENTS SPECIFICATION** **4**


**2.1.1** **Roadway Network Interface Requirements**


Table 1 lists the interface requirements for supporting the roadway network data transmission.


**Table 1. Roadway Network Interface Requirements**






|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
|C2C-IF-IS01|For each roadway network it maintains, the<br>Center shall provide the following information.<br>1. <br>Network identifier<br>2. <br>Network name<br>3. <br>Number of links in the network<br>4. <br>Number of nodes in the network<br>5. <br>List of link data<br>6. <br>List of node data||
|C2C-IF-IS02|<br> <br>The Center shall provide the following link information:<br>1. <br>Link identifier<br>2. <br>Link name<br>3. <br>Road number<br>4. <br>Link type<br>5. <br>Link type description<br>6. <br>Start node (see below for node information)<br>7. <br>End node (see below for node information)<br>8. <br>Direction<br>9. <br>Length<br>10. Capacity<br>11. Speed limit<br>12. Speed limit truck<br>13. Number of lanes||
|C2C-IF-IS03|The Center shall provide the following node information:<br>1. <br>Node identifier<br>2. <br>Node name<br>3. <br>Node jurisdiction<br>4. <br>Owner<br>5. <br>Latitude/longitude<br>6. <br>Type of node (i.e., intersection or bridge)<br>7. <br>Node type description<br>8. <br>Number of links||



**2.1.2** **Traffic Conditions Interface Requirements**


Table 2 lists the interface requirements for supporting the traffic conditions data transmission.


**SOFTWARE REQUIREMENTS SPECIFICATION** **5**


**Table 2. Traffic Conditions Interface Requirements**






|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
|C2C-IF-IS04|For each link defined within the Center:<br>1. <br>Network identifier<br>2. <br>Link identifier<br>3. <br>Data type<br>4. <br>Data type description<br>5. <br>Delay<br>6. <br>Travel time<br>7. <br>Volume<br>8. <br>Speed<br>9. <br>Density<br>10. Occupancy||



**2.1.3** **Incident Data Interface Requirements**


Table 3 lists the interface requirements for supporting the incident data transmission.


**Table 3. Incident Data Interface Requirements**






|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
|C2C-IF-IS05|The Center shall support the following information about<br>each incident:<br>1. <br>Network identifier<br>2. <br>Incident ID<br>3. <br>Incident description<br>4. <br>Roadway<br>5. <br>Cross street<br>6. <br>Latitude/longitude<br>7. <br>Link identifier<br>8. <br>Direction<br>9. <br>Status<br>10. Update Type<br>11. Affected lanes<br>12. Classification<br>13. Severity<br>14. Incident type<br>15. Incident type description<br>16. Road conditions<br>17. Weather<br>18. Confirmed date & time<br>19. Cleared date & time||



**2.1.4** **Lane Closure Interface Requirements**


Table 4 lists the interface requirements for supporting the lane closure data transmission.


**SOFTWARE REQUIREMENTS SPECIFICATION** **6**


**Table 4. Lane Closure Interface Requirements**






|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
|C2C-IF-IS06|The Center shall support the following information about<br>each lane closure:<br>1. <br>Network identifier<br>2. <br>Lane closure ID<br>3. <br>Closure description<br>4. <br>Starting roadway<br>5. <br>Starting cross street<br>6. <br>Latitude/longitude of starting location<br>7. <br>Ending roadway<br>8. <br>Ending cross street<br>9. <br>Latitude/longitude of ending location<br>10. Direction of roadway<br>11. Link identifier<br>12. Current status<br>13. Update type<br>14. Affected lanes<br>15. Lane closure source<br>16. Contact<br>17. Days closed<br>18. Start time of day<br>19. End time of day<br>20. Start date of series<br>21. End date of series||



**2.1.5** **Dynamic Message Sign Interface Requirements**


Table 5 lists the interface requirements for supporting the Dynamic Message Sign (DMS) data
transmission.


**SOFTWARE REQUIREMENTS SPECIFICATION** **7**


**Table 5. DMS Interface Requirements**






|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
|C2C-IF-IS07|The Center shall provide the following status information<br>about each DMS:<br>1. <br>Network Identifier<br>2. <br>DMS Identifier<br>3. <br>DMS Name<br>4. <br>Location (latitude/longitude)<br>5. <br>Sign Geometry (row/column)<br>6. <br>Status (online/offline)<br>7. <br>Current message (MULTI string)<br>8. <br>Beacons (on/off)||
|C2C-IF-IS08|<br> <br>To support DMS control in other centers, the Center shall<br>be able to support the following device control command<br>for a DMS:<br>1. <br>Network identifier<br>2. <br>DMS Identifier<br>3. <br>Username<br>4. <br>Password<br>5. <br>Beacons (on/off)<br>6. <br>Immediate message (MULTI string)||



**2.1.6** **Lane Control Signal Interface Requirements**


Table 6 lists the interface requirements for supporting the Lane Control Signal (LCS) data
transmission.


**SOFTWARE REQUIREMENTS SPECIFICATION** **8**


**Table 6. LCS Interface Requirements**






|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
|C2C-IF-IS09|The Center shall support the following status information<br>about each LCS:<br>1. <br>Network identifier<br>2. <br>LCS identifier<br>3. <br>LCS name<br>4. <br>Location (latitude/longitude)<br>5. <br>Geometry (number of heads)<br>6. <br>Head capabilities<br>7. <br>Status<br>8. <br>Current pattern||
|C2C-IF-IS10|<br> <br>To support LCS control in other centers, the Center shall<br>be able to support the following device control command<br>for a LCS:<br>1. <br>Network Identifier<br>2. <br>LCS Identifier<br>3. <br>Username<br>4. <br>Password<br>5. <br>Signal Pattern||



**2.1.7** **Closed Circuit Television Interface Requirements**


Table 7 lists the interface requirements for supporting the Closed Circuit Television (CCTV)
data transmission.


**SOFTWARE REQUIREMENTS SPECIFICATION** **9**


**Table 7. CCTV Interface Requirements**








|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
|C2C-IF-IS11|The Center shall provide the following information status<br>information about each CCTV:<br>1. <br>Network identifier<br>2. <br>CCTV identifier<br>3. <br>CCTV name<br>4. <br>Location (latitude/longitude)<br>5. <br>Status (online/offline)<br>6. <br>Locked/unlocked<br>7. <br>Lock holder (if locked)<br>8. <br>Supported directions<br>9. <br>Current direction<br>10. Current preset position<br>11. Current pan<br>12. Current tilt<br>13. Current zoom<br>14. Current focus<br>15. Current iris||
|C2C-IF-IS12|<br>To support CCTV control in other centers, the Center<br>shall be able to support the following CCTV control<br>request:<br>1. <br>Network identifier<br>2. <br>CCTV Identifier<br>3. <br>Username<br>4. <br>Password<br>5. <br>CCTV request (one of the following):<br>§ Lock camera<br>§ Set direction<br>§ Set preset<br>§ Set absolute (pan/tilt/zoom/focus/iris)<br>§ Stop offset (pan/tilt/zoom/focus/iris)|Ft. Worth will not support<br>Momentary<br>Pan/Tilt/Zoom/Iris/Focus<br>command|
|C2C-IF-IS13|To support video snapshots, the Center shall be able to<br>support the following status information:<br>1. <br>Network identifier<br>2. <br>CCTV Identifier<br>3. <br>CCTV Name<br>4. <br>Status<br>5. <br>Current camera direction<br>6. <br>Size of snapshot<br>7. <br>Video snapshot (in JPEG format)||
|C2C-IF-IS14|To support CCTV switching in other centers, the Center<br>shall be able to support the following CCTV switching<br>command:<br>1. <br>Network identifier (owner of CCTV)<br>2. <br>Username<br>3. <br>Password<br>4. <br>Video channel input identifier<br>5. <br>Video channel output identifier|Dallas will not support the Tour<br>video switch command|



**2.1.8** **Ramp Meter Requirements**


Table 8 lists the interface requirements for supporting the ramp meter data transmission.

**SOFTWARE REQUIREMENTS SPECIFICATION** **10**


**Table 8. Ramp Meter Interface Requirements**






|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
|C2C-IF-IS15|The Center shall support the following status information<br>about each ramp meter:<br>1. <br>Network identifier (owner of ramp meter)<br>2. <br>Ramp Meter Identifier<br>3. <br>Ramp Meter Name<br>4. <br>Location (latitude/longitude)<br>5. <br>Status<br>6. <br>Status Source<br>7. <br>Plan<br>8. <br>Cycle Time||
|C2C-IF-IS16|<br> <br>To support Ramp Meter control in other centers, the<br>Center shall be able to support the following device<br>control command for a ramp meter:<br>1. <br>Network identifier (owner of ramp meter)<br>2. <br>Ramp Meter Identifier<br>3. <br>Username<br>4. <br>Password<br>5. <br>Plan<br>6. <br>Duration||



**2.1.9** **Highway Advisory Radio Requirements**


Table 9 lists the interface requirements for supporting the Highway Advisory Radio (HAR) data
transmission.


**SOFTWARE REQUIREMENTS SPECIFICATION** **11**


**Table 9. HAR Interface Requirements**






|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
|C2C-IF-IS17|The Center shall support the following status information<br>about each HAR:<br>1. <br>Network identifier (owner of HAR)<br>2. <br>HAR Identifier<br>3. <br>HAR Name<br>4. <br>Location (latitude/longitude)<br>5. <br>Status<br>6. <br>Current Message<br>7. <br>Current Message Text||
|C2C-IF-IS18|<br> <br>To support HAR control in other centers, the Center shall<br>be able to support the following device control command<br>for a HAR:<br>1. <br>Network identifier (owner of HAR)<br>2. <br>HAR Identifier<br>3. <br>Username<br>4. <br>Password<br>5. <br>Message<br>6. <br>Message Text<br>7. <br>Duration||



**2.1.10** **Traffic Signals Requirements**


Table 10 lists the interface requirements for supporting the Traffic Signals data transmission.


**SOFTWARE REQUIREMENTS SPECIFICATION** **12**


**Table 10. Traffic Signals Interface Requirements**






|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
|C2C-IF-IS19|The Center shall support the following status information<br>about each Traffic Signal:<br>1. <br>Network identifier (owner of traffic signal)<br>2. <br>Traffic Signal Identifier<br>3. <br>Traffic Signal Name<br>4. <br>Location (latitude/longitude)<br>5. <br>Status<br>6. <br>Status Source<br>7. <br>State<br>8. <br>Failure State<br>9. <br>Plan<br>10. Plan Expiration<br>11. Signal Preemption||
|C2C-IF-IS20|<br>To support Traffic Signal control in other centers, the<br>Center shall be able to support the following device<br>control command for a Traffic Signal:<br>1. <br>Network identifier (owner of traffic signal)<br>2. <br>Traffic Signal Identifier<br>3. <br>Username<br>4. <br>Password<br>5. <br>Traffic Signal Plan Identifier<br>6. <br>Duration||



**2.1.11** **Environment Sensor Station Requirements**


Table 11 lists the interface requirements for supporting the Environmental Sensor Station (ESS)
data transmission.


**Table 11. ESS Interface Requirements**






|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
|C2C-IF-IS21|The Center shall support the following status information<br>about each ESS:<br>1. <br>Network identifier (owner of sensor)<br>2. <br>Environmental Sensor Identifier<br>3. <br>Environmental Sensor Name<br>4. <br>Type<br>5. <br>Location (latitude/longitude)<br>6. <br>Status<br>7. <br>Type<br>8. <br>Reading<br>9. <br>Units<br>10. Alarm status||



**2.1.12** **High Occupany Vehicle Requirements**


Table 12 lists the interface requirements for supporting the High Occupancy Vehicle (HOV) data
transmission.


**SOFTWARE REQUIREMENTS SPECIFICATION** **13**


**Table 12. HOV Interface Requirements**






|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
|C2C-IF-IS22|The Center shall support the following status information<br>about each HOV:<br>1. <br>Network identifier (owner of HOV)<br>2. <br>HOV Identifier<br>3. <br>HOV Name<br>4. <br>Link Identifier<br>5. <br>Status<br>6. <br>Failure State<br>7. <br>Plan<br>8. <br>State<br>9. <br>Status Source<br>10. Occupants<br>11. Next Transition Time||
|C2C-IF-IS22.1|To support HOV Lane control in other centers, the<br>Center shall be able to support the following device<br>control command for a HOV Lane:<br>1. <br>Network identifier (owner of HOV)<br>2. <br>HOV Lane Identifier<br>3. <br>Username<br>4. <br>Password<br>5. <br>Lane Plan<br>6. <br>Duration||



**2.1.13** **Parking Lot Requirements**


Table 13 lists the interface requirements for supporting the Parking Lot data transmission.


**Table 13. Parking Lot Interface Requirements**






|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
|C2C-IF-IS23|The Center shall support the following status information<br>about each Parking Lot:<br>1. <br>Network identifier (owner of parking lot)<br>2. <br>Parking Lot Identifier<br>3. <br>Parking Lot Name<br>4. <br>Location (latitude/longitude)<br>5. <br>Status<br>6. <br>Capacity<br>7. <br>Utilization<br>8. <br>Entrance<br>9. <br>Restrictions<br>10. Special Capabilities||



**2.1.14** **School Zone Requirements**


Table 14 lists the interface requirements for supporting the School Zone data transmission.


**SOFTWARE REQUIREMENTS SPECIFICATION** **14**


**Table 14. School Zone Interface Requirements**






|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
|C2C-IF-IS24|The Center shall support the following status information<br>about each School Zone:<br>1. <br>Network identifier (owner of school zone)<br>2. <br>Link Identifier<br>3. <br>School Zone Identifier<br>4. <br>School Zone Name<br>5. <br>Location (latitude/longitude)<br>6. <br>Status<br>7. <br>Failure Status<br>8. <br>State Plan<br>9. <br>State Source||
|C2C-IF-IS25|<br> <br>To support School Zone control in other centers, the<br>Center shall be able to support the following device<br>control command for a School Zone:<br>1. <br>Network identifier (owner of school zone)<br>2. <br>School Zone Identifier<br>3. <br>Username<br>4. <br>Password<br>5. <br>Plan||



**2.1.15** **Railroad Crossing Requirements**


Table 15 lists the interface requirements for supporting the Railroad Crossing data transmission.


**Table 15. Railroad Crossing Interface Requirements**






|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
|C2C-IF-IS26|The Center shall support the following status information<br>about each Railroad Crossing:<br>1. <br>Network identifier (owner of railroad Crossing)<br>2. <br>Link Identifier<br>3. <br>Rail Crossing Identifier<br>4. <br>Rail Crossing Name<br>5. <br>Location (latitude/longitude)<br>6. <br>Status<br>7. <br>Rail Type<br>8. <br>Estimated Time for Train to Clear of Intersection<br>9. <br>Estimated Minutes to Train Arrival<br>10. Rail closing signal type||



**2.1.16** **Reversible Lanes Requirements**


Table 16 lists the interface requirements for supporting the Reversible Lanes data transmission.


**SOFTWARE REQUIREMENTS SPECIFICATION** **15**


**Table 16. Reversible Lanes Interface Requirements**






|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
|C2C-IF-IS27|The Center shall support the following status information<br>about each Reversible Lane:<br>1. <br>Network identifier (owner of reversible lane)<br>2. <br>Reversible Lane Identifier<br>3. <br>Reversible Lane Name<br>4. <br>Link Identifier<br>5. <br>Indicator Status<br>6. <br>Indicator Failure State<br>7. <br>Plan<br>8. <br>Direction<br>9. <br>Direction Transition Time<br>10. Status Source||
|C2C-IF-IS28|<br>To support Reversible Lane control in other centers, the<br>Center shall be able to support the following device<br>control command for a Reversible Lane:<br>1. <br>Network identifier (owner of reversible lane)<br>2. <br>Reversible Lane Identifier<br>3. <br>Username<br>4. <br>Password<br>5. <br>Plan<br>6. <br>Duration||



**2.1.17** **Dynamic Lane Assignments Requirements**


Table 17 lists the interface requirements for supporting the Dynamic Lane Assignment data
transmission.


**SOFTWARE REQUIREMENTS SPECIFICATION** **16**


**Table 17. Dynamic Lane Assignments Interface Requirements**






|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
|C2C-IF-IS29|The Center shall support the following status information<br>about each Dynamic Lane:<br>1. <br>Network identifier (owner of dynamic lane)<br>2. <br>Link Identifier<br>3. <br>Dynamic Lane Identifier<br>4. <br>Dynamic Lane Name<br>5. <br>Indicator Status<br>6. <br>Failure State<br>7. <br>Plan<br>8. <br>Type<br>9. <br>Transition Time||
|C2C-IF-IS30|<br> <br>To support Dynamic Lane control in other centers, the<br>Center shall be able to support the following device<br>control command for a Dynamic Lane:<br>1. <br>Network identifier (owner of dynamic lane)<br>2. <br>Dynamic Lane Identifier<br>3. <br>Username<br>4. <br>Password<br>5. <br>Lane Plan<br>6. <br>Duration||



**2.1.18** **Transit Requirements**


Table 18 lists the interface requirements for supporting the Transit data transmission.


**SOFTWARE REQUIREMENTS SPECIFICATION** **17**


**Table 18. Transit Interface Requirements**






|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
|C2C-IF-IS30|The Center shall support the following status information<br>about each Bus Stop:<br>1. <br>Network identifier (owner of bus stop)<br>2. <br>Link Identifier1<br>3. <br>Relative Link Location<br>4. <br>Identifier<br>5. <br>Name<br>6. <br>Location (Node)<br>7. <br>Bus Routes<br>8. <br>Frequency||
|C2C-IF-IS31|<br><br>The Center shall support the following status information<br>about each Bus Location:<br>1. <br>Network identifier (owner of bus)<br>2. <br>Link Identifier<br>3. <br>Bus Identifier<br>4. <br>Bus Name<br>5. <br>Location (latitude/longitude)<br>6. <br>Schedule Adherence<br>7. <br>Vehicle Attributes<br>8. <br>Capacity||
|C2C-IF-IS32|The Center shall support the following status information<br>about each Light/Commuter Stop:<br>1. <br>Network identifier (owner of stop)<br>2. <br>Link Identifier<br>3. <br>Commuter / Light Rail Stop Identifier<br>4. <br>Commuter / Light Rail Stop Name<br>5. <br>Location<br>6. <br>Routes<br>7. <br>Frequency||
|C2C-IF-IS33|The Center shall support the following status information<br>about each Light/Commuter Location:<br>1. <br>Network identifier (owner of train)<br>2. <br>Link Identifier<br>3. <br>Commuter / Light Rail Identifier<br>4. <br>Commuter / Light Rail Name<br>5. <br>Location (latitude/location)<br>6. <br>Schedule Adherence<br>7. <br>Vehicle Attributes<br>8. <br>Capacity||



1 Associating a bus stop, commuter / light rail stop, bus location, etc. with a link within a roadway network may be
an inherently difficult problem from a configuration management perspective. The roadway network and transit
information may be managed by separate centers, i.e. City of Dallas vs. DART. Updates to the roadway network,
i.e. renaming links, may cause the associated link information within the transit data to become outdated and
inconsistent with the location data.

**SOFTWARE REQUIREMENTS SPECIFICATION** **18**


|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
|C2C-IF-IS34|The Center shall support the following status information<br>about each Park and Ride Lot:<br>1. <br>Network identifier (owner of lot)<br>2. <br>Park and Ride Lot Identifier<br>3. <br>Park and Ride Lot Name<br>4. <br>Location (latitude/location)<br>5. <br>Status<br>6. <br>Capacity<br>7. <br>Utilization<br>8. <br>Entrance<br>9. <br>Restrictions<br>10. Special Capabilities||
|C2C-IF-IS35|<br>The Center shall support the following status information<br>about each Vehicle Priority:<br>1. <br>Vehicle Identifier<br>2. <br>Network identifier (owner of signal)<br>3. <br>Link Identifier<br>4. <br>Intersection Identifier<br>5. <br>Priority Request Status<br>6. <br>Departure Time<br>7. <br>Desired Arrival Time<br>8. <br>Priority<br>9. <br>Vehicle Classification<br>10. Service Strategy||



**2.1.19** **Network Device Status Interface Requirments**


Table 19 lists the interface requirements for supporting network device status data transmission.


**SOFTWARE REQUIREMENTS SPECIFICATION** **19**


**Table 19. Network Device Status Requirements**






|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
|C2C-IF-IS36|The Center shall support the following information about<br>network device status:<br>1. <br>Network identifier<br>2. <br>Number of DMSs<br>3. <br>Number of LCSs<br>4. <br>Number of CCTVs<br>5. <br>Number of CCTV video inputs<br>6. <br>Number of CCTV video outputs<br>7. <br>Number of Ramp Meters<br>8. <br>Number of HARs<br>9. <br>Number of Traffic Signals<br>10. Number of ESSs<br>11. Number of HOVs<br>12. Number of Parking Lots<br>13. Number of School Zones<br>14. Number of Railroad Crossings<br>15. Number of Reversible Lanes<br>16. Number of Dynamic Lanes<br>17. DMS status data<br>18. LCS status data<br>19. CCTV status data<br>20. Video input channel identifiers<br>21. Video output channel identifiers<br>22. Ramp Meter status data<br>23. HAR status data<br>24. Traffic Signal status data<br>25. ESS status data<br>26. HOV status data<br>27. Parking Lot status data<br>28. School Zone status data<br>29. Railroad Crossing status data<br>30. Reversible Lane status data<br>31. Dynamic Lane status data||



**2.1.20** **Command Timeframe Request / Response Interface Requirements**


Table 20 lists the interface requirements supporting command timeframe requests and responses.


**SOFTWARE REQUIREMENTS SPECIFICATION** **20**


**Table 20. Command Timeframe Request / Response Interface Requirements**



|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
|C2C-IF-IS37|The device status requestor and Center shall support the<br>following information for command timeframe request:<br>1. <br>Network identifier<br>2. <br>Device Type|This is used to determine when a<br>center will accept a command<br>from a remote user. These are<br>device type dependent.|
|C2C-IF-IS38|The device status requestor and Center shall support the<br>following information for command timeframe request:<br>1. <br>Network identifier<br>2. <br>Device Type<br>3. <br>Days Commands Accepted<br>4. <br>Times Commands Accepted|This is the response to a<br>command timeframe request.|


**2.2** **Functional**







The follow sections detail the functional requirements of the C2C project.


**2.2.1** **Data Collector Requirements**


The Data Collector Requirements define what must be stored on the Data Collector. The
requirements are listed in Table 21.


**Table 21. Data Collector Requirements**

|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
|C2C-DS-01|The Data Collector shall be designed to support the<br>storage of TMDD data elements and message set<br>information.||



**2.2.2** **Data Transmission Requirements**


The Data Transmission Requirements define the messaging protocols and message sets to be
used for C2C communications and are listed in Table 22.


**Table 22. Data Transmission Requirements**

|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
|C2C-DT-01|The C2C Project shall utilize the TMDD standard<br>(including message sets) to transmit information.||
|C2C-DT-02|DATEX/ASN shall be used to transmit the TMDD<br>message sets.||
|C2C-DT-03|TCP/IP shall be used to transmit the DATEX/ASN data.|Derived from this requirement is<br>the necessary TCP/IP connection<br>management.|



**SOFTWARE REQUIREMENTS SPECIFICATION** **21**


**2.2.3** **Web Map Requirements**


The Web Map application generates a map that can be displayed on an Internet WWW server.
The map provides a graphical depiction of the traffic conditions. The requirements for the
WWW map are listed in Table 23.


**Table 23. WWW Map Requirements**

|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
|C2C-MP-01|The map shall display interstates and state highways on<br>the graphical map.||
|C2C-MP-03|The basemap data shall be derived from the North<br>Central Texas Council of Governments (NCTCOG) Geo-<br>Data warehouse.||
|C2C-MP-03|The map user shall be able to alter the current<br>magnification (zoom level) of the map.||
|C2C-MP-04|The map user shall be able to pan the map in each of the<br>following directions: North, South, East or West.||
|C2C-MP-05|Each link displayed on the map shall be color coded to<br>provide a graphical depiction of speeds. A configuration<br>file shall be provided to specify specific speed values.<br>The color coding shall be as follows:<br>• Green - speeds > TBD MPH<br>• Yellow - speeds between TBD and TBD MPH<br>• Red – speeds below TBD MPH||
|C2C-MP-06|The map shall display the current incidents (as icons)<br>known to the C2C Project.||
|C2C-MP-07|The user shall be able to click on an incident icon to<br>obtain further information about the incident.||
|C2C-MP-08|All current incidents shall be displayed in tabular format<br>with the following information contained in the table:<br>• Location<br>• Type of incident (e.g., accident, lane closure)<br>• Severity of incident<br>• Incident status<br>• Travel direction<br>• Effected lanes||
|C2C-MP-09|The map shall be capable of displaying the following for<br>a DMS:<br>1. <br>Location<br>2. <br>Current Message||
|C2C-MP-10|The map shall be capable of displaying the following for<br>a LCS:<br>1. <br>Location<br>2. <br>Current Signals||
|C2C-MP-11|The map shall be capable of displaying the following for<br>a CCTV:<br>1. <br>Location<br>2. <br>Status||



**SOFTWARE REQUIREMENTS SPECIFICATION** **22**


**2.2.4** **Incident GUI Requirements**


The Incident GUI must provide data to the C2C Infrastructure. The GUI requirements are listed
in Table 24.


**Table 24. Incident GUI Requirements**









|Requirement<br>Number|Requirement Description|Rationale or<br>Comments|
|---|---|---|
|C2C-GI-01|The Incident GUI shall allow the user to enter incident or lane closure<br>information without the use of an Center.||
|C2C-GI-02|The Incident GUI shall allow the user to input the following<br>information for each incident:<br>• <br>Location (latitude/longitude)<br>• <br>Description<br>• <br>Status<br>• <br>Effected lanes<br>• <br>Detection time<br>• <br>Response time<br>• <br>Estimated time to clear queue<br>• <br>Queue length||
|C2C-GI-03|The Incident GUI shall allow the user to input the following<br>information for each lane closure:<br>• <br>Location (latitude/longitude)<br>• <br>Description<br>• <br>Effected lanes<br>• <br>Date<br>• <br>Start time<br>• <br>End time||
|C2C-GI-04|The GUI shall provide a list of previously entered incidents.||
|C2C-GI-05|The GUI shall allow the data about an incident to be modified.||
|C2C-GI-06|The GUI shall allow a user to delete a previously entered incident.||
|C2C-GI-07|The GUI shall provide a list of previously entered lane closures.||
|C2C-GI-08|The GUI shall allow a user to delete a previously entered lane closure.||
|C2C-GI-09|The GUI shall allow a user to delete a previously entered lane closure.||


**2.2.5** **Remote Control GUI**


Table 25 contains the requirements for the Remote Control GUI.


**SOFTWARE REQUIREMENTS SPECIFICATION** **23**


**Table 25. Remote Control GUI**















|Col1|Requirement<br>Number|Requirement Description|Rationale or Comments|Col5|
|---|---|---|---|---|
||C2C-CG-01|The remote Center Control GUI shall be designed to<br>execute on a public network (e.g., Internet) and transmit<br>equipment requests to the C-2-C software system.|The Remote Control GUI will<br>execute as a local application on<br>a PC. The application will<br>generate TMDD device control<br>messages that will be sent to a<br>Center for processing.<br>Connectivity through the various<br>firewalls and gateways is not<br>addressed by this requirement.|The Remote Control GUI will<br>execute as a local application on<br>a PC. The application will<br>generate TMDD device control<br>messages that will be sent to a<br>Center for processing.<br>Connectivity through the various<br>firewalls and gateways is not<br>addressed by this requirement.|
||C2C-CG-02|When the GUI application is initiated, the user shall be<br>prompted for the following information:<br>• <br>User name<br>• <br>Password|||
||C2C-CG-03|The user shall be provided with the capability to select a<br>network identifier for a device command/control request.|||
||C2C-CG-04|Once an Center is selected, the user shall be able to select<br>a DMS from a list and provide the following information:<br>• <br>Target DMS<br>• <br>Message to be displayed<br>• <br>Beacons On/Off|||
||C2C-CG-05|Once an Center is selected, the user shall be able to select<br>a LCS from a list and provide the following information:<br>• <br>Target LCS<br>• <br>Assignment of lane arrows|||
||C2C-CG-06|Once an Center is selected, the user shall be able to issue<br>a CCTV switching command:<br>• <br>Source (input)<br>• <br>Destination port (output)|||
||C2C-CG-07|Once an Center is selected, the user shall be able to select<br>a CCTV from a list and provide the following<br>information:<br>• <br>Target CCTV<br>• <br>Device control including:<br>• <br>Pan<br>• <br>Tilt<br>• <br>Zoom|||
||C2C-CG-08|Once an Center is selected, the user shall be able to select<br>a Ramp Meter from a list and provide the following<br>information:<br>• <br>Target Ramp Meter<br>• <br>Plan|||
||C2C-CG-09|Once an Center is selected, the user shall be able to select<br>a HAR from a list and provide the following information:<br>• <br>Target HAR<br>• <br>Text to be sent to the HAR|||
||C2C-CG-10|Once an Center is selected, the user shall be able to select<br>a Traffic Signal from a list and provide the following<br>information:<br>• <br>Target Traffic Signal<br>• <br>Plan|||
||C2C-CG-11|Once an Center is selected, the user shall be able to select|||


**SOFTWARE REQUIREMENTS SPECIFICATION** **24**


|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
||a HOV from a list and provide the following information:<br>• <br>Target HOV<br>• <br>Plan||
|C2C-CG-12|<br><br>Once an Center is selected, the user shall be able to select<br>a School Zone from a list and provide the following<br>information:<br>• <br>Target School Zone<br>• <br>Plan||
|C2C-CG-13|Once an Center is selected, the user shall be able to select<br>a Reversible Lane from a list and provide the following<br>information:<br>• <br>Target Reversible Lane<br>• <br>Plan||
|C2C-CG-14|Once an Center is selected, the user shall be able to select<br>a Dynamic Lane from a list and provide the following<br>information:<br>• <br>Target Dynamic Lane<br>• <br>Plan||
|C2C-CG-15|For each device command/control status request sent by<br>the Remote GUI, the status returned from the network<br>identifier will be displayed in a scrollable list on the GUI.||


**2.3** **Design and Construction Standards**


The computer resource requirements are listed in Table 26.


**Table 26. Computer Resource Requirements**

|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
|C2C-DC-01|The C2C Server shall execute in a Microsoft Windows<br>NT environment.||
|C2C-DC-02|A DATEX/ASN runtime library shall be available on any<br>computer communicating to the C2C project.||
|C2C-DC-03|The web server application shall use ESRI's ARC<br>Internet Map Server (ARC IMS) product for creating of<br>map images.||



The Design and implementation requirements are listed in the in Table 27.


**SOFTWARE REQUIREMENTS SPECIFICATION** **25**


**Table 27. Design and Implementation Requirements**



|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
|C2C-DC-04|The C2C shall execute in a Microsoft Windows NT<br>environment.||
|C2C-DC-05|The C2C shall be implemented in the C/C++<br>programming language.||
|C2C-DC-06|The C2C web interface shall be implemented using<br>C/C++ and ESRI ARC IMS.||
|C2C-DC-07|The Incident GUI shall be implemented using C/C++ and<br>ESRI Map Objects.||
|C2C-DC-08|The Remote Control GUI shall be implemented using<br>C/C++ and ESRI Map Objects.||


**2.4** **Operational**


The C2C Project shall be capable of operating in one of two modes: normal mode for normal
operations or in test mode for development and testing. The requirements for these modes are
listed in Table 28.


**Table 28. Required States and Modes Requirements**






|Requirement<br>Number|Requirement Description|Rationale or Comments|
|---|---|---|
|C2C-OP-01|The C2C shall be able to operate in normal mode. In this<br>mode the C2C receives data from all connected systems,<br>including the Incident GUI, and combines the data into a<br>single data store (database).||
|C2C-OP-02|The C2C shall be able to operate in test mode.  In this<br>mode, the C2C performs normal mode operations and<br>also logs activities.|To provide additional<br>information for development and<br>testing.|



**SOFTWARE REQUIREMENTS SPECIFICATION** **26**


## **APPENDIX A** **ACRONYMS**

**SOFTWARE REQUIREMENTS SPECIFICATION**


## **ACRONYMS**

ASN.1 Abstract Syntax Notation One
ATIS Advance Traveler Information System

ATMS Advanced Traffic Management System

CCTV Closed Circuit Television

DATEX/ASN DATEX/Abstract Syntax Notation

DFW Dallas/Ft. Worth
DMS Dynamic Message Sign

DT Data Transmission

ESS Environmental Sensor Stations

GI Incident GUI

GUI Graphical User Interface
HAR Highway Advisory Radio

HOV High Occupancy Vehicle

ICD Interface Control Document

IMS Internet Map Server

ISP Information System Provider
ITS Intelligent Transportation Systems

LCS Lane Control Signal

MPH Miles Per Hour

MULTI Mark-Up Language for Transportation Information

NCTCOG North Central Texas Council of Governments
NTCIP National Transportation Communications for ITS Protocol

SRS Software Requirements Specification

TBD To Be Determined

TCP/IP Transmission Control Protocol/Internet Protocol

TMC Traffic Management Center
TMDD Traffic Management Data Dictionary

TxDOT Texas Department of Transportation

WWW World Wide Web


**SOFTWARE REQUIREMENTS SPECIFICATION** **A-** 1


