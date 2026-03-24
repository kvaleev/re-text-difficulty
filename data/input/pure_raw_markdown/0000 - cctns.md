---
consensus_grade_level: 12.9
headings_per_sentence: 0.0
lists_per_sentence: 0.0
smao_sentences_pct: 3.4
vague_words_per_sentence: 0.22
anaphora_per_sentence: 0.34
sentence_cv: 1.29
cpre_terms_per_sentence: 0.86
---
## **E-GOVERNANCE** **MISSION MODE PROJECT (MMP)** **CRIME & CRIMINAL TRACKING** **NETWORK AND SYSTEMS**

##### **(CCTNS)**

# **FUNCTIONAL REQUIREMENTS** **SPECIFICATION V1.0**
### **(DRAFT)**

##### **MINISTRY OF HOME AFFAIRS** **GOVERNMENT OF INDIA**


_E-Governance Mission Mode Project: Crime & Criminals Tracking Network and Systems_


**TABLE OF CONTENTS**

|S. NO.|CONTENTS|
|---|---|
|**1**.|**INTRODUCTION **|
|**2**.|**FUNCTIONALOVERVIEW **|
|**3**.|**DESCRIPTION OF THEMODULES ANDFUNCTIONALREQUIREMENTS **|
|**4**.|**NON-FUNCTIONALREQUIREMENTS **|
|**5**.|**FUNCTIONALARCHITECTURERECOMMENDATIONS **|
|**A1**|**REGISTRATION **|
|**A2**|**INVESTIGATION **|
|**A3**|**PROSECUTION **|
|**A4**|**SEARCH **|
|**A5**|**CITIZENINTERFACEMODULE **|
|**A6**|**NAVIGATIONMODULE **|
|**A7**|**CONFIGURATIONMODULE **|



_Ministry of Home Affairs                Draft Core Scope Document                 Page 2 of 19_


_E-Governance Mission Mode Project: Crime & Criminals Tracking Network and Systems_


**1.** **INTRODUCTION**

The Functional Requirements Specifications (FRS) report provides the detailed description


of the functionalities required for the first version of the CCTNS. The key guiding principle


behind the functional design of CCTNS V1.0 is to focus on the critical functionality that


provides value to the police personnel at the cutting edge which in turn can improve the


outcomes in the areas of “Investigation of Crime” and “Detection of Criminals”.


**2.** **FUNCTIONAL OVERVIEW**

CCTNS V1.0 functionality is designed to focus on delivering value to IOs, records room


staff and citizens within the broad crime investigation area. Based on the guiding principles


stated above, nine different function blocks have been identified and the detailed


functionality of each block was determined.


_Ministry of Home Affairs                Draft Core Scope Document                 Page 3 of 19_


_E-Governance Mission Mode Project: Crime & Criminals Tracking Network and Systems_


**3.** **DESCRIPTION OF THE MODULES AND FUNCTIONAL REQUIREMENTS**

The functionality of the CCTNS application is focused on providing value to the police


personnel, especially the officers operating at the cutting edge and easing the day to day


operations of the police function.


**Registration**


Citizens can register their complaints with police and then based on the evidence, facts and


following investigation, police shall take the complaint forward. The Registration module


acts as an interface between the police and citizens and it eases the approach, interaction and


information exchange between police and complainants.


**Investigation**


After a complaint is initiated, police initiates the investigation process. The Investigation


module of the CCTNS facilitates the investigation process and introduces operational


efficiencies by automating most of the tasks that take place after initial entries are made


during Registration.


**Prosecution**


Interfacing with the courts during the prosecution of cases is an integral part of the


responsibilities of police personnel. A designated constable from each police station


constantly interfaces with the courts. The Prosecution module of the CCTNS aids this


interfacing by providing a platform to record entries of the court interactions.


**Search**


The Search module of the CCTNS gives police personnel the ability to execute a basic or


advanced search on cases. Using the search functionality, police personnel can search for a


particular person, type of crime, modus operandi, property etc. It also gives the user the


ability to customize the results view by criminal/accused or by cases. It makes reporting easy


for police by enabling them to execute different types of queries such as monthly reporting,


RTI related etc.


_Ministry of Home Affairs                Draft Core Scope Document                 Page 4 of 19_


_E-Governance Mission Mode Project: Crime & Criminals Tracking Network and Systems_


**Citizen Interface**


The Citizen Interface module of the CCTNS acts as a conduit for the information exchange


between citizens and police units/personnel. Citizens can use it as a tool to get information


or acknowledgements from police. The police in turn can use it to respond to citizens with


very little turnaround time. It improves overall productivity by helping citizens and police to


cut short the drudgery of large amounts of paperwork.


**Navigation**


The Navigation module of the CCTNS provides role based landing pages which help in


navigating through the CCTNS application. It shows information such as cases assigned,


alerts, pending tasks etc hence helping police personnel to plan better and execute with


greater efficiency.


**Application Configuration**


The Configuration module of the CCTNS helps keep the application configured according


to the states’ requirements in addition to keeping data elements/rules up to date. With a


proper configuration, information such as act and sections, state specific data, castes, tribes,


property information etc. can be created updated and deleted.


The functional requirements for each of the modules are provided as A1 to A7 in separate


enclosures.


_Ministry of Home Affairs                Draft Core Scope Document                 Page 5 of 19_


_E-Governance Mission Mode Project: Crime & Criminals Tracking Network and Systems_


**4.** **NON-FUNCTIONAL REQUIREMENTS**

The non-functional requirements specify the qualitative attributes such as user-friendliness
and performance of the system that are critical for the increased user-acceptance of the
application.


|Help Module|Col2|
|---|---|
|1.|The solution should provide detailed context-sensitive help material for all the<br>possible actions and scenarios on all user interfaces in the application.|
|2.  <br>|The help should be accessible to the users both in the offline and online mode|








|Support Module|Col2|
|---|---|
|1.|The solution should provide an interface for the user to log any defects or<br>enhancement requests on the application and track thereafter.|
|2.|The solution should send alerts (e.g., email, SMS) to the user if the user chooses<br>to whenever any action has been taken on the alert|
|3.|The solution should enable the user to track the submitted defect or<br>enhancement request.|
|4.|The solution should enable the help-desk user to view the reports on the<br>submitted defects or enhancement requests category-wise, status-wise, and age-<br>wise.|
|5.|The support solution should be accessible to the users both from within the<br>application and also outside the application through a browser interface.|






|Audit Module|Col2|
|---|---|
|1.|An audit trail is a record of actions taken by either the user or the system<br>triggers. This includes actions taken by users or Administrators, or actions<br>initiated automatically by the system as a result of system parameters. The<br>System must keep an unalterable audit trail capable of automatically capturing<br>and storing information about:<br>• All the actions (create/read/update/delete) that are taken upon the critical<br>entities (case, suspect, property,…) in the system<br>• The user initiating and or carrying out the action;<br>• The date and time of the event.|



_Ministry of Home Affairs                Draft Core Scope Document                 Page 6 of 19_


_E-Governance Mission Mode Project: Crime & Criminals Tracking Network and Systems_













|Col1|•<br>Administrative parameters<br>The word “unalterable” is to mean that the audit trail data cannot be modified<br>in any way or deleted by any user; it may be subject to re-department and<br>copying to removable media if required, so long as its contents remain<br>unchanged.|
|---|---|
|2.|Once the audit trail functionality has been activated, the System must track<br>events without manual intervention, and store in the audit trail information<br>about them.|
|3.|The System must maintain the audit trail for as long as required, which will be at<br>least for the life of the case to which it refers.|
|4.|The System must ensure that audit trail data is available for inspection on<br>request, so that a specific event can be identified and all related data made<br>accessible, and that this can be achieved by authorised external personnel who<br>have little or no familiarity with the system.|
|5.|The System must be able to export audit trails for specified cases (without<br>affecting the audit trail stored by the System). This functionality can be used by<br>external auditors who wish to examine or analyse system activity.|
|6.|The System must be able to capture and store violations (i.e. A user’s attempts<br>to access a case to which he is denied access), and (where violations can validly<br>be attempted) attempted violations, of access control mechanisms.|
|7.|The System must at a minimum be able to provide reports for actions on cases<br>organised:<br>• By case;<br>• By user;<br>• In chronological sequence.|
|8.|The System should be able to provide reports for actions on cases organised by<br>workstation and (where technically appropriate) by network address.|


The requirements specify the requirements to control the user access to correspondences,


files, and records and various functionalities provided within the system.

|Access Module|Col2|
|---|---|
|1.|The System must allow the user to limit access to cases to specified users or<br>user groups.|
|2.|The system should provide for role-based control for the functionality within|



_Ministry of Home Affairs                Draft Core Scope Document                 Page 7 of 19_


_E-Governance Mission Mode Project: Crime & Criminals Tracking Network and Systems_












|Col1|the system.|
|---|---|
|3.|The System must allow a user to be a member of more than one group.|
|4.|The System must allow only admin-users to set up user profiles and allocate<br>users to groups.|
|5.|The System should allow a user to stipulate which other users or groups can<br>access cases.|
|6.|The System must allow changes to security attributes for groups or users (such<br>as access rights, security level, privileges, password allocation and management)<br>to be made only by super-user.|
|7.|If a user requests access to, or searches for, a case which he does not have the<br>right to access, the System must provide one of the following responses<br>(selectable at configuration time):<br>• display title and metadata;<br>• display the existence of a case but not its title or other metadata;<br>• do not display any case information or indicate its existence in any way.<br>These options are presented in order of increasing security.  Note that the<br>requirement in the third option (i.e. the most stringent) implies that the System<br>must not include such cases in any count of search results; this level of security<br>is normally appropriate for cases dealing with matters such as national security.|
|8.|If a user performs a quick or advanced search, the System must never include in<br>the search result list any record which the user does not have the right to access.|
|9.|If the System allows users to make unauthorised attempts to access cases, it<br>must log these in the audit trail.|
|10.|Any access to cases, and all other activities involving the cases and related<br>documents or data should also need to be stored in the audit trail to ensure legal<br>admissibility and to assist in data recovery.|









|Ease of Use|Col2|
|---|---|
|1.|All error messages produced by the System must be meaningful, so that they can be<br>appropriately acted upon by the users who are likely to see them. Ideally, each error<br>message will be accompanied by explanatory text and an indication of the action(s)<br>which the user can take in response to the error.|
|2.|The System must employ a single set of user interface rules, or a small number of<br>sets to provide a familiar and common look and feel for the application.|


_Ministry of Home Affairs                Draft Core Scope Document                 Page 8 of 19_


_E-Governance Mission Mode Project: Crime & Criminals Tracking Network and Systems_


















|3.|The System must be able to display several entities (cases, suspects) simultaneously.|
|---|---|
|4.|The interfaces must be made customizable or user-configurable to the extent<br>possible. (e.g., the displayed columns in the table, move, resize, modify the<br>appearance). Such configurations must be saved in the user profile.|
|5.|The System user interface must be suitable for users with special needs; that is,<br>compatible with specialist software that may be used and with appropriate interface<br>guidelines|
|6.|The System must provide End User and Administrator functions which are easy to<br>use and intuitive throughout.|
|7.|The System must allow persistent defaults for data entry where desirable.  These<br>defaults should include:<br>• user-definable values;<br>• values same as previous item;<br>• values derived from context, e.g. date, file reference, user identifier;|
|8.|Frequently-executed System transactions must be designed so that they can be<br>completed with a small number of interactions (e.g. mouse clicks).|
|9.|Where the System employs a graphical user interface, it must allow users to<br>customise it. Customisation should include, but need not be limited to the following<br>changes:<br>• menu contents;<br>• layout of screens;<br>• use of function keys;<br>• on-screen colours, fonts and font sizes;|








|Usability|Col2|
|---|---|
|1.|The user interfaces should be designed to make them user-intuitive.|
|2.|The user interfaces of the system should comply with Standard ISO 9241.|
|3.|ICT accessibility: ISO 9241-20 shall be the standard for guidance on ICT<br>accessibility. Application user interfaces to meet its requirements and<br>recommendations. Software accessibility ISO 9241-171 shall be the standard for<br>guidance on software accessibility. User interfaces should meet its requirements<br>and recommendations. Content accessibility WCAG 1.0 shall be the standard used<br>for guidance on content accessibility. The application logo to be available on all<br>pages as a link to the home page.|



_Ministry of Home Affairs                Draft Core Scope Document                 Page 9 of 19_


_E-Governance Mission Mode Project: Crime & Criminals Tracking Network and Systems_






|4.|Providing text equivalents for non-text media objects: All non-text media objects,<br>such as graphical images or video, should be provided with alternative equivalent<br>textual descriptions and/or with equivalent text-based functionality.|
|---|---|
|5.|Making navigation self-descriptive: Navigation should be designed to help users<br>understand where they are, where they have been and where they can go next.<br>General guidance on achieving self-descriptiveness is given in ISO 9241-110.|
|6.|Showing users where they are: Each presentation segment (page or window)<br>should provide the user with a clear and sufficient indication of where he or she is<br>in the navigation structure and of the current segment position with respect to the<br>overall structure.|
|7.|Offering alternative access paths: Alternative access paths for navigating to a<br>specific unit of content should be offered to support different navigation<br>strategies.|
|8.|Minimizing navigation effort: The number of navigation steps needed to reach a<br>certain piece of content should be minimized as long as different mental models,<br>navigation strategies and tasks of the user are taken into account.|
|9.|Splash screens should be avoided unless they provide useful content or feedback<br>about the application state to the user. If a splash screen is used, a navigation<br>option to skip it should be offered.|
|10.|Avoiding opening unnecessary windows: Additional windows such as new browser<br>windows or pop-up windows should only be opened if this supports the user’s<br>task. Opening new windows can distract, confuse or impede users for a variety of<br>reasons. They can superimpose the primary window, hiding relevant information.<br>They could make it cognitively more difficult to understand the navigation<br>structure with negative effects on both usability and accessibility. They also require<br>additional user actions for closing unwanted windows.|
|11.|Vertical scrolling should be minimized. This may be done by placing important<br>information at the top and providing links to information that is further down the<br>page. Horizontal scrolling should be avoided wherever possible.|
|12.|Designing for input device independence: User interfaces should be designed to<br>allow activation of controls by a variety of input devices. The ability to choose<br>between different input devices for activating controls such as links, fields and<br>buttons is important both for users who prefer a certain input mode, mobile users<br>and users with disabilities. In general, device independence can be achieved if the<br>functionality is operable via a keyboard.|
|13.|Making user interfaces robust: User interfaces should be designed to be as robust<br>as possible in the face of changing technology. This encompasses being able to<br>present content containing newer technologies by older user agents as well as|



_Ministry of Home Affairs                Draft Core Scope Document                 Page 10 of 19_


_E-Governance Mission Mode Project: Crime & Criminals Tracking Network and Systems_



















|Col1|designing content to be usable with future technologies.|
|---|---|
|14.|Acceptable opening / download times: Application pages should be designed and<br>implemented so that there are acceptable opening times and download times for<br>the expected range of technical contexts of use (e.g. bandwidth between the<br>application and the user). This is particularly important for frequently accessed<br>pages or pages that are important for user navigation and exploration, such as the<br>home page.|
|15.|Minimizing user errors: Potential user errors as well as the effort needed to<br>recover from errors should be minimized.|
|16.|Providing clear error messages: The content of error messages shown on the pages<br>or special error pages should clearly state the reason why the error occurred and, if<br>possible, actions the user can take to resolve the error. Users expect error messages<br>to be in the same language as the user interface.|
|17.|Using appropriate formats, units of measurement or currency: When designing<br>user interfaces for use by diverse groups, input and output of information<br>elements such as currency, units of measurement, temperatures, date and time,<br>phone numbers, address or postal codes should be designed so that they are<br>usable.|
|18.|Making text resizable by the user: Text should be able to be resized by the user,<br>using functions provided by the user agent or other appropriate means i.e. see ISO<br>9241-171.|
|19.|Text quality: The quality of textual content with respect to spelling and grammar<br>should be sufficient so as not to impede readability.|
|20.|Writing style: The reading and understanding of the textual content on the screen<br>should be supported by suitable means, including the use of short sentences, the<br>division of the text into shorter chunks or the presentation of content items in the<br>form of bullet points.|
|21.|Supporting text skimming: Fast skimming of text should be supported by the<br>provision of clear links, bulleted lists, highlighted keywords, logical headings, and<br>short phrases and sentences.|
|22.|Readability of text: Text presented on the pages should be readable taking into<br>account the expected display characteristics and spatial arrangement. ISO 9241-303<br>shall be consulted for screen text legibility requirements.|
|23.|Distinguishable within-page links: Within-page links should be clearly<br>distinguishable from other links that lead to a different page. EX. Within-page<br>links are shown with dashed rather than solid underlines|
|24.|Avoiding link overload: Text pages containing large proportions of links should|


_Ministry of Home Affairs                Draft Core Scope Document                 Page 11 of 19_


_E-Governance Mission Mode Project: Crime & Criminals Tracking Network and Systems_












|Col1|be formatted so that the presence of links does not impede the readability of the<br>text.|
|---|---|
|25.|Using familiar terminology for navigation links: Navigation links — particularly<br>links representing the main navigation structure — should be labelled with terms<br>that are familiar to the user, based on his/her general knowledge, prior experience<br>in the application domain or experience of using other systems.|
|26.|Using descriptive link labels: The target or purpose of a link should be directly<br>indicated by its label, avoiding generic labels such as “go” or “click here” except<br>where the purpose of the link is clear from its context on the page or the labels<br>have commonly understood semantics in the particular application domain. Using<br>appropriate terminology specific to the user’s tasks and information needs is<br>important for making the content easy to understand.|
|27.|Marking links opening new windows: Links that open new browser windows or<br>pop-up windows should be clearly marked.|
|28.|Distinguishing navigation links from controls: Navigation links should be clearly<br>distinguishable from controls activating some action.  Typical action types in user<br>interfaces<br>include<br>manipulating<br>application<br>data,<br>performing<br>searches,<br>communication actions, such as opening a new e-mail window or starting a chat<br>function, andHpresentation-related actions, such as sorting a list of search results.|
|29.|Providing printable document versions: If a document is either too long, dispersed<br>over several pages or in a specific layout that is not suitable for online reading, a<br>printer-friendly version of the document should be provided that prints the<br>content in a form acceptable to the user (e.g. in the expected layout, paper format,<br>or orientation).|
|30.|Use of “white space”:  “White space” on a page i.e. space filled only with the<br>background color should be used in such a way that it does not impair the visual<br>skimming of the page. While white space is an important means of visually<br>organizing the different content elements on a page, if the distance between the<br>blocks of information displayed becomes too large, rapid skimming of the page<br>can be impeded.|
|31.|Selecting appropriate page lengths The length of a page should be selected so as to<br>support the primary purpose and use of the page. Short pages are generally more<br>appropriate for homepages, navigation pages, or overview pages that need to be<br>read quickly. Longer pages can be more appropriate when users want to read the<br>content without interruptions or when the page needs to match a paper<br>counterpart.|
|32.|Using colour: Colour should be used with care, taking into account human<br>capabilities and restrictions in perceiving colour, and not as the only means of<br>conveying information. Color should never be the only means of coding. Some<br>users may have difficulties in perceiving certain colors or color combinations|



_Ministry of Home Affairs                Draft Core Scope Document                 Page 12 of 19_


_E-Governance Mission Mode Project: Crime & Criminals Tracking Network and Systems_


















|Col1|(color-blindness).|
|---|---|
|33.|Using frames with care: If frames are used, care should be taken to avoid possible<br>problems, for example, those involving the use of the back button, bookmarking<br>of pages, or scrolling of information. When frames are used, it is important to title<br>each frame, and to describe its purpose and how frames relate to one another<br>other.|
|34.|Providing alternatives to frame-based presentation: If frames are used, an<br>alternative way of presenting relevant information without frames should be<br>provided. Providing alternative text-only pages: When style sheets and/or frames<br>are turned off it should be possible for the user to read and understand the page;<br>alternatively, the user should be provided with an equivalent alternative text-only<br>page.|
|35.|Consistent page layout: Pages should be designed using consistent layout schemes,<br>supporting the user in finding similar information at the same position on different<br>pages. Overall layout schemes apply to all pages and are preferable when all pages<br>have a similar structure. Frequently, however, different pages have different<br>purposes and types of content. In such cases, pages can usually be grouped in<br>different categories, using one layout scheme for each category consistently.|
|36.|Placing title information consistently: Page titles should be placed in a consistent<br>location on the different pages.|
|37.|Observing principles of human perception When designing application pages, the<br>general principles of human perception should be taken into account. The<br>International Standards mentioned below shall be consulted for guidance. Practical<br>guidelines for presenting information to the user are to be found in ISO 9241-12.<br>Guidance on selecting and using different forms of interaction techniques is to be<br>found in ISO 9241-14 to ISO 9241-17. ISO 9241-14 gives guidance about menus,<br>ISO 9241-15 about command dialogues, ISO 9241-16 about direct manipulation<br>and ISO 9241-17 about forms. In addition, when designing multimedia<br>information presentations, the design principles and recommendations described<br>in ISO 14915-1 to ISO 14915-3 should be taken into account. Appropriate content<br>presentation also plays a key role in accessibility.|
|38.|Linking back to the home page or landmark pages: Each page should contain a<br>link leading to the home page of the application or to a landmark page that is easy<br>to recognize for the user.|
|39.|Providing a site map: A separate navigation overview such as a site map should be<br>provided for application showing the structure of the site in an overview form.|
|40.|Consistency between navigation components and content: If navigation<br>components (or overviews) are shown in conjunction with associated content,<br>consistency between the navigation component and the content shown should be<br>maintained by indicating in the navigation  component (e.g. highlighting) the topic|



_Ministry of Home Affairs                Draft Core Scope Document                 Page 13 of 19_


_E-Governance Mission Mode Project: Crime & Criminals Tracking Network and Systems_














|Col1|currently visible in the content area.|
|---|---|
|41.|Placing navigation components consistently: Navigation components should be<br>placed consistently on the pages or in the framesets in the pages of the application.|
|42.|Individualization and user adaptation : Adapting the content and the navigation of<br>a user interface to individual users or user groups can be a useful mechanism for<br>providing information that is of interest to the users and for making access to<br>relevant information more efficient. User adaptation can also be important for<br>making the user interface more accessible. Different approaches can be used for<br>achieving these goals, like providing users with means for customizing the user<br>interface to their personal needs i.e. individualization designing content and<br>navigation differently for varying user groups or roles i.e. such as employees of<br>different levels, citizens etc, monitoring the user’s behaviour and adapting to the<br>user’s goals that are inferred from the behaviour observed, recommending<br>information that is potentially more relevant or interesting to the specific user,<br>based on the behaviour of all users or a user group.|
|43.|Taking account of the users’ tasks and information needs: When providing<br>different access paths or navigation structures for different user groups, the tasks<br>and information needs of these user groups should be taken into consideration.|
|44.|Making individualization and adaptation evident: It should be made evident to the<br>user when individualization and/or adaptation are used.|
|45.|Making user profiles evident: If predefined user profiles or user-specified profiles<br>are used for individualizing or adapting content, the profile currently used should<br>be made evident. If profiles are used, it is important to provide users with<br>information about this concept and its implications.|
|46.|Allowing users to see and change profiles: If user-specified profiles are used, users<br>should be able to see, modify and delete that profile on demand.|
|47.|The user interfaces of the system should follow the guidelines specified under<br>www.usability.gov|







|System Availability|Col2|
|---|---|
|1.|The System must be available to users:<br>• from <xx:00> to <xx:00>;<br>• on <all weekdays/xxx days per year>.|
|2.|The planned downtime for the System must not exceed <xx> hours per <rolling<br>three month period>.|


_Ministry of Home Affairs                Draft Core Scope Document                 Page 14 of 19_


_E-Governance Mission Mode Project: Crime & Criminals Tracking Network and Systems_


|Col1|The System is considered to be down if any user is unable to perform any normal<br>System function and if this failure is attributed to any component of the System<br>other than the workstation.|
|---|---|
|3.|Unplanned downtime for the System must not exceed <xx hours/minutes> per<br><rolling three month period>.|
|4.|The number of incidents of unplanned downtime for the System must not exceed<br><x> per <rolling three month period>.|
|5.|In the event of any software or hardware failure, it must be possible to restore the<br>System (with inline synchronization) within no more than <xx> hours.|







|Performance and Scalability|Col2|
|---|---|
|1.|The System must provide adequate response times for commonly performed<br>functions under both standard and peak conditions|
|2.|The System must be able to perform a simple search within 5-8 seconds and a<br>advanced search (multiple search criteria) within 10-15 seconds regardless of the<br>storage capacity or number of cases in the system. In this context, performing a<br>search means returning a result list. It does not include retrieving the records<br>themselves.|
|3.|The System must be able to retrieve and display within 5-8 seconds the case which<br>has been accessed within the previous 2 months, regardless of storage capacity or<br>number of cases in the system. This requirement is intended to allow for rapid<br>retrieval of frequently-used cases, on the understanding that frequency of use is<br>typically correlated with recent use.|
|4.|The System must be able to retrieve and display within 20 seconds the case which<br>has not been accessed within the previous 2 months, regardless of storage capacity<br>or number of cases in the system. This requirement is intended to allow for cases<br>where cases used infrequently are stored on slower media than more active<br>records.|
|5. <br>|The System be scaleable and must not have any features which would preclude use<br>in small or large police stations, with varying numbers of cases handled.|


_Ministry of Home Affairs                Draft Core Scope Document                 Page 15 of 19_


_E-Governance Mission Mode Project: Crime & Criminals Tracking Network and Systems_


**5.** **FUNCTIONAL ARCHITECTURE RECOMMENDATIONS**


The proposed functional architecture is modeled around centralized deployment to facilitate


ease of maintenance and leverage advancement in open standards and web technologies.


The 3 C’s (Core-Configuration-Customization) forms the guiding principle for the


architecture. The functional architecture of the CCTNS solution is given in the figure below.


The functional architecture is composed of 4 major components based on SOA principles.


Each of the components contains multiple services as defined by Service Definition. The


core services, support layer and security and access control components can be deployed as


standard components with necessary configuration changes. The customization layer can


override and add to the core services based on the specific state requirements and can be


plugged with the core services.


**CCTNS Functional Architecture Overview**


_Ministry of Home Affairs                Draft Core Scope Document                 Page 16 of 19_


_E-Governance Mission Mode Project: Crime & Criminals Tracking Network and Systems_


The deployment of the application will be at state level and will be configured and


customized as per the state specific extensions.


The systems should be designed with the following broad guidelines:


**System Functionality**





































|1)|The system should support multilingual interface|
|---|---|
|2)|The system should be designed in manner that operational data is not lost in case of any<br>failure of equipment or communication network.|
|3)|The system should work even in an offline mode with the critical functionality|
|4)|The system should be designed to have satisfactory performance even in Police Stations<br>connected on low-bandwidth|
|5)|The system should be implemented using Service Oriented Architecture (SOA) and have a<br>modular design|
|6)|The system should be developed on Open Standards|
|7)|The system should be built on a common User Access and Authentication Service to<br>ensure Single-Sign on for the end-user|
|8)|The system should be developed for a centralized deployment and maintenance|
|9)|The system should be developed to be deployed in a 3-tier datacenter architecture|
|10)|The system should be designed to have a n-tier architecture with the presentation logic<br>separated from the business logic that is again separated from the data-access logic|
|11)|The system should be extensible to provide access to the interfaces through PDA’s and<br>mobile data terminals|
|12)|The system should adopt standardized formats and common metadata elements|
|13)|The system should be designed for access through browser-based systems and must<br>impose minimal requirements on the client device|
|14)|The system must support multiple types of communication services for remote access|
|15)|The system should have capability to support public access to a subset of data and<br>functionality|
|16)|The system should support multi-tier authentication where required|


_Ministry of Home Affairs                Draft Core Scope Document                 Page 17 of 19_


_E-Governance Mission Mode Project: Crime & Criminals Tracking Network and Systems_












|17)|The system should support SSL encrypted connections|
|---|---|
|18)|The system should support secure virtual private network connections|
|19)|The system should use HTTPS as the communication protocol, i.e., HTTP over an<br>encrypted secure socket layer (SSL)|
|20)|The system should run on multiple browsers|
|21)|The system should support selective encryption of the stored data|
|22)|The system should ensure secure transmission of data over the network and utilize SSL<br>and 2-way digital signatures|
|23)|The system should ensure high standards of security and access control through:<br>a) _Prevent cross-site scripting_ <br>b) _Validate the incoming data / user request_ <br>c) _Encode the incoming data / user request_ <br>d) _Prevent SQL Injection_<br>e) _Utilize parameterized queries_<br>f) _Sanitize the user-inputs_<br>g) _Validate the data both at the client and server_<br>h) _Do not allow hard delete and perform only soft tagging the row for deletion_|
|24)|The system should ensure high scalability and performance through:<br>a) _Use of cache for storing frequent data_ <br>b) _Use of AJAX based technology to improve user experience. Aggressive page loading to_<br>_be considered based on the screen and estimate usage pattern_ <br>c) _Leverage Asynchronous HTTP socket capabilities of web server for scalability and_<br>_performance_ <br>d) _Host all the static content (documents, images) on the web server_ <br>e) _The search results should be fetched from the database in batches of 10 or 20 maximum_<br>_as configured within the application_ <br>f) _Display of records on the screen in batches/paged manner_<br>g) _The search should fetch only the fields that need to be displayed to the user. Only when_<br>_the user clicks on a particular record to view its further details should a query be fired to_<br>_fetch the additional details for this particular record only_ <br>h) _A hierarchical cache should be configured and used for caching of results of most_|



_Ministry of Home Affairs                Draft Core Scope Document                 Page 18 of 19_


_E-Governance Mission Mode Project: Crime & Criminals Tracking Network and Systems_





_Ministry of Home Affairs                Draft Core Scope Document                 Page 19 of 19_


