---
consensus_grade_level: 13.7
headings_per_sentence: 0.13
lists_per_sentence: 0.04
smao_sentences_pct: 0.2
vague_words_per_sentence: 0.2
anaphora_per_sentence: 0.16
sentence_cv: 1.899
cpre_terms_per_sentence: 0.71
---
### **SOFTWARE REQUIREMENTS SPECIFICATION** **FOR THE** **X-RAY TELESCOPE** **CONTROL PROCESSOR** **FOR THE** **SWIFT GAMMA RAY BURST EXPLORER**

Document No. 04121-XCPSRS-01 Rev. 2 Chg. 0

April 23, 2001


SwRI Project No. 10-04121


Prepared for


**Penn State University**

**Department of Astronomy and Astrophysics**

**University Park, PA 16802**


Prepared by


**S O U T H W E S T R E S E A R C H I N S T I T U T E**

Automation and Data Systems Division

6220 Culebra Road, San Antonio, Texas 78228-0510

(210) 684-5111                        - FAX (210) 522-5499


### **SOFTWARE REQUIREMENTS SPECIFICATION** **FOR THE** **X-RAY TELESCOPE** **CONTROL PROCESSOR** **FOR THE** **SWIFT GAMMA RAY BURST EXPLORER**

Document No. 04121-XCPSRS-01 Rev. 2 Chg. 0

April 23, 2001


SwRI Project No. 10-04121


Prepared by: ________________________ Date: _______________________

Robert Klar, SwRI Software Lead


Prepared by: ________________________ Date: _______________________
David Koller, PSU Software Lead


Approved by: ________________________ Date: _______________________

Mike McLelland, SwRI Swift Project Manager


Approved by: ________________________ Date: _______________________
David Burrows, PSU XRT Lead


Approved by: ________________________ Date: _______________________
SwRI Software Quality Assurance


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page ii



REVISION NOTICE

|Version Identifier|Date of Issue|Summary of Changes|
|---|---|---|
|WIP 11/22/00|11/22/2000|Software Peer Review Version.|
|Rev. 0 Chg. 0|2/22/2001|Software Requirements Review Version.|
|WIP 3/1/01|3/1/2001|Changes from SRR held on 2/26.|
|WIP 3/8/01|3/8/2001|Changes from SRR held on 3/7.|
|Rev. 1 Chg. 0|3/16/2001|Pre-approval baseline.|
|Rev. 1 Chg. 1|4/02/2001|Pre-approval baseline.|
|Rev. 1 Chg. 2|4/12/2001|Initial release.|
|Rev. 2 Chg. 0|4/22/2001|Deleted Formatter CSC. Removed most values from current<br>value table and deleted associated requirements as per<br>discussion with PSU on 4/20/2001.|



This document contains information that is as complete as possible. Where final numerical values or specification
references are not available, best estimates are given and noted **TBR** (To Be Reviewed). Items which are not yet
defined are noted **TBD** (To Be Determined). The following table summarizes the TBD/TBR items in this revision of
the document, and supplements the revision notice above.






|Section|Description|
|---|---|
|2.0|Some referenced document data is incomplete.|
|3.0|Some abbreviations are TBR.|
|Table 2|Some information about science data acquisition modes is TBD.|
|6|Some items in Data Dictionary are TBD/TBR.|
|Appendix A,<br>Sections 5.22, 5.23,<br>5.24, 5.26, 5.27|Requirements in these sections are TBD/TBR.  PSU input is needed.  Verification is<br>TBD.|
|||
|||
|||
|||


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page iii



TABLE OF CONTENTS

1. Scope...........................................................................................................................................................................1

1.1 System Overview..................................................................................................................................................1

2. Referenced Documents...............................................................................................................................................7

3. Abbreviations............................................................................................................................................................11

4. Overview...................................................................................................................................................................15

4.1 System Context...................................................................................................................................................15

4.2 Operational Concepts.........................................................................................................................................16

4.3 Constraints..........................................................................................................................................................28

4.4 Goals...................................................................................................................................................................28

4.5 Software Components........................................................................................................................................30

5. Context Diagrams......................................................................................................................................................35

5.1 MIL-STD-1553B Driver....................................................................................................................................35

5.2 RS-422 Driver....................................................................................................................................................35

5.3 Analog I/O Driver..............................................................................................................................................36

5.4 Built-In Tests CSC.............................................................................................................................................36

5.5 Bootstrap CSC....................................................................................................................................................37

5.6 CCD Interface CSC............................................................................................................................................37

5.7 Command and Control CSC...............................................................................................................................37

5.8 CCD Data Driver................................................................................................................................................39

5.9 Data Compression CSC......................................................................................................................................39

5.10 Error Detection and Correction CSC...............................................................................................................40

5.11 EEPROM File System CSC.............................................................................................................................40

5.12 EEPROM Interface Driver...............................................................................................................................41

5.13 Engineering Ethernet Driver............................................................................................................................42

5.14 Power Distribution Driver................................................................................................................................42

5.15 Periodic Processing CSC..................................................................................................................................42

5.16 Real-Time Operating System CSC...................................................................................................................44

5.17 SCU Interface CSC..........................................................................................................................................44

5.18 Sequencer Interface CSC..................................................................................................................................45

5.19 Time Synchronization CSC..............................................................................................................................45

5.20 Timer/Sequencer Driver...................................................................................................................................46

5.21 Tube Heater Control CSC................................................................................................................................46

5.22 Baffle Heater Control.......................................................................................................................................47

5.23 Data Collection Control CSC...........................................................................................................................47

5.24 Event Recognition Processor CSC...................................................................................................................48

5.25 (Deleted) Formatter CSC.................................................................................................................................49

5.26 Telescope Alignment Monitor CSC.................................................................................................................49

5.27 Thermo-Electric Cooler CSC...........................................................................................................................50


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page iv



6. Data Dictionary.........................................................................................................................................................51


APPENDIX A – Detailed Software Requirements.....................................................................................................A-1

APPENDIX B – EEPROM Memory Maps................................................................................................................B-1

APPENDIX C – Telecommands.................................................................................................................................C-1

APPENDIX D – CPU Throughput Calculation..........................................................................................................D-1


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page v



LIST OF FIGURES


Figure 1. XEP Block Diagram.......................................................................................................................................2

Figure 2. CCD Diagram.................................................................................................................................................3

Figure 3. Requirements Flow-Down..............................................................................................................................6

Figure 4. Flight Software Context Diagram – External Interfaces...............................................................................15

Figure 5. Flight Software Context Diagram – Hardware Module Interfaces...............................................................15

Figure 6. Observing Sequence (Part 1)........................................................................................................................17

Figure 7. Observing Sequence (Part 2)........................................................................................................................18

Figure 8. Observing Sequence (Part 3)........................................................................................................................19

Figure 9. XCP Flight Software States..........................................................................................................................21

Figure 10. Application Software Data Flow Diagram – Command.............................................................................30

Figure 11. Application Software Data Flow Diagram – Telemetry.............................................................................31

Figure 12. Application Software Data Flow Diagram – Task Control.........................................................................32

Figure 13. MIL-STD-1553B Driver Context Diagram................................................................................................35

Figure 14. RS-422 Driver Context Diagram................................................................................................................35

Figure 15. Analog I/O Driver Context Diagram..........................................................................................................36

Figure 16. Built-In Tests CSC Context Diagram.........................................................................................................37

Figure 17. Bootstrap CSC Context Diagram................................................................................................................37

Figure 18. CCD Interface CSC Context Diagram........................................................................................................37

Figure 19. Command and Control CSC Context Diagram...........................................................................................38

Figure 20. CCD Data Driver Context Diagram............................................................................................................39

Figure 21. Data Compression CSC Context Diagram..................................................................................................40

Figure 22. Error Detection and Correction CSC Context Diagram.............................................................................40

Figure 23. EEPROM File System CSC Context Diagram...........................................................................................41

Figure 24. EEPROM Interface Driver Context Diagram.............................................................................................41

Figure 25. Engineering Ethernet Driver Context Diagram..........................................................................................42

Figure 26. Power Distribution Driver Context Diagram..............................................................................................42

Figure 27.  Periodic Processing CSC Context Diagram...............................................................................................43

Figure 28. Real-Time Operating System CSC Context Diagram.................................................................................44

Figure 29. SCU Interface CSC Context Diagram........................................................................................................45

Figure 30. Sequencer Interface CSC Context Diagram................................................................................................45

Figure 31. Time Synchronization CSC Context Diagram............................................................................................46

Figure 32. Timer/Sequencer Driver Context Diagram.................................................................................................46

Figure 33. Tube Heater Control CSC Context Diagram..............................................................................................47

Figure 34. Baffle Heater Control CSC.........................................................................................................................47

Figure 35. Data Collection Control CSC Context Diagram.........................................................................................48

Figure 36. Event Recognition Processor CSC Context Diagram.................................................................................49

Figure 37. (Deleted) Formatter CSC Context Diagram...............................................................................................49


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page vi



Figure 38. Telescope Alignment Monitor CSC Context Diagram...............................................................................50

Figure 39. Thermo-Electric Cooler CSC Context Diagram.........................................................................................50


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page vii



LIST OF TABLES


Table 1. FSW States.....................................................................................................................................................22

Table 2. Science Data Acquisition Modes...................................................................................................................23

Table 3. Science Telemetry Rates for Typical 30 Minute Observation.......................................................................25

Table 4. Science Data Rates for Theoretical 24-Hour Observation.............................................................................26

Table 5. Constraints.....................................................................................................................................................28

Table 6. XCP Software Goals......................................................................................................................................28

Table 7. Data Dictionary..............................................................................................................................................51

Table 8. XCP_EEPROM Memory Map........................................................................................................................1

Table 9. SYSTEM_BLOCK Memory Map...................................................................................................................1

Table 10. SYSTEM_CONFIG_AREA Memory Map...................................................................................................1

Table 11. SYSTEM_VOLATILE_AREA Memory Map..............................................................................................2

Table 12. BIT_DATA Memory Map.............................................................................................................................2

Table 13. BIT_DRAM Memory Map............................................................................................................................3

Table 14. Telecommands...............................................................................................................................................1


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**

#### **1.SCOPE**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 1



This document defines the software requirements for the Swift X-Ray Telescope (XRT) Control Processor (XCP)
Flight Software (FSW). This document is a Level 4 specification as defined in document GSFC-410.4-SPEC-0004,
_Swift Missions Requirements Document_ .

#### 1.1System Overview


The Swift observatory is the next in a series of National Aeronautics and Space Administration (NASA) mediumclass explorer (MIDEX) satellites and is the first-of-its-kind observatory for multi-wavelength transient astronomy.
The goal of the Swift mission is to determine the origin of Gamma-Ray Bursts (GRBs) and to exploit data from these
bursts to probe the early universe.  Swift instrumentation will exploit newly discovered GRB afterglow
characteristics to make a comprehensive study of approximately 1000 bursts over its planned three-year mission.
Swift will determine the origin of GRBs, reveal how GRB blast waves interact with surroundings, and identify
different classes of bursts and associated physical processes. To accomplish these mission goals, Swift employs
three semi-autonomous science instruments. The Burst Alert Telescope (BAT) is a wide-angle x-ray telescope that
detects GRBs. On detection, the spacecraft slews in the direction of the GRB, bringing it into the view of two
narrow-field telescopes for higher-resolution multi-wavelength observation. The narrow-field telescopes are the
X-Ray Telescope (XRT), and the Ultraviolet/Optical Telescope (UVOT).

The XRT is a sensitive, autonomous X-ray Charge-Coupled Device (CCD) imaging spectrometer designed to
measure the flux, spectrum, and light curve of GRBs and afterglow over a wide dynamic range covering more than
seven orders of magnitude in flux. It will refine the BAT positions (~1-4' uncertainty) to 2.5" within 5 seconds of
target acquisition for typical bursts, allowing ground-based optical telescopes to begin immediate spectroscopic
observations of the afterglow.

The XRT will reuse some components from the following previous projects: Cosmic Unresolved Background
Instrument using CCDs (CUBIC), Imager for Magnetopause-to-Aurora Global Exploration (IMAGE), Joint
European X-Ray Telescope (JET-X), and the X-Ray Multi-Mirror (XMM) satellite.

The XRT electronics is split into two parts: the XRT Electronics Package (XEP), and the Camera Head.


1.1.1XRT Electronics Package (XEP)


The XEP is mounted on the Spacecraft (S/C) and is comprised of:

  - A VERSAmodule European (VME) enclosure with two separate Faraday shielded compartments for
separate digital and analog sections

  - A split backplane for separate digital and analog sections

  - A low voltage power supply with fixed voltage outputs

  - A Lockheed-Martin Federal Systems (LMFS) single board computer using the RAD6000 microprocessor

  - The Communication board which has a Dual Redundant MIL-STD-1553 (1553) interface, a Real Time
Clock (RTC), a Universal Asynchronous Receiver-Transmitter (UART) to interface to the Telescope
Alignment Monitor (TAM), and a CCD data buffer

  - A Relay board which has relays to control the heaters, TAM power, camera door High-Output Paraffin
(HOP) actuators, and the camera pressure relief valve HOP actuator. The Relay board also has the Digitalto-Analog Converters (DACs) for controlling the CCD voltages.

  - The Sequencer board which uses an AD21020 microprocessor to generate the CCD clock waveforms

  - The Housekeeping board that reads voltages, temperatures, and pressure.

  - The Clock board that drives the CCD’s clock and bias voltage inputs.

  - The Signal Chain board that processes the CCD’s analog video output and converts it to a digital bit stream.
The Signal Chain board is dual redundant.

  - A Thermo-Electric Cooler (TEC) power supply with a variable voltage output


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 2




  - The Engineering Units (EU) will also have an Ethernet board for software development, but the Flight Units
(FU) will not.
A one-meter maximum length cable electrically connects the XEP and Camera Head. The XRT Interface Control
Document (Pennsylvania State University [PSU] document # XRT-PSU-018) describes the interface between these
two components.













































|DDioioddee OORR|Col2|Col3|Col4|
|---|---|---|---|
|EMI<br>FILTER<br>EMI<br>FILTER|||EMI<br>FILTER<br>EMI<br>FILTER|
|5V DC/D~~C~~<br>5V DC/DC|5V DC/D~~C~~<br>5V DC/DC|5V DC/D~~C~~<br>5V DC/DC|5V DC/DC<br>5V DC/DC|
|5V DC/D~~C~~<br>5V DC/DC||||
|+/-12V<br>DC/DC<br>+/-12V<br>DC/DC|+/-12V<br>DC/DC<br>+/-12V<br>DC/DC|+/-12V<br>DC/DC<br>+/-12V<br>DC/DC|+/-12V<br>DC/DC<br>+/-12V<br>DC/DC|


**POWER**
**SUPPLY**


























































|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
||VME BUS<br>VME BUS|||||||
||VME BUS<br>VME BUS|||||||
||<br>HK DATA<br>HK START ACQ|||||||
||<br>HK DATA<br>HK START ACQ|||||||
||<br>HK DATA<br>HK START ACQ||||I|||
||<br>HK DATA<br>HK START ACQ||||TERS|||



























**Figure 1. XEP Block Diagram**


1.1.2Camera Head


The major component of the XRT's electronics is the CCD camera. The CCD camera collects science data in the
form of images, light curves, photon-counts, and spectral data. The CCD camera has three main modes of operation
and up to sixty-four modes total.

The Camera Head is mounted on the telescope tube and is comprised of a CCD and two video preamplifiers.

The CCD itself has an image section, a store section, and two readout registers with video outputs. There are four
synchronized three-phase clocks that shift the pixel rows in the image and store sections and shift the individual
pixels in the two readout registers. The Clock Sequencer in the XEP generates these clocks. Each readout register
has five guard pixels at the output side, and the readout register will not be operated in the split mode; therefore, both
readout registers will be clocked in the same direction transferring all of the pixels to one, but not both, of the video


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 3



outputs. Since the readout registers are comprised of split-pixels, the readout registers have to be clocked twice
(double-clocked) to shift out one pixel. The readout registers will be double-clocked an extra 30 times (overclocks)
to produce an output row length of 640 pixels. The clocking of an empty output register produces overclocked
pixels that are used to determine system noise information. To transfer an image from the Image Section to the Store
Section, the Image Section and Store Section three-phase clocks must be clocked simultaneously 602 times. The
Clock Sequencer can be programmed with up to 64 waveform patterns which corresponds to the 64 modes of
operation previously mentioned.


~~24 mm~~











φ R2 RD2 OS2 OD2



OS1 OD1 RD1 φ R1


1.1.3Thermo-Electric Cooler(TEC)



R φ 31 R φ 21 R φ 11 R φ 12 R φ 22 R φ 32


**Figure 2. CCD Diagram**



The CCD is cooled by a TEC. The CCD's temperature is closed-loop controlled by the FSW. Telecommands will
control the temperature setpoint, the ramp rate, and the mode — open or closed loop. A digital potentiometer with
100 wiper tap points will control the temperature setpoint. Two digital logic signals will control the wiper position:
the up/down input and the clock input.


1.1.4Power


The XRT is powered by the S/C by two 28VDC power buses. They are the Operational Power Bus (OPB) and the
Survival Power Bus (SPB). During normal operation, both buses are on. If the XRT fails to communicate to the
S/C, the S/C will turn off the XRT’s OPB, thereby deactivating the XEP. The hardware-reset function is exercised


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 4



by cycling the OPB off then back on. The SPB supplies power to heaters that prevent the XRT from being damaged
by low temperatures. The S/C may switch off the SPB, but it will only do this in an emergency condition. The OPB
is dual redundant, and the SPB is single string.


1.1.5Communications Network


The XRT communicates to the S/C via a dual redundant MIL-STD-1553B serial interface. Data transmitted to the S/
C from the XRT and commands received by the XRT from the S/C are formatted into "packets" within "frames" in
accordance with the _Swift 1553 Bus Protocol Interface Control Document_ (Spectrum Astro document # 1143-EIS19121). The BAT, UVOT, XRT, two Star Trackers, and the S/C are all networked together on the 1553 bus.


1.1.6Real Time Clock (RTC)


A local copy of the spacecraft clock is maintained and is used to timestamp the data packets, which are formatted as
Consultative Committee for Space Data Systems (CCSDS) Source Packets. To synchronize the clocks in the
instruments with the clock in the S/C the S/C provides an At-The-Tone-The-Time-Will-Be message, delivered via
the 1553 interface, and an RS422, One-Pulse-Per-Second (1PPS), hardwired signal that is the "Tone."


1.1.7Telescope Alignment Monitor (TAM)


The XRT's tube has uses a device called the Telescope Alignment Monitor (TAM) to measure the change in
mechanical alignment of the XRT's tube. The TAM consists of a point source of light that is reflected by mirrors
across the length of the telescope tube to a CCD camera. The change in the telescope's alignment is proportional to
the change in the position of the point source of light shining on the CCD's pixel array. To obtain a resolution better
than the pixel size, a centroid algorithm will be utilized. The TAM receives power from the XEP and delivers image
data through an RS-422 serial interface. The TAM power can be turned on or off by a telecommand.


1.1.8Doors and Sun Shutter


The XRT has two doors: a telescope tube door and a camera door. The telescope tube door is controlled by the S/C.
The camera door is controlled by circuitry in the XEP. Once opened, the camera door cannot be closed; therefore, it
is important that the door is not inadvertently opened.

The Sun Shutter is powered by the SPB and has its own solar panel for backup power. It is automatically opened
and closed by a photosensor but can be overridden by a telecommand.


1.1.9Heaters


The telescope tube has 36 heater groups. Each heater group is closed-loop controlled by the FSW with the
temperature set point and hysteresis controlled by a telecommand. These controllers are simple on-off type with
hysteresis.


The Mirror Baffle has three heater groups: Survival, Control 1, and Control 2. The Survival Heaters are powered
and controlled by the Spacecraft Bus.  The Control Heaters are closed-loop controlled by the FSW with a
temperature set point controlled by a telecommand. The Control Heaters will be driven by solid state relays to allow
for the numerous on-off cycles that will be required to regulate the temperature. The XRT Thermal Design
Specification (PSU document # XRT-PSU-012) describes the heaters in greater detail.


1.1.10Housekeeping


The XRT monitors several items and reports them as Housekeeping (HK) telemetry. Numbers in parenthesis
indicate how many of each housekeeping item are being monitored. The housekeeping items are:

  - CCD bias voltages (10)

  - CCD clock voltages (16)


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**


  - Miscellaneous voltages (7: analog, digital, and clock driver)

  - Circuit board temperature sensors (10)

  - Mirror temperature sensors (10)

  - Telescope tube temperature sensors (20 forward and 20 rear)

  - Contamination sensors(4: focal plane, mirror, and one unassigned)

  - Mirror baffle temperature sensors (3)

  - TEC sensors (4: voltage, current, and temperature)



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 5




  - Miscellaneous temperature sensors (5: cold finger, CCD, camera, and optical bench interface)

  - Miscellaneous sensors (6: camera door position, sun shutter position, camera vacuum pressure, and bellows
pressure)


The _XRT Data Formats_ document (PSU document # XRT-PSU-028) describes the HK formats in detail.


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 6










|Swift Science Requirements<br>Swift Science Requirements<br>GSFC-661-SWIFT-SRD<br>GSFC-661-SWIFT-RD|Col2|
|---|---|
|||












|Swift Interface<br>Swift Interface<br>Requirements Document<br>Requirements Document<br>GSFC-730-SWIFT-IRD<br>GSFC-730-SWIFT-IRD|Col2|
|---|---|
|||


|Swift Mission<br>Swift Mission<br>Requirements Document<br>Requirements Document<br>GSFC-410.4-SPEC-0004<br>GSFC-410.4-SPEC-0004|Col2|
|---|---|
|||












|XRT Requirements<br>Document<br>XRT-PSU-015|Col2|
|---|---|
|||


|MIDEX Safety, Reliability, and<br>MIDEX Safety, Reliability, and<br>Quality Assurance Requirements<br>Quality Assurance Requirement<br>GSFC-410-MIDEX-003<br>GSFC-410-MIDEX-003|Col2|
|---|---|
|||










































|XRT Requirements<br>XRT Requirements Documen<br>XDRoTc-PumSUen-0t15<br>(AllocXaRteTd- PtoS USo-0ft2w1are)<br>XXRRTT--PPSSUU--002213<br>System ICDs<br>System ICDs<br>Bus Protocol -1143-EI-S19121<br>1553 Bus - 1143-EI-S19121<br>Data Formats - XRT-PSU-028<br>XRT Interfaces - XRT-PSU-18<br>XRT Hardware ICDs<br>PSM - 04121-XEPPSMSPEC-01<br>XRXTC MHa -r d04w1a2r1e-I CXEDPsXCMSPEC-01<br>P XDRMT -C 0o4m12/M1e-XmE -P ICPDDM-0S41P2E1C-2-04100<br>T RSAMD -6 0040102 -1 L-XMEFPST-SRMSCS-PWEBC-01|XRT Requirements<br>XRT Requirements Documen<br>XDRoTc-PumSUen-0t15<br>(AllocXaRteTd- PtoS USo-0ft2w1are)<br>XXRRTT--PPSSUU--002213|Col3|
|---|---|---|
|**XRT Hardware ICDs**<br>     XRT Com/Mem - ICD-04121-2400<br>     RAD6000 - LMFS-RSC-WB<br>**XRT Hardware ICDs**<br> <br>PSM - 04121-XEPPSMSPEC-01<br>XCM - 04121-XEPXCMSPEC-01<br>PDM - 04121-XEPPDMSPEC-01<br>TSM - 04121-XEPTSMSPEC-01<br>**System ICDs**<br>     1553 Bus - 1143-EI-S19121<br>     XRT Interfaces - XRT-PSU-18<br>**System ICDs**<br>     Bus Protocol -1143-EI-S19121<br>     Data Formats - XRT-PSU-028<br>XRT Requirements Documen<br>XRT-PSU-015<br>XRT-PSU-021<br>XRT-PSU-023<br>XRT Requirements<br>Document<br>(Allocated to Software)<br>XRT-PSU-021|XRT Requirements Documen<br>XRT-PSU-015<br>XRT-PSU-021<br>XRT-PSU-023<br>XRT Requirements<br>Document<br>(Allocated to Software)<br>XRT-PSU-021||
|**XRT Hardware ICDs**<br>     XRT Com/Mem - ICD-04121-2400<br>     RAD6000 - LMFS-RSC-WB<br>**XRT Hardware ICDs**<br> <br>PSM - 04121-XEPPSMSPEC-01<br>XCM - 04121-XEPXCMSPEC-01<br>PDM - 04121-XEPPDMSPEC-01<br>TSM - 04121-XEPTSMSPEC-01|**XRT Hardware ICDs**<br>     XRT Com/Mem - ICD-04121-2400<br>     RAD6000 - LMFS-RSC-WB<br>**XRT Hardware ICDs**<br> <br>PSM - 04121-XEPPSMSPEC-01<br>XCM - 04121-XEPXCMSPEC-01<br>PDM - 04121-XEPPDMSPEC-01<br>TSM - 04121-XEPTSMSPEC-01|**XRT Hardware ICDs**<br>     XRT Com/Mem - ICD-04121-2400<br>     RAD6000 - LMFS-RSC-WB<br>**XRT Hardware ICDs**<br> <br>PSM - 04121-XEPPSMSPEC-01<br>XCM - 04121-XEPXCMSPEC-01<br>PDM - 04121-XEPPDMSPEC-01<br>TSM - 04121-XEPTSMSPEC-01|
|<br>|<br>|<br>|


|XRT Software<br>XRT Software<br>Development Plan<br>Development Plan<br>04121-XCPSDP-01<br>04121-XCPSDP-01|Col2|
|---|---|
|||


|Commercial Software Documents /<br>Swift Mission Assurance<br>Documents for ReuseSoftware<br>Requirements and Guidelines<br>Components<br>GSFC-SWIFT-410-002/003|Col2|
|---|---|
|||











**Figure 3. Requirements Flow-Down**


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**

#### **2.REFERENCED DOCUMENTS**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 7



The following documents, of the exact issue shown, were referenced as indicated during the development of this
SRS. The applicability statement associated with each document reference indicates _Superceding_ if the referenced
document supersedes this document in the event of a conflict.


Document ID: 04121-XCPSDP-01
Originator: Southwest Research Institute, San Antonio TX
Issue: Rev 2 Chg 0 (December 2000)
Title: Software Development Plan for the X-Ray Telescope Control Processor for the Swift
Gamma Ray Burst Explorer.
Applicability: Establishes and identifies this document, and describes the requirements analysis process
used to produce it.


Document ID: PAIP-00-15-3691
Originator: Southwest Research Institute, San Antonio TX
Issue: Revision 0
Title: Performance Assurance Implementation Plan (PAIP) for SwRI Project 15-03691 and
15-04121
Applicability: Provides performance assurance guidelines for the SwRI Swift DPU and XRT projects, as
derived from the Swift Mission Assurance Requirements and Swift Mission Assurance
Guidelines. _Superseding_ .


Document ID: 10-26977
Originator: Southwest Research Institute, San Antonio TX
Issue: January 2000
Title: Swift Digital Electronics Module (DEM) Chassis and Data Processing Unit (DPU)
Applicability: Is the proposal to PSU for the UVOT DPU system-level flight software. Some of these
components will be reused for XRT.


Document ID: 10-26977D
Originator: Southwest Research Institute, San Antonio TX
Issue: Revision D, August 18, 2000
Title: Swift XRT Chassis, XRT Digital Electronics, and System Software Framework
Applicability: Is the proposal to PSU for the flight software activities addressed by this SDP.


Document ID: 1143-EI-S19121
Originator: Spectrum Astro, Inc.
Issue: Rev –, 25 August 2000
Title: Swift 1553 Bus Protocol Interface Control Document.
Applicability: Specifies the instrument-generic interface between the remote terminal (RT) Instruments
and the Spacecraft from which software requirements in this document are derived.
_Superceding_ .


Document ID: 04121-XEPPDMSPEC-01
Originator: Southwest Research Institute, San Antonio TX
Issue: December 2000 (Draft 12/20/2000)
Title: Swift Specification XRT Electronics Package Power Distribution Module
Applicability: Specifies the interface to the XRT Power Distribution Module from which software
requirements in this document were derived.


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 8



Document ID: 04121-XEPPSMSPEC-01
Originator: Southwest Research Institute, San Antonio TX
Issue: Rev. 0 Chg. 0, March 2001
Title: Swift Specification XRT Electronics Package Power Supply Module
Applicability: Specifies the interface to the XRT Power Supply Module Module from which software
requirements in this document were derived.


Document ID: 04121-XEPTSMSPEC-01
Originator: Southwest Research Institute, San Antonio TX
Issue: Rev. 0 Chg. 0, March 2001
Title: Swift Specification XRT Electronics Package Timing and Sequence Module
Applicability: Specifies the interface to the XRT Timing and Sequence Module from which software
requirements in this document were derived.


Document ID: 04121-XEPXCMSPEC-01
Originator: Southwest Research Institute, San Antonio TX
Issue: Rev. 0 Chg. 0, March 2001
Title: Swift Specification XRT Electronics Package Communications Module
Applicability: Specifies the interface to the XRT Communications Module from which software
requirements in this document were derived.


Document ID: 7384-BSPS-01
Originator: Southwest Research Institute, San Antonio TX
Issue: Rev 0 Chg 0 (February 1997)
Title: Bootstrap Monitor Protocol Specification for the Space Station Furnace Facility Control
Units.
Applicability: Specifies the Bootstrap Monitor interface for the Space Station Furnace Facility (SSFF)
control units.  The SSFF Bootstrap Monitor was reused on the IMAGE Central
Instrument Data Processor (CIDP) with minimal modifications to the user interface. The
IMAGE bootstrap will be reused on the XCP with minor adjustments to accommodate
hardware address differences. Therefore, the protocol and user interfaces documented in
the referenced specification are relevant.


Document ID: 7384-SRS-01
Originator: Southwest Research Institute, San Antonio TX
Issue: Rev 0 Chg 0 (March 1997)
Title: Software Requirements Specification for the SSFF Command and Data Handling
Subsystem Control Units. The MIL-STD-1553 and Ethernet drivers are reuse code from
SSFF.
Applicability: Specifies the requirements for SSFF. A significant amount of the SSFF code will be
reused on the XCP.


Document ID: 8089-CIDPSRS-01
Originator: Southwest Research Institute, San Antonio TX
Issue: Rev 0 Chg 1 (March 1999)
Title: Software Requirements Specification for the Central Instrument Data Processor for the
Imager for Magnetopause-to-Aurora Global Exploration
Applicability: Specifies the requirements for the IMAGE CIDP. A significant amount of the IMAGE
CIDP code will be reused on the XCP.


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 9



Document ID: 9000-0013
Originator: NASA Goddard Space Flight Center, Greenbelt MD
Issue: June 1999
Title: Phase A Study Report in Response to AO-98-OSS-03
Applicability: Describes the Swift mission science goals, overall observatory design, and outlines the
high level component design and integration plans.


Document ID: GSFC-410.4-SPEC-0004
Originator: Goddard Space Flight Center, Greenbelt MD
Issue: TBD
Title: Swift Mission Requirements Document
Applicability: Defines the mission level requirements for the Swift observatory.


Document ID: GSFC-410.4-SPEC-0005 (aka GSFC-661-SWIFT-SRD)
Originator: Goddard Space Flight Center, Greenbelt MD
Issue: Version 1.0 (August 21, 2000)
Title: Swift Science Requirements Document
Applicability: Defines the Swift mission and specifies high-level requirements for the Swift observatory,
and is the Level 1 specification for Swift. _Superceding_ .


Document ID: GSFC-730-SWIFT-IRD
Originator: Goddard Space Flight Center, Greenbelt MD
Issue: Version 1.2 (April 6, 2000)
Title: Swift Interface Requirements Document
Applicability: Defines the high-level interface requirements for the Swift observatory.


Document ID: IBM-POWER-ARCH (for reference in the document only)
Originator: IBM Advanced Workstations Division, Austin TX
Issue: Version 1.53 (July 22, 1991)
Title: POWER Processor Architecture
Applicability: Contains the procedure for accessing the Rios Single Chip (RSC)-VME processor board
Real-Time Clock.


Document ID: IBM-FAULT-MGMT (for reference in the document only)
Originator: IBM Advanced Workstations Division, Austin, TX
Issue: Version 1.1 (February 3, 1992)
Title: RSC System: Fault Handling and Storage Management
Applicability: Contains a description of RSC processing unit fault handling and storage management
facilities, from which software requirements in this document are derived.


Document ID: LMFS-EMAIL-112497 (for reference in this document only)
Originator: Lockheed Martin Federal Systems, Manassas VA
Issue: November 24, 1997
Title: Email from Lockheed Martin Federal Systems (LMFS) to SwRI - “FYI: RAD6000
Diagnostic Mode”
Applicability: Contains a description of the behavior of the EDAC capability of the RAD6000 DRAM,
from which software requirements in this document are derived.


Document ID: LMFS-RSC-WB (for reference in this document only)
Originator: Lockheed Martin Federal Systems, Manassas VA
Issue: September 10, 1996
Title: RSC VME Engineering Workbook (Breadboard/EM/Flight FPGA-Based Configuration)
Applicability: Contains design details of the RAD6000 CPU Module from which software requirements
in this document are derived.


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 10



Document ID: MIL-STD-1553B
Originator: Department of Defense, Washington DC
Issue: September 21, 1978, with Notices 1 & 2
Title: MIL-STD-1553B
Applicability: Describes the MIL-STD-1553B standard referenced by software requirements within this
document.


Document ID: SED-SSP (for reference in this document only)
Originator: Southwest Research Institute, San Antonio TX
Issue: April 2000
Title: Software Engineering Department Standard Software Process
Applicability: Specifies the standard processes and procedures for software development in the Software
Engineering Department (SED) at SwRI.


Document ID: XRT-PSU-012
Originator: Penn State University, State College PA
Issue: Version 2.0, 23/09/2000
Title: XRT Thermal Design Specification
Applicability: Specifies the thermal design specification for the XRT.


Document ID: XRT-PSU-015
Originator: Penn State University, State College PA
Issue: Version 2.4, 11/28/2000
Title: XRT Requirements Document
Applicability: Specifies the science requirements for the XRT, and is the Level 3 specification for the
XRT. _Superceding_ .


Document ID: XRT-PSU-021
Originator: Penn State University, State College PA
Issue: Version 1.2, 02/10/2001
Title: XRT Software Requirements Document
Applicability: Specifies the software requirements for the XRT.


Document ID: XRT-PSU-028
Originator: Penn State University, State College PA
Issue: Version 1.1, 11/21/2000
Title: XRT Data Formats
Applicability: Specifies the data formats for the XRT.


Document ID: UTMC-SUMMIT (for reference in this document only)
Originator: United Technologies Microelectronics Center, Inc., Colorado Springs CO
Issue: 1994
Title: Summit LX/DX 1553 Product Handbook
Applicability: Describes the MIL-STD-1553B controller interface from which software requirements in
this document are derived.


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**

#### **3.ABBREVIATIONS**


µ M Micrometer
µ sec Microsecond
1553 MIL-STD-1553B Bus
1PPS One-Pulse-Per-Second
ADC Analog to Digital Converter
BAT Burst Alert Telescope
BIT Built-In Test
bps Bits/Second
CCD Charge-Coupled Device
CCSDS Consultative Committee for Space Data Systems
CIDP Central Instrument Data Processor (IMAGE)
CONT Control/Controller
COTS Commercial Off-The-Shelf
cps Counts/sec
CPU Central Processing Unit
CSC Computer Software Component
CSCI Computer Software Configuration Item
CTRL Control/Controller
CUBIC Cosmic Unresolved Background Instrument using CCDs
DAC Digital-to-Analog Converter
DC Direct Current
DC/DC DC to DC (converter)
DEM Digital Electronics Module
DMA Direct Memory Access
DPU Data Processing Unit
DRAM Dynamic Random Access Memory
DSP Digital Signal Processor
EDAC Error Detection And Correction
EEFS EEPROM File System
EEPROM Electrically Erasable Programmable Read-Only Memory
EM Engineering Model
EMI Electromagnetic Interference
EU Engineering Unit
FIFO First In First Out
FPGA Field Programmable Gate Array
FSW Flight Software
FU Flight Unit
GRB Gamma Ray Burst
GSE Ground Support Equipment
GSFC Goddard Space Flight Center



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 11


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 12



GSW Ground Software
HK Housekeeping
HOP High-Output Paraffin
I&T Integration and Test
I/O Input/Output
IBM International Business Machines
IMAGE Imager for Magnetopause-to-Aurora Global Exploration
INST Instruction
ITOS Integrated Test and Operations System
JET-X Joint European X-Ray Telescope
Kb Kilo-bits
kbps Kilo-bits/second
Kbyte 1024 bytes
KW 1024 words
LDS Large Data Structure
LMFS Lockheed Martin Federal Systems
Mars98 RAD6000 Module produced by LMFS
MB Mega-bytes
mCrabs Milli-Crabs
MIDEX Medium Class Explorer
mm Milimeter
MS-DOS Microsoft Disk Operating System
msec Millisecond
MUX Multiplexer
N/A Not Applicable
NASA National Aeronautics and Space Administration
OFP Operational Flight Program (Operating System + System Software + Applications)
OPB Operational Power Bus
PAIP Performance Assurance Implementation Plan
PDM Power Distribution Module
PID Proportional-Integral-Derivitive
PREAMP Preamplifier
PROM Programmable Read-Only Memory
PS Power Supply
PSF Point Source Frame (TBR)
PSM Power Supply Module
PSU Pennsylvania State University
PWR Power
RBI RSC Bus Interface
RSC Rios Single Chip
RT Remote Terminal (1553 term for a science instrument on the 1553 bus), real-time
RTC Real Time Clock
s Second


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**


S/C Spacecraft
SCU Spacecraft Control Unit
SDP Software Development Plan
sec Second
SED Software Engineering Department
SMOC Science Mission Operations Center
SPB Survival Power Bus
SSFF Space Station Furnace Facility
SSP Standard Software Process
SSR Solid State Recorder
SwRI Southwest Research Institute
TAM Telescope Alignment Monitor
TBD To Be Determined
TBR To Be Reviewed
TDRSS Tracking and Data Relay Satellite System
TEC Thermo-Electric Cooler
TSM Timer/Sequencer Module
UART Universal Asynchronous Receiver-Transmitter
UTC Universal Time Coordinate
UVOT Ultraviolet/Optical Telescope
V Volt(s)
VDC Volts of Direct Current
VME VERSAmodule European
XCM XRT Communications Module
XCP XRT Control Processor (RAD6000 Module)
XCP-1553 MIL-STD-1553B Bus Driver
XCP-422 RS-422 Driver
XCP-ANIO Analog I/O Driver
XCP-BHC Baffle Heater Control CSC
XCP-BIT Built-In Tests CSC
XCP-CCD CCD Interface CSC
XCP-CCM Command and Control CSC
XCP-CDD CCD Data Driver
XCP-DCC Data Collection Control CSC
XCP-EDAC Error Detection And Correction CSC
XCP-EEFS EEPROM File System CSC
XCP-EEPRM EEPROM Interface Driver
XCP-ENET Engineering Ethernet Driver
XCP-ERP Event Recognition Processor CSC
XCP-PDD Power Distribution Driver
XCP-PP Periodic Processing CSC
XCP-RTOS Real-Time Operating System CSC
XCP-SCUI Spacecraft Control Unit Interface CSC



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 13


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**


XCP-SEQ Sequencer Interface CSC
XCP-TAM Telescope Alignment Monitor CSC
XCP-TEC Thermo-electric Cooler CSC
XCP-THC Tube Heater Control CSC
XCP-TIS Time Synchronization CSC
XCP-TSD Timer/Sequencer Driver
XEP XRT Electronics Package
XMM X-Ray Multi-Mirror
XRT X-Ray Telescope



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 14


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**

#### **4.OVERVIEW**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 15



This section provides an overview of the FSW including a system context, operational concepts, goals and
constraints, and a list of the computer software components (CSCs) which comprise the FSW. Detailed functional,
performance, error recovery, and interface requirements for the identified CSCs are provided in Appendix A.

#### 4.1System Context


From a system (observatory) perspective, the FSW interfaces with the Spacecraft Control Unit (SCU) via the MILSTD-1553B bus and the one pulse per second (1PPS) interface. The interfaces of the FSW in this context are
illustrated in the following figure.









**Figure 4. Flight Software Context Diagram – External Interfaces**


From a XCP hardware interface perspective, the FSW executes on the XCP, stores and retrieves data from XCP
Electrically Erasable Programmable Read Only Memory (EEPROM), and communicates with the Spacecraft using
the MIL-STD-1553B Bus.  The MIL-STD-1553B and Camera Head Interfaces are contained on the XRT
Communications Module (XCM). The interfaces of the FSW in this context are illustrated in the following figure.









XCP_MEM_ERR)





Interrupt
~~(XCM_1553,~~
XCM_CCD_FIFO,

XCM_HK_FIFO,

XCM_422_RX,

XCM_422_TX)





**Figure 5. Flight Software Context Diagram – Hardware Module Interfaces**


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**

#### 4.2Operational Concepts



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 16



The following sections describe the operational concepts of the FSW, including its functions, interfaces, performance
characteristics, error detection, reporting and recovery mechanisms, and ground systems concepts.


4.2.1Functions


The FSW has the following primary functions:

- Process science data from the camera and relay it to the Spacecraft Control Unit (SCU) in the form of CCSDS
Source Packets.

- Receive commands from the SCU that establish the current instrument state and camera mode.

- Transmit detailed housekeeping data to the SCU in the form of CCSDS Source Packets.

- Receive a time message from the SCU and synchronize the XCP local copy of the spacecraft clock.

- Control the heaters on the telescope tube and on the thermal baffles.

- Read the TAM.


4.2.2Observation Sequence


The XRT supports three different, but very similar, observation sequences. The three observation types are:


- Automatic

- Preplanned

- Target of Opportunity


Figure 6 and Figure 7 show a detailed flowchart for the observation types. The sequence shown in the figures
assumes the software is in automatic mode and not presently engaged in performing an observation. The sequence
starts when a SISCATTITUDE message is received with the IS_SETTLED indication set to _false_ . The message also
indicates IS_IN_10_ARCMIN, which is _true_ when the S/C is within ten arc minutes of the target position. When the
distance remaining to slew is greater than ten arc minutes, the S/C begins the first of up to three activities that
precede an observation. Each activity is initiated when the distance remaining is greater than ten arc minutes and the
previous activity is complete. The pre-observation activities are:


- Calculate row bias map

- Calculate image bias map

- Collect raw data image


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 17



Swift XRT Observing Sequence Flow Diagram










|While IS_SETTLED<br>= FALSE<br>Take Bias Rows<br>(windowed timing<br>mode)|Col2|
|---|---|
|||










|IS_IN_<br>TEN_ARCMIN<br>Yes<br>Flag = TRUE<br>?<br>No|Col2|Col3|
|---|---|---|
|Yes<br>No<br>IS_IN_<br>TEN_ARCMIN<br>Flag = TRUE<br>?|While IS_SETTLED<br>= FALSE<br>Take Bias Map<br>Frames (high gain,<br>2.56 second<br>exposure)|While IS_SETTLED<br>= FALSE<br>Take Bias Map<br>Frames (high gain,<br>2.56 second<br>exposure)|
|Yes<br>No<br>IS_IN_<br>TEN_ARCMIN<br>Flag = TRUE<br>?|||













































**Figure 6. Observing Sequence (Part 1)**


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 18


|D|Col2|
|---|---|
|||




























|IS_AT_TARGET is a sub-field flag of the<br>FO_NEXTOBS_INFO message from the FoM.<br>No IS_AT_TARGET<br>"IS_AT_TARGET = Yes" means that this is the<br>first observance of an Automated Target (AT).<br>Yes T=0<br>Take Image Frame<br>(low gain, 0.1 second<br>exposure)<br>While IS_SETTLED<br>= TRUE<br>Begin Photo-Diode<br>Take Image Frame<br>Mode<br>(low gain, 2.56<br>second exposure)<br>T=2.66s<br>IS_SETTLED End<br>No<br>Flag = TRUE? Observation<br>Yes No<br>Accumulate images<br>Detectable Accumulation<br>No in memory and filter<br>Source? Time > 30s<br>out cosmic rays<br>Yes (> 20 mCrabs) Yes<br>While IS_SETTLED<br>= TRUE<br>Centroid on Source<br>and Determine<br>Intensity<br>T=5s<br>IS_SETTLED End<br>No<br>Flag = TRUE? Observation<br>Yes<br>Send XRT Send XRT<br>Standard Send XRT<br>Centroiding Error Centroiding Error<br>No Deviation of PSF Yes Position Message<br>(source confusion) (no source found)<br>Okay? to TDRSS & UVOT<br>to TDRSS & UVOT to TDRSS & UVOT|Col2|Col3|
|---|---|---|
|Begin Photo-Diode<br>Mode|Begin Photo-Diode<br>Mode|Begin Photo-Diode<br>Mode|
||||
||Send XRT<br>Centroiding Error<br>(no source found)<br>to TDRSS & UVOT|Send XRT<br>Centroiding Error<br>(no source found)<br>to TDRSS & UVOT|
||Send XRT<br>Centroiding Error<br>(no source found)<br>to TDRSS & UVOT||





**Figure 7. Observing Sequence (Part 2)**


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 19































Version 1.5
PMA 03/14/01


**Figure 8. Observing Sequence (Part 3)**


The row bias map is maintained by the system so that it does not have to be recalculated prior to each observation;
however, recalculation is preferred to provide the best results. One frame is acquired for the row bias map. Once the
frame has been acquired, the software recalculates and stores the updated row bias map. Next, the software
recalculates the image bias map, if more than ten arc minutes remain to the target location. The software accumulates
3-6 frames for the recalculation of the row bias map. Otherwise, the existing image bias map is reused. Finally, if the
acquire raw data image flag is true and the distance to the target location is more than ten arc minutes, then the
software acquires a single raw data image which is saved for later download to the ground.


At this point, the S/C has come to within ten arc minutes of the target or the observation preliminary activities are
complete, and the software switches to the fast timing mode. When the SISCATTITUDE message indicates that the
S/C is settled, the software starts the main portion of the observation sequence.


The software now acquires a frame of data and begins counting the pixels above a detection threshold. To be
considered of interest, this count of pixels must exceed a programmable threshold. If the count does not exceed the
threshold, then another image is acquired and summed with the first image. This new image is subjected to the pixel
count. This process continues until the count threshold is met or the timeout period is exceeded. If the timeout is
exceeded, an “XRT Centroid Error” message is transmitted to UVOT and to the ground (via TDRSS). Otherwise,


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 20



when the source is detected, the software performs a centroid calculation on the image. If the centroid calculation
fails, an “XRT Centroid Error” message is sent; otherwise, an “XRT Position” message is sent.


Next, the software enters the fast timing mode. In this mode, the CCD reports a single value representing the entire
image. The CCD reports one pixel every 16 µ sec, or approximately 60,000 pixels/sec. The software remains in this
mode while the lit pixel rate exceeds 40 cps. Once the count falls below 40 cps, the software switches to normal
timing mode. In this mode, the CCD reports one row every 5 msec. Each row report sums up the CCD columns.
This method is used until the rate drops below 2 cps. At this point, the software switches to photon counting mode.
In this mode, the entire image is collected and scanned for lit pixels. The update rate is approximately once every
2.5 sec. The observation sequence ends when the target is occulted and the S/C slews to a new target.


Preplanned observations differ from automatic ones in that the “XRT Position” message is not used. Processing is
otherwise similar.  The target of opportunity observations are treated like preplanned observations from an
operational point of view of the software.


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 21



The FSW has the following states: Off, Boot, Init, Manual, Red, and Auto. The following diagram illustrates these
states and their transitions.

# **SWIFT XRT STATE TRANSITIONS**










|Col1|After<br>Com<br>Com<br>has O|
|---|---|
|**RED**|**RED**|



**Unpowered**


**EEPROM** **RAM**



Commanded Transitions


Autonomous Transitions


Preferred Spacecraft-Controlled Transitions


**Figure 9. XCP Flight Software States**



Note, the state diagram indicates that the S/C can only switch off the XRT's power when the XRT is in the Boot, Init,
or Manual state. This is the preferred mode of operation and can only be accomplished if the S/C first sends a
"Safehold Notification" message to the XRT. In a time critical emergency condition the S/C will turn off the power
to the XRT regardless of what state it is in.


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 22



The following table describes the XCP states and, for each mode, indicates whether the FSW is commandable,
whether the FSW produces any telemetry, and whether or not detector events are processed.














|Table 1. FSW States|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**State**|**Entered On**|**Description**|**Command**|**Telemetry**|**CCD Data**|
|OFF|Power Off|Unpowered electronics|No|No|None|
|BOOT|Power Up, or<br>Watchdog<br>Reset|Bootstrap software executes, performs<br>Built-In Test (BIT) Stage 1, and then starts<br>the flight program|No|No|None|
|INIT|Automatically<br>from BOOT|Check CCD voltages, perform Built-In<br>Test Stage 2, transition to MANUAL or<br>IDLE|No|Startup<br>Packet|None|
|AUTO|Commanded<br>from IDLE, or<br>MANUAL|Automatically calculate a bias map and a<br>mean-row map each time the state is<br>entered,  follow observation sequence|Yes|Yes|Processed|
|MANUAL|Automatically<br>from INIT if<br>CCD voltages<br>are not correct<br>Automatically<br>from RED after<br>execution of a<br>command,<br>Commanded<br>from IDLE,<br>AUTO, or RED|CCD is unpowered if state was entered<br>from INIT.  CCD is powered if state was<br>entered from IDLE, AUTO, or RED.<br>Commands must be sent to put XRT into<br>different observation modes and produce<br>telemetry.|Yes|Yes|May be<br>processed|
|RED|Commanded<br>from MANUAL|Returns to MANUAL mode after execution<br>of RED command.  If a command is<br>received in this state that is not a RED<br>command, the command will be rejected<br>and the state will transition to MANUAL.|Yes|HK only|Discarded|



XCP has multiple modes. These modes are detailed in Table 2.


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 23


|Table 2. Science Data Acquisition Modes|Col2|Col3|Col4|
|---|---|---|---|
|**Mode and Description**|**Entered On**|**Setup**|**Activities and**<br>**Data Products**|
|Bias Image Calculation<br>The purpose of the Bias<br>Calculation is to establish a map<br>which contains a bias for every<br>CCD pixel will be subtracted from<br>every image.<br>Perform bias calculation on<br>command– collect a N “dark”<br>frames (5-10 frames), samples<br>what CCDs look like with “no<br>events” to establish bias map –<br>contains a bias for every pixel.<br>This will get subtracted from every<br>frame created.  Looking for the<br>number of times you see an event<br>with a given amplitude.  Get a<br>graph and analyze it in software.<br>Algorithm is smart enough to<br>ignore the x-rays, so don’t care if<br>door is open or closed.  Will have<br>at least three bias algorithms on<br>ground – select which algorithm on<br>ground command. Send full frame<br>to ground also so can check the<br>bias.||||
|Bias Row Calculation<br>The purpose of the Bias Row<br>Calculation is to establish a map<br>which contains a bias for every<br>CCD column which  will be<br>subtracted from every row in<br>Normal Timing Mode.<br>Perform bias calculation on<br>command– collect a N “dark” rows<br>(5-10 rows), samples what CCDs<br>look like with “no events” to<br>establish bias row – contains a<br>bias for every column.  This will get<br>subtracted from every row created<br>in Normal Timing Mode.  Looking<br>for the number of times you see an<br>event with a given amplitude.  Get<br>a graph and analyze it in software.<br>Algorithm is smart enough to<br>ignore the x-rays, so don’t care if<br>door is open or closed.  Will have<br>at least three bias algorithms on<br>ground – select which algorithm on<br>ground command. Send full row to<br>ground also so can check the bias.||||


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**











04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 24


|Table 2. Science Data Acquisition Modes|Col2|Col3|Col4|
|---|---|---|---|
|**Mode and Description**|**Entered On**|**Setup**|**Activities and**<br>**Data Products**|
|Image<br>The purpose of Image Mode is to<br>centroid on the source, and to<br>create an image until the count rate<br>drops below 8500 counts per<br>second.  Provides photometry and<br>position for <26x Crabs.|On receipt of slew settle,<br>or<br>Observation of target with<br>count rate greater than<br>8500 cps, or<br>Ground command|Read out prior mode<br>data<br>Select and download<br>sequencer program<br>Verify DAC setup|Acquire single frame, locate<br>source, centroid, produce<br>**XRT Position Message** to<br>UVOT and TDRSS (new<br>burst)<br>Create**Postage Stamp**<br>**Report** and transmit via<br>TDRSS within 1200<br>seconds of burst alert<br>Collect and transmit<br>**Postage Stamp Image**<br>**Report** to spacecraft|
|Photo-Diode Mode (Fast Timing)<br>The purpose of Photo-Diode Mode<br>is to measure the rate of burst<br>decay at a much higher rate (0.5<br>msec) by collapsing the entire CCD<br>into a single pixel.  Provides<br>lightcurve and intensity spectrum<br>for source fluxes between 40<br>mCrabs and 8.5 Crabs.|On receipt of Slew Start, or<br>Observation of target with<br>count rate between 40 and<br>8500 cps, or<br>Ground Command|Read out prior mode<br>data<br>Select and download<br>sequencer program<br>Verify DAC setup|Acquire and accumulate<br>timing mode pixels.<br>Produce**Fast Timing**<br>**Frame Report** and transmit<br>to spacecraft.|
|Windowed Timing (Slow Timing)<br>The purpose of Windowed Timing<br>Mode is to measure the rate of<br>burst decay at a much higher rate<br>(5 msec) by collapsing the entire<br>CCD into a single row.  Provides<br>lightcurve and intensity spectrum<br>for source fluxes between 2 and 40<br>mCrabs.|Observation of target with<br>count rate between 2 and<br>40 cps, or<br>Ground Command|Read out prior mode<br>data<br>Select and download<br>sequencer program<br>Verify DAC setup|Histogram timing mode<br>pixels for TBD seconds,<br>produce**Spectrum Report**, <br>and transmit to TDRSS<br>within 1200 second of new<br>burst.<br>Acquire and accumulate<br>timing mode pixels.<br>Produce**Normal Timing**<br>**Frame Report** and transmit<br>to spacecraft.|
|Photon Counting<br>The purpose of Photon Counting<br>Mode is to provide energy and<br>position of individual photons.<br>Each event represents nine pixels.|Observation of target with<br>count rate less than 2 cps,<br>or<br>Ground command|Read out prior mode<br>data<br>Select and download<br>sequencer program<br>Verify DAC setup|Execute event recognition<br>algorithm on successive<br>five-row event sets.<br>Produce**Event List Report**<br>and transmit to spacecraft.|
|Null<br>The purpose of Null Mode is to<br>clock the CCD with a selected<br>sequencer program without<br>producing an output.  This mode<br>can be used to continuously clock<br>the CCD to sweep out charge when<br>data is not being collected.|Clocking of CCD during<br>TEC cool-down,<br>Observation of target when<br>in the SAA, or<br>Ground command|Read out prior mode<br>data<br>Select and download<br>sequencer program<br>Verify DAC setup|No report.|
|Raw Data<br>The purpose of the Raw Data<br>Mode is to provide a complete<br>unprocessed CCD image for<br>diagnostic purposes.|Ground Command|Read out prior mode<br>data<br>Select and download<br>sequencer program<br>Verify DAC setup|Should include a parameter<br>to send every Nth frame.<br>Produce**Raw Frame**<br>**Report** and transmit to<br>spacecraft.|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 25






|Table 2. Science Data Acquisition Modes|Col2|Col3|Col4|
|---|---|---|---|
|**Mode and Description**|**Entered On**|**Setup**|**Activities and**<br>**Data Products**|
|Ramp DACs<br>The purpose of the Ramp DACs<br>Mode is to continuously ramp the<br>CCD bias voltages through all<br>possible values.|RED Ground Command||No report.<br>Used only during<br>Integration and Test to<br>verify CCD bias voltage<br>circuitry before installing<br>CCD.  Real-time telemetry<br>(strip chart mode) is used to<br>check this data.|



4.2.3Interfaces and Performance


Estimates of the maximum amount of memory required to buffer an observation were computed according to the
following analyses.

Table 3 shows the science telemetry data rates expected for a burst whose x-ray emission has dropped below about 3
Crabs within 30 seconds. Since in this case it is assumed that it takes the S/C 50 seconds to slew to the source, the
flux is already at or below 4000 cps by the time the S/C has slewed to the target and generated an XRT Position and
an XRT image report. At this flux, the XRT is generating science telemetry at a rate of just over 100kbps, but only
for about 50 seconds. Within 30 minutes, the maximum length of an observation before the target is occulted, the
data rate has dropped to less than 700bps. During such an observation the XRT would generate about 2.7MB of
data, for an average rate of about 12kbps.
























|Table 3. Science Telemetry Rates for Typical 30 Minute Observation|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Time Since Burst (sec)**|**Time Since Burst (sec)**|**Time Since Slew Settle**<br>**(sec) ***|**Time Since Slew Settle**<br>**(sec) ***|**Duration**|**Flux**<br>**(cps)**|**Report**|**Bytes**<br>**per**<br>**Report**|**Number**<br>**of**<br>**Reports**|**Total Bytes**|**Total Bytes**|**Bits per**<br>**Second**|
|**Start**|**Stop**|**Start**|**Stop**|||||||||
|50|55|0|5|5|N/A|XRT Position|960|1|960|1536|1536|
|55|56|5|6|1|N/A|XRT Image|5760|1|5760|46080|46080|
|56|100|6|50|44|3000|Fast Timing|1050|528|554400|100800|100800|
|100|300|50|250|200|1000|Fast Timing|1050|800|840000|33600|33600|
|300|1000|250|950|700|300|Fast Timing|1050|840|882000|10080|10080|
|1000|1150|950|1100|150|100|Fast Timing|1050|60|63000|3360|3360|
|1050|1150|1000|1100|100|N/A|XRT<br>Spectrum|2880|1|2880|230.4|230.4|
|1150|1850|1100|1800|700|100|Fast Timing|1050|280|294000|3360|3360|
|||||||||||||
|||0|1800|1800|N/A|30 min<br>Automated<br>Observation|||2643000|11747|11747|
|||||||||||||
|Assume time duration of slew is 50 sec.|Assume time duration of slew is 50 sec.|Assume time duration of slew is 50 sec.|Assume time duration of slew is 50 sec.|Assume time duration of slew is 50 sec.|Assume time duration of slew is 50 sec.|Assume time duration of slew is 50 sec.||||||



Table 4 shows the expected data that would be generated by the XRT if it could observe the burst described above
for 24 continuous hours. Of course, the XRT cannot observe the burst for more than 30 minutes per orbit. However,


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 26



whatever time it was not observing the burst, it would be observing the afterglows of bursts a day or more old, at
expected data rates of less than 700bps, or about the minimum data rate of the continuous observation of the new
burst. Hence, the data rate of the continuous, 24-hour observation of a new burst represents the maximum data rate
expected for the XRT. Under this scenario, the XRT would generate about 10MB of data per day, for an average
rate of about 1kbps, which is well within the 3.9kbps average rate allocated to the XRT for science telemetry.
Hence, under these conditions, if the amount of memory allocated for observation buffers exceeds 10MB, the XRT
should easily be able to meet its allocated science telemetry rate.
























|Table 4. Science Data Rates for Theoretical 24-Hour Observation|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Time Since Burst (sec)**|**Time Since Burst (sec)**|**Time Since Slew Settle**<br>**(sec) ***|**Time Since Slew Settle**<br>**(sec) ***|**Duration**|**Flux**<br>**(cps)**|**Report**|**Bytes**<br>**per**<br>**Report**|**Number**<br>**of**<br>**Reports**|**Total Bytes**|**Bits per**<br>**Second**|
|**Start**|**Stop**|**Start**|**Stop**||||||||
|50|55|0|5|5|N/A|XRT Position|960|1|960|1536|
|55|56|5|6|1|N/A|XRT Image|5760|1|5760|46080|
|56|100|6|50|44|3000|Fast Timing|1050|528|554400|10080<br>0|
|100|300|50|250|200|1000|Fast Timing|1050|800|840000|33600|
|300|1000|250|950|700|300|Fast Timing|1050|840|882000|10080|
|1000|1150|950|1100|150|100|Fast Timing|1050|60|63000|3360|
|1050|1150|1000|1100|100|N/A|XRT<br>Spectrum|2880|1|2880|230.4|
|1150|3000|1100|2950|1850|100|Fast Timing|1050|740|777000|3360|
|3000|10000|2950|9950|7000|30|Slow Timing|360|2800|1008000|1152|
|10000|30000|9950|29950|20000|10|Slow Timing|160|8000|1280000|512|
|30000|86450|29950|86400|56450|3|Photon<br>Counting|210|22580|4741800|672|
||||||||||||
|||0|86400|86400|N/A|24 Hour<br>Automated<br>Observation|||10155800|940.4|
||||||||||||
|Assume time duration of slew is 50 sec.|Assume time duration of slew is 50 sec.|Assume time duration of slew is 50 sec.|Assume time duration of slew is 50 sec.|Assume time duration of slew is 50 sec.|Assume time duration of slew is 50 sec.|Assume time duration of slew is 50 sec.|||||



Estimates for Central Processing Unit (CPU) margin are computed in Appendix D.


4.2.4Error Detection, Reporting and Recovery


The following sections summarize the error handling, reporting and recovery mechanisms of the XCP.


4.2.4.1Software Configuration Integrity


The XCP maintains primary and alternate FSW configurations in EEPROM. The primary FSW configuration in
EEPROM is software locked to be read-only. The primary FSW provides MIL-STD-1553B communications with
the SCU provided there are no failures. The XCP bootstrap software autonomously switches to the alternate FSW
configuration in the event the primary configuration fails to boot.

Problems with the FSW that are identified on-orbit can be corrected by patch or by a complete software reload. The
FSW contains an EEPROM-resident file system on which an object file containing a software patch can be loaded.
This object file can then be dynamically loaded and linked into the active FSW. Alternatively, a complete software


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 27



build can be loaded to the alternate FSW location in EEPROM and the XCP commanded to boot the alternate
configuration rather than the primary.


4.2.4.2Memory Error Detection and Correction


The processor board includes the EEPROM that holds the FSW, including the bootstrap and EEPROM File System
(EEFS), and the Dynamic Random Access Memory (DRAM) that is used for program and data memory. The
EEPROM includes a section that contains the bootstrap. This section of the EEPROM is software write locked prior
to flight and includes a checksum that is compared against the stored data as part of the Built-In Tests (BIT) that are
executed on system startup. The DRAM includes Error Detecting and Correcting (EDAC) memory. This facility
stores redundant information in parallel with each memory word. Whenever a memory word is read, the EDAC is
checked. The EDAC can detect and correct single bit errors. The EDAC can detect double bit errors. Both events
cause an interrupt, and the software logs information about the error including the affected address and incrementing
the EDAC error count. Multiple bit errors (two or more) cause the software to reset the processor by discontinuing
strobing of the watchdog timer, which causes the watchdog timer to reset the board when it times out.


A low priority software task called the Memory Scrubber runs when no other tasks are executing. This task steps
through DRAM and reads each location. When a word is read that contains a single-bit error, this routine rewrites it
to correct the problem, and the problem is logged to EEPROM through the interrupt mechanism. The scrubbing
process seeks to repair single bit errors before they become uncorrectable multiple bit errors. Multiple bit errors
uncovered by the scrubber result in a reset, even if the memory was not currently in use for processing by the FSW.


4.2.4.3Error Reporting


Errors are reported in XCP housekeeping telemetry. If an unrecoverable error occurs (such as an uncorrectable
memory error), the XCP will reboot via watchdog timer. Detectable exceptions that cause a watchdog reboot are
recorded to EEPROM.


4.2.4.4Keep Alive Messaging


A heartbeat message from XRT to the SCU serves to indicate “aliveness” of the XRT Instrument to the Spacecraft.


4.2.5Ground Systems


Ground systems are required for the following purposes:

  - Low-level driver integration and testing,

  - XCP process integration and verification testing,

  - Control and monitoring of XRT on orbit, and

  - Operational display of downlinked data.

Low-level driver integration and testing is accomplished using a XCP-resident test application which exercises the
hardware interfaces via actual flight software drivers. A Ground Support Equipment (GSE)-resident application
communicates with the XCP-resident test application over an RS-232 port which is unused on flight. The GSEresident application commands the XCP-resident application to output or receive data on a particular hardware
interface. The GSE has a direct connection to each hardware interface, and stimulates or measures the interface in
accordance with the command sent to the XCP. Because the RS-232 port is not used on flight, each interface can be
tested without interfering with the command-and-response communication between the XCP and GSE resident
applications.

Simulators are used to facilitate integration and verification of the FSW. To contain costs and smooth integration,
the external interfaces to the simulators used for integration testing and verification of the FSW are the same as the
ground system interfaces in the Science Mission Operations Center (SMOC).  This approach allows, at the


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 28



conceptual level, software and displays built for the display of data during simulated tests, to be reused for the
operational display of downlinked data without modification.

#### 4.3Constraints


Certain constraints are imposed upon the specification and design of the FSW and are derived from upper-level
specifications and known system design constraints. These constraints are listed in Table 5, along with the
implications of the constraint.



|Table 5. Constraints|Col2|Col3|Col4|
|---|---|---|---|
|**#**|**Constraint**|**Implication(s)**|**Source**|
|**C1**|The TDRSS downlink bandwidth is limited<br>to 1 kbps for the S/C.|This limits the rate at which housekeeping will be<br>produced.|Document<br>GSFC-410.4-<br>SPEC-0004, Table<br>EB-1.|
|**C2**|Malindi ground contacts are limited to<br>about 7 ground contacts per day (or less)<br>of 7-10 minutes each. This is based on a<br>96-minute orbital period.|The design of the FSW must avoid any time-<br>consuming setup or configuration as part of its<br>nominal operation. This may also have implications<br>for the way in which large software loads are<br>structured.|Document 9000-0013,<br>Section 3.6.6.2.|
|**C3**|The interface with the S/C provides that<br>real-time HK packets be limited to 230<br>bytes or less. Instrument HK is placed<br>into the last 230 bytes of the regular S/C<br>RT HK frame.|The FSW design must structure its HK packets such<br>that the 230-byte constraint is not violated. In<br>addition, the HK rate should be optimized to help<br>ensure that a HK packet can reasonably appear in<br>the S/C frame at an acceptable rate. It is not clear<br>whether this also has implication to memory dumps.<br>The FSW may have to provide for small dump<br>packets if going down the RT link, and larger ones if<br>going to the Solid State Recorder (SSR).|Document 1143-EI-<br>S19121, section 4.8.3.|
|**C4**|The S/C does not reassemble segmented<br>packets and the Integrated Test and<br>Operations System (ITOS) ground system<br>is not currently capable of reassembling<br>segmented packets.|Any packet that must be processed by ITOS should<br>not be segmented. Based on a meeting with Mike<br>Rackley on 08/30/00, ITOS will be upgraded to<br>reassemble packets, but it is not yet known when<br>this capability will be implemented. This may also<br>have impact on memory dump packets.|Document 1143-EI-<br>S19121, section 4.8.<br>Meeting with Mike<br>Rackley of GSFC on<br>08/30/00.|
|**C5**|The ITOS ground system will not be<br>capable of decompressing packets.|The FSW cannot compress any packet that must be<br>recognized and processed by ITOS.|Meeting with Mike<br>Rackley of GSFC on<br>08/30/00.|

#### 4.4Goals







Table 6 presents goals that serve to guide the specification, design, and development of the software.  These goals
should contribute to the simplicity (S), reliability (Rl), maintainability (M), reusability (Ru), and testability (T) of the
system.






|Table 6. XCP Software Goals|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Goal**|**Goal**|**S**|**Rl**|**M**|**Ru**|**T**|
|**G1**|Maintain simple, consistent data flow interfaces between the FSW and<br>its external interfaces.|X||||X|
|**G2**|Produce a design that requires as little a priori knowledge of the<br>internal operations of the SCU as possible.|X||X||X|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 29
















|Table 6. XCP Software Goals|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Goal**|**Goal**|**S**|**Rl**|**M**|**Ru**|**T**|
|**G3**|Produce modular, project-generic designs and code to maximize<br>reusability on other system components and on future projects.  This<br>should be done in such a way as to minimize modifications required as<br>a result of project or component-specific design, coding, comments, or<br>naming conventions.|||X|X||
|**G4**|Produce a design which provides for upgrade and maintenance|||X|||
|**G5**|Produce a flexible design that includes the mechanisms needed to<br>support ground Integration and Test (I&T) and provide for off-nominal<br>configurations in flight.||X|||X|
|**G6**|Produce a design that benefits from the reuse of software components<br>from the SSFF, IMAGE, and CUBIC projects.||||X||
|**G7**|Produce error-free code.||X||||
|**G8**|Minimize the amount of re-work necessary at each level of integration.||X||X|X|
|**G9**|Produce a design that is reasonably fault-tolerant.||X||||


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**

#### 4.5Software Components



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 30



The Software Development Plan for the XCP lists and identifies the computer software configuration items (CSCIs)
for the FSW and ground software. The following sections describe these CSCIs and their components. The
following figures illustrate the overall data flows among the application-level CSCs.



























































































**Figure 10. Application Software Data Flow Diagram – Command**


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 31





































































**Figure 11. Application Software Data Flow Diagram – Telemetry**


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 32





























































**Figure 12. Application Software Data Flow Diagram – Task Control**


4.5.1System and Framework Flight Software


This section lists and describes the computer software components (CSCs) of the System and Application
Framework Flight Software. This software will be developed at SwRI.

The MIL-STD-1553B Driver, identified XCP-1553, provides an application interface to the MIL-STD-1553B data
bus hardware on the XCM.

The RS-422 Driver, identified XCP-422, provides an application interface to the RS-422 interface on the XCM.

The Analog I/O Driver, identified XCP-ANIO, provides an application interface to the Analog/Digital Converter,
and Digital/Analog Converters on the XCM.

The Built-In Tests CSC, identified XCP-BIT, provides a set of functions to perform and record the results of
memory and hardware interface Built-In Tests (BIT).


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 33



The Bootstrap CSC, identified XCP-BOOT, is a EEPROM-resident program which performs a basic hardware BIT,
loads the flight program from EEPROM, and provides a simple RS-232-based monitor useful during development
for examining memory and for downloading programs.

The CCD Interface CSC, identified XCP-CCD, creates a ring buffer in XCP local memory and block transfers CCD
row data from the XCM using XCP-CDD.

The Command and Control CSC, identified XCP-CCM, is an application program that establishes and maintains the
current system state, receives and dispatches commands.

The CCD Data Driver, identified XCP-CDD, provides an application interface to read CCD rows from the CCD
hardware interface.

The Data Compression CSC, identified XCP-DCX, is an application program that compresses the data products
produced by the by the Event Recognition Processor CSC.

The Error Detection and Correction CSC, identified XCP-EDAC, provides a set of functions to facilitate the
tracking, handling, and recording of memory errors.

The EEPROM File System CSC, identified XCP-EEFS, provides a file system, which is media-compatible with
Microsoft Disk Operating System (MS-DOS). The file system facilitates dynamic loading of application programs
using the VxWorks loader.

The EEPROM Interface Driver, identified XCP-EEPRM, provides an application interface to the EEPROM on the
XCP.

The Engineering Ethernet Driver, identified XCP-ENET, provides a network driver that can be used to support
networking on the EU.

The Power Distribution Driver, identified XCP-PDD, provides an application interface to relays on the Power
Distribution Module (PDM).

The Periodic Processing CSC, identified XCP-PP, is an application program that collects housekeeping telemetry,
monitors the running tasks, and is responsible for overall error handling.

The Real-Time Operating System CSC, identified XCP-RTOS, provides a real-time, multi-tasking environment. The
XCP-RTOS is a Commercial Off-The-Shelf (COTS) product, identified as VxWorks 5.3, kernel version WIND 2.4,
from Wind River Systems. The basic operating system is supplemented with a library of system utilities for memory
management, and accessing the VME bus.

The SCU Interface CSC, identified XCP-SCUI, is an application program that manages communications with the
SCU over the 1553 interface at the application data protocol level.

The Sequencer CSC, identified XCP-SEQ, provides an application interface that is capable of loading a sequencer
program from the EEPROM File System and starting it on the TSM.

The Time Synchronization CSC, identified as XCP-TIS, provides an application interface to access the XCM clock,
compute Universal Time Coordinate (UTC) time, and perform clock synchronization with the Spacecraft.

The Timer/Sequencer Driver, identified XCP-TSD, provides an application interface to the Timer/Sequencer Module
(TSM).

The Tube Heater Control CSC, identified XCP-THC, is an application program that controls the operation of the
telescope heaters.


4.5.2Science Flight Software


This section lists and describes the computer software components (CSCs) of the Science Flight Software. This
software will be developed at PSU.

The Baffle Heater Control CSC, identified XCP-BHC, is an application program that controls the operation of the
baffle heaters using a proportional-integral-derivative (PID) control algorithm.


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 34



The Data Collection Control CSC, identified XCP-DCC, receives data collection commands, programs the sequencer
through XCP-SEQ, and sets up CCD clocks and bias voltages through XCP-PDD and XCP-ANIO. In AUTO mode,
XCP-DCC selects the camera mode based on counts-per-second.

The Event Recognition Processor CSC, identified XCP-ERP, receives raw CCD data from XCP-CCD, generates
output Reports, and outputs them to XCP-DCX for compression and transmission to the Spacecraft. It also contains
the Event Recognition Algorithm, the Centroid Algorithm, the bad pixel/row/column routines, bias algorithms,
baseline correction, and mean row correction.

The Telescope Alignment Monitor CSC, identified XCP-TAM, reads an image from the TAM CCD, processes the
image through a centroid algorithm, and computes a position correction for XCP-ERP.

The Thermo-electric Cooler CSC, identified XCP-TEC, is an application program that controls the operation of the
thermo-electric cooler using a PID control algorithm.


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**

#### **5.CONTEXT DIAGRAMS**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 35



The following sections provide a context diagram for each CSC. The detailed requirements for each CSC are
enumerated in an electronic spreadsheet to facilitate requirements traceability and verification tracking. A copy of
this spreadsheet is contained in Appendix A. The electronic spreadsheet is configuration-controlled, and the copy
attached to this document contains the version of the requirements applicable to the indicated revision of this
document.

#### 5.1MIL-STD-1553B Driver


A context diagram for the MIL-STD-1553B (1553) Driver is shown in the following figure.









**Figure 13. MIL-STD-1553B Driver Context Diagram**

#### 5.2RS-422 Driver


A context diagram for the RS-422 Driver is shown in the following figure.


Interrupt
( ~~X~~ C ~~M_4~~ 2 ~~2~~ _ ~~R~~ X)









**Figure 14. RS-422 Driver Context Diagram**


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**

#### 5.3Analog I/O Driver


A context diagram for the Analog I/O Driver is shown in the following figure.



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 36











**Figure 15. Analog I/O Driver Context Diagram**

#### 5.4Built-In Tests CSC


A context diagram for the Built-In Tests (BIT) CSC is shown in the following figure.
















#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**


**Figure 16. Built-In Tests CSC Context Diagram**

#### 5.5Bootstrap CSC


A context diagram for the Bootstrap CSC is shown in the following figure.



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 37

























**Figure 17. Bootstrap CSC Context Diagram**

#### 5.6CCD Interface CSC


A context diagram for the CCD Interface CSC is shown in the following figure.























**Figure 18. CCD Interface CSC Context Diagram**

#### 5.7Command and Control CSC


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**


A context diagram for the XCP-CCM is shown in the following figure.



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 38

















































**Figure 19. Command and Control CSC Context Diagram**


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**

#### 5.8CCD Data Driver


A context diagram for the CCD Data Driver is shown in the following figure.



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 39











**Figure 20. CCD Data Driver Context Diagram**

#### 5.9Data Compression CSC


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**


A context diagram for the Data Compression CSC is shown in the following figure.



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 40











|Control|Col2|
|---|---|
|Data Compression<br>CSC,<br>XCP-DCX<br>PKG_SS<br>Control<br>~~(~~TASK_HBEAT~~)~~<br>ERRNO<br>Periodic<br>Processing CSC,<br>XCP-PP<br>Spacecraft Control<br>Unit Interface CSC,<br>XCP-SCUI<br>HK_DCX|Data Compression<br>CSC,<br>XCP-DCX<br>PKG_SS<br>Control<br>~~(~~TASK_HBEAT~~)~~<br>ERRNO<br>Periodic<br>Processing CSC,<br>XCP-PP<br>Spacecraft Control<br>Unit Interface CSC,<br>XCP-SCUI<br>HK_DCX|
|Periodic<br>Processing CSC,<br>XCP-PP|Spacecraft Control<br>Unit Interface CSC,<br>XCP-SCUI|


**Figure 21. Data Compression CSC Context Diagram**




#### 5.10Error Detection and Correction CSC

A context diagram for the Error Detection and Correction (EDAC) CSC is shown in the following figure.


Interrupt





















**Figure 22. Error Detection and Correction CSC Context Diagram**

#### 5.11EEPROM File System CSC


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 41



A context diagram for the EEPROM File System CSC is shown in the following figure.















**Figure 23. EEPROM File System CSC Context Diagram**

#### 5.12EEPROM Interface Driver


A context diagram for the EEPROM Interface Driver is shown in the following figure.















**Figure 24. EEPROM Interface Driver Context Diagram**


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**

#### 5.13Engineering Ethernet Driver



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 42



A context diagram for the Engineering Ethernet Driver is shown in the following figure.









**Figure 25. Engineering Ethernet Driver Context Diagram**

#### 5.14Power Distribution Driver


A context diagram for the Power Distribution Driver is shown in the following figure.









**Figure 26. Power Distribution Driver Context Diagram**

#### 5.15Periodic Processing CSC


A context diagram for the Periodic Processing CSC is shown in the following figure.


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 43





































































































**Figure 27.  Periodic Processing CSC Context Diagram**


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**

#### 5.16Real-Time Operating System CSC


A context diagram for the Operating System CSC is shown in the following figure.



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 44
























|XRT Control<br>Processor<br>(Mars98),<br>XCP<br>XCP_RTCU +<br>XCP_RTCL<br>XCP_EICRS<br>Interrupt<br>XCP_IOCC<br>(XCP_TIMR)<br>XCP_DRAM<br>Interrupt<br>(XCP_DEC)<br>Real-Time<br>Operating System XRT<br>CSC, Communications<br>XCM_W DR<br>XCP-RTOS Module,<br>XCM<br>TASK_BLOCK<br>BIT_DRAM Control<br>(Execute) Control ELF_MODULE<br>(W D Strobe)<br>EEPROM Interface Periodic EEPROM File<br>Built-In Test CSC,<br>Driver, Processing CSC, System CSC,<br>XCP-BIT<br>XCP-EEPRM XCP-PP XCP-EEFS|Col2|
|---|---|
|EEPROM Interface<br>Driver,<br>XCP-EEPRM|EEPROM File<br>System CSC,<br>XCP-EEFS|



**Figure 28. Real-Time Operating System CSC Context Diagram**

#### 5.17SCU Interface CSC


A context diagram for the XCP-SCUI is shown in the following figure.


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 45





































**Figure 29. SCU Interface CSC Context Diagram**

#### 5.18Sequencer Interface CSC


A context diagram for the Sequencer Interface CSC is shown in the following figure.





















**Figure 30. Sequencer Interface CSC Context Diagram**

#### 5.19Time Synchronization CSC


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 46



A context diagram for the Time Synchronization CSC is shown in the following figure.









XRT
Communications







Module,

XCM











**Figure 31. Time Synchronization CSC Context Diagram**

#### 5.20Timer/Sequencer Driver


A context diagram for the Timer/Sequencer Driver is shown in the following figure.









**Figure 32. Timer/Sequencer Driver Context Diagram**

#### 5.21Tube Heater Control CSC


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**


A context diagram for the Tube Heater Control CSC is shown in the following figure.



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 47























**Figure 33. Tube Heater Control CSC Context Diagram**

#### 5.22Baffle Heater Control

















**Figure 34. Baffle Heater Control CSC**

#### 5.23Data Collection Control CSC


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 48



A context diagram for the Data Collection Control CSC is shown in the following figure.




















|Command and<br>Control CSC,<br>XCP-CCM|DCC_CMD|
|---|---|
|Command and<br>Control CSC,<br>XCP-CCM||



















**Figure 35. Data Collection Control CSC Context Diagram**

#### 5.24Event Recognition Processor CSC


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 49



A context diagram for the Event Recognition Processor CSC is shown in the following figure.

































**Figure 36. Event Recognition Processor CSC Context Diagram**

#### 5.25(Deleted) Formatter CSC


A context diagram for the Formatter CSC is shown in the following figure.


**Figure 37. (Deleted) Formatter CSC Context Diagram**

#### 5.26Telescope Alignment Monitor CSC


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 50



A context diagram for the Telescope Alignment Monitor CSC is shown in the following figure.











Periodic
Processing CSC,

XCP-PP


|RS-422<br>Driver,<br>XCP-422|DATA<br>HK_TAM<br>tor<br>ERRNO<br>Control<br>(TASK_HBEAT)|
|---|---|
|Telescope<br>Alignment Moni<br>CSC,<br>XCP-TAM<br>S422_CMD<br>TAM_|Telescope<br>Alignment Moni<br>CSC,<br>XCP-TAM<br>S422_CMD<br>TAM_|



**Figure 38. Telescope Alignment Monitor CSC Context Diagram**

#### 5.27Thermo-Electric Cooler CSC


A context diagram for the Thermo-Electric Cooler CSC is shown in the following figure.

















**Figure 39. Thermo-Electric Cooler CSC Context Diagram**


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**

#### **6.DATA DICTIONARY**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 51



This section contains the data dictionary for the FSW. In this dictionary, Data Elements are described either as types
or as composites. Composite Data Elements are constructed from more elementary components.




































|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|1553_SUB_ADRS|Type: UINT16<br>Range: 1-31|MIL-STD-1553B Sub-address|
|1553_SUB_DATA|Composite:<br>32{UINT16}32|MIL-STD-1553B Sub-address Buffer|
|ADDRESS|Type: Fundamental, char *|Address|
|ALT_OS_BLOCK|Composite:<br>128{UINT32}128<br>Location:<br>eeBase32 + 0x880000 through<br>eeBase32 + 0x8FFFFF|Alternate Configuration of OFP|
|ALTITUDE|Type: UINT32|Altitude<br>(from SISCATTITUDE)|
|ANIO_BUS_VOLTAGE|Type: UINT16|Spacecraft Bus Voltage<br>(from ANIO_DATA)|
|ANIO_DATA|Composite:<br>128{UINT16}128|Analog I/O Data<br>(from hardware)|
|ANIO_SAMPLES|Type: UINT32|Total number of accumulated samples|
|ANIO_SQUARES|Composite:<br>128{DOUBLE}128|Accumulated I/O Sum of Squares|
|ANIO_STAT|Composite:<br>ANIO_SUMS +<br>ANIO_SQUARES +<br>ANIO_SAMPLES|Accumulated I/O Statistics|
|ANIO_SUMS|Composite:<br>128{DOUBLE}128|Accumulated I/O Sums|
|APID|Type: UINT16|Application ID|
|BAD_COL|Type: INT16|Bad Row<br>for Photo-Diode or windowed timing modes|
|BAD_COL_TBL|Composite:<br>{BAD_COL}|Bad Column Table|
|BAD_PIX|Composite:<br>BAD_PIX_ROW +<br>BAD_PIX_COL|Bad Pixel Coordinate<br>-1 for BAD_PIX_ROW indicates entire column<br>-1 for BAD_PIX_COL indicates entire row|
|BAD_PIX_COL|Type: INT16|Bad Pixel Column|
|BAD_PIX_ROW|Type: INT16|Bad Pixel Row|
|BAD_PIX_TBL|Composite:<br>{BAD_PIX}|Bad Pixel Table|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 52


























|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|BC_INDEX|Type: UINT32<br>Value:<br>0x0: Boot Alternate<br>0x1-0xFFFFFFFF:  Boot Primary|Boot Configuration Index|
|BC1_CHKS_32|Type: CHKS_32<br>Location: eeBase32 + 0xAF0050|Stored checksum of OFP bytes|
|BC1_CHKS_NEW|Type: CHKS_32|Freshly calculated checksum of OFP bytes|
|BC1_COPY_ADDR|Type: ADDRESS<br>Location: eeBase32 + 0xAF0048|Start address in DRAM to copy OFP|
|BC1_END_ADDR|Type: ADDRESS<br>Location: eeBase32 + 0xAF0044|End address of OFP in EEPROM|
|BC1_ENTRY_ADDR|Type: ADDRESS<br>Location: eeBase32 + 0xAF004C|Address of entry point of OFP in DRAM|
|BC1_START_ADDR|Type: ADDRESS<br>Location: eeBase32 + 0xAF0040|Start address of OFP in EEPROM|
|BHTR_ID|Type: UINT8|Baffle Heater ID|
|BHTR_PARMS|Composite: (TBR)<br>BHTR_SETPT_LO +<br>BHTR_SETPT_HI|Baffle Heater Control Parameters|
|BHTR_PARMS_TBL|Composite:<br>{BHTR_PARMS}|Baffle Heater Parameters Table|
|BHTR_SETPT_HI|Type: UINT16|Baffle Heater Control Upper Threshold|
|BHTR_SETPT_LO|Type: UINT16|Baffle Heater Control Lower Threshold|
|BIAS_ALG_ID|Type: UINT8|Bias Algorithm|
|BIAS_MAP_ID|Type: UINT8|Bias Map ID|
|BIAS_THRSH|Type: UINT16|Bias Map Threshold|
|BIT_1553_INT|Type: BIT_RESULT<br>Location: eeBase32 + 0xAF1084|MIL-STD-1553B Internal BIT results|
|BIT_1553_RAM|Type: BIT_RESULT<br>Location: eeBase32 + 0xAF1080|MIL-STD-1553B Device RAM BIT results|
|BIT_CPU_BRANCH|Type: BIT_RESULT<br>Location: eeBase32 + 0xAF1040|Branch Processor BIT result|
|BIT_CPU_FLTPT|Type: BIT_RESULT<br>Location: eeBase32 + 0xAF1048|Floating Point Processor BIT result|
|BIT_CPU_FXPT|Type: BIT_RESULT<br>Location: eeBase32 + 0xAF1044|Fixed Point Processor BIT result|
|BIT_CPU_INT|Type: BIT_RESULT<br>Location: eeBase32 + 0xAF104C|Interrupt Processor BIT results|
|BIT_CPU_TIMER|Type: BIT_RESULT<br>Location: eeBase32 + 0xAF1054|Timer Processor BIT results|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 53


























|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|BIT_DATA|Composite:<br>BIT_DRAM +<br>BIT_CPU_BRANCH +<br>BIT_CPU_FXPT +<br>BIT_CPU_FLTPT +<br>BIT_CPU_INT +<br>BIT_CPU_TIMER +<br>BIT_1553_RAM +<br>BIT_1553_INT<br>Location:<br>eeBase32 + 0xAF1000 through<br>eeBase32 + 0xAF11FC|Built-In Tests Data|
|BIT_DRAM|Composite:<br>{BIT_RESULT}<br>Location:<br>eeBase32 + 0xAF1100 through<br>eeBase32 + 0xAF113C|Built-In Tests Data for DRAM|
|BIT_EDAC_MBE|Type: BIT_RESULT<br>Location: eeBase32 + 0xAF105C|Multiple-bit error EDAC BIT result|
|BIT_EDAC_SBE|Type: BIT_RESULT<br>Location: eeBase32 + 0xAF1058|Single-bit error EDAC BIT result|
|BIT_PROM_CHKS|Type: BIT_RESULT<br>Location: eeBase32 + 0xAF1060|PROM checksum BIT result|
|BIT_RESULT|Type: UINT32<br>Value:<br>0: PASS<br>-1: FAIL|Built-In Test Result|
|BIT_SUMMARY|Type: UINT32|Built-In Test Results with 1 bit per test|
|BOOL|Type: Fundamental, char<br>Value: FALSE or TRUE|Boolean value|
|BOOT_BLOCK|Composite:<br>4096{UINT32}4096|Bootstrap Program Storage|
|BOOT_CNT|Type: UINT32|Count of the number of  times booted|
|BUF_LEN|Type: UINT32|Buffer length|
|CCD_DATA|Composite:<br>{UINT16}|CCD Data|
|CCD_LINES|Type: UINT8|CCD Number of Lines|
|CCSDS_APID|Composite:<br>11{MBIT}11<br>Value:<br>0x480-0x4DF: real-time telemetry<br>0x4E0-0x53F: TDRSS telemetry<br>0x540-0x59F: Stored science telemetry<br>0x680-0x69F: Telecommands|CCSDS Application ID|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 54


























|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|CCSDS_HDR|Composite:<br>CCSDS_VER_NUM +<br>CCSDS_TYPE +<br>CCSDS_SEC_HDR +<br>CCSDS_APID +<br>CCSDS_SEQ_FLG +<br>CCSDS_SEQ_CNT +<br>CCSDS_PKT_LEN|CCSDS Packet Header|
|CCSDS_PKT_LEN|Type: UINT16|CCSDS Packet Length<br>(Application data length – 1)|
|CCSDS_SEC_HDR|Type: MBIT<br>Value:<br>0: No secondary header<br>1: Secondary header is used|CCSDS flag indicating whether or not a<br>secondary header is present|
|CCSDS_SEQ_CNT|Composite:<br>14{MBIT}14<br>Range: 0 - 16383|CCSDS sequence count for segmented data<br>packets|
|CCSDS_SEQ_FLG|Composite:<br>2{MBIT}2<br>Value:<br>00: Continuation segment of app data<br>01: 1st segment of app data<br>10: Last segment of app data<br>11: Unsegmented app data|CCSDS sequence flags|
|CCSDS_TLM_PKT|Composite:<br>CCSDS_HDR +<br>CCSDS2_TLM_HDR<br>TLM_DATA |<br>SS_DATA|CCSDS Telemetry Data Packet|
|CCSDS_TYPE|Type: MBIT<br>Value:<br>0: telemetry packets<br>1: telecommand packets|CCSDS packet type|
|CCSDS_VER_NUM|Composite:<br>3{MBIT}3<br>Value: 0 (Version 1 CCSDS packet)|CCSDS Version Number|
|CCSDS2_APDATA|Type: UINT16|CCSDS secondary header application data|
|CCSDS2_CHKS|Type: CHKS_16|CCSDS secondary header checksum|
|CCSDS2_CMD_HDR|Composite:<br>CCSDS2_HDR_TYPE +<br>CCSDS2_RESERVED +<br>CCSDS2_FCODE +<br>CCSDS2_APDATA +<br>CCSDS2_CHKS|CCSDS telecommand Secondary Packet<br>Header|
|CCSDS2_FCODE|Type: UINT8|CCSDS secondary header function code|
|CCSDS2_HDR_TYPE|Type: BIT<br>Value: 0 (secondary header)|Flag indicating data is secondary header|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 55


































|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|CCSDS2_RESERVED|Composite:<br>7{MBIT}7<br>Value: 0|Reserved bits in CCSDS secondary header|
|CCSDS2_SECONDS|Type: UINT32|CCSDS secondary header time (seconds)|
|CCSDS2_SUB_SECONDS|Type: UINT16|CCSDS secondary header time (sub-seconds)|
|CCSDS2_TLM_HDR|Composite:<br>CCSDS2_SECONDS +<br>CCSDS2_SUB_SECONDS|CCSDS Telemetry Secondary Packet Header|
|CENT_PARMS|Composite: TBD|Centroid Algorithm Parameters|
|CENT_PARMS|Type: TBD|Centrod Algorithm Parameters|
|CENT_THRSH|Type: UINT16|Centroid Algorithm Threshold|
|CENT_THRSH|Type: UINT16 (TBR)|Centroid Algorithm Threshold|
|CHKS_16|Type: UINT16<br>Value:<br>Sum of UINT8 ignoring carry|Vertical Checksum|
|CHKS_32|Type: UINT32<br>Value:<br>Sum of several UINT32 ignoring carry|PROM or EEPROM checksum|
|CMD|Composite:<br>SC_TIME +<br>BYTE_CNT +<br>CMD_DATA +<br>CHKS_16|XRT Ground Command<br>(See Appendix C for a complete list of the<br>commands and associated details.)|
|CMD_CNT|Type: UINT32|Number of telecommands received since last<br>reset|
|CMD_ECHO|Type: 62{CHAR}62|Echo of recent telecommand|
|CMD_ECHO|Composite:<br>CMD_REJ_FLAG +<br>CMD|Three most recent telecommands and their<br>dispatch time|
|CMD_REJ_FLAG|Type: BOOL|Time of recent telecommand|
|CMD_RUN|Type: UINT32|Number of telecommands dispatched since last<br>reset|
|COLD_MEM_SIZE|Type: MEM_SIZE|Memory size for a cold boot|
|COLD_SKIP_BIT|Type: SKIP_BIT|Skip BIT flag for a cold boot|
|Control (Bias Voltage Error)|Type:  Fundamental, Control|Respond to a bias voltage error|
|Control (CCD_PURGE)|Type:  Fundamental, Control|Purge data from receive queue|
|Control (Disable CCD<br>Voltages)|Type:  Fundamental, Control|Disable CCD bias voltages|
|Control (Enter Auto)|Type:  Fundamental, Control|Enter automatic observation mode|
|Control (Execute)|Type:  Fundamental, Control|Execute routine in caller’s context|
|Control (Exit Auto)|Type:  Fundamental, Control|Exit automatic observation mode|
|Control (PDM Disable)|Type:  Fundamental, Control|PDM Relay Disable|
|Control (PDM Enable)|Type:  Fundamental, Control|PDM Relay Enable|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 56


































|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|Control (Reload DACs)|Type:  Fundamental, Control|Reload DACs controlling CCD bias voltages|
|Control (Run BIT)|Type:  Fundamental, Control|Activate driver built-in test|
|Control (SEQ Start)|Type:  Fundamental, Control|Start sequencer program|
|Control (SEQ Stop)|Type:  Fundamental, Control|Stop sequencer program|
|Control (TASK_HBEAT)|Type:  Fundamental, Control|Report that task is alive|
|Control (TSM DSP Reset)|Type:  Fundamental, Control|Reset processor on sequencer module|
|Control (WD Strobe)|Type:  Fundamental, Control|Strobe watchdog timer|
|CPU_SPEED|Type: UINT32<br>Location: eeBase32 + 0xAF0034<br>Range: 0-4<br>Value:<br>0: 2.5 MHz<br>1: 5 MHz<br>2: 10 MHz<br>3: 20 MHz|Processor Clock Speed|
|DAC_ID|Type: UINT8|DAC Identifier (for CCD Voltages)|
|DAC_TBL|Composite:<br>{DAC_VOLTAGE}|Bias Voltage Table (for CCD Voltages)|
|DAC_VOLTAGE|Type: UINT8|Count Value (for CCD Voltages)|
|DCC_CMD|Type: CMD|Data Collection Control Command|
|DCC_STATUS|Type: CMD|Data Collection Control Status|
|DEC|Type: UINT32|Declination|
|DEC_POINT_DIR|Type: INT32|Declination of pointing direction|
|DOOR_ACT_ID|Type: UINT8<br>Value:<br>1: Actuator 1<br>2: Actuator 2<br>3: Actuator 1 and 2|Door Actuator ID|
|DOOR_TIMEOUT|Type: UINT8|Door timeout in seconds|
|DOS_FILE_DATA|Composite:<br>{UINT8}|DOS File Data|
|DOS_FILENAME|Composite:<br>[A-Z | a-z] +0{[A-Z | a-z | 0-9]}7 + 0{.}1 +  0{A-Z |<br>a-z | 0-9}3|DOS Filename|
|DOUBLE|Type: Fundamental, double|Floating Point, Double-precision|
|DUMP_ADDRESS|Type: ADDRESS|Source Address for Dump|
|DUMP_PARMS|Composite:<br>DUMP_ADDRESS +<br>DUMP_SIZE|Memory Dump Parameters|
|DUMP_SIZE|Type: UINT16|Size of memory dump in bytes|
|edacEeMbeAdrs|Type: ADDRESS|EEPROM Multiple-Bit Error Last Occurrence|
|edacEeMbeCnt|Type: UINT32|EEPROM Multiple-Bit Error Count|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 57
















|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|edacEeMbePrev|Type: ADDRESS|EEPROM Multiple-Bit Error Next-to-last<br>Occurrence|
|edacEeSbeAdrs|Type: ADDRESS|EEPROM Single-Bit Error Last Occurrence|
|edacEeSbeCnt|Type: UINT32|EEPROM Single-Bit Error Count|
|edacEeSbePrev|Type: ADDRESS|EEPROM Single-Bit Error Next-to-last<br>Occurrence|
|edacRscMbeAdrs|Type: ADDRESS|DRAM Multiple-Bit Error Last Occurrence|
|edacRscMbeCnt|Type: UINT32|DRAM Multiple-Bit Error Count|
|edacRscMbePrev|Type: ADDRESS|DRAM Multiple-Bit Error Next-to-last Occurrence|
|edacRscSbeAdrs|Type: ADDRESS|DRAM Single-Bit Error Last Occurrence|
|edacRscSbeCnt|Type: UINT32|DRAM Single-Bit Error Count|
|edacRscSbePrev|Type: ADDRESS|DRAM Single-Bit Error Next-to-last Occurrence|
|eeBase32|Type: ADDRESS<br>Value:  0xFF000000|Base address for EEPROM|
|EEPRM_PAGE|Composite:<br>128{UINT32}128|EEPROM Page|
|eicrBase32|Type: ADDRESS<br>Value:  0xD0000000|Base address for External Interrupt Control<br>Registers on the RAD6000 CPU Module|
|ELF_MODULE|Composite:<br>{BYTES}|Program object file for patches (relocatable)|
|ENET_HOST_IP|Type: UINT32<br>Location: eeBase32 + 0xAF01F8|32-Bit Integer representation of Host IP|
|ENET_IP|Type: UINT32<br>Location: eeBase32 + 0xAF01F4|32-Bit Integer representation of XCP IP|
|ENET_MAC|Composite:<br>2{UINT32}2<br>Location:<br>eeBase32 + 0xAF0014 through<br>eeBase32 + 0xAF0018|Ethernet Media Access Control Address<br>Only first six bytes are valid.|
|ERP_CMD|Type: CMD|Event recognition processor command|
|ERRNO|Type: UINT32<br>Bits:<br>31-16: Module Number<br>15-0: Sequence Number|Error Number|
|ERROR_SET|Composite:<br>5{ERRNO}5|Top 5 errors on PP error queue|
|EVENT_STHRSH|Type: UINT16|Timing Mode Split Event Threshold|
|EVENT_THRSH|Type: UINT16|Timing Mode Event Threshold|
|EVENT_ULD|Type: UINT16|Timing Mode Upper Level Discriminator|
|FCODE|Type: CCSDS2_FCODE|CCSDS secondary header function code|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 58






















|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|FILE_SYSTEM_BLOCK|Composite:<br>{UINT32}<br>Location:<br>eeBase32 + 0x500000 through<br>eeBase32 + 0x7EFFFF|File System Block|
|FLOAT|Type: Fundamental, float|Floating Point, Single-precision|
|FLUX|Type: UINT32|Flux|
|FO_OBS_MODE|Type: UINT8 (TBR)|Observation Mode<br>(from FO_NEXTOBS_INFO)|
|FO_OBS_TYPE|Type: UINT8 (TBR)|Observation Type<br>(from FO_NEXTOBS_INFO)|
|HDR_DATA|Type: UINT8|Data Package Header|
|HK_BHC|Composite:<br>TBD|Baffle Heater Control CSC Housekeeping|
|HK_BIT|Composite:<br>BOOT_CNT+<br>BIT_CPU_BRANCH+<br>BIT_CPU_FXPT +<br>BIT_CPU_FLTPT +<br>BIT_CPU_INT +<br>BIT_CPU_TIMER +<br>BIT_EDAC_SBE +<br>BIT_EDAC_MBE +<br>BIT_PROM_CHKS +<br>BIT_1553_RAM +<br>BIT_1553_INT +<br>BIT_IIM_RAM +<br>BIT_DRAM|XCP BIT Housekeeping Package|
|HK_CCD|Composite:<br>HK_CCD_LINES +<br>HK_CCD_FRAMES +<br>HK_CCD_OVERFLOW +<br>HK_CCD_READERR +<br>HK_CCD_LC_OVERFLOW +<br>HK_CCD_STATUS|CCD Interface CSC Housekeeping|
|HK_CCD_FRAMES|Type: UINT32|Number of lines read since last reset|
|HK_CCD_LC_OVERFLOW|Type: UINT32|Number of line counter overflow errors since last<br>reset|
|HK_CCD_LINES|Type: UINT32|Number of lines read since last reset|
|HK_CCD_OVERFLOW|Type: UINT32|Number of overflow errors since last reset|
|HK_CCD_READERR|Type: UINT32|Number of read errors since last reset|
|HK_CCD_STATUS|Type: UINT32|Last hardware status|
|HK_CCM|Composite:<br>HK_CCM_N_CMD_REC +<br>HK_CCM_N_CMD_REJ +<br>HK_CCM_LAST_REJCMD +<br>HK_CCM_N_LAST_REJ|Command and Control CSC Housekeeping|
|HK_CCM_LAST_ECMD|Type: CMD|Echo of last command executed|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 59


























|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|HK_CCM_LAST_RCVCMD|Type: CMD|Echo of last command received|
|HK_CCM_LAST_REJCMD|Type: CMD|Echo of last command rejected|
|HK_CCM_N_CMD_REC|Type: UINT32|Number of commands received|
|HK_CCM_N_CMD_REJ|Type: UINT32|Number of commands rejected|
|HK_CCM_N_LAST_EXEC|Type: UINT32|Index of last command executed|
|HK_CCM_N_LAST_RCV|Type: UINT32|Index of last command received|
|HK_CCM_N_LAST_REJ|Type: UINT32|Index of last command rejected|
|HK_DCC|Composite:<br>TBD|Data Collection Control CSC Housekeeping|
|HK_DCX|Composite:<br>HK_DCX_NUM_IN +<br>HK_DCX_NUM_CMP +<br>HK_DCX_NUM_OUT|Data Compression CSC Housekeeping|
|HK_DCX_NUM_CMP|Type: UINT32|Number of packets compressed|
|HK_DCX_NUM_IN|Type: UINT32|Number of packets enqueued|
|HK_DCX_NUM_OUT|Type: UINT32|Number of packets output|
|HK_EDAC|Composite:<br>edacRscSbeCnt +<br>edacRscSbeAdrs +<br>edacRscSbePrev +<br>edacRscMbeCnt +<br>edacRscMbeAdrs +<br>edacRscMbePrev|Error Detection and Correction Data|
|HK_ERP|Composite:<br>TBD|Event Recognition Processor CSC<br>Housekeeping|
|HK_SAMP_TIME|Type: SC_TIME|Time of last sample|
|HK_SCUI|Composite:<br>SCU_BUFFER_RATE +<br>SCU_XMIT_BYTES|SCU Interface CSC Housekeeping|
|HK_SEQ|Composite:<br>HK_LAST_SEQ_ID|Sequencer Interface CSC Housekeeping|
|HK_SEQ_LAST_SEQ_ID|Type: SEQ_ID|Identifier of last sequencer program loaded|
|HK_TAM|Composite:<br>TBD|Telescope Alignment Monitor CSC<br>Housekeeping|
|HK_TEC|Composite:<br>TBD|Thermo-electric Cooler CSC Housekeeping|
|HK_THC|Composite:<br>HK_THC_RELAY_STATUS|Tube Heater Control CSC Housekeeping|
|HK_THC_RELAY_STATUS|Type:<br>3{UINT16}3|Current Status of Heater Relays|
|HK_TIS|Composite:<br>HK_TIS_LAST_TIME +<br>HK_TIS_NUM_TIMES|Time Synchronization CSC Housekeeping|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 60










|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|HK_TIS_LAST_TIME|Type: SC_TIME|Time from last time-at-the-tone message<br>received|
|HK_TIS_NUM_TIMES|Type: UINT32|Number of time-at-the-tone messages received|
|HK_UTC_CORR|Type: UTC_OFFSET|UTC correction for last sample|
|HTR_ID|Type: UINT8|Heater Number|
|IN_SAA_FLAG|Type: BOOL|Flag to indicate the Spacecraft is in the SAA|
|IN_SAFE_MODE|Type: BOOL|Flag to indicate if the Spacecraft is in Safe<br>Pointing|
|INT16|Type: Fundamental, short|Short Integer|
|INT32|Type: Fundamental, int|Integer|
|Interrupt (TSM_WD)|N/A|Timer/Sequencer Watchdog Interrupt|
|Interrupt (XCM_1553)|N/A|MIL-STD-1553B Interrupt|
|Interrupt (XCM_422_RX)|N/A|RS-422 Receiver Ready|
|Interrupt (XCM_ANIO)|N/A|Analog/Digital Conversion Complete Interrupt|
|Interrupt (XCM_CCD)|N/A|CCD Data Ready Interrupt|
|Interrupt (XCM_ENET)|N/A|Ethernet Interrupt|
|Interrupt (XCP_DEC)|N/A|Decrementer Interrupt|
|Interrupt (XCP_MEM_ERR)|N/A|EDAC Interrupt|
|Interrupt (XCP_TIMR)|N/A|RSC Bus Interface Timer Interrupt|
|IOCC_EOI_IRQ7|Type: UINT32<br>Type: UINT32<br>Location: ioccBase32 + 0x47008C<br>Bits:<br>31-0: Reserved|End of Interrupt Register (IRQ7)|
|ioccBase32|Type: ADDRESS<br>Value:  0xE0000000|Base address for the Input/Output Channel<br>Controller on the RAD6000 CPU Module|
|IS_AT_TARGET|Type: BOOL|New Automated Target Indicator|
|IS_IN_10_ARCMIN|Type: BOOL|Flag to indicate the Spacecraft is with 10 arcmin<br>of the target|
|IS_SETTLED|Type: BOOL|Flag to indicate the Spacecraft is slewing/ or<br>stopped|
|LAST_BOOT_TIME|Type: SC_TIME|Time of last XCP boot|
|LATTITUDE|Type: UINT32|Lattitude<br>(from SISCATTITUDE)|
|LE_DAR|Type: UINT32|Last exception Data Access Register|
|LE_DSISR|Type: UINT32|Last exception Data Storage Interrupt Status<br>Register|
|LE_ERRNO|Type: ERRNO|Last exception ERRNO|
|LE_FPS|Type: UINT32|Last exception Floating Point Status and Control<br>Register|
|LE_MASK0|Type: UINT32|Last exception External Interrupt Mask Register<br>0|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 61




















|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|LE_MASK1|Type: UINT32|Last exception External Interrupt Mask Register<br>1|
|LE_SPTR|Type: ADDRESS|Last exception stack pointer|
|LE_TASK_ID|Type: TASK_ID|Last exception task ID|
|LE_VNUM|Type: UINT32|Last exception vector number|
|LE_VOFF|Type: UINT32|Last exception vector offset|
|LONGITUDE|Type: UINT32|Longitude<br>(from SISCATTITUDE)|
|MBIT|Type Fundamental, binary digit<br>Value: 0 or 1|Binary digit|
|MEM_SIZE|Type: UINT32<br>Range: 0x00800000-0x08000000<br>Value:<br>0x00800000: 8 MB<br>0x01000000: 16 MB<br>0x02000000: 32 MB<br>0x04000000: 64 MB<br>0x08000000: 128 MB  (and values  in between)|Size in bytes of DRAM to clear/test|
|MRC_ALG_ID|Type: UINT8|Mean Row Correction Algorithm|
|MRC_FQ|Type: UINT16|Mean Row Correction Frequency|
|MRC_ROW|Type: UINT16|Mean Row Correction Row|
|MRC_THRSH|Type: UINT16|Mean Row Correction Threshold|
|N_CCD_ROWS|Type: UINT8|Number of CCD rows|
|OBS_BUF|Composite:<br>BUF_LEN<br>{BYTES}|Observation buffer|
|OBS_ID|Type: UINT16|Observation ID|
|PAST_OBS_TIME|Type: SC_TIME|Past Observation Time<br>(from FO_NEXTOBS_INFO)|
|PDM_CLPD|Type: UINT16<br>Location: pdmBase16 + 0x000002<br>Bits:<br>15-9: Reserved<br>8-5: Wax Actuators Disable<br>  (Write: 1 – Disable)<br>4: +35V Supply Disable<br>  (Write: 1 – Disable)<br>3: Reserved<br>2: TAM Supply Disable<br>  (Write: 1 – Disable)<br>1: Reserved<br>0: TEC Supply Disable<br>  (Write: 1 – Disable)|PDM CL Power Disable Register (Write Only)|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 62








|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|PDM_CLPE|Type: UINT16<br>Location: pdmBase16 + 0x000000<br>Bits:<br>15-9: Reserved<br>8-5: Wax Actuators Enable<br>  (Write: 1 – Enable)<br>4: +35V Supply Enable<br>  (Write: 1 – Enable)<br>3: Reserved<br>2: TAM Supply Enable<br>  (Write: 1 – Enable)<br>1: Reserved<br>0: TEC Supply Enable<br>  (Write: 1 – Enable)|PDM CL Power Enable Register (Write Only)|
|PDM_CLPS|Type: UINT16<br>Location: pdmBase16 + 0x000000<br>Bits:<br>15-14: Reserved<br>13-6: Wax Actuator Over-current & Status<br>5: +35V Supply Over-current<br>  (Read: 0 – Nominal, 1 – Over-current)<br>4: +35V Supply Status<br>  (Read: 0 – Off,  1 – Off)<br>3: TAM Supply Over-current<br>  (Read: 0 – Nominal, 1 – Over-current)<br>2: TAM Supply Status<br>  (Read: 0 – Off, 1 – On)<br>1: TEC Supply Over-current<br>  (Read: 0 – Nominal, 1 – Over-current)<br>0: TEC Supply Status<br>  (Read: 0 – Off, 1 – On)|PDM CL Power Status Register (Read Only)|
|PDM_DIS|Composite:<br>PDM_H1PD +<br>PDM_H2PD +<br>PDM_H3PD|PDM Heater Disables|
|PDM_EN|Composite:<br>PDM_H1PE +<br>PDM_H2PE +<br>PDM_H3PE|PDM Heater Enables|
|PDM_H1PD|Type: UINT16<br>Location: pdmBase16 + 0x000006<br>Bits:<br>15-0: Heater Disables<br>  (Write: 1 – Disable)|PDM Heater Bank 1 Power Disable Register<br>(Write Only)|
|PDM_H1PE|Type: UINT16<br>Location: pdmBase16 + 0x000004<br>Bits:<br>15-0: Heater Enables<br>  (Write: 1 – Enable)|PDM Heater Bank 1 Power Enable Register<br>(Write Only)|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 63








|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|PDM_H1PS|Type: UINT16<br>Location: pdmBase16 + 0x000004<br>Bits:<br>15-0: Heater Statuses<br>  (Read: 0 – Off, 1 – On)|PDM Heater Bank 1 Power Status Register<br>(Read Only)|
|PDM_H2PD|Type: UINT16<br>Location: pdmBase16 + 0x00000A<br>Bits:<br>15-0: Heater Disables<br>  (Write: 1 – Disable)|PDM Heater Bank 2 Power Disable Register<br>(Write Only)|
|PDM_H2PE|Type: UINT16<br>Location: pdmBase16 + 0x000008<br>Bits:<br>15-0: Heater Enables<br>  (Write: 1 – Enable)|PDM Heater Bank 2 Power Enable Register<br>(Write Only)|
|PDM_H2PS|Type: UINT16<br>Location: pdmBase16 + 0x000008<br>Bits:<br>15-0: Heater Statuses<br>  (Read: 0 – Off, 1 – On)|PDM Heater Bank 2 Power Status Register<br>(Read Only)|
|PDM_H3PD|Type: UINT16<br>Location: pdmBase16 + 0x00000E<br>Bits:<br>15-0: Heater Disables<br>  (Write: 1 – Disable)|PDM Heater Bank 3 Power Disable Register<br>(Write Only)|
|PDM_H3PE|Type: UINT16<br>Location: pdmBase16 + 0x00000C<br>Bits:<br>15-0: Heater Enables<br>  (Write: 1 – Enable)|PDM Heater Bank 3 Power Enable Register<br>(Write Only)|
|PDM_H3PS|Type: UINT16<br>Location: pdmBase16 + 0x00000C<br>Bits:<br>15-0: Heater Statuses<br>  (Read: 0 – Off, 1 – On)|PDM Heater Bank 3 Power Status Register<br>(Read Only)|
|PDM_HTR_STATUS|Composite:<br>3{UINT16}3|PDM Heater Status|
|PDM_RESET|Type: UINT16<br>Location: pdmBase16 + 0x00001E<br>Bits:<br>15-0: Reserved|PDM Master Reset<br>A write to this register resets all of the relays to<br>the Off state.|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 64
















|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|PDM_STAT|Composite:<br>PDM_H1PS +<br>PDM_H2PS +<br>PDM_H3PS|PDM Heater Status Registers|
|PDM_TEC_CTRL|Type: UINT16<br>Location: pdmBase16 + 0x000016<br>Bits:<br>15-0: TBD|PDM TEC Control Register|
|PDM_TEC_STAT|Type: UINT16<br>Location: pdmBase16 + 0x000016<br>Bits:<br>15-0: TBD|PDM TEC Status Register|
|PKG_RTHK|Composite:<br>APID+<br>SCUI_CTRL+<br>BUF_LEN+<br>TLM_DATA|The detailed format of the stored science data is<br>contained in XRT-PSU-028 Section 3.  The<br>CCSDS headers and checksums listed in the<br>document are not part of this data dictionary<br>item.|
|PKG_SS|Composite:<br>APID +<br>SCUI_CTRL+<br>BUF_LEN +<br>SS_DATA|Stored science data package|
|PKG_TDRSS|{BYTES}|The detailed format of the TDRSS messages is<br>contained in XRT-PSU-028 Section 2.  The<br>CCSDS headers and checksums listed in the<br>document are not part of this data dictionary<br>item.|
|PP_RANGE|Type: UINT16|Periodic Processing Range|
|PP_RANGE_TBL|Composite:<br>{PP_RANGE} +<br>STRIP_INTERVAL|Periodic Processing Range Table|
|PP_RATE|Type: UINT8<br>Value:<br>255:  Never<br>0:  At startup only<br>1-254: Period in seconds|Periodic Processing Rate|
|PP_RATE_TBL|Composite:<br>10{PP_RATE}10|Periodic Processing Rate Table|
|PRIME_OS_BLOCK|Composite:<br>128{UINT32}128<br>Location:<br>eeBase32 + 0x800000 through<br>eeBase32 + 0x87FFFF|Primary Configuration of OFP|
|RA|Type: UINT32|Right Ascension|
|RA_POINT_DIR|Type: INT32|Right ascension of pointing direction|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 65






















|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|RAD_SRC_FLAG|Type: UINT8<br>Value:<br>0: without radioactive source<br>1: with radioactive source.|Close Shutter Radioactive Source Flag|
|RAW_HK_DATA|Type: 80{UINT16}80|Raw housekeeping values from hardware|
|RED_APID|Type: APID|Application ID for Next RED Command|
|RED_FCODE|Type: FCODE|Function Code for Next RED Command|
|RML|Type: UINT16|Running Mean Length|
|ROLL|Type: UINT32|Roll|
|RPT_STATUS|Type: DCC_CMD (TBR)|Report Status|
|RPT_TYPE|Type: UINT8|Report Type|
|SAA_FLAG|Type: UINT8 (TBR)<br>Value:<br>0: Disable,<br>1: Use Spacecraft SAA,<br>2: Use 3-circle method|Flag to determine how to determine when XRT<br>is in the SAA|
|SAA_PARMS|Composite:<br>9{FLOAT}9|3-circle method parameters:<br>Circle 1 center: longitude<br>Circle 1 center: latitude<br>Circle 1 radius<br>Circle 2 center: longitude<br>Circle 2 center: latitude<br>Circle 2 radius<br>Circle 3 center: longitude<br>Circle 3 center: latitude<br>Circle 3 radius|
|SC_CHKS_32|Type CHKS_32<br>Location: eeBase32 + 0xAF01FC<br>Value:  (See CHKS_32)|Stored 32-Bit checksum on System<br>Configuration Area|
|SC_CHKS_NEW|Type CHKS_32|Freshly calculated 32-Bit checksum on System<br>Configuration Area|
|SC_TIME|Composite:<br>SC_TIME_HI +<br>SC_TIME_MI +<br>SC_TIME_LO|Spacecraft Time|
|SC_TIME_HI|Type: UINT16<br>Units:  65536 seconds|Spacecraft Time,<br>Seconds, Upper|
|SC_TIME_LO|Type UINT16<br>Units: Microseconds|Spacecraft Time,<br>Sub-seconds|
|SC_TIME_MI|Type: UINT16<br>Units: seconds|Spacecraft Time,<br>Seconds, Lower|
|SCLK_SECONDS|Type: UINT32|Spacecraft time in seconds|
|SCU_BUFFER_RATE|Type: UINT32|SCU Rate Buffering Parameter|
|SCU_XMIT_BYTES|Type: UINT32|Number of bytes transferred to SCU|
|SEQ_ID|Type: UINT8|Sequencer ID|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 66




















|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|SEQ_ID|Type: UINT8|Sequencer Program ID<br>Null, Image (4 modes: low-gain fast-exposure,<br>low-gain slow-exposure, high-gain fast-<br>exposure, high-gain slow-exposure), Photo-<br>Diode, Windowed Timing, Photon-Counting,<br>Bias Image Calculation, Bias Row Calculation,<br>Raw-Data, Predetermined Science Telemetry<br>Pattern|
|SEQ_PRG|Composite:<br>{BYTES}|Sequencer Program Image|
|SEQ_TBL|Composite: (TBR)<br>{SEQ_ID} +<br>{FLUX} +<br>{DAC_VOLTAGE}|Table with the following columns:<br>Mode: Null, Image (4 modes: low-gain fast-<br>exposure, low-gain slow-exposure, high-gain<br>fast-exposure, high-gain slow-exposure), Photo-<br>Diode, Windowed Timing, Photon-Counting,<br>Bias Image Calculation, Bias Row Calculation,<br>Raw-Data, Predetermined Science Telemetry<br>Pattern<br>Counts Per Second (CPS)<br>Sequence Program No.<br>Charge Injection|
|SKIP_BIT|Type: UINT32<br>Value:<br>0x00000000-0x736B697F: Perform BIT<br>0x736B6970: Skip Stage 1 BIT<br>0x736B6971-0xFFFFFFFF: Perform BIT|Skip Stage 1 Built-In Tests|
|SS_DATA|{BYTES}|The detailed format of the stored science data is<br>contained in XRT-PSU-028 Section 4.  The<br>CCSDS headers and checksums listed in the<br>document are not part of this data dictionary<br>item.|
|ST_PDU|Composite:<br>XFER_REQ_CNTR<br>{CCSDS_TLM_PKT}|Swift telemetry data protocol data unit|
|STATE_CODE|Type: UINT8|State Code|
|STATE_NEXT|Type: STATE_CODE|Next State|
|STRING|Type: Fundamental, char *|Character String|
|STRIP_INTERVAL|Type: PP_RATE|Strip-chart interval|
|SYSTEM_BLOCK|Composite:<br>SYSTEM_CONFIG_AREA +<br>SYSTEM_VOLATILE_AREA +<br>BIT_DATA<br>Location:<br>eeBase32 + 0xAF0000 through<br>eeBase32 + 0xAFFFFF|System Configuration Block|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 67






















|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|SYSTEM_CONFIG_AREA|Composite:<br>SKIP_BIT +<br>MEM_SIZE +<br>ENET_MAC +<br>CPU_SPEED +<br>BC1_START_ADDR +<br>BC1_END_ADDR +<br>BC1_ENTRY_ADDR +<br>BC1_CHKS_32 +<br>ENET_IP +<br>ENET_HOST_IP +<br>SC_CHKS_32<br>Location:<br>eeBase32 + 0xAF0000 through<br>eeBase32 + 0xAF01FF|System Configuration Area|
|SYSTEM_VOLATILE_AREA|Composite:<br>BC_INDEX +<br>BOOT_CNT +<br>XCP_MODE +<br>CQ_START_ADDR<br>Location:<br>eeBase32 + 0xAF0400 through<br>eeBase32 + 0xAF05FF|System Volatile Area|
|TAM_BORE_LED1|Type: UINT16 (TBR)|LED 1 Boresight Offset|
|TAM_BORE_LED2|Type: UINT16 (TBR)|LED 2 Boresight Offset|
|TAM_CMD|Type: CMD|Telescope Alignment Monitor Command|
|TAM_DATA|Composite: (TBD)<br>{BYTES}|Telescope Alignment Monitor Data|
|TAM_RDFQ|Type: UINT16 (TBR)|TAM Sampling Period in Seconds|
|TAM_RS422_CMD|Type: CMD|Telescope Alignment Monitor Command|
|TARGET_ID|Type: UINT16|Target ID<br>(from FO_NEXTOBS_INFO)|
|TASK_BLOCK|Composite:<br>TASK_DELAY +<br>TASK_ID +<br>TASK_PRIORITY +<br>TASK_STATUS +<br>TASK_PC +<br>TASK_SP +<br>TASK_ERRNO|Task Control Block Information|
|TASK_DELAY|Type: UINT32|Task Delay (number of clock ticks task is<br>sleeping)|
|TASK_ERRNO|Type: UINT32|Task Error Number|
|TASK_ID|Type: ADDRESS|Task Identifier,<br>Pointer to Task Control Block|
|TASK_PC|Type: ADDRESS|Task Program Counter|
|TASK_PRIORITY|Type: UINT8|Task Priority|
|TASK_SP|Type: ADDRESS|Task Stack Pointer|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 68










|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|TASK_STATUS|Type: UINT8|Task Status|
|TEC_ACOOL_DCOEFF|Type: FLOAT (TBR)|TEC Automatic Cooling Derivative Coefficient|
|TEC_ACOOL_ICOEFF|Type: FLOAT (TBR)|TEC Automatic Cooling Integral Coefficient|
|TEC_ACOOL_PCOEFF|Type: FLOAT (TBR)|TEC Automatic Cooling Proportional Coefficient|
|TEC_ACOOL_RR|Type: UINT8 (TBR)|TEC Automatic Cooling Ramp Rate<br>(Percentage)|
|TEC_ACOOL_SETPT|Type: UINT16 (TBR)|TEC Automatic Cooling Set Point|
|TEC_AHEAT_DCOEFF|Type: FLOAT (TBR)|TEC Automatic Heating Derivative Coefficient|
|TEC_AHEAT_ICOEFF|Type: FLOAT (TBR)|TEC Automatic Heating Integral Coefficient|
|TEC_AHEAT_PCOEFF|Type: FLOAT (TBR)|TEC Automatic Heating Proportional Coefficient|
|TEC_AHEAT_RR|Type: FLOAT (TBR)|TEC Automatic Heating Ramp Rate|
|TEC_AHEAT_SETPT|Type: UINT16 (TBR)|TEC Automatic Heating Set Point|
|TEC_AHEAT_TIMEOUT|Type: UINT16 (TBR)|TEC Automatic Heating Timeout|
|TEC_CMD|Type: CMD|Thermo-Electric Cooler Command|
|TEC_MCOOL_RR|Type: UINT8 (TBR)|TEC Manual Cooling Ramp Rate<br>(Percentage)|
|TEC_MHEAT_RR|Type: UINT8 (TBR)|TEC Manual Heating Ramp Rate<br>(Percentage)|
|TEC_MHEAT_TIMEOUT|Type: UINT16 (TBR)|TEC Manual Heating Timeout|
|TEC_PARMS_TBL|Composite:<br>TEC_ACOOL_SETPT +<br>TEC_SENS_ID +<br>TEC_ACOOL_RR +<br>TEC_ACOOL_PCOEFF +<br>TEC_ACOOL_ICOEFF +<br>TEC_ACOOL_DCOEFF +<br>TEC_AHEAT_SETPT +<br>TEC_SENS_ID +<br>TEC_AHEAT_RR +<br>TEC_AHEAT_PCOEFF +<br>TEC_AHEAT_ICOEFF +<br>TEC_AHEAT_DCOEFF +<br>TEC_AHEAT_TIMEOUT +<br>TEC_VOLTAGE +<br>TEC_MCOOL_RR +<br>TEC_VOLTAGE +<br>TEC_MHEAT_RR +<br>TEC_MHEAT_TIMEOUT|TEC Parameters Table|
|TEC_SENS_ID|Type: UINT8<br>Value:<br>0: Sensor 1<br>1: Sensor 2|TEC Temperature Sensor ID|
|TEC_VOLTAGE|Type: UINT16 (TBR)|TEC Voltage (for Manual Cooling/Heating)|
|TGT_ID|Type: UINT16|Target ID|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 69




















|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|THC_PARMS_TBL|Composite:<br>THTR_PWR +<br>THTR_RESIST +<br>THTR_LIMIT +<br>{THTR_PARMS}|Tube Heater Control Parameters Table|
|THTR_ENABLE|Type: UINT8<br>Value:<br>0: Automatic Control<br>1-255: Manual Control|Tube Heater Control Manual Control Flag|
|THTR_ID|Type: UINT8|Tube Heater ID|
|THTR_LIMIT|Type: UINT8|Maximum number of tube heaters that can be<br>on simultaneously in manual mode.|
|THTR_PARMS|Composite:<br>THTR_SETPT_LO +<br>THTR_SETPT_HI +<br>THTR_ENABLE|Tube Heater Control Parameters|
|THTR_PWR|Type: UINT8|Power budget in volts for the tube heaters.|
|THTR_RESIST|Type: UINT16|Resistance in ohms for one of the tube heaters<br>(all are assumed to be the same).|
|THTR_SETPT_HI|Type: UINT16|Tube Heater Control Upper Threshold|
|THTR_SETPT_LO|Type: UINT16|Tube Heater Control Lower Threshold|
|TIMING_PARMS|Composite: TBD|Timing Algorithm Parameters|
|TIMING_THRSH|Type: UINT16|Timing Threshold|
|TLM_DATA|{BYTES}|The detailed format of the real-time<br>housekeeping telemetry data is contained in<br>XRT-PSU-028 Section 3.  The CCSDS headers<br>and checksums listed in the document are not<br>part of this data dictionary item.|
|TSM_IMR|Type: UINT16<br>Location:<br>tsmBase16 + 0xA10300<br>Bits:<br>15-8: Reserved<br>7: Watchdog Interrupt<br>6-0: Reserved|TSM Interrupt Mask Register|
|TSM_IPR|Type: UINT16<br>Location:<br>tsmBase16 + 0xA10304<br>Bits:<br>15-8: Reserved<br>7: Watchdog Interrupt<br>6-0: Reserved|TSM Interrupt Pending Register|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 70
















|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|TSM_IVR|Location:<br>tsmBase16 + 0xA10308<br>Bits:<br>15-8: Reserved<br>7: Watchdog Interrupt<br>6-0: Reserved|TSM Interrupt Vector Registers|
|TSM_MCR|Type: UINT16 (TBD)<br>Bits:<br>15-1: Reserved<br>0: EEPROM Write Inhibit|Memory Control Register|
|TSM_MEM_INS|Type: UINT16<br>Location:<br>tsmBase16 + 0x000000 through<br>tsmBase16 + 0x3FFFFC|TSM DSP 21020 Instruction SRAM|
|TSM_P2_ENABLE|Type: UINT16<br>tsmBase16 + 0xA10310<br>Bits:<br>15-1: Reserved<br>0: Output Latch Enable<br>    (Write: 0 – Disable, 1 – Enable)|TSM DSP to P2 Output Latch Enable|
|TSM_RESET|Type: UINT16<br>tsmBase16 + 0xA1030C<br>Bits:<br>15-1: Reserved<br>0: DSP Reset<br>    (Write: 0 – Release, 1 – Set/Hold Reset)|TSM DSP 21020 Hardware Reset Register|
|tsmBase16|Type: ADDRESS|TSM Base Address|
|UINT16|Type: Fundamental, unsigned short|Unsigned Short Integer|
|UINT32|Type: Fundamental, unsigned int|Unsigned Integer|
|UINT8|Type: Fundamental, unsigned char|Unsigned Character, Byte|
|UPLD_APARM1|Type: UINT32|Target address for memory uploads|
|UPLD_APARM2|Type: UINT32|Block Checksum|
|UPLD_DATA|Composite:<br>1{BYTE}42|Data Payload for Upload Command|
|UPLD_DATA_ID|Type: UINT8<br>Value:<br>0: Raw memory write<br>1: Sequencer Program|File System ID|
|UPLD_HDR|Composite:<br>UPLD_DATA_ID +<br>UPLD_SEQ_ID +<br>UPLD_APARM1+<br>UPLD_APARM2|Upload Header|
|UPLD_SEQ_ID|Type: SEQ_ID|Sequencer Program ID|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 71




















|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|UTC_DELTA|Composite:<br>UTC_DELTA_SECS +<br>UTC_DELTA_SUBSECS|Universal Time Coordinate offset|
|UTC_DELTA_SECS|Type: UINT32|Delta from Spacecraft time to compute UTC|
|UTC_DELTA_SUBSECS|Type: UINT16|Delta from Spacecraft time to compute UTC|
|UTC_SECONDS|Type: UINT32|UTC seconds<br>(from SISCATTITUDE)|
|UTC_SUBSECONDS|Type: UINT16|UTC sub-seconds<br>(from SISCATTITUDE)|
|UTC_TIME|Type: SC_TIME|Universal Time Coordinate|
|VALVE_HTR_ID|Type: UINT8<br>Value:<br>1: Heating Element 1<br>2: Heating Element 2|Valve Heater ID|
|VALVE_TIMEOUT|Type: UINT8|Timeout in seconds|
|XCM_1553|Composite:<br>XCM_1553_BIT +<br>XCM_1553_BLK +<br>XCM_1553_CTRL +<br>XCM_1553_CWD +<br>XCM_1553_ILL +<br>XCM_1553_ILR +<br>XCM_1553_IMR +<br>XCM_1553_INIT +<br>XCM_1553_IPR +<br>XCM_1553_RTBITS +<br>XCM_1553_STS +<br>XCM_1553_TMR|XCM 1553 Interface|
|XCM_1553_BASE|Type: ADDRESS<br>Value:<br>xcmBase16 + 0x20000|Base address of 1553 Interface Chip|
|XCM_1553_BIT|Type: UINT16<br>Location: xcmBase16 + 0x00000C<br>Bits:<br>15: DMA Fail<br>14: Wrap Fail<br>13: Terminal Address Parity Fail<br>12: BIT Fail<br>11: Channel A Fail<br>10: Channel B Fail<br>9-0: User-Defined Bits|Summit Interrupt BIT Word Register|
|XCM_1553_BLK|Type: UINT16<br>Location: xcmBase16 + 0x000010<br>Bits:<br>15-0: Remote Terminal Descriptor Address Bits|Summit Remote Terminal Descriptor Pointer<br>Register|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 72








|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|XCM_1553_CTRL|Type: UINT16<br>Location: xcmBase16 + 0x000000<br>Bits:<br>15: Start Execution<br>14: Start BIT<br>13: Start Software Reset<br>12: Channel A Enable<br>11: Channel B Enable<br>10: External Timer Clock Enable<br>9-7: Reserved<br>6: Buffer Mode Enable<br>5: Reserved<br>4: Broadcast Enable<br>3: Dynamic Bus Control Acceptance<br>2: Ping-Pong Enable<br>1: Interrupt Log Enable<br>0: Transmit Last Status Word|Summit Control Register|
|XCM_1553_CWD|Type: UINT16<br>Location: xcmBase16 + 0x000004<br>Bits:<br>15-0: Current Command Bits|Summit Current Command Register|
|XCM_1553_ILL|Type: UINT16<br>Location: xcmBase16 + 0x000020<br>Bits: Refer to UTMC-SUMMIT|Summit Illegalization Register|
|XCM_1553_ILR|Type: UINT16<br>Location: xcmBase16 + 0x00000A<br>Bits:<br>15-0: Interrupt Log List Pointer Bits|Summit Interrupt Log List Pointer Register|
|XCM_1553_IMR|Type: UINT16<br>Location: xcmBase16 + 0x000006<br>Bits:<br>15: DMA Fail Interrupt<br>14: Wrap Fail Interrupt<br>13: Terminal Address Parity Fail Interrupt<br>12: BIT Fail Interrupt<br>11: Message Error Interrupt<br>10: Subaddress Accessed Interrupt<br>9: Broadcast Command Received Interrupt<br>8: Index Equal Zero Interrupt<br>7: Illegal Command Interrupt<br>6-0: Reserved|Summit Interrupt Mask Register|
|XCM_1553_INIT|Type: UINT16<br>Location: xcmBase16 + 0x000014<br>Bits:  Refer to UTMC-SUMMIT|Summit Initialization Block Register|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 73








|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|XCM_1553_IPR|Type: UINT16<br>Location: xcmBase16 + 0x000008<br>Bits:<br>15: DMA Fail Interrupt<br>14: Wrap Fail Interrupt<br>13: Terminal Address Parity Fail Interrupt<br>12: BIT Fail Interrupt<br>11: Message Error Interrupt<br>10: Subaddress Accessed Interrupt<br>9: Broadcast Command Received Interrupt<br>8: Index Equal Zero Interrupt<br>7: Illegal Command Interrupt<br>6-0: Reserved|Summit Interrupt Pending Register|
|XCM_1553_RTBITS|Type: UINT16<br>Location: xcmBase16 + 0x000012<br>Bits:<br>15: Immediate Clear Function<br>14-10: Reserved<br>9: Instrumentation Bit<br>8: Service Request Bit<br>7-4: Reserved<br>3: Busy<br>2: Subsystem Flag Bit<br>1: Reserved<br>0: Terminal Flag|Summit Status Word Bits Register|
|XCM_1553_STS|Type: UINT16<br>Location: xcmBase16 + 0x000002<br>Bits:<br>15: Terminal Address Bit 4<br>14: Terminal Address Bit 3<br>13: Terminal Address Bit 2<br>12: Terminal Address Bit 1<br>11: Terminal Address Bit 0<br>10: Terminal Address Parity<br>9: Mode Select 1<br>8: Mode Select 0<br>7: Military Standard A or B<br>6: LOCK Pin<br>5: AUTOEN Pin<br>4: SSYSF Pin<br>3: Summit MCM-C Executing<br>2: Terminal Parity Fail<br>1: READY Pin<br>0: TERACT Pin|Summit Operational Status Register|
|XCM_1553_TMR|Type: UINT16<br>Location: xcmBase16 + 0x00000E<br>Bits:<br>15-0: Time-tag Counter Bits|Summit Time-Tag Register|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 74








|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|XCM_APMI_CSR|Type: UINT16<br>Location: xcmBase16 + 0x010426<br>Bits:<br>15: Reset FIFO<br>  (Write: 1 – Reset)<br>14: End-Of-Line Interrupt Enable<br>  (Write: 1 – Enable)<br>13: End-Of-Line Interrupt Status<br>  (Read: 0 – No interrupt, 1 – Interrupt present)<br>  (Write: 1 – Reset interrupt)<br>12: End-Of-Frame Interrupt Enable<br>  (Write: 1 – Enable)<br>11: End-Of-Frame Interrupt Status<br>  (Read: 0 – No interrupt, 1 – Interrupt present)<br>  (Write: 1 – Reset interrupt)<br>10: Overflow Interrupt Enable<br>  (Write: 1 – Enable)<br>9: Overflow Interrupt Status<br>  (Read: 0 – No interrupt, 1 – Interrupt present)<br>  (Write: 1 – Reset interrupt)<br>8: Half Full Flag<br>  (0 – Not half-full, 1 – At least half full)<br>7: Empty Flag<br>  (0 – Not empty, 1 – FIFO is empty)<br>6: FIFO Read Error<br>  (0 – No error, 1 – Read past end)<br>5-4: Reserved<br>3-0: EOL Interrupt Count<br>  (Number of EOL flags before EOL Interrupt)|XCM APMI Control and Status Register|
|XCM_APMI_EOL|Type: UINT16<br>Location: xcmBase16 + 0x010426<br>Bits:<br>15-9: Reserved<br>8: EOL Counter Overflow<br>7-0: EOL Counter|XCM APMI End-Of-Line Counter Register|
|XCM_CCD_FIFO|Type: UINT16<br>Location: xcmBase16 + 0x010100|XCM CCD Data FIFO|
|XCM_DAC1_CTRL|Type: UINT16<br>Location: xcmBase16 + 0x010428<br>Bits:<br>15-0: Timer Bits|XCM DAC1 Control Register|
|XCM_DAC2_CTRL|Type: UINT16<br>Location: xcmBase16 + 0x010428<br>Bits:<br>15-0: Timer Bits|XCM DAC2 Control Register|
|XCM_EEPROM|Type: {UINT32}<br>Locations:<br>eeBase32 + 0x800000 through<br>eeBase32 + 0xAFFFFC|EEPROM on the XCM.<br>Refer to Appendix B for memory map.|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 75








|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|XCM_ENET|Composite:<br>{UINT16}|Ethernet engineering support board control and<br>data registers|
|XCM_ENET_BASE|Type: ADDRESS<br>Value:<br>xcmBase16 + 0x020300|Base address of Ethernet External Port|
|XCM_HK_CSR|Type: UINT16<br>Location: xcmBase16 + 0x010426<br>Bits:<br>15: Reset HK FIFO<br>  (Write: 1 – Reset FIFO)<br>14: Reserved<br>13-12: Acquisition Mode Set<br>11: Reserved<br>10: FIFO Empty Flag<br>9: Frame Received Interrupt Status<br>8: Frame Received Interrupt Enable<br>7-0:  Multiplexer Address Set|XCM Housekeeping Control and Status Register|
|XCM_HK_FIFO|Type: UINT16<br>Location: xcmBase16 + 0x010200|XCM Housekeeping Data FIFO|
|XCM_HK_START|Type: UINT16<br>Location: xcmBase16 + 0x010426<br>Bits:<br>15-0: Reserved|XCM Housekeeping Start Register (Write Only)<br>Write to register starts Analog/Digital<br>Conversion according to mode set in<br>XCM_HK_CSR|
|XCM_IMR|Type: UINT16<br>Location: xcmBase16 + 0x020604<br>Bits:<br>15-7: Reserved<br>6: 1553 Interrupt<br>5: Rx Ready Interrupt<br>4: HK Done Interrupt<br>3: APMI Error Interrupt<br>2: APMI EOL or EOF Interrupt<br>1: Ethernet Interrupt<br>0: Reserved|XCM Interrupt Mask Register|
|XCM_IPR|Type: UINT16<br>Location: xcmBase16 + 0x020606<br>Bits:<br>15-7: Reserved<br>6: 1553 Interrupt<br>5: Rx Ready Interrupt<br>4: HK Done Interrupt<br>3: APMI Error Interrupt<br>2: APMI EOL or EOF Interrupt<br>1: Ethernet Interrupt<br>0: Reserved|XCM Interrupt Pending Register|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 76














|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|XCM_IVR|Type: UINT16<br>Location: xcmBase16 + 0x020608<br>Bits:<br>15-8: Reserved<br>7-3: VME Status/ID<br>2-0: IRQ (Read only)|XCM Interrupt Vector Register|
|XCM_MEM_1553|Composite: {UINT16}<br>Location:<br>xcmBase16 + 0x030000 through<br>xcmBase16 + 0x03FFFC|MIL-STD-155B Shared Memory|
|XCM_MEM_ENET|Type: {UINT32}|Ethernet engineering support board memory|
|XCM_METCSR|Type: UINT16<br>Location: xcmBase16 + 0x020616<br>Bits:<br>15-3: Reserved<br>2: MET Reset Enable<br>1: MET Time Jam Enable<br>0: MET PPS Source Select|MET Control and Status Register|
|XCM_METRST|Type: UINT16<br>Location: xcmBase16 + 0x020618<br>Bits:<br>15-0: Reserved|MET Reset Register|
|XCM_SER_CSR|Type: UINT16<br>Location: xcmBase16 + 0x010426<br>Bits:<br>15-10: Reserved<br>9: Serial Channel 2 Frame Error<br>8: Serial Channel 1 Frame Error<br>7: Serial Channel 2 Tx Interrupt Enable<br>6: Serial Channel 2 Rx Interrupt Enable<br>5: Serial Channel 2 Tx Empty<br>4: Serial Channel 2 Rx Ready<br>3: Serial Channel 1 Tx Interrupt Enable<br>2: Serial Channel 1 Rx Interrupt Enable<br>1: Serial Channel 1 Tx Empty<br>0: Serial Channel 1 Rx Ready|XCM Serial Interface Control and Status<br>Register|
|XCM_SER_RX|Composite:<br>XCM_SER1_RX +<br>XCM_SER2_RX|XCM RS-422 Receive Registers|
|XCM_SER_TX|Composite:<br>XCM_SER1_TX +<br>XCM_SER2_TX|XCM RS-422 Transmit Registers|
|XCM_SER1_RX|Type: UINT16<br>Location: xcmBase16 + 0x010426<br>Bits: 2 bytes received|XCM Serial Interface 1 Receive Register|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 77














|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|XCM_SER1_TX|Type: UINT16<br>Location: xcmBase16 + 0x010426<br>Bits:<br>15-0: 2 bytes to transmit|XCM Serial Interface 1 Transmit Register|
|XCM_SER2_RX|Type: UINT16<br>Location: xcmBase16 + 0x010426<br>Bits: 2 bytes received|XCM Serial Interface 2 Receive Register|
|XCM_SER2_TX|Type: UINT16<br>Location: xcmBase16 + 0x010426<br>Bits: 2 bytes to transmit|XCM Serial Interface 2 Transmit Register|
|XCM_TMFINE|Type: UINT16<br>Location: xcmBase16 + 0x010428<br>Bits:<br>15-0: Timer Bits|XCM Timer Register Fine|
|XCM_TMHI|Type: UINT16<br>Location: xcmBase16 + 0x010424<br>Bits:<br>15-0: Timer Bits|XCM Timer Register High|
|XCM_TMLO|Type: UINT16<br>Location: xcmBase16 + 0x010426<br>Bits:<br>15-0: Timer Bits|XCM Timer Register Low|
|XCM_WDR|Type: UINT16<br>Location: xcmBase16 + 0x010436<br>Bits:<br>15-0: Reserved|XCM Watchdog Strobe Register<br>A write to this register, regardless of contents,<br>strobes the watchdog timer on the Power Supply<br>Module (PSM).|
|xcmBase16|Type: ADDRESS<br>Value: 0xCF000000|Base address of XCM (D16 access)<br>(Base address of XCM is 0xFF000000 VME.)|
|XCP_BYTES_LAST|Type: UINT32|Number of bytes sent by XCP last spin|
|XCP_DRAM|Type: UINT32|XCP Main Memory|
|XCP_EEPROM|Composite:<br>{UINT32}|XCP EEPROM<br>(See Appendix B.)|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 78










|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|XCP_EICR_EIM0|Type: UINT16<br>Location: eicrBase32 + 0x000000<br>Bits:<br>31: RBI Timer Interrupt<br>30: Reserved<br>29: UART Interrupts<br>28-24: Reserved<br>23: VME IRQ 7<br>22: VME IRQ 6<br>21: VME IRQ 5<br>20: VME IRQ 4<br>19: VME IRQ 3<br>18: Reserved<br>17: VME IRQ 2<br>16: VME IRQ 1<br>15-0: Reserved|External Interrupt Mask Register|
|XCP_EICR_MEAR|Type: UINT16<br>Location: eicrBase32 + 0x00001C<br>Bits:<br>31-24: Syndrome<br>23-0:  Bits 3-26 or Real Address|Machine Check Error Address Register|
|XCP_EICR_MESR|Type: UINT16<br>Location: eicrBase32 + 0x000018<br>Bits:<br>31: Error occurred in Diagnostic Mode<br>30: Error occurred on a processor load or store<br>29: Reserved<br>28: Address Exception<br>27: Attempted store into a Read-Only Segment<br>26: Uncorrectable ECC Error<br>25-0: Reserved|Machine Check Error Status Register|
|XCP_EICR_SBAR|Type: UINT16<br>Location: eicrBase32 + 0x00002C<br>Bits:<br>31-24: Syndrome<br>23-0:  Bits 3-26 or Real Address|Single-Bit Error Address Register|
|XCP_EICR_SBSR|Type: UINT16<br>Location: eicrBase32 + 0x000028<br>Bits:<br>31: Single-Bit ECC Error<br>30-0: Reserved|Single-Bit Error Status Register|
|XCP_EICRS|Composite:<br>EICR_MEAR +<br>EICR_MESR +<br>EICR_SBAR +<br>EICR_SBSR +<br>EICR_EIM0|External Interrupt Control Registers|
|XCP_FUNC_ENABLED|Type: BOOL|Indicates whether or not a particular automatic<br>control function is enabled.|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 79








|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|XCP_IOCC|Composite:<br>XCP_IOCC_IRQ_REGS +<br>XCP_IOCC_RBI_TIMER +<br>XCP_IOCC_INT_REG +<br>XCP_IOCC_EOI_REGS|Input/Output Channel Controller Registers|
|XCP_IOCC_EOI_IRQ1|Type: UINT32<br>Location: ioccBase32 + 0x41008C<br>Bits:<br>31-0: Reserved|End of Interrupt Register (IRQ1)|
|XCP_IOCC_EOI_IRQ2|Type: UINT32<br>Location: ioccBase32 + 0x42008C<br>Bits:<br>31-0: Reserved|End of Interrupt Register (IRQ2)|
|XCP_IOCC_EOI_IRQ3|Type: UINT32<br>Location: ioccBase32 + 0x43008C<br>Bits:<br>31-0: Reserved|End of Interrupt Register (IRQ3)|
|XCP_IOCC_EOI_IRQ4|Type: UINT32<br>Location: ioccBase32 + 0x44008C<br>Bits:<br>31-0: Reserved|End of Interrupt Register (IRQ4)|
|XCP_IOCC_EOI_IRQ5|Type: UINT32<br>Location: ioccBase32 + 0x45008C<br>Bits:<br>31-0: Reserved|End of Interrupt Register (IRQ5)|
|XCP_IOCC_EOI_IRQ6|Type: UINT32<br>Location: ioccBase32 + 0x46008C<br>Bits:<br>31-0: Reserved|End of Interrupt Register (IRQ6)|
|XCP_IOCC_EOI_REGS|Composite:<br>IOCC_EOI_SYSFAIL +<br>IOCC_EOI_IRQ1 +<br>IOCC_EOI_IRQ2 +<br>IOCC_EOI_IRQ3 +<br>IOCC_EOI_IRQ4 +<br>IOCC_EOI_IRQ5 +<br>IOCC_EOI_IRQ6 +<br>IOCC_EOI_IRQ7|End of Interrupt Registers|
|XCP_IOCC_EOI_SYSFAIL|Type: UINT32<br>Location: ioccBase32 + 0x40008C<br>Bits:<br>31-0: Reserved|End of Interrupt Register (SYSFAIL)|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 80










|Table 7. Data Dictionary|Col2|Col3|
|---|---|---|
|**Name**|**Attributes**|**Description**|
|XCP_IOCC_RBI_CFG|Type: UINT32<br>Location: ioccBase32 + 0x400010<br>Bits:<br>31: Master Enable<br>30: Reserved<br>29-28: Turbo clock<br>27-26: VME AML<br>25-24: VME LIM<br>23: Reserved<br>22-20: TCW Table Size<br>19: Reserved<br>18: Bus Hold/ 3P DMA K bit<br>17: PIO/3P Select<br>16: Clock Control<br>15-0: Reserved|RBI Configuration Register|
|XCP_IOCC_RBI_TIMER|Type: UINT32<br>Location: ioccBase32 + 0x480004<br>Bits:<br>31-16: Interrupt Interval<br>(two’s complement of interval)<br>15-0: Reserved<br>Units:<br>2.17µsecs|RBI Time Control Register,<br>Real Time Incrementer (Interval Timer)|
|XCP_IOCC_SYSFAIL|Type: UINT32<br>Location: ioccBase32 + 0x400004<br>Bits:<br>31-0: Reserved|VME SYSFAIL Interrupt Register,<br>Store Generate,<br>Load Acknowledge|
|XCP_PROM|Composite: {UINT32}<br>Location:<br>eeBase32 + 0x0A0000 through<br>eeBase32 + 0x0A7FFC|Bootstrap Area in EEPROM|
|XCP_PROM_CHKS|Type: CHKS_32<br>Location: eeBase32 + 0x0A7FFC<br>Value: (See CHKS_32)|Preprogrammed PROM Checksum|
|XCP_PROM_MBE|Type: UINT32<br>Location: eeBase32 + 0x0A7FF4<br>Value: 0xC0000000 (uncorrected)|Preprogrammed PROM Multiple Bit Error<br>Location|
|XCP_PROM_SBE|Type: UINT32<br>Location: eeBase32 + 0x0A7FF8<br>Value:<br>0x00000000 (corrected)<br>0x80000000 (uncorrected)|Preprogrammed PROM Single-Bit Error<br>Location|
|XCP_RTCL|Type: UINT16|XCP Real-time Clock low|
|XCP_RTCU|Type: UINT16|XCP Real-time Clock upper|
|XCP_STATE|Type: STATE_CODE|System State|
|XFER_REQ_CNTR|Type: UINT16|ST_PDU transfer request counter|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page 81


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page A-1


## **APPENDIX A** **DETAILED SOFTWARE REQUIREMENTS**

Note: If reviewing this document electronically, the detailed software requirements are contained

in a separate Microsoft® Excel spreadsheet file, _04121-xrtsrs-01.xls_ .


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page B-1


## **APPENDIX B** **EEPROM MEMORY MAPS**

The following table details the locations of the various components of the Electrically-Eraseable Programmable
Read-Only Memory, **XCP_EEPROM** .






|Table 8. XCP_EEPROM Memory Map|Col2|
|---|---|
|**Location**|**Data Dictionary Entry**|
|eeBase32 + 0x800000 through<br>eeBase32 + 0x807FFF|BOOT_BLOCK|
|eeBase32 + 0x808014 through<br>eeBase32 + 0x88FFFF|PRIME_OS_BLOCK|
|eeBase32 + 0x980000 through<br>eeBase32 + 0x98FFFF|ALT_OS_BLOCK|
|eeBase32 + 0xA00000 through<br>eeBase32 + 0xAEFFFF|FILE_SYSTEM_BLOCK|
|eeBase32 + 0xAF0000 through<br>eeBase32 + 0xAFFFFF|SYSTEM_BLOCK|



The following table details the locations of the various components of the **SYSTEM_BLOCK** .






|Table 9. SYSTEM_BLOCK Memory Map|Col2|
|---|---|
|**Location**|**Data Dictionary Entry**|
|eeBase32 + 0xAF0000 through<br>eeBase32 + 0xAF01FF|SYSTEM_CONFIG_AREA|
|eeBase32 + 0xAF0200 through<br>eeBase32 + 0xAF03FF|Reserved|
|eeBase32 + 0xAF0400 through<br>eeBase32 + 0xAF05FF|SYSTEM_VOLATILE_AREA|
|eeBase32 + 0xAF0600 through<br>eeBase32 + 0xAF0FFF|Reserved|
|eeBase32 + 0xAF1000 through<br>eeBase32 + 0xAF11FF|BIT_DATA|
|eeBase32 + 0xAF1200 through<br>eeBase32 + 0xAFFFFF|Reserved|



The following table details the locations of the components of the **SYSTEM_CONFIG_AREA** .


|Table 10. SYSTEM_CONFIG_AREA Memory Map|Col2|
|---|---|
|**Location**|**Data Dictionary Entry**|
|eeBase32 + 0xAF0000|Reserved|
|eeBase32 + 0xAF0004|COLD_SKIP_BIT|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page B-2





















|Table 10. SYSTEM_CONFIG_AREA Memory Map|Col2|
|---|---|
|**Location**|**Data Dictionary Entry**|
|||
|eeBase32 + 0xAF0008 through<br>eeBase32 + 0xAF0008|Reserved|
|eeBase32 + 0xAF0010|COLD_MEM_SIZE|
|eeBase32 + 0xAF0014 through<br>eeBase32 + 0xAF0018|ENET_MAC (Test Only)|
|eeBase32 + 0xAF001C through<br>eeBase32 + 0xAF0030|Reserved|
|eeBase32 + 0xAF0034|CPU_SPEED|
|eeBase32 + 0xAF0038|Reserved|
|eeBase32 + 0xAF003C|Reserved|
|eeBase32 + 0xAF0040|BC1_START_ADDR|
|eeBase32 + 0xAF0044|BC1_END_ADDR|
|eeBase32 + 0xAF0048|BC1_COPY_ADDR|
|eeBase32 + 0xAF004C|BC1_ENTRY_ADDR|
|eeBase32 + 0xAF0050|BC1_CHKS_32|
|eeBase32 + 0xAF0054 through<br>eeBase32 + 0xAF01F0|Reserved|
|eeBase32 + 0xAF01F4|ENET_IP (Test only)|
|eeBase32 + 0xAF01F8|ENET_HOST_IP (Test only)|
|eeBase32 + 0xAF01FC|SC_CHKS_32|


The following table details the locations of the components of the **SYSTEM_VOLATILE_AREA** .






|Table 11. SYSTEM_VOLATILE_AREA Memory Map|Col2|
|---|---|
|**Location**|**Data Dictionary Entry**|
|eeBase32 + 0xAF0400|BC_INDEX|
|eeBase32 + 0xAF0404|BOOT_CNT|
|eeBase32 + 0xAF0408 though<br>eeBase32 + 0xAF05FF|Reserved|



The following table details the locations of the components of the **BIT_DATA** .








|Table 12. BIT_DATA Memory Map<br>Value: (one result/word [4 bytes])<br>Failure: FFFFFFFF<br>Success: 00000000|Col2|
|---|---|
|**Location**|**Data Dictionary Entry**|
|eeBase32 + 0xAF1000 through<br>eeBase32 + 0xAF103C|Reserved|
|eeBase32 + 0xAF1040|BIT_CPU_BRANCH|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page B-3












|Table 12. BIT_DATA Memory Map<br>Value: (one result/word [4 bytes])<br>Failure: FFFFFFFF<br>Success: 00000000|Col2|
|---|---|
|**Location**|**Data Dictionary Entry**|
|eeBase32 + 0xAF1044|BIT_CPU_FXPT|
|eeBase32 + 0xAF1048|BIT_CPU_FLTPT|
|eeBase32 + 0xAF104C|BIT_CPU_INT|
|eeBase32 + 0xAF1050|Reserved|
|eeBase32 + 0xAF1054|BIT_CPU_TIMER|
|eeBase32 + 0xAF1058|BIT_EDAC_SBE|
|eeBase32 + 0xAF105C|BIT_EDAC_MBE|
|eeBase32 + 0xAF1060|BIT_PROM_CHKS|
|eeBase32 + 0xAF1064 through<br>eeBase32 + 0xAF107C|Reserved|
|eeBase32 + 0xAF1080|BIT_1553_RAM|
|eeBase32 + 0xAF1084|BIT_1553_INT|
|eeBase32 + 0xAF1088 through<br>eeBase32 + 0xAF10FC|Reserved|
|eeBase32 + 0xAF1100 through<br>eeBase32 + 0xAF113C|BIT_DRAM|
|eeBase32 + 0xAF1140 through<br>eeBase32 + 0xAF11FC|Reserved|



The following table details the locations of the components of the **BIT_DRAM** .


|Table 13. BIT_DRAM Memory Map<br>Value: Packed (1 bit for each 256Kb block)<br>Failure: 1<br>Success: 0|Col2|
|---|---|
|**Location**|**Description**|
|eeBase32 + 0xAF1100|0MB-8MB Result|
|eeBase32 + 0xAF1104|8MB-16MB Result|
|eeBase32 + 0xAF1108|16MB-24MB Result|
|eeBase32 + 0xAF110C|24MB-32MB Result|
|eeBase32 + 0xAF1110|32MB-40MB Result|
|eeBase32 + 0xAF1114|40MB-48MB Result|
|eeBase32 + 0xAF1118|48MB-56MB Result|
|eeBase32 + 0xAF111C|56MB-64MB Result|
|eeBase32 + 0xAF1120|64MB-72MB Result|
|eeBase32 + 0xAF1124|72MB-80MB Result|
|eeBase32 + 0xAF1128|80MB-88MB Result|
|eeBase32 + 0xAF112C|88MB-96MB Result|
|eeBase32 + 0xAF1130|96MB-104MB Result|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page B-4


|Table 13. BIT_DRAM Memory Map<br>Value: Packed (1 bit for each 256Kb block)<br>Failure: 1<br>Success: 0|Col2|
|---|---|
|**Location**|**Description**|
|eeBase32 + 0xAF1134|104MB-112MB Result|
|eeBase32 + 0xAF1138|112MB-120MB Result|
|eeBase32 + 0xAF113C|120MB-128MB Result|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**

## **APPENDIX C** **TELECOMMANDS**


The following table lists the telecommands supported by XRT.



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page C-1








|Table 14. Telecommands|Col2|Col3|Col4|
|---|---|---|---|
|**Mnemonic**|**Description**|**State**|**Parameters (See Data Dictionary)**|
|FO_NEXTOBS_INFO|The FOM Has Identified a Target<br>Preliminary information from FOM<br>Peer Review presentation.|ALL|TARGET_ID,<br>RA,<br>DEC,<br>ROLL,<br>FO_OBS_MODE,<br>FO_OBS_TYPE,<br>PAST_OBS_TIME,<br>IS_AT_TARGET|
|SINOOP|Command ignored.<br>Broadcast Telecommand Test<br>See Spectrum Astro document #<br>1143-EI-S22904, Swift Spacecraft to<br>Payload Telecommand Interface<br>Control Document.|ALL|None|
|SISCATTITUDE|Attitude of the Spacecraft<br>See Spectrum Astro document #<br>1143-EI-S22904, Swift Spacecraft to<br>Payload Telecommand Interface<br>Control Document.|ALL|UTC_SECONDS,<br>UTC_SUBSECONDS,<br>TARGET_ID,<br>RA,<br>DEC,<br>ROLL,<br>LATTITUDE,<br>LONGITUDE,<br>ALTITUDE,<br>IN_SAA_FLAG,<br>IS_IN_10_ARCMIN,<br>IS_SETTLED,<br>IN_SAFE_MODE|
|SISLEWABORT|Command ignored.<br>The Spacecraft Has Aborted the Slew<br>See Spectrum Astro document #<br>1143-EI-S22904, Swift Spacecraft to<br>Payload Telecommand Interface<br>Control Document.|ALL|None|
|SISLEWWARNING|Command ignored.<br>The Spacecraft is About to Slew<br>See Spectrum Astro document #<br>1143-EI-S22904, Swift Spacecraft to<br>Payload Telecommand Interface<br>Control Document.|ALL|None|
|SITIMETONE|Time of the Spacecraft<br>See Spectrum Astro document #<br>1143-EI-S22904, Swift Spacecraft to<br>Payload Telecommand Interface<br>Control Document.|ALL|SCLK_SECONDS,<br>UTC_DELTA_SECS,<br>UTC_DELTA_SUBSECS|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page C-2
































|Table 14. Telecommands|Col2|Col3|Col4|
|---|---|---|---|
|**Mnemonic**|**Description**|**State**|**Parameters (See Data Dictionary)**|
|X_ALG_SET_CPARMS|Set the FPC's Centroid Algorithm<br>Parameters|MAN|CENT_PARMS|
|X_ALG_SET_CTHRSH|Set the FPC's Centroid Pixel<br>Threshold|MAN|CENT_THRSH|
|X_ALG_SET_ETHRSH|Set Event Threshold|MAN|EVENT_THRSH|
|X_ALG_SET_STHRSH|Set Split Event Threshold|MAN|EVENT_STHRSH|
|X_ALG_SET_TPARMS|Set Photo-Diode Mode and Windowed<br>Timing Mode Parameters<br>Photo-Diode Mode is primarily used to<br>generate light curves.<br>Windowed Timing Mode is primarily<br>used to generate a spectrum.|MAN|TIMING_PARMS|
|X_ALG_SET_TTHRSH|Set Photo-Diode Mode and Windowed<br>Timing Mode Event Threshold|MAN|TIMING_THRSH|
|X_ALG_SET_ULD|Set Upper Level Discriminator<br>The ULD is the upper energy<br>threshold used for the event<br>recognition algorithm.|MAN|EVENT_ULD|
|X_BHTR_DIS|Disable Thermal Baffle Control Heater|MAN|BHTR_ID|
|X_BHTR_EN|Enable Thermal Baffle Control Heater|MAN|BHTR_ID|
|X_BHTR_SET_PARMS|Set Thermal Baffle Control Heater's<br>Control Parameters|MAN|BHTR_PARMS|
|X_CCD_BASEL_DIS|Disable the FPC's Baseline Correction|MAN|None|
|X_CCD_BASEL_EN|Enable the FPC's Baseline Correction|MAN|None|
|X_CCD_CALC_MRC|Calculate Mean Row Correction Row|MAN|None|
|X_CCD_CLR_RAW_IM|Clear Raw Image Flag Manually|ALL|None|
|X_CCD_DAC_DIS|Disable DACs|MAN|None|
|X_CCD_DAC_EN|Enable DACs|MAN|None|
|X_CCD_DUMP_BAD_P|Dump Bad Pixel Table|MAN|None|
|X_CCD_DUMP_BAD_R|Dump Bad Row<br>For Photo-Diode and Windowed<br>Timing modes|MAN|None|
|X_CCD_DUMP_MRC|Dump the MRC Row|MAN|None|
|X_CCD_MRC_DIS|Mean Row Correction Disable|MAN|None|
|X_CCD_MRC_EN|Mean Row Correction Enable|MAN|None|
|X_CCD_RSET_BAD_P|Reset Bad Pixel in Bad Pixel Table<br>-1 to reset an entire row or column|MAN|BAD_PIX_ROW,<br>BAD_PIX_COL|
|X_CCD_RSET_BAD_R|Reset Bad Pixel in Bad Row<br>For Photo-Diode and Windowed<br>Timing modes|MAN|BAD_PIX_COL|
|X_CCD_SEL_B_ALG|Select the Focal Plane Camera’s<br>(FPC) Bias Algorithm|MAN|BIAS_ALG_ID|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page C-3


































|Table 14. Telecommands|Col2|Col3|Col4|
|---|---|---|---|
|**Mnemonic**|**Description**|**State**|**Parameters (See Data Dictionary)**|
|X_CCD_SEL_BMAP|Select the FPC's Active Bias Map|MAN|BIAS_MAP_ID|
|X_CCD_SEL_MRC_ALG|Select Mean Row Correction<br>Algorithm|MAN|MRC_ALG_ID|
|X_CCD_SEL_MRC_ROW|Select Mean Row Correction Row|MAN|MRC_ROW|
|X_CCD_SET_BAD_P|Set Bad Pixel in Bad Pixel Table<br>-1 to set an entire row or column|MAN|BAD_PIX_ROW,<br>BAD_PIX_COL|
|X_CCD_SET_BAD_R|Set Bad Pixel in Bad Row<br>For Photo-Diode and Windowed<br>Timing modes|MAN|BAD_PIX_COL|
|X_CCD_SET_BTHRSH|Set the FPC's Bias Threshold<br>When updating the bias, only use<br>pixels to update bias if less than<br>threshold.|MAN|BIAS_THRSH|
|X_CCD_SET_DAC_T|Set DAC Table<br>Set the CCD DAC value located in<br>memory and use for all future DAC<br>loads.|MAN|DAC_TBL|
|X_CCD_SET_MRC_FQ|Set MRC Row Update Frequency|MAN|MRC_FQ|
|X_CCD_SET_MTHRSH|Set MRC Threshold|MAN|MRC_THRSH|
|X_CCD_SET_RAW_IM|Set Raw Image Flag<br>A raw image report will be generated<br>at the beginning of the next spacecraft<br>slew, and the raw image flag is<br>cleared automatically by the XRT<br>FSW.|ALL|None|
|X_CCD_SET_RML|Set the FPC's Running Mean Length|MAN|RML|
|X_CLK_SET_TIME|Set Clock Time|MAN|SC_TIME|
|X_CLK_SYNC_DIS|Disable Time Synchronization with<br>Spacecraft|MAN|None|
|X_CLK_SYNC_EN|Enable Time Synchronization with<br>Spacecraft|MAN|None|
|X_HK_CMDECHO_DIS|Disable Command Echo|ALL|None|
|X_HK_CMDECHO_EN|Enable Command Echo|ALL|None|
|X_HK_SET_LIMITS|Set the Upper and Lower HK Limits<br>Critical HK parameters are monitored<br>by the flight software for proper<br>operating range.|MAN|PP_RANGE_TBL|
|X_HK_SET_PERIOD|Set Housekeeping Period|ALL|PP_RATE_TBL|
|X_HK_SET_STRIP|Set Stripchart Time Interval|ALL|STRIP_INTERVAL|
|X_HK_START_SEND|Resend Startup Packet|ALL|None|
|X_HK_STRIP_DIS|Disable Stripchart Mode|ALL|None|
|X_HK_STRIP_EN|Enable Stripchart Mode|ALL|None|
|X_LED_OFF|Turn Off the CCD Test LED|MAN|None|
|X_LED_ON|Turn On the CCD Test LED|MAN|None|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page C-4




























|Table 14. Telecommands|Col2|Col3|Col4|
|---|---|---|---|
|**Mnemonic**|**Description**|**State**|**Parameters (See Data Dictionary)**|
|X_MEM_DUMP|Download Memory|MAN|DUMP_PARMS|
|X_MEM_UPLD|Upload Memory|MAN|UPLD_HDR,<br>UPLD_DATA|
|X_MEM_UPLD_STORE|Store Upload Buffer to Memory|RED|UPLD_HDR,<br>UPLD_DATA|
|X_SEQ_ABORT|Abort current mode, reset Sequencer<br>and FIFO and flush ERP, and start<br>null mode.|MAN|None|
|X_SEQ_RAMP_START|Execute Ramp DACs Mode<br>Ramp CCD DAC voltages for I&T<br>purposes only.  Will be available in<br>I&T software only.|RED|DAC_ID|
|X_SEQ_START|Start Manual Mode|MAN|SEQ_ID<br>Null, Image (4 modes: low-gain fast-<br>exposure, low-gain slow-exposure, high-gain<br>fast-exposure, high-gain slow-exposure),<br>Photo-Diode, Windowed Timing, Photon-<br>Counting, Bias Image Calculation, Bias Row<br>Calculation, Raw-Data, Predetermined<br>Science Telemetry Pattern|
|X_SEQ_UPLD_PRG|Upload Sequencer Program|MAN|UPLD_HDR,<br>UPLD_DATA|
|X_SEQ_UPLD_TBL|Upload Sequencer Programs Lookup<br>Table|MAN|SEQ_TBL|
|X_SYS_CHKS32|Calculate and store checksum|MAN|3{ADDRESS}3|
|X_SYS_CLOS_SHUTR|Close Sun Shutter|RED|RAD_SRC_FLAG|
|X_SYS_DCX_OFF|Turn Off Data Compression|MAN|None|
|X_SYS_DCX_ON|Turn On Data Compression|MAN|None|
|X_SYS_LKOP_SHUTR|Lock the Sun Shutter Open|RED|None|
|X_SYS_OPEN_DOOR|Open Camera Door<br>There are two HOP type actuators,<br>and they require many seconds to<br>heat the wax (150 seconds typical).  A<br>timeout value will prevent current draw<br>after the door is open if the door<br>switch fails, and it will also allow the<br>actuators to be tested if the timeout<br>value is set to a low value (5<br>seconds).|RED|DOOR_ACT_ID,<br>DOOR_TIMEOUT|
|X_SYS_OPEN_SHUTR|Open Sun Shutter|RED|None|
|X_SYS_OPEN_VALVE|Open Camera Pressure Relief Valve<br>This is a HOP type actuator, and<br>requires many seconds to heat the<br>wax (150 seconds typical).  A timeout<br>value will prevent current draw after<br>the valve is open, and it will also allow<br>the actuator to be tested if the timeout<br>value is set to a low value (5<br>seconds).|RED|VALVE_HTR_ID,<br>VALVE_TIMEOUT|
|X_SYS_RSET_CMDCTR|Reset the Command Counters|MAN|None|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page C-5
































|Table 14. Telecommands|Col2|Col3|Col4|
|---|---|---|---|
|**Mnemonic**|**Description**|**State**|**Parameters (See Data Dictionary)**|
|X_SYS_SET_BUFFER|Sets when the buffer's interrupt will<br>occur.  After the specified number of<br>CCD rows have been written into the<br>buffer, an interrupt will be generated.|MAN|N_CCD_ROWS|
|X_SYS_SET_SAA_MODE|This command sets configuration<br>information used by XRT to determine<br>how to handle the SAA.|ALL|SAA_FLAG,<br>SAA_PARMS|
|X_SYS_SHELL|Execute a command at the VxWorks<br>shell|RED|STRING|
|X_SYS_STATE_AUTO|Set State to AUTO|MAN|STATE_NEXT|
|X_SYS_STATE_MAN|Set State to MAN|ALL|STATE_NEXT|
|X_SYS_STATE_RED|Set State to RED|MAN|STATE_NEXT,<br>RED_APID,<br>RED_FCODE|
|X_SYS_STOP_DOOR|Cancel the Open Camera Door<br>Command|ALL|DOOR_ACT_ID|
|X_SYS_STOP_VALVE|Cancel the Open Camera Pressure<br>Relief Valve Command|ALL|VALVE_HTR_ID|
|X_TAM_CORR_DIS|Disable TAM Correction|MAN|None|
|X_TAM_CORR_EN|Enable TAM Correction|MAN|None|
|X_TAM_LED1_ON|Turn on TAM LED 1, and turn off TAM<br>LED 2 if it's on.|MAN|None|
|X_TAM_LED2_ON|Turn on TAM LED 2, and turn off TAM<br>LED 1 if it's on.|MAN|None|
|X_TAM_LEDS_OFF|Turn off TAM LEDs.|MAN|None|
|X_TAM_PWR_DIS|Telescope Alignment Monitor (TAM)<br>Disable|MAN|None|
|X_TAM_PWR_EN|Telescope Alignment Monitor (TAM)<br>Enable|MAN|None|
|X_TAM_READ|Forces the TAM to be read<br>immediately.|MAN|None|
|X_TAM_READ_FREQ|Set the Period for Reading TAM|MAN|TAM_RDFQ|
|X_TAM_SET_CPARMS|Set the TAM's Centroid Algorithm<br>Parameters|MAN|CENT_PARMS|
|X_TAM_SET_CTHRSH|Set the TAM's Centroid Pixel<br>Threshold|MAN|CENT_THRSH|
|X_TAM_SET_OFFSET|Set the TAM's Boresight Calibration<br>Offsets|MAN|TAM_BORE_LED1,<br>TAM_BORE_LED2|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page C-6








|Table 14. Telecommands|Col2|Col3|Col4|
|---|---|---|---|
|**Mnemonic**|**Description**|**State**|**Parameters (See Data Dictionary)**|
|X_TEC_AUTO_COOL|TEC Automatic Cooling Mode<br>If TEC is off: set the parameters as<br>specified, set the TEC Power Supply's<br>SHUTDOWN input to a low logic level,<br>and start the TEC Cooling Mode PID<br>Control Loop.<br>If TEC is in Manual Cooling Mode: set<br>the parameters as specified and start<br>the TEC Cooling Mode PID Control<br>Loop.<br>If TEC is in Automatic Cooling Mode:<br>set the parameters as specified.<br>If TEC is in Manual Heating Mode:<br>ignore command.<br>If TEC is in Automatic Heating Mode:<br>ignore command.|RED|TEC_ACOOL_SETPT,<br>TEC_SENS_ID,<br>TEC_ACOOL_RR,<br>TEC_ACOOL_PCOEFF,<br>TEC_ACOOL_ICOEFF,<br>TEC_ACOOL_DCOEFF|
|X_TEC_AUTO_HEAT|TEC Automatic Heating Mode<br>If TEC is off: set the parameters as<br>specified, energize the heating relay,<br>set the TEC Power Supply's<br>SHUTDOWN input to a low logic level,<br>and start the TEC Heating Mode PID<br>Control Loop.<br>If TEC is in Manual Heating Mode: set<br>the parameters as specified and start<br>the TEC Heating Mode PID Control<br>Loop.<br>If TEC is in Automatic Heating Mode:<br>set the parameters as specified.<br>If TEC is in Manual Cooling Mode:<br>ignore command.<br>If TEC is in Automatic Cooling Mode:<br>ignore command.|RED|TEC_AHEAT_SETPT,<br>TEC_SENS_ID,<br>TEC_AHEAT_RR,<br>TEC_AHEAT_PCOEFF,<br>TEC_AHEAT_ICOEFF,<br>TEC_AHEAT_DCOEFF,<br>TEC_AHEAT_TIMEOUT|
|X_TEC_EMER_OFF|Turn off the TEC Immediately<br>Stops the TEC Control Loop, sets the<br>TEC Power Supply's SHUTDOWN<br>input to a high logic level, sets the<br>TEC Power Supply's digital<br>potentiometer to its minimum value,<br>and if the TEC is in Automatic or<br>Manual Heating Mode, the heating<br>relay is deenergized.|RED|None|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page C-7
















|Table 14. Telecommands|Col2|Col3|Col4|
|---|---|---|---|
|**Mnemonic**|**Description**|**State**|**Parameters (See Data Dictionary)**|
|X_TEC_MAN_COOL|TEC Manual Cooling Mode<br>If TEC is off: set the TEC Power<br>Supply's SHUTDOWN input to a low<br>logic level, and ramp the TEC Power<br>Supply's output voltage to the<br>specified value.<br>If TEC is in Manual Cooling Mode:<br>ramp the TEC Power Supply's output<br>voltage to the specified value.<br> If TEC is in Automatic Cooling Mode:<br>stop the TEC Cooling Mode PID<br>Control Loop, and ramp the TEC<br>Power Supply's output voltage to the<br>specified value.<br>If TEC is in Manual Heating Mode:<br>ignore command.<br>If TEC is in Automatic Heating Mode:<br>ignore command.|RED|TEC_VOLTAGE,<br>TEC_MCOOL_RR|
|X_TEC_MAN_HEAT|TEC Manual Heating Mode<br>If TEC is off: energize the heating<br>relay, set the TEC Power Supply's<br>SHUTDOWN input to a low logic level,<br>and ramp the TEC Power Supply's<br>output voltage to the specified value.<br>If TEC is in Manual Heating Mode:<br>ramp the TEC Power Supply's output<br>voltage to the specified value.<br> If TEC is in Automatic Heating Mode:<br>stop the TEC Heating Mode PID<br>Control Loop, and ramp the TEC<br>Power Supply's output voltage to the<br>specified value.<br>If TEC is in Manual Cooling Mode:<br>ignore command.<br>If TEC is in Automatic Cooling Mode:<br>ignore command.|RED|TEC_VOLTAGE,<br>TEC_MHEAT_RR,<br>TEC_MHEAT_TIMEOUT|
|X_TEC_NORMAL_OFF|Turn off the TEC Gracefully<br>Stops the TEC Control Loop, ramps<br>the TEC Power Supply's digital<br>potentiometer to its minimum value,<br>sets the TEC Power Supply's<br>SHUTDOWN input to a high logic<br>level, and if the TEC is in Automatic or<br>Manual Heating Mode, the heating<br>relay is deenergized.|RED|None|
|X_THTR_DIS|Disable Telescope Tube Heater|MAN|THTR_ID|
|X_THTR_EN|Enable Telescope Tube Heater|MAN|THTR_ID|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page C-8








|Table 14. Telecommands|Col2|Col3|Col4|
|---|---|---|---|
|**Mnemonic**|**Description**|**State**|**Parameters (See Data Dictionary)**|
|X_THTR_SET_PARMS|Set theTelescope Tube Heater<br>Temperature Set Point<br>Adjust until the temperature ripple is<br>centered on the desired temperature.<br>Also, starts the Thermal Baffle Control<br>Heater's control loop if it is currently<br>stopped.|MAN|THTR_LIMIT,<br>THTR_RESIST,<br>THTR_PWR,<br>{THTR_ID +<br>THTR_PARMS}|


#### **Southwest Research Institute**

**XRT Control Processor**

**Software Requirements Specification**



04121-XCPSRS-01

April 23, 2001  Rev. 2 Chg. 0

Page D-1


## **APPENDIX D** **CPU THROUGHPUT CALCULATION**

Note: If reviewing this document electronically, the CPU throughput calculations are contained

in a separate Microsoft® Excel spreadsheet file, _XRTcpu_rev1.xls_ .


