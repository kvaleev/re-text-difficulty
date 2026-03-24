---
consensus_grade_level: 10.9
headings_per_sentence: 0.1
lists_per_sentence: 0.01
smao_sentences_pct: 2.4
vague_words_per_sentence: 0.14
anaphora_per_sentence: 0.15
sentence_cv: 2.495
cpre_terms_per_sentence: 0.38
---
# **SYSTEM REQUIREMENTS SPECIFICATION** **EVLA Correlator Monitor & Control**

Project Document:


Revision 1.0


_Preliminary Draft_


Bruce Rowen, December 5, 2002


National Radio Astronomy Observatory


Array Operations Center


P.O. Box O


Socorro, NM 87801-0387


# Revision History

|Date|Version|Description|Author|
|---|---|---|---|
|12-5-2002|1.0|Initial draft|Bruce Rowen|
|||||
|||||
|||||
|||||



EVLA Correlator Monitor and Control SRS ii


# Table of Contents

_**1**_ _**Introduction............................................................................................................................................................1**_


**1.1** **Purpose...........................................................................................................................................................1**


**1.2** **Scope ................................................................................................................................................................1**


**1.3** **Definitions, Acronyms, and Abbreviations ...........................................................................................1**
1.3.1 Definitions..............................................................................................................................................1


**1.4** **References ......................................................................................................................................................2**


**1.5** **Overview.........................................................................................................................................................2**


_**2**_ _**Overall Description................................................................................................................................................3**_


**2.1** **Product Perspective .....................................................................................................................................3**


**2.2** **Product Functionality.................................................................................................................................3**
2.2.1 Monitoring..............................................................................................................................................3
2.2.2 Control ....................................................................................................................................................3
2.2.3 Data Output............................................................................................................................................3
2.2.4 Data Input...............................................................................................................................................4
2.2.5 Recovery .................................................................................................................................................4


**2.3** **User characteristics .....................................................................................................................................5**
2.3.1 Array Operator.......................................................................................................................................5
2.3.2 Engineers and Technicians..................................................................................................................5
2.3.3 Software Developer ..............................................................................................................................5
2.3.4 Web User................................................................................................................................................5


**2.4** **Constraints.....................................................................................................................................................5**
2.4.1 Criticality of the Application...............................................................................................................5
2.4.2 Computer Hardware Limitations........................................................................................................5
2.4.3 Computer Software Limitations .........................................................................................................5


**2.5** **Assumptions...................................................................................................................................................6**
2.5.1 Configuration Data Stream..................................................................................................................6
2.5.2 Auxiliary Data .......................................................................................................................................6
2.5.3 Outgoing Data Stream..........................................................................................................................6


_**3**_ _**Specific Requirements...........................................................................................................................................7**_


**3.1** **Communication Network Interface Requirements.............................................................................7**
3.1.1 Correlator CMIB, MCCC, CPCC Interface......................................................................................7
3.1.2 MCCC to EVLA M&C Interface .......................................................................................................7
3.1.3 CMIB to Correlator Hardware Interface ...........................................................................................7


**3.2** **Computer Functional Requirements ......................................................................................................8**
3.2.1 General....................................................................................................................................................8
3.2.2 CMIB.......................................................................................................................................................8
3.2.3 MCCC.....................................................................................................................................................9
3.2.4 CPCC.......................................................................................................................................................9


**3.3** **Performance Requirements.......................................................................................................................9**
3.3.1 Hardware ................................................................................................................................................9
3.3.2 Software ................................................................................................................................................10


**3.4** **Reliability/Availability..............................................................................................................................10**


**3.5** **Serviceability...............................................................................................................................................11**


EVLA Correlator Monitor and Control SRS iii


**3.6** **Maintainability ...........................................................................................................................................11**


**3.7** **Scalability .....................................................................................................................................................11**


**3.8** **Security .........................................................................................................................................................12**


**3.9** **Installation and Upgrades........................................................................................................................12**


**3.10** **Documentation ............................................................................................................................................13**


EVLA Correlator Monitor and Control SRS iv


# **1 Introduction**

## **_1.1 Purpose_**

The primary goal of this document is to provide a complete and accurate list of requirements for
the EVLA Correlator Monitor & Control System.

The primary audience of this document includes, but is not limited to, project leaders, the
designers and developers of the system and the end user. The document may also be of interest to
EVLA project scientists and engineers or as a reference for individuals involved in similar projects
with similar requirements.

Much of this document is based on preliminary ideas and concepts from NRC-EVLA Memo #015

[8] and previous System Requirement Documents [5] and [9].

The requirements contained in this document are numbered based on the section/subsection in
which they appear.

## **_1.2 Scope_**


The Correlator Monitor & Control System provides the physical link between the WIDAR
Correlator hardware and the EVLA monitor & control system. It is the primary interface by which
the correlator is configured, operated, and serviced.

The primary functions of the Correlator Monitor & Control System are as follows:

     - Receive configuration information from the EVLA M&C system and translate this info into a
physical correlator hardware configuration.

     - Process and transfer dynamic control data (models, filter parameters, etc), and monitor data
(auto correlation products, state counts, etc.)

     - Monitor Correlator and correlator subsystem health and take corrective action autonomously
(where possible) to recover from hardware and computing system faults.

     - Perform limited amounts of real-time data processing and probing such as providing tools to
collect and display auto correlation products.

     - Allow for easy system access to aid testing and debugging.

## **_1.3 Definitions, Acronyms, and Abbreviations_**

### **1.3.1 Definitions**

**Administrator**     - An individual with unrestricted access to all aspects of the system.
**Real-time**     - Monitor and control operations which have hard deadlines that when missed result in
data corruption/loss.
**Backend**    - A computer system that performs final real time post-correlation processing on data
received from the correlator baseline boards.


EVLA Correlator Monitor and Control SRS 1


**CMCS**    - Correlator Monitor and Control System
**MCCC**   - Master Correlator Control Computer
**CPCC**    - Correlator Power Control Computer
**CPU**   - Central Processing Unit. In this document CPU refers to a single board computer or
computer system
**e2e**     - End-to-End System (archive)
**M&C**   - Monitor and Control System
**EVLA**   - The VLA Expansion Project
**RFI**     - Radio Frequency Interference
**SyRS**    - Refers to the _System Requirements_ document.
**SRS**    - Refers to the _Software Requirements Specification_ document.
**VCI**    - Virtual Correlator Interface.

## **_1.4 References_**


1) ANSI/IEEE Std 830-1998, IEEE Recommended Practice for Software Requirements
Specifications
2) ANSI/IEEE Std 1233-1996, IEEE Guide for Developing System Requirements Specifications
3) EVLA Memo No. 15, Scientific Requirements for the EVLA Real-Time System
4) EVLA Project Book
5) EVLA System Requirements (SyRS)
6) EVLA Architecture and Design
7) Refined EVLA WIDAR Correlator Architecture, NRC-EVLA Memo# 014, Brent Carlson, Oct.
2, 2001.
8) EVLA Correlator Monitor and Control System, Test Software, and Backend Software
Requirements and Design Concepts, NRC-EVLA Memo # 015, Brent Carlson, Jan. 23, 2002.
9) EVLA Correlator Backend, Software Requirements Specification.

## **_1.5 Overview_**


The remainder of this document contains a more detailed description of the Correlator Monitor
and Control System as well as the primary requirements necessary to design and build the system.
Section 2 provides a general description of the Correlator M&C System. Section 3 details the
requirements of the product and is the core of this document.

The format of the document follows that outlined in the IEEE STD 830 document, IEEE
Recommended Practice for Software Requirements Specifications.


EVLA Correlator Monitor and Control SRS 2


# **2 Overall Description**

## **_2.1 Product Perspective_**

The EVLA Correlator Monitor and Control System is responsible for correlator configuration, real
time monitor/control, and hardware testing/servicing. The CMCS exists as an integrated part of the
overall EVLA Monitor and Control Structure. The CMCS will provide a level of abstraction to
modularize the correlator system within the EVLA environment. The “gateway” to the correlator
will be through the Virtual Correlator Interface (VCI) which will exist as a software entity on the
MCCC.

The CMCS will be designed and implemented as a Master/Slave network with one computer
system coordinating the activities of a number of “intelligent” hardware control processors. The
Master is expected to handle the bulk of the monitor/control interface with the outside world
whereas the slaves will be only concerned with the correlator hardware systems under their direct
control. This topology will place the real-time computing requirements in the slave layer and the
quasi real-time, network-chaotic loads into the master layer. One of the primary benefits of this
structure is isolation (ease of serviceability, programmability) of the correlator hardware from the
EVLA M&C environment. The system is expected to be redundant in critical areas and highly
modular.

## **_2.2 Product Functionality_**

### **2.2.1 Monitoring**

The Correlator monitor subsystem will provide EVLA system wide access to all correlator system
states (including the M&C supervisor system state). Some of this information will be provided on
a time synchronous basis as required by other systems (backend, monitor archive, data archive,
etc.) and other information will only be presented on a request basis. The CMCS will be a fully
observable system with the only limits placed on information access being those imposed by
hardware, bandwidth, and/or security restrictions. Error and status messages will be provided in a
concise time/location referenced format to upper system levels in a content controllable manner.

### **2.2.2 Control**

Correlator configurations and control instructions will be received from the EVLA M&C system
in a form suitable for translation by the MCCC. The translation will provide the correlator with
specific goal oriented hardware configuration tables to satisfy the configuration requested by the
EVLA M&C. A second interface with a human GUI will also allow for configuration of the
correlator hardware, preferably through the same table structures used above. This translation
interface will be called the Virtual Correlator Interface (VCI).

### **2.2.3 Data Output**

Specific data sets required by the Backend Data Processing System (state counts, auto
correlations, etc) will be provided in a timely and robust fashion over a secondary virtual network.
Ancillary monitor data including system health, error messages and configuration echoes will be
spooled such that temporary loss of network communication with the EVLA M&C network will
not result in loss of monitor data. Data sample rates and contents will be fully controllable via
either the EVLA M&C or the Backend processing controller.


EVLA Correlator Monitor and Control SRS 3


### **2.2.4 Data Input**

The MCCC will accept external data feeds for models, time standards, fiber-link phase corrections
and other required data to be packaged with control data delivered to the correlator hardware.

### **2.2.5 Recovery**



The ability to attempt recovery from failure or hot-swapped hardware devices will be built into
this system. Should a CMIB subsystem fail and not respond to reboot requests or other self-heal
attempts, an alert notice will be issued so appropriate personnel can affect a hardware repair. The
CMIB subsystem will then be automatically restarted and configured back into the current
operational environment.
MCCC health will be monitored by internal software processes (watchdogs) and external systems
(the CPCC). Should a non-recoverable MCCC system failure occur, the backup MCCC system
will be activated automatically via the CPCC or by external human intervention? It is intended that
both primary and secondary MCCC systems maintain full CMCS state information such that any
hard failure (unrecoverable) in the primary node can be corrected by simply rerouting M&C
communications to the secondary.
Watchdog processes and the MCCC will likewise monitor CPCC health. Due to the more
hardware specific connections and controls of the CPCC, actions taken by external system upon
hard failures are TBD.


Virtual Correlator Interface


Correlator Data Output



&





Virtual Correlator Interface









Correlator Data Output





Interface




|Col1|CMCS Test<br>Interface|Col3|
|---|---|---|
||CMCS Test<br>Interface||
|Correlator<br>Monitor<br>& <br>Control System<br>Correlator<br>Hardware<br>Correlator<br>Backend<br>Data Processing|Correlator<br>Monitor<br>& <br>Control System<br>Correlator<br>Hardware<br>Correlator<br>Backend<br>Data Processing|Correlator<br>Monitor<br>& <br>Control System<br>Correlator<br>Hardware<br>Correlator<br>Backend<br>Data Processing|
|Correlator<br>Hardware|Correlator<br>Hardware|Correlator<br>Hardware|
||||
|Correlator<br>Backend<br>Data Processing|Correlator<br>Backend<br>Data Processing|Correlator<br>Backend<br>Data Processing|
||||
||||
|<br>e2e System<br>Image Processing<br>& <br>Archive|<br>e2e System<br>Image Processing<br>& <br>Archive|<br>e2e System<br>Image Processing<br>& <br>Archive|



EVLA Correlator Monitor and Control SRS 4


## **_2.3 User characteristics_**

All use of the Correlator Monitor and Control System will be through the VCI or MCCC.
Software tools will be provided to assist the user at all access levels from system wide
configuration and control to a low level CMIB command line instruction.

### **2.3.1 Array Operator**

The primary contact with array operations will be via status and error messages channeled through
the Monitor and Control System.

### **2.3.2 Engineers and Technicians**

The ability of the Correlator System to achieve and maintain high reliability and uptime will be
vitally dependent upon reliable operation and rapid diagnosis and repair of faults in the hardware
and software systems. These individuals will be responsible for performing corrective and
preventive maintenance along with periodic performance tests and upgrades. Engineers and
technicians will need tools to inspect and monitor individual CMIB layer devices from remote
locations and have the ability to fault trace to a specific hot-swappable subsystem.

### **2.3.3 Software Developer**

These individuals are responsible for developing the software and will interact with the system to
ensure that it is functioning properly. The software developer requires remote access to the system
so that troubleshooting can be accomplished away from the EVLA and during non-working hours.

### **2.3.4 Web User**

A few authorized individuals may be allowed access to parts of the system that are usually
considered restricted.

## **_2.4 Constraints_**

### **2.4.1 Criticality of the Application**

The Correlator Monitor and Control is a critical component in the Astronomical data path. If it is
unavailable, incoming astronomical data will be lost.

### **2.4.2 Computer Hardware Limitations**

The ultimate determiner of a reliable and available correlator is dependent on the stability of the
CMCS network and control computers. Functionality needs to be modularized to provide the
easiest means of fault detection and repair.

### **2.4.3 Computer Software Limitations**

The ultimate ease of use and flexibility of the correlator is rooted in the CMCS software. Full
access is required with a high level of data integration to provide the user with a logical and
coherent interface.


EVLA Correlator Monitor and Control SRS 5


## **_2.5 Assumptions_**

### **2.5.1 Configuration Data Stream**

It is assumed that the Correlator will receive configuration data in a format that is unambiguous and
results in a convergent hardware configuration (requested configuration is valid and achievable).

### **2.5.2 Auxiliary Data**

It is assumed that all auxiliary data needed for real time update of correlator parameters (delay
models, fiber round trip phase corrections, time codes, dynamic configuration data, etc.) will be
provided directly by the EVLA M&C system or by dedicated servers.

### **2.5.3 Outgoing Data Stream**

It is assumed that the backend data processing and EVLA M&C systems will be capable of
accepting output data rates (both those required and those requested) generated by the CMCS.


|Col1|Stati|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||Stati|Stati|Stati|Stati|||
||||Stati|Stati|Stati|||
||||Stati|Stati|Stati|on|Bo|
|||||||||
||||||CMI|CMI|CMI|
|||||||||








|Col1|Phasing Board|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
||||||||
|||||Baselin<br>CMI|Baselin<br>CMI|B|
|||||Baselin<br>CMI|CMI|CMI|
||||||||


|Baseline Rack (one of many)<br>Phasing Board<br>Baseline Board<br>CMIB<br>Power Control<br>Module|Col2|Col3|
|---|---|---|
|Baseline Rack  (one of many)<br>Phasing Board<br>Baseline Board<br>Power Control<br>Module<br>CMIB|Power Control<br>Module|Power Control<br>Module|
|Baseline Rack  (one of many)<br>Phasing Board<br>Baseline Board<br>Power Control<br>Module<br>CMIB|Power Control<br>Module||



|100Base Ethernet Station Rack (one of many)<br>Power M&C bus (TBD)<br>RS-232C<br>Station Board<br>CMIB<br>Ethernet<br>Switch<br>o Main Correlator Power Control<br>M&C Control Computer Module<br>(MCCC)<br>Baseline Rack (one of many)<br>Phasing Board<br>Redundant<br>Keep-Alive Baseline Board<br>Link<br>CMIB<br>Correlator Power<br>Power Control<br>Control Computer<br>M&C Module<br>(CPCC)<br>M&C<br>Ports<br>Power Monitor/Control Bus|Col2|Col3|Col4|Station Rack (one of many)<br>Station Board<br>CMIB<br>Power Control<br>Module|Col6|
|---|---|---|---|---|---|
|Station Rack (one of many)<br>Station Board<br>Power Control<br>Module<br>CMIB<br>Baseline Rack (one of many)<br>Phasing Board<br>Baseline Board<br>Power Control<br>Module<br>CMIB<br>Main Correlator<br>Control Computer<br> <br>(MCCC)<br>Ethernet<br>Switch<br> Correlator Power<br>Control Computer<br> <br>(CPCC)<br>M&C<br>Ports<br>Power Monitor/Control Bus<br>Redundant<br>Keep-Alive<br>Link<br> o<br> M&C<br> <br> M&C<br>100Base Ethernet<br>Power M&C bus (TBD)<br>RS-232C|Correlator Power<br>Control Computer<br> <br>(CPCC)<br>M&C<br>Ports|Correlator Power<br>Control Computer<br> <br>(CPCC)<br>M&C<br>Ports|Correlator Power<br>Control Computer<br> <br>(CPCC)<br>M&C<br>Ports|Correlator Power<br>Control Computer<br> <br>(CPCC)<br>M&C<br>Ports|Correlator Power<br>Control Computer<br> <br>(CPCC)<br>M&C<br>Ports|
|||||||
|||M&C<br>Ports|M&C<br>Ports|M&C<br>Ports|M&C<br>Ports|
|||M&C<br>Ports|Power Monitor/Control Bus|Power Monitor/Control Bus|Power Monitor/Control Bus|


**Figure 2.** CMCS network connection topology (Only two racks/subsystems shown)


EVLA Correlator Monitor and Control SRS 6


# **3 Specific Requirements**

## **_3.1 Communication Network Interface Requirements_**

### **3.1.1 Correlator CMIB, MCCC, CPCC Interface**

.

|Col1|Description|
|---|---|
|3.1.1.1|Network Protocol –_The interface between the CMIB, MCCC, and CPCC_<br>_shall be Ethernet (IEEE 802.3 compliant) of 100 Mbits/sec or better data_<br>_rate._|
|3.1.1.2|Network Topology –_The interface shall be transformer coupled copper_<br>_twisted pair unless other materials are required for noise (RFI), ground_<br>_isolation, or physical layout constraints (long distances)._|
|3.1.1.3|Network Distribution -_Network switches shall be employed to distribute_<br>_traffic within a correlator rack and where their use will significantly_<br>_reduce overall network wiring complexity_.|
|3.1.1.4|Network Isolation –_The MCCC-CMIB, MCCC-CPCC, and MCCC-EVLA_<br>_M&C networks shall be on separate physical interfaces._|
|3.1.1.5|Redundant Communication -_There shall be a redundant communication_<br>_path (serial RS-232c or equivalent) between the MCCC and CPCC to_<br>_provide for remote reboot in the event of a networking or computing_<br>_failure._|


### **3.1.2 MCCC to EVLA M&C Interface**

|Req. ID|Description|
|---|---|
|3.1.2.1|Network Protocol_– The interface between the MCCC and external_<br>_networks (EVLA M&C) shall be Ethernet (IEEE 802.3 compliant) of 100_<br>_Mbits/sec or better data rate._|
|3.1.2.2|Network Topology –_Pathways penetrating the correlator shielded room_<br>_shall be fiber optic or other low RFI material to meet RFI specifications._|
|3.1.2.3|Security -_Network routers/switches shall be employed at the MCCC-_<br>_EVLA M&C interface level (or higher) to protect the MCCC from_<br>_unauthorized access and irrelevant network traffic._|


### **3.1.3 CMIB to Correlator Hardware Interface**


EVLA Correlator Monitor and Control SRS 7


|Req. ID|Description|
|---|---|
|3.1.3.1|Hardware communications –_The CMIB daughter board shall_<br>_communicate with the correlator carrier boards via either the PCI or ISA_<br>_busses_. Alternative communication paths may be through a serial or<br>parallel connection as required.|
|3.1.3.2|Hardware identification_– The CMIB shall be capable of reading a 16-bit_<br>_identifier from the host correlator board_. This identifier will be used to<br>form a unique IP address for CMIB network addressing and allow carry<br>over IP addressing for hot swap modules.|
|3.1.3.3|Hardware addressing –_The CMIB shall be able to read back the contents_<br>_of all writeable hardware control registers where meaningful_. It is desired<br>that the state of the correlator hardware be available through interrogation<br>across the CMIB bus for monitoring and fault tolerance.|
|3.1.3.4|Hardware Booting –_The CMIB shall have control of hardware “warm_<br>_boots” such that an external command from the MCCC to reboot the_<br>_CMIB shall have an option to force a hardware warm boot._|
|3.1.3.5|Hardware Visual Health Monitoring –_The carrier board for the CMIB_<br>_shall have an externally visible indicator (LED or other) that will provide_<br>_a user with a physical indication of CMIB operational status (red = fault,_<br>_green = ok)._|

## **_3.2 Computer Functional Requirements_**

### **3.2.1 General**

|Req. ID|Description|
|---|---|
|3.2.1.1|Power Supplies–_Where applicable, all computers and peripherals shall_<br>_be powered though UPS type devices with sufficient capacity for the_<br>_computers to safely coordinate a system wide shutdown of the correlator_<br>_hardware in the event of a prolonged power outage._The UPS devices<br>need the ability to signal the CMCS when a power outage has occurred<br>and keep the CMCS apprised of time remaining on backup power.|
|3.2.1.2|Accessibility –_All computers within the CMCS system shall have the_<br>_ability for authorized users to directly access individual systems for_<br>_maintenance and monitoring through remote logins._|
|3.2.1.3|Self-Monitoring –_Each computer system in the CMCS shall have a_<br>_hardware based watchdog timer configured to reboot the system in the_<br>_case of a system hang._ Reboots should result in minimal system<br>interruptions with the offending CPU reconfiguring and returning to<br>service autonomously.|


### **3.2.2 CMIB**

**Req. ID** **Description**


EVLA Correlator Monitor and Control SRS 8


|3.2.2.1|Form Factor– The CMIB shall conform to both electrical and physical<br>PC104+ standards.|
|---|---|
|3.2.2.2|Module Features_– The CMIB shall contain 64 Mbytes or greater of_<br>_SDRAM, IDE hard disk interface, minimum of one serial and one parallel_<br>_interface, PCI/ISA buses, 100BaseT network interface, capacity to boot_<br>_and run a generic COTS operating system in a near real-time environment_<br>_from local non-volatile storage._|
|3.2.2.3|Operating System –_The operating system/module combination shall be_<br>_capable of supporting the real-time requirements of the correlator_<br>_hardware, hardware monitor/control/diagnostics with support for_<br>_standalone “test bench” operation with simulated control data_<br>_generation, and the ability to access and upgrade correlator hardware_<br>_PLD/FPGA personalities through its network connection._|

### **3.2.3 MCCC**

|Req. ID|Description|
|---|---|
|3.2.3.1|Form Factor –_The MCCC shall be a high availability type general-_<br>_purpose computer capable of supporting multiple Ethernet interfaces,_<br>_COTS operating systems, and support server/host services for the CMIB_<br>_operating system._ This computer may exist as a hot swappable or<br>redundant CPU device capable of self-healing where possible.|
|3.2.3.2|System Isolation –_The MCCC shall have all required disk and file system_<br>_facilities installed locally such that the system can boot and run in a_<br>_stand-alone configuration._ This should allow the correlator CMIBs to<br>boot, configure, and run without any communication outside of the<br>correlator M&C network.|


### **3.2.4 CPCC**

|Req. ID|Description|
|---|---|
|3.2.4.1|Form Factor –_The CPCC shall be a high availability type general-_<br>_purpose computer capable of supporting a COTS operating system and_<br>_have the ability to accept a large number of external hardware status_<br>_signals (power, temp, etc) either directly or through external interface_<br>_hardware._ This computer may exist as a hot swappable or redundant CPU<br>device capable of self-healing where possible.|
|3.2.4.2|System Isolation–_The CPCC shall have all required disk and file system_<br>_facilities installed locally such that the system can boot and run in a_<br>_stand-alone configuration._ This requirement is to allow correlator power<br>monitoring and control to continue in the event of an M&C network<br>failure.|


## **_3.3 Performance Requirements_**

### **3.3.1 Hardware**

|Req. ID|Description|
|---|---|
|3.3.1.1|Processing Software Performance –_ The CMCS processors shall be_|



EVLA Correlator Monitor and Control SRS 9


|Col1|capable of meeting all data processing deadlines and anticipated future<br>requirements|
|---|---|
|3.3.1.2|Processor Hardware Performance –_The CMCS processors shall be_<br>_capable of responding to correlator hardware inputs (interrupts) in a_<br>_deterministic fashion with sufficient performance to avoid data loss,_<br>_corruption or overflows._|

### **3.3.2 Software**

|Req. ID|Description|
|---|---|
|3.3.2.1|Errors –_All lower system error and debug messages shall be present at_<br>_the MCCC layer._ Aside from a networking or CPU failure, It should never<br>be necessary to directly access a CPU to display error messages.|
|3.3.2.2|Error Message Access –_All system error and debug messages shall be_<br>_categorized in a logical fashion such that message traffic can be filtered_<br>_as to content, detail, and message rate_. Personnel interested in error<br>messages should be able to easily filter the error message stream.|
|3.3.2.3|Time Stamps –_All messages passed between CMCS system layers shall_<br>_have both UTC and wall clock time stamp information appropriate for the_<br>_message type._ Error messages will be stamped with their discovery time,<br>control messages will be stamped with their generation time. Other<br>message internal time stamps can be used as monitor/control parameters<br>as deemed necessary.|
|3.3.2.4|Test Software. -_Software shall be provided that allows an authorized user_<br>_full access to all messaging, monitor, and control traffic throughout the_<br>_CMCS._ This software will provide full system access for testing,<br>debugging, and control while the correlator is off line or under the control<br>of the EVLA M&C system.|
|3.3.2.5|Test Software GUI._A Graphical User Interface shall be provided as an_<br>_interface to the CMCS test software that allows for a convenient and_<br>_configurable tool to access the CMCS remotely through the VCI._|


## **_3.4 Reliability/Availability_**

|Req. ID|Description|
|---|---|
|3.4.1|Auto-correction –_the CMCS shall be self-monitoring._It will be capable<br>of detecting, reporting on and automatically taking action to remedy or<br>lessen the impact of, at a minimum, the following types of abnormal<br>conditions: processor hardware failure, operating system hangs or crashes,<br>temperature or voltage deviations, computational performance below<br>minimum specifications, computational error rates above maximum<br>specification, internal communications failures, and external (with the<br>EVLA M&C) communications disruptions.|
|3.4.2|Software –_the software part of the system shall be able to perform without_<br>_total system restart due to internal failure between system maintenance_<br>_windows._|
|3.4.3|Hardware –_the hardware part of the system shall be able to perform_<br>_indefinitely without complete loss of service, except in the event of total_<br>_failure of primary and backup power_.|



EVLA Correlator Monitor and Control SRS 10


|3.4.4|Loss of Control Data– the system shall be able to continue processing of<br>all correlator configuration/control events until the queues of parameters<br>are exhausted and external communications are restored|
|---|---|
|3.4.5|Standby Mode –_the system shall be able to sit at idle and resume_<br>_operations with minimal (amount TBD) delay_.|

## **_3.5 Serviceability_**

|Req. ID|Description|
|---|---|
|3,5,1|Hardware Accessibility –_all system processing and interconnect_<br>_hardware shall be readily accessible for maintenance, repair, replacement_<br>_and/or reconfiguration_. This excludes items that due to their physical<br>location, are not practical to configure for ready access (i.e. backplanes)|
|3.5.2|Software Accessibility –_all systems and application source code shall be_<br>_available to or on the systems that execute it_.|
|3.5.3|Debugging –_all software application modules shall be debuggable._They<br>should be organized such that all inputs and outputs can be simulated if<br>necessary.|
|3.5.4|Processes –_all software processes shall be killable, restartable,_<br>_debuggable and testable with minimal impact on normal system_<br>_operations_.|


## **_3.6 Maintainability_**

|Req. ID|Description|
|---|---|
|3.6.1|Software tools –_software tools and pre-built applications that do not have_<br>_source code available shall come with a complete diagnostic package and_<br>_customer support_.|
|3.6.2|Operating Systems –_operating system software shall either have source_<br>_code available or come with sufficient diagnostics and customer support_.|


## **_3.7 Scalability_**

|Req. ID|Description|
|---|---|
|3.7.1|Hardware –_I/O, communications, and processing hardware shall be_<br>_easily expandable, reconfigurable, augmentable and replaceable to meet_<br>_increasing data traffic and processing demands imposed by EVLA science,_<br>_Correlator changes, and availability of new hardware._|
|3.7.2|Transparency –_3.7.1, above, shall be accomplished in manner that is_<br>_transparent to processing, communications and I/O software functions_<br>_with the possible exception of recompilation of executables_.|
|3.7.3|Seamlessness –_3.7.1, above, shall be accomplished in a manner that is_<br>_seamless, in that it does not affect hardware modules or software_<br>_functionality that it meets at interfaces_.|



EVLA Correlator Monitor and Control SRS 11


## **_3.8 Security_**

The CMCS needs a robust security mechanism in place so that unauthorized users are not allowed
access. Authorized users are expected to be restricted to software and hardware development,
testing, maintenance and operations personnel.

All users of the CMCS must be uniquely identified. This could be done via a username and
associated password scheme that would authenticate and authorize the user access to the system
and, if applicable, grant the user access to restricted or controlled parts of the system. If a user
cannot be identified, they will not be given access. In order to monitor all past access to the
system, all attempts to access the system should be logged.

Users’ needs and expectations from the system will be different. Systems operations should be
given unrestricted access to all aspects of the system and should have the authority to grant and
revoke privileges on a per-user basis. Development, testing and maintenance personnel, on the
other hand, require access to some parts of the system, but not all, indicating that an access level is
needed that allows privileges to be granted on a per-user and what-do-you-need-to-do basis.

|Req. ID|Description|
|---|---|
|3.8.1|_All users of the system shall login using some form of unique_<br>_identification._(e.g., username and password)<br>|
|3.8.2|_All login attempts shall be done in a secure manner._(e.g., encrypted<br>passwords)<br>|
|3.8.3|_A system administrator shall have unrestricted access to all aspects of the_<br>_system_. <br>|
|3.8.4|_Each user shall have a set of system access properties that defines the_ <br>_user’s privileges within the system._ (e.g., the subsystems a user may<br>control or system tools the user may access).<br>|
|3.8.5|_The administrator shall have the ability to create and add a new user to_<br>_the system_. <br>|
|3.8.6|_The administrator shall have the ability to remove a user from the system_. <br>|
|3.8.7|_The administrator shall have the ability to edit a user’s system access_<br>_properties_. <br>|
|3.8.8|_The administrator shall have the ability to block all access to the system_<br>_for all users or selectively by user_. (All blocked users with active sessions<br>shall automatically be logged off.)<br>|


## **_3.9 Installation and Upgrades_**

|Req. ID|Description|
|---|---|
|3.9.1|Operations Activities –_ the system shall continue operations, although not_|



EVLA Correlator Monitor and Control SRS 12


|Col1|necessarily at full capacity, on all unaffected resources during partial<br>shutdowns for maintenance, repair and/or upgrade.|
|---|---|
|3.9.2|Replaceability_–modular design principles shall be employed to the_<br>_maximum extent possible. Maximal practical use of available “hot-_<br>_swappable” devices and components shall be made_.|

## **_3.10  Documentation_**

|Req. ID|Description|
|---|---|
|3.10.1|Hardware –_complete and comprehensible hardware systems_<br>_specifications and configuration information shall be readily available_.|
|3.10.2|Software Coding Practices–_software system and application code shall be_<br>_well documented and written in a generally familiar language or_<br>_languages (preferably not more than two)._ _Software shall be written in a_<br>_style that is easily readable and using practices that allow for minimal_<br>_confusion._|



.


EVLA Correlator Monitor and Control SRS 13


