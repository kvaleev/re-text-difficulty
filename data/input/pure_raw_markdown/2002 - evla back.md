---
consensus_grade_level: 10.1
headings_per_sentence: 0.0
lists_per_sentence: 0.0
smao_sentences_pct: 2.0
vague_words_per_sentence: 0.18
anaphora_per_sentence: 0.12
sentence_cv: 1.539
cpre_terms_per_sentence: 0.31
---
# **SYSTEM REQUIREMENTS SPECIFICATION** **EVLA Correlator Backend**

Project Document: A25251N0000


Revision 2.0


Tom Morgan, May 10, 2002


National Radio Astronomy Observatory


Array Operations Center


P.O. Box O


Socorro, NM 87801-0387


# Revision History

|Date|Version|Description|Author|
|---|---|---|---|
|26-Feb-2002|1.0|Initial draft|Tom Morgan|
|05-Mar-2002|1.1|Revised section 3.2.2|Tom Morgan|
|10-May-2002|2.0|Clean-up of section 1, revisions to section 2 and 3|Tom Morgan|
|||||
|||||



EVLA Operations System SRS ii


# Table of Contents

_**1**_ _**Introduction ........................................................................................................................................... 1**_


**1.1** **Purpose.......................................................................................................................................... 1**


**1.2** **Scope.............................................................................................................................................. 1**


**1.3** **Definitions, Acronyms, and Abbreviations................................................................................. 1**
1.3.1 Definitions .............................................................................................................................. 1
1.3.2 Acronyms ............................................................................................................................... 2


**1.4** **References ..................................................................................................................................... 2**


**1.5** **Overview........................................................................................................................................ 2**


_**2**_ _**Overall description................................................................................................................................. 4**_


**2.1** **Product perspective ...................................................................................................................... 4**


**2.2** **Product functionality.................................................................................................................... 4**
2.2.1 Data Input ............................................................................................................................... 4
2.2.2 Data Processing ...................................................................................................................... 4
2.2.3 Data Output ............................................................................................................................ 4
2.2.4 Monitoring.............................................................................................................................. 5
2.2.5 Recovery................................................................................................................................. 5
2.2.6 Control.................................................................................................................................... 5


**2.3** **User characteristics ...................................................................................................................... 6**
2.3.1 Array Operator........................................................................................................................ 7
2.3.2 Engineers and Technicians ..................................................................................................... 7
2.3.3 Astronomer/Scientist .............................................................................................................. 7
2.3.4 Software Developer ................................................................................................................ 7
2.3.5 Web User................................................................................................................................ 7


**2.4** **Constraints .................................................................................................................................... 7**
2.4.1 Criticality of the Application.................................................................................................. 7
2.4.2 Computer Hardware Limitations ............................................................................................ 7
2.4.3 Communications Limitations.................................................................................................. 8
2.4.4 Reliability ............................................................................................................................... 8


**2.5** **Assumptions .................................................................................................................................. 8**
2.5.1 Incoming Data Stream............................................................................................................ 8
2.5.2 Auxiliary Data ........................................................................................................................ 8
2.5.3 Outgoing Data Stream ............................................................................................................ 8


_**3**_ _**Specific requirements ............................................................................................................................ 9**_


**3.1** **External Interface Requirements................................................................................................ 9**
3.1.1 Correlator to Backend Interface.............................................................................................. 9
3.1.2 Backend to End-to-End Interface ......................................................................................... 10
3.1.3 Backend to/from Monitor and Control Interface .................................................................... 9


**3.2** **Functional Requirements........................................................................................................... 10**
3.2.1 Information and data flows................................................................................................... 10
3.2.2 Process Descriptions............................................................................................................. 10
3.2.3 Data Construct Specifications............................................................................................... 12


**3.3** **Performance Requirements ....................................................................................................... 13**
3.3.1 General ................................................................................................................................. 13
3.3.2 Hardware .............................................................................................................................. 13
3.3.3 Software................................................................................................................................ 14


EVLA Operations System SRS iii


**3.4** **Reliability/Availability ............................................................................................................... 14**


**3.5** **Serviceability............................................................................................................................... 15**


**3.6** **Maintainability ........................................................................................................................... 15**


**3.7** **Scalability .................................................................................................................................... 15**


**3.8** **Security........................................................................................................................................ 16**


**3.9** **Installation and Upgrades.......................................................................................................... 16**


**3.10** **Documentation............................................................................................................................ 17**


EVLA Operations System SRS iv


# **1 Introduction**

## **_1.1 Purpose_**

The primary goal of this document is to provide a complete and accurate list of requirements for
the EVLA Correlator Backend System. Upon completion, the document will act as a binding
contract between developers and users and will provide a common point of reference for system
expectations.

The primary audience of this document includes, but is not limited to, project leaders, the
designers and developers of the system and the end user. The document may also be of interest to
EVLA project scientists and engineers or as a reference for individuals involved in similar projects
with similar requirements.

The requirements contained in this document are numbered based on the section/subsection in
which they appear.

Note: Text found between “<” and “>” indicates questions or comments to myself and/or readers.
And In most cases, the phrase “The user” can be replaced with “An authorized user”.

## **_1.2 Scope_**


The Correlator Backend System lies between the Correlator and the End-to-End Systems. It is the
primary component of the real-time astronomical data processing capability (the processing
pipeline) of the EVLA. Its primary responsibility is to perform basic data assembly, formatting
and processing services and to support the desire for real-time inspection of the astronomical data
stream.

The major functions the Correlator Backend System must perform are as follows:
�� Receive data from the Correlator in real-time.
�� Assemble time-series from the Correlator lag output.
�� Perform Fourier Transforms of the assembled time series.
�� Perform a limited number of additional processes upon user request.
�� Deliver suitably formatted results to the End-to-End System.

This document will define only those requirements that must be fulfilled by the Correlator
Backend System.

## **_1.3 Definitions, Acronyms, and Abbreviations_**

### **1.3.1 Definitions**

**Administrator**     - An individual with unrestricted access to all aspects of the system.
**Auxiliary Data**     - All other (non-astronomical) data.
**Data**    - Astronomical observational data.


EVLA Operations System SRS 1


**Lag Set**     - A complete, properly ordered series of lag values that can be submitted to the Fourier
Transform function. The lag frames received from the Correlator will contain up to 128 lag values,
so lag sets longer than 128 values will span multiple lag frames and require proper ordering and
assembly into complete lag sets.
**Metadata**    - All data about the astronomical data.
**NaN**    - Literally, “Not a Number”. For floating point data types, a bit string that does not translate
into a valid floating point number.
**Non-real-time**     - Offline operations with data input from some external storage device or
generated internal (e.g., for testing).
**Processing Pipeline**     - The series of BE functions performed on the astronomical data, i.e., that set
of functions that the data passes directly through.
**Processor**     - A physical computation device (hardware).
**Process**     - A data processing procedure (software).
**Real-time**     - Online operations with active astronomical data streaming from the Correlator.

### **1.3.2 Acronyms**

**AOC** –Array Operations Center
**CMIB**   - Correlator Monitor Interface Board
**CMCS**    - Correlator Monitor and Control System
**e2e**     - End-to-End System (archive)
**M&C**   - Monitor and Control System
**EVLA**   - The VLA Expansion Project
**RFI**    - Radio Frequency Interference
**SyRS**    - Refers to the _System Requirements_ document.
**SRS**    - Refers to the _Software Requirements Specification_ document.

## **_1.4 References_**


1) ANSI/IEEE Std 830-1998, IEEE Recommended Practice for Software Requirements
Specifications
2) ANSI/IEEE Std 1233-1996, IEEE Guide for Developing System Requirements Specifications
3) EVLA Memo No. 15, Scientific Requirements for the EVLA Real-Time System
4) EVLA Project Book
5) EVLA System Requirements (SyRS)
6) EVLA Architecture and Design
7) The Very Large Array Observing Log (J. Nieri, February 1994)
8) Refined EVLA WIDAR Correlator Architecture, NRC-EVLA Memo# 014, Brent Carlson, Oct.
2, 2001.
9) EVLA Correlator Monitor and Control System, Test Software, and Backend Software
Requirements and Design Concepts, NRC-EVLA Memo # 015, Brent Carlson, Jan. 23, 2002.

## **_1.5 Overview_**


The remainder of this document contains a more detailed description of the Correlator Backend
System as well as the requirements necessary to design and build the system. Section 2 provides a
general description of the Correlator Backend System. Section 3 details the requirements of the
product and is the core of this document.


EVLA Operations System SRS 2


The format of the document follows that outlined in the IEEE STD 830 document, IEEE
Recommended Practice for Software Requirements Specifications.


EVLA Operations System SRS 3


# **2 Overall Description**

## **_2.1 Product Perspective_**

The EVLA Correlator Backend System will be designed and implemented as a real-time data
processing system. The system is expected to be implemented on a distributed memory cluster of
connected processors. Computers in the system will all be exactly the same and operating systems
and applications running on them will communicate with one another and the Monitor and Control
System over a network. Data input to the system from the Correlator and output from it to the
End-to-End System will be over very high-speed networks. The networks connecting the internal
processors, the Correlator and the E2E are part of the BE System. Currently, only a conceptual
diagram exists for the system and should be viewed as such (see Figure 1). The BE Management
functions will run on one of the cluster processors with one or more shadow processors standing
by. The remaining processors will be running the Data Processing functions.

## **_2.2 Product Functionality_**

### **2.2.1 Data Input**

Correlator lag data will be received directly from the Correlator Baseline Boards in the form of
Lag Frames. The lag frames contain correlation lag values and all auxiliary parameters needed to
assemble the lags into complete lag sets (properly ordered time series). It is currently assumed that
all observational modes yielding correlator results that are transmitted to the Backend will be in
the form of lag frames.

Additional auxiliary data and meta-data needed for processing prior to output to the e2e System
will arrive via the Monitor and Control System, whether produced by the Correlator or some other
part of the EVLA System.

The BE will receive and act upon status requests and control commands originating in or via the
M&C System.

### **2.2.2 Data Processing**

The Correlator lag frames will be assembled into time series, normalized, and when necessary
time stamp adjusted. The time series will also be Fourier Transformed and other user selectable
time and/or frequency domain processes will be applied. Prior to output, the end results will be
formatted to meet the internal needs of the e2e.

### **2.2.3 Data Output**

Formatted spectra will be transferred to the End-to-End System. All pertinent meta-data will be
contained in the formatted output. The fundamental unit of output is the minimum sub-band crosspower spectrum produced by the Correlator. (No “stitching” operations that combine spectra from
different sub-bands will be performed.)

The BE will produce a variety of error, warning, status and other reports and messages that will be
transferred to the M&C for final disposition.


EVLA Operations System SRS 4


### **2.2.4 Monitoring**

The Correlator Backend System will conduct a number of self-monitoring activities on application
and system software as well as hardware systems to detect system failure and out of spec
conditions.

### **2.2.5 Recovery**

The ability to attempt recovery from failure and out of spec performance conditions will be built
into the system.

### **2.2.6 Control**

The system will provide control and auxiliary parameters to input, output, processing, monitor,
recovery, and other functions and receive status and performance data from them. It will also
communicate with the external Monitor and Control System.


EVLA Operations System SRS 5


|M&C System|Correlator|
|---|---|
|Backend<br>Manager<br>Data<br>Processing<br>Pipeline<br>Backend System|Backend<br>Manager<br>Data<br>Processing<br>Pipeline<br>Backend System|
|||


# e2e System

**Figure 1: Correlator Backend System Main Functional Components Diagram**

## **_2.3 User characteristics_**

All use of the Correlator Backend System will be indirect via the Monitor and Control System.
The BE system will not directly produce any user interface screens.


EVLA Operations System SRS 6


### **2.3.1 Array Operator**

The primary contact with array operations will be via status and error messages channeled through
the Monitor and Control System.

### **2.3.2 Engineers and Technicians**

The ability of the Backend System to achieve and maintain real-time processing will be vitally
dependent upon reliable operation and rapid diagnosis and repair of faults in the hardware and
software systems. These individuals will be responsible for performing corrective and preventive
maintenance along with periodic performance tests and upgrades. Engineers and technicians will
need tools to inspect individual devices from remote locations.

### **2.3.3 Astronomer/Scientist**

These individuals are primarily interested in the science that is obtained from the instrument. Their
main interaction will be to select and provide parameters for any additional data processing
beyond the Fourier transforms.

### **2.3.4 Software Developer**

These individuals are responsible for developing the software and will interact with the system to
ensure that it is functioning properly. The software developer requires remote access to the system
so that troubleshooting can be accomplished away from the EVLA and during non-working hours.

### **2.3.5 Web User**

A few authorized individuals may be allowed access to parts of the system that are usually
considered restricted.

## **_2.4 Constraints_**

### **2.4.1 Criticality of the Application**

The Correlator Backend System is a critical component in the Astronomical data path. If it is
unavailable, incoming astronomical data will be lost.

### **2.4.2 Computer Hardware Limitations**

The ultimate throughput capability of the real-time data processing pipeline of the Backend
System will be constrained by the computational performance limits of available computer
hardware and the practical ability to configure and maintain large numbers of processors.

### **2.4.3 Computer Software Limitations**

The ultimate throughput capability of the real-time data processing pipeline of the Backend
System will be constrained by the efficiency of supporting software systems, data processing code
and our ability to configure and tune them for maximum performance.
.


EVLA Operations System SRS 7


### **2.4.4 Communications Limitations**

The ability to realize and maintain real-time operations is critically dependent upon the
performance levels of available network systems.

### **2.4.5 Processing Limitations**

Operations performed shall be reversible. That is, the original raw uncorrected data must be
recoverable from the processing output.

### **2.4.6 Reliability**

The ability to maintain real-time operations over realistic extended periods of time is dependent on
the mean time to failure of the hardware and software components of the computing and
communications systems.

## **_2.5 Assumptions_**

### **2.5.1 Incoming Data Stream**

It is assumed that the Correlator will deliver suitably formatted network data packets to the input
network of the Backend System. Lag frames will not necessarily arrive in Lag Set order. All lag
frames for the same baseline will be directed to the same Backend processor. It is further assumed
that the number of lags per Lag Set will always be a power of two.

### **2.5.2 Auxiliary Data**

It is assumed that all auxiliary data needed for processing and formatting operations will be
provided directly by the correlator or indirectly by the Monitor and Control System in a timely
manner. Much of this data will originate from the Station Board CMIBS.

### **2.5.3 Outgoing Data Stream**

It is assumed that the e2e System will be capable of accepting output data rates and volumes
generated by the Backend System. Visibility data from different baselines could be processed by
different BE processors. Final assembly of all visibility data is expected to be performed by the e2e
system.


EVLA Operations System SRS 8


# **3 Specific Requirements**

## **_3.1 External Interface Requirements_**

### **3.1.1 Correlator to Backend Interface**

.

|Col1|Description|
|---|---|
|3.1.1.1|Lag Frames –_The BE shall receive LTA or Speed Dump Lag Frames from_<br>_the Correlator_. For a detailed description of the two dump formats see<br>Reference 8, pages 69 to 71. This will most likely be in the form of one or<br>more frames per UDP/IP packet|
|3.1.1.2|Transfers – The transfer shall take place in such a manner that all data<br>needed to perform any Fourier Transform shows-up on a single processor.|


### **3.1.2 Backend to/from Monitor and Control Interface**

|Req. ID|Description|
|---|---|
|3.1.2.1|State Counts –_The BE shall receive, via M&C, State Count data produced_<br>_by the Correlator._|
|3.1.2.2|Data Valid Counts -|
|3.1.2.3|Quantizer Power Measurement Data -|
|3.1.2.4|Filter Parameters -|
|3.1.2.5|Frequency Shift Parameters -|
|3.1.2.6|Windowing Parameters -|
|3.1.2.7|Observational Mode –_The BE shall receive, via M&C, data and_<br>_parameters specific to the current EVLA Observational Mode needed for_<br>_processing the Correlator Lag values_.|
|3.1.2.8|Meta-data –_The BE shall receive, via M&C, all meta-data necessary to_<br>_format BE results for delivery to the E2E_.|
|3.1.2.9|Operational Status and Control –_The BE shall provide operational status_<br>_data to and receive control data from the M&C System_. This includes Lag<br>Frame destination addresses and address changes.|
|3.1.2.10|Error and Warning –_The BE shall provide error and warning reports to_<br>_M&C as operating conditions warrant_.|
|3.1.2.11|Debug/Test Messages –_The BE shall provide several optionally selectable_<br>_levels of printed messages detailing operational parameters at critical_<br>_locations in the system_.|



EVLA Operations System SRS 9


### **3.1.3 Backend to e2e Interface**

|Req. ID|Description|
|---|---|
|3.1.3.1|Formatted Output –_The BE shall deliver formatted final results to the e2e_<br>_System_. _The BE shall produce all data needed by the e2e System for_<br>_archiving and further processing_. The output is currently expected to be in<br>a form compatible with AIPS++ Measurement Sets.|


## **_3.2 Functional Requirements_**

### **3.2.1 Information and data flows**

|Req. ID|Description|
|---|---|
|3.2.1.1|Monitor and Control System –_The BE shall acknowledge receipt of all_<br>_data received from M&C._|
|3.2.1.2|Correlator System –_The BE shall notify M&C of any detected_<br>_interruptions of data delivery from the Correlator_.|
|3.2.1.3|e2e –_The BE shall verify successful delivery of output to the e2e._|
|3.2.1.4|Internal Data –_The BE shall guarantee safe delivery of all internal_<br>_messages_.|
|3.2.1.5|Lag Frames –_The BE shall be able to handle lag frames of less than 128_<br>_values._|
|3.2.1.6|Lag Sets -_The BE shall be able to handle lag sets up to a maximum size of_<br>_262,144 values._|


### **3.2.2 Process Descriptions**

|Req. ID|Description|
|---|---|
|3.2.2.1|Data Receive –_The BE shall receive incoming data packets from the_<br>_Correlator to Backend network interface_. This network is a part of the BE<br>System.|
|3.2.2.2|Verify Receive –_The BE shall verify the successful receipt of incoming_<br>_data from the Correlator_. This includes checking for receive errors and<br>determining that all expected data was received, accumulation of error<br>statistics and comparison against tolerances, and reporting of all out of<br>tolerance conditions.|
|3.2.2.3|Input Data Management -_The BE shall store input data records in a_<br>_memory buffer and track buffer locations of all input data until data_<br>_processing is complete_. Report any buffer overflow conditions.|
|3.2.2.4|Processing Management –_The BE shall respond to incoming correlator_<br>_mode changes, user optional processing sequence and/or parameter_<br>_changes, and other external inputs that affect the data processing pipeline_. <br>Update internal parameter tables and synchronize data processing pipeline|



EVLA Operations System SRS 10


|Col1|with new operational conditions.|
|---|---|
|3.2.2.5|Time Series Assembly –_The BE shall assemble the received input data_<br>_into continuous time series (lag sets)_.|
|3.2.2.6|Data Integrity Verification –_The BE shall ensure that time series data is_<br>_correctly ordered and contains valid data values along its entire extent_. <br>Compare against tolerances and report all out of tolerance conditions.|
|3.2.2.7|Data Invalid –_The BE shall replace all invalid data with zero values_.|
|3.2.2.8|Data Invalid Count –_The BE shall keep track of data invalids_.|
|3.2.2.9|Normalization –_The BE shall be able to apply normalizations based on_<br>_reported data invalid counts_.|
|3.2.2.10|Coarse Quantization Correction -_The BE shall be able to apply_<br>_corrections based on state count and/or quantizer power measurement_<br>_data_. This is the VanVleck correction|
|3.2.2.11|Time Stamp Adjustment –_The BE shall be able to make time stamp_<br>_adjustments as required by the observational mode and correlator output_<br>_parameters_. This may arise when recirculation is used.|
|3.2.2.12|Windowing –_The BE shall be able to perform windowing operations_<br>_prior and subsequent to Fourier Transform_. This will be needed for<br>narrow band RFI mitigation. Post Fourier Transform windowing will be<br>applied as a convolution.|
|3.2.2.13|Time Domain Processing –_The BE shall be able to apply user selected_<br>_time domain processes_. These processes should be constructed to be<br>chainable (output of any time domain process can be piped to input of any<br>other, including replica of self and Fourier Transform) and repeatable in<br>the chain. No Optional time domain processes have as yet been proposed.|
|3.2.2.14|Fourier Transform Processing –_The BE shall be able to perform Fourier_<br>_Transform the lag set time series_. A power-of-two complex-to-complex<br>Fast Fourier Transform with retention of all output positive and negative<br>frequencies will be used. This process must be able to accept as input the<br>output of any of the time domain processes.|
|3.2.2.15|Frequency Domain Processing –_The BE shall be able to apply user_<br>_selected frequency domain processes_. These processes should be<br>constructed to be chainable (output of Fourier Transform and any<br>frequency domain process can be piped to input of any frequency domain<br>process including replica of self) and repeatable in the chain. No<br>frequency domain processes have as yet been proposed.|
|3.2.2.16|Integration –_The BE shall be able to sum the frequency domain, spectral_<br>_results_. The amount (time duration) of summation will be controlled by an<br>observational mode parameter obtained via M&C._The BE shall keep track_<br>_of the number of samples/dumps integrated in each spectral channel._ The<br>summation will occur after all optional frequency domain processing, or if<br>none, after the Fourier Transform. Integration for long periods of time is<br>what will throttle the output of the Correlator to a rate manageable by the<br>E2E.|
|3.2.2.17|Output Formatting –_The BE shall combine the finished spectra with meta-_<br>_and auxiliary data to form suitably formatted output data sets_. AIPS++<br>Measurement Sets are the expected entities.|
|3.2.2.18|Output Data Management –_The BE shall store formatted output data_<br>_records in a memory buffer with backup disk buffering_. Store data ready<br>for transmission to the e2e System until successful transfer has occurred.<br>Report any errors and buffer overflow conditions that occur.|
|3.2.2.19|Data Send –_The BE shall send output data to the e2e System_.|
|3.2.2.20|Send Verify –_The BE shall verify that all sent data was successfully_<br>_received_. Report all errors.|
|3.2.2.21|Monitor I/O Performance –_ The BE shall monitor data transfer rates from_|


EVLA Operations System SRS 11


|Col1|the Correlator and to the e2e. Accumulate data transfer statistics and<br>compare against tolerances. Report all out of tolerance conditions.|
|---|---|
|3.2.2.22|Monitor Compute Performance –_The BE shall monitor the overall data_<br>_processing rate_. Compare against tolerances and report all out of tolerance<br>conditions.|
|3.2.2.23|Monitor Compute Errors –_The BE shall trap, flag and repair inf’s, NaN’s,_<br>_underflows, overflows and other computation errors_. Accumulate<br>computation error statistics and compare against tolerances. Report all out<br>of tolerance conditions.|
|3.2.2.24|Monitor Processes –_The BE shall periodically or upon request check_<br>_PID’s and assure that all started tasks are alive and running_. Report<br>missing, stopped, defunct and other damaged processes.|
|3.2.2.25|Monitor Processors –_The BE shall periodically or upon request check_<br>_Backend physical processors and assure that all needed processors are_<br>_alive and responding._Report all crashed, stopped, or unresponsive<br>processors.|
|3.2.2.26|Monitor Networks –_The BE shall periodically or upon request check all_<br>_Backend internal networks and assure that all communication connections_<br>_are intact and functioning_. Report all non-functioning components.|
|3.2.2.27|Start Process –_The BE shall be able to initiate a processing task on any_<br>_Backend processor_.|
|3.2.2.28|Stop Process –_The BE shall be able to signal a kill for any Backend_<br>_process_.|
|3.2.2.29|Alter Priority –_The BE shall be able to alter the priority of any of the BE_<br>_tasks._|
|3.2.2.30|Reboot Processor –_The BE shall be able to initiate a reboot of any_<br>_Backend a physical processor_.|
|3.2.2.31|Reboot network –_The BE shall be able to initiate a reboot of any internal_<br>_network._|
|3.2.2.32|Offload –_The BE shall be able to redistribute internal workload among its_<br>_processors._This may involve change of destination IP address(es) for the<br>Correlator network.|
|3.2.2.33|General –_BE processes shall not violate archive data requirements. All_<br>_processes shall be reversible_; the raw unconverted input always being<br>recoverable from the output.|

### **3.2.3 Data Construct Specifications**

|Req. ID|Description|
|---|---|
|3.2.3.1|Input Data Queue – a memory buffer of lag frames. Data entry status<br>queue to track each record in the buffer. The lag frames will contain all<br>information necessary to properly assemble complete lag sets.|
|3.2.3.2|Output Data Queue – a memory buffer plus backup disk storage of all<br>processed spectra. These will be converted to output AIPS++<br>Measurement Set entities prior to transfer to the e2e. Data entry status<br>queue to track each record in the buffer.|
|3.2.3.3|Processing Parameters – names, position(s) in sequence, and adjustable<br>parameters for all fixed and user selectable processing pipeline<br>applications.|
|3.2.3.4|Processing flags – a table of flags needed to identify various internal<br>conditions relating to error response and processing state.|



EVLA Operations System SRS 12


|3.2.3.5|Metadata – All internally and externally generated data about the<br>processed time series and spectra including invalid data flags, processes<br>applied, coordinates, etc.|
|---|---|
|3.2.3.6<br>|Error Report – error number (translatable into text error message), error<br>source, error rates (as applicable), and time stamp.|
|3.2.3.7|Warning Report – warning number (translatable into text warning<br>message), warning source, warning rates (as applicable), and time stamp.|
|3.2.3.8|Failure Report – internal system component (e.g., disk drive, processors,<br>processes, and networks) failure number (translatable into text error<br>message) and time stamp.|
|3.2.3.9|Recovery Report – internal system component (process, processor,<br>network) recovery action result.|
|3.2.3.10|Status Report – internal system component (process, processor, network)<br>functional state.|

## **_3.3 Performance Requirements_**

### **3.3.1 General**

|3.3.1.1|Data Integrity – the Backend System shall maintain input data fidelity and<br>dynamic range across all processing, manipulation and I/O functions.|
|---|---|
|3.3.1.2|Error Handling –_the system shall be capable of flagging and marking_<br>_corrupted data segments and proceeding without interruption or effect on_<br>_other data._ This includes, but is not limited to, partial data, zero data,<br>underflows, overflows, infinities, and NaN’s whether obtained on input or<br>arising during processing.|


### **3.3.2 Hardware**

|Req. ID|Description|
|---|---|
|3.3.2.1|Input –_The BE System shall be capable of accepting an aggregate data_<br>_input stream from the Correlator of a minimum of 1.6 Gbytes/sec_. This<br>must be done simultaneously with the output stream, but not necessarily<br>over the same interconnects. This is an initial deployment specification<br>and will be increased over time.|
|3.3.2.2|Output –_The BE System shall be capable of delivering an output data_<br>_stream to the e2e System of a minimum of 25 MBytes/sec_. This includes<br>resends and simultaneous transfer of data stored due to a previous e2e<br>connection outage. This must be done simultaneously with the output<br>stream, but not necessarily over the same interconnects. This is an initial<br>deployment specification and will be increased over time.|
|3.3.2.3|CPU –_The total processor capability of the BE System shall be_<br>_(combination of numbers of processors and individual processor speed)_<br>_sufficient to accomplish all processing tasks while avoiding loss or delay_<br>_on the input and output data streams_.|
|3.3.2.4|Memory –_The BE System shall have sufficient (amount TBD) memory_<br>_with sufficient (rate TBD) access speeds to accomplish all processing_<br>_tasks while avoiding loss or delay on the input and output data streams_.|
|3.3.2.5|Excess Storage –_The BE System shall have sufficient storage (memory_<br>_and/or disk) with sufficient access speeds to meet short duration_|



EVLA Operations System SRS 13


### **3.3.3 Software**

|3.3.3.1|Applications – all math/science application software shall take optimal<br>advantage of all language, compiler, and system computational features<br>and resources to reduce run times to the minimum practical level.|
|---|---|
|3.3.3.2|Management –_all management software functions shall take optimal_<br>_advantage of all language, compiler and system features and resources to_<br>_reduce overheads to the minimum practical level_.|
|3.3.3.2|I/O –_all input and output, and storage and retrieval operations shall take_<br>_optimal advantage of all system resources to reduce overhead and latency_<br>_to the minimal practical level_.|
|3.3.3.4|Processing –_all data processing functions shall be chainable (outputs_<br>_pipeable to inputs) and repeatable in the processing pipeline in cases_<br>_where this makes computational sense_.|
|3.3.3.5|General -_Operating system, message passing and other middle-ware, and_<br>_programming language(s) used shall follow industry standards and be_<br>_commonly available and widely used. Availability of source code for the_<br>_OS will be very important._|


## **_3.4 Reliability/Availability_**

|3.4.1|Auto-correction – the Backend System shall be self-monitoring. It will be<br>capable of detecting, reporting on and automatically taking action to<br>remedy or lessen the impact of, at a minimum, the following types of<br>abnormal conditions: processor hardware failure, operating system hangs<br>or crashes, computational performance below minimum specifications,<br>computational error rates above maximum specification, internal<br>communications failures, and external (with the Correlator and E2E)<br>communications disruptions.|
|---|---|
|3.4.2|Software –_the software part of the system shall be able to perform without_<br>_total system restart due to internal failure between array maintenance_<br>_windows._|
|3.4.3|Hardware –_the hardware part of the system shall be able to perform_<br>_indefinitely without complete loss of service, except in the event of total_<br>_failure of primary and backup power_.|
|3.4.4|Correlator mode changes –_the system shall be capable of responding in a_<br>_loss-less manner to I/O and processing changes arising from Correlator_<br>mode changes.|
|3.4.5|Loss of e2e –_the system shall continue to operate in a loss-less manner in_<br>_the event of a temporary (time duration TBD) loss of availability of the_<br>_e2e System_.|
|3.4.6|Loss of Correlator –_the system shall be able to complete processing of all_<br>_onboard data, deliver the results to the End-to-End System and maintain_<br>_availability for immediate resumption of operations once Correlator_<br>_access is restored._|
|3.4.7|Loss of M&C –_the system shall continue to operate during the absence of_|



EVLA Operations System SRS 14


|Col1|the M&C System until the first encounter of unavailable critical auxiliary<br>data. The system will cache a predetermined amount (TBD) of correlator<br>data after the first encounter of unavailable critical data and complete all<br>requested operations on cached data once the unavailable critical data is<br>obtained.|
|---|---|
|3.4.8|Standby Mode –_the system shall be able to sit at idle and resume_<br>_operations with minimal (amount TBD) delay_.|

## **_3.5 Serviceability_**

|3.5.1|Hardware Accessibility – all system processing and interconnect<br>hardware shall be readily accessible for maintenance, repair, replacement<br>and/or reconfiguration.|
|---|---|
|3.5.2|Software Accessibility –_all systems and application source code shall be_<br>_available to or on the systems that execute it_.|
|3.5.3|Debugging –_all software application modules shall be debuggable._|
|3.5.4|Processes –_all software processes shall be killable, restartable,_<br>_debuggable and testable without affecting normal operations_.|


## **_3.6 Maintainability_**

|3.6.1|Software tools – software tools and pre-built applications that do not have<br>source code available shall come with a complete diagnostic package and<br>customer support.|
|---|---|
|3.6.2|Operating Systems –_operating system software shall either have source_<br>_code available or come with sufficient diagnostics and customer support_.|


## **_3.7 Scalability_**

|3.7.1|Hardware – I/O, communications, and processing hardware shall be<br>easily expandable, reconfigureable, augmentable and replaceable to meet<br>increasing data transfer and processing demands imposed by EVLA<br>science, Correlator changes, and availability of new hardware.|
|---|---|
|3.7.2|Transparency –_3.7.1, above, shall be accomplished in manner that is_<br>_transparent to processing, communications and I/O software functions_<br>_with the possible exception of recompilation of executables_.|
|3.7.3|Seamlessness –_3.7.1, above, shall be accomplished in a manner that is_<br>_seamless, in that it does not affect hardware modules or software_<br>_functionality that it meets at interfaces_.|
|3.7.4|Performance –_the Backend system shall ultimately be scaleable to an_<br>_extent that it will be capable of handling up to two Gbytes per second per_<br>_Correlator output channel in real-time_.|



EVLA Operations System SRS 15


## **_3.8 Security_**

The Backend System needs a robust security mechanism in place so that unauthorized users are
not allowed access. Authorized users are expected to be restricted to software and hardware
development, testing, maintenance and operations personnel.

All users of the Backend System must be uniquely identified. This could be done via a username
and associated password scheme that would authenticate and authorize the user access to the
system and, if applicable, grant the user access to restricted or controlled parts of the system. If a
user cannot be identified, they will not be given access. In order to monitor all past access to the
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


EVLA Operations System SRS 16


|Col1|shutdowns for maintenance, repair and/or upgrade.|
|---|---|
|3.9.2|Test Mode –_the system shall be able to handle non-real-time operations_<br>_in a transparent fashion (i.e., as if real-time)._ Note: non-real-time refers to<br>input data from a source other than the Correlator (defined as real-time).|
|3.9.3|Replaceability_–modular design principles shall be employed to the_<br>_maximum extent possible. Maximal practical use of available “hot-_<br>_swappable” devices and components shall be made_.|

## **_3.10  Documentation_**

|3.10.1|Hardware – complete and comprehensible hardware systems<br>specifications and configuration information shall be readily available.|
|---|---|
|3.10.2|Software Coding Practices–_software system and application code shall be_<br>_well documented and written in a generally familiar language or_<br>_languages (preferably not more than two)._ _Software shall be written in a_<br>_style that is easily readable and using practices that allow for minimal_<br>_confusion._|



.


EVLA Operations System SRS 17


Filename: be_srs_2.0.doc
Directory: C:\TEMP
Template: C:\WINNT\Profiles\tromero\Application
Data\Microsoft\Templates\Normal.dot
Title: EVLA Operations System
Subject:
Author: rich
Keywords:
Comments:
Creation Date: 5/10/02 4:58 PM
Change Number: 2
Last Saved On: 5/10/02 4:58 PM
Last Saved By: tromero
Total Editing Time: 2 Minutes
Last Printed On: 5/10/02 5:02 PM
As of Last Complete Printing
Number of Pages: 21
Number of Words: 5,453 (approx.)
Number of Characters: 31,086 (approx.)


