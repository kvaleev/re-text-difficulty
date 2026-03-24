---
consensus_grade_level: 10.7
headings_per_sentence: 0.02
lists_per_sentence: 0.04
smao_sentences_pct: 0.0
vague_words_per_sentence: 0.06
anaphora_per_sentence: 0.1
sentence_cv: 1.119
cpre_terms_per_sentence: 0.44
---
## **Agency for Enterprise Information Technology (AEIT)**

# **Enterprise E-mail Functional Requirements** **Specification**

### **Version 1.5**


|Enterprise E-mail|Version: 1.5|
|---|---|
|~~Customer (Functional) Requirements~~<br>|<br>~~ Created on 07/23/2009~~|

# **Revision History**






|Date|Version|Description|Author|
|---|---|---|---|
|~~8/27/2009~~<br>|~~1.0~~<br>|~~Basic and Extended requirements~~<br>added to document for review by<br>functional requirements team.<br>|~~Scott Jecko~~<br>|
|~~9/1/2009~~<br>|~~1.1~~<br>|~~Basic and extended requirements~~<br>updated based on feedback from<br>requirements team.<br>|~~Scott Jecko~~<br>|
|~~9/2/2009~~<br>|~~1.2~~<br>|~~Document updated (archiving~~<br>requirements added) in preparation<br>for sending to team and key<br>stakeholders for final review.<br>|~~Scott Jecko~~<br>|
|~~9/4/2009~~<br>|~~1.3~~<br>|~~Document updated: added basic~~<br>requirements 1.9 and 1.10 (public<br>folders) based on feedback from<br>technical team.<br>|~~Scott Jecko~~<br>|
|~~9/15/2009~~<br>|<br>~~1.4~~<br>|~~Document updated: added basic~~<br>requirement 1.27 (ability for user to<br>customize their view in the client<br>application) based on feedback<br>from AEIT Advisory Committee.<br>|~~Scott Jecko~~<br>|
|~~9/17/2009~~<br>|~~1.5~~|~~Document updated: modified~~<br>requirements 1.14, 1.22, 1.72, and<br>1.77 based on feedback from<br>HSMV.|~~Scott Jecko~~|



9/17/2009 AEIT ii


|Enterprise E-mail|Version: 1.5|
|---|---|
|~~Customer (Functional) Requirements~~<br>|<br>~~ Created on 07/23/2009~~|

# **Table of Contents**

1. Enterprise E-mail Scope 1


2. Requirements Workgroup Methodology 2


3. Requirements Workgroup Goals 3


4. Requirements Workgroup Glossary 4


5. Requirements Workgroup Team 5


6. Requirements Workgroup References 5


7. Basic Functional Requirements 6


8. Extended Functional Requirements 10


9. Functional Requirements Summary 12


9/17/2009 AEIT iii


|Enterprise E-mail|Version: 1.5|
|---|---|
|~~Customer (Functional) Requirements~~<br>|<br>~~ Created on 07/23/2009~~|

# **Requirements Specification**

**1.** **Enterprise E-mail Scope**


9/17/2009 AEIT 1


|Enterprise E-mail|Version: 1.5|
|---|---|
|~~Customer (Functional) Requirements~~<br>|<br>~~ Created on 07/23/2009~~|


**2.** **Requirements Workgroup Methodology**


9/17/2009 AEIT 2


|Enterprise E-mail|Version: 1.5|
|---|---|
|~~Customer (Functional) Requirements~~<br>|<br>~~ Created on 07/23/2009~~|


**3.** **Requirements Workgroup Goals**












|Goal ID:|Name – Description|
|---|---|
|**3.1**<br>|~~**Manage Scope:**Understand the preliminary scope statement for the statewide e-~~<br>mail system and ensure that requirements remain within scope.<br>|
|~~**3.2**~~|~~**Manage Time:** Specification must be complete within 6 weeks (30 business days).~~<br>|
|**3.3**|~~**Manage Time:** Workgroup will use the 2006 Messaging Optimization Workgroup~~<br>Survey as a basis for the 2009 Enterprise e-mail survey.<br>|
|**3.4**|~~**Ensure Completeness:**Specification must be complete and detailed enough to~~<br>submit to outside vendors as Request For Information (RFI) or Request For<br>Proposals (RFP) or an Invitation to Negotiate (ITN).<br>|
|**3.5**|<br>~~**Ensure Completeness:** Specification must include an attachment which provides a~~<br>narrative and breakdown of existing agency resources (personnel, equipment –<br>including storage capabilities, software-licenses) and current spend (reuse IV-C data<br>where applicable) on e-mail. (Note: this information will be captured in the inventory<br>survey which is being compiled by the Enterprise E-mail technical team – and is not<br>included in this functional specification.) <br>|
|**3.6**<br>|<br>~~**Ensure Completeness:** Specification must include an attachment which lists each~~<br>agencies’ risks, issues, or constraints (such as software-application dependencies,<br>contracts, or legal requirements) that may affect their ability to transition to an<br>Enterprise E-mail System.(Note: this information will be compiled into a FAQ<br>document which will be posted to the project web site and made available to all<br>stakeholders.)|



9/17/2009 AEIT 3


|Enterprise E-mail|Version: 1.5|
|---|---|
|~~Customer (Functional) Requirements~~<br>|<br>~~ Created on 07/23/2009~~|


**4.** **Requirements Workgroup Glossary**




















|Glossary<br>ID:|Name – Description|
|---|---|
|**4.1**|~~**Basic requirements** - The functional requirements that should be met as part of the~~<br>“basic” (minimal) solution-offering (whether in house or outsourced).Note: all functional<br>requirements will be subject to a technical and financial feasibility analysis.<br>|
|**4.2**|~~**Extended requirements** - The functional requirements that could be met as part of the~~<br>“extended” solution offering (potentially at an additional cost to the customer).Note: all<br>functional requirements will be subject to a technical and financial feasibility analysis. <br>|
|**4.3**|~~**E-mail, Calendar, Contacts** - The end-user services of an e-mail product that can be~~<br>found in all e-mail platforms in use by the State today.<br> <br>|
|**4.4**|<br>~~**Archiving, Retention, Discovery** - The method of retaining e-mail messages to comply~~<br>with the Freedom of Information Act, Florida Public Records Law, State and Federal<br>retention requirements, Sarbanes Oxley, HIPAA or agency-specific requirements;<br>Archiving is a systematic approach to saving and protecting e-mail messages in their<br>entirety which can be retrieved by the individual user and/or a system administrator;<br>Retention is a period of time e-mail messages are retained to meet agency and/or<br>federal requirements; Discovery is the ability to search e-mail archives, journals, etc.<br>based on specific criteria to provide information for legal and public records requests;<br>Search is the ability to scan e-mails based on specific criteria such as sender, date,<br>subject, content, etc. and produce results for review. E-mail Searches for compliance<br>with Federal Rules of Civil Procedure, public record requests, court ordered production<br>of electronic records, IG or internal investigations, etc. include various levels of<br>complexity, software utilities and their underlying databases. <br>|
|**4.5**|~~**Disaster Recovery -** The services that allow an agency to continue to work during~~<br>and/or soon after a disaster. Disasters can affect one agency in the loss of a server to<br>affecting multiple agencies after a natural disaster such as a hurricane. Business<br>continuity and recovery plans are designed to address all severity levels. <br>|
|**4.6**|~~**Backup & Restore -** Making copies of data so that these additional copies may be used~~<br>to recover the original after a data loss event. <br>|
|**4.7**|~~**Security, Anti-Virus, Filtering -** The services that protect the end-user from receiving~~<br>inappropriate, threatening and/or destructive messages as well as protecting sent data. <br>|
|**4.8**|~~**Remote Access, Mobile Messaging** - The method by which a user can access their e-~~<br>mail and/or other services by means other than at their work site. <br>|
|**4.9**|~~**Additional E-mail Services** - The features and services that allow users to~~<br>communicate with their co-workers, project team, etc. outside of sending an e-mail.|



9/17/2009 AEIT 4


|Enterprise E-mail|Version: 1.5|
|---|---|
|~~Customer (Functional) Requirements~~<br>|<br>~~ Created on 07/23/2009~~|


**5.** **Requirements Workgroup Team**

|Name|Role|Contact E-mail|Contact Phone|
|---|---|---|---|
|Jason Allison|Project Lead<br>|Jason.Allison@aeit.myflorida.com|~~414-8046~~<br>|
|Scott Jecko|~~Requirements~~<br>Lead<br>|Scott.jecko@aeit.myflorida.com|~~414-6776~~<br>|
|Terry Kester|~~Requirements~~<br>Lead<br>|Terry.Kester@aeit.myflorida.com|~~413-7906~~<br>|
|Scott H. Higgins|~~Workgroup~~<br>Participant<br>|scott_higgins@dcf.state.fl.us|~~921-4487~~<br>|
|Joel Gallay|~~Workgroup~~<br>Participant<br>|gallayj@fdva.state.fl.us|~~727.518.3202 ext.~~<br>507<br>|
|James Payne|~~Workgroup~~<br>Participant<br>|James.Payne1@dot.state.fl.us|~~414-4057~~<br>|
|Stacey Burns|~~Workgroup~~<br>Participant<br>|Stacey.Burns@dot.state.fl.us|~~414-4417~~<br>|
|Phillip Gorden|~~Workgroup~~<br>Participant<br>|Phil.Gorden@dot.state.fl.us|~~728-6308~~<br>|
|Kevin Kerckhoff|~~Workgroup~~<br>Participant<br>|Kevin.Kerckhoff@dep.state.fl.us|~~245-3117~~<br>|
|<br>George Powell<br>|~~Workgroup~~<br>Participant|George.Powell@ssrc.myflorida.com|~~414-2952~~|



**6.** **Requirements Workgroup References**












|Reference Name<br>and Description|Location|
|---|---|
|~~**Preliminary Scope**~~<br>**Statement**<br>|~~AEIT Site~~<br>http://www.myflorida.com/myflorida/cabinet/aeit/index.php?pg=proj&proj<br>~~=ent_e-mail ~~<br>|
|~~**Florida Statute**~~<br>**282.34**<br>(Statewide e-mail<br>system)<br>|~~Fl Senate Site~~<br>http://www.leg.state.fl.us/STATUTES/index.cfm?App_mode=Display_Sta<br>~~tute&Search_String=&URL=Ch0282/SEC34.HTM&Title=-%3e2009-~~<br>~~%3eCh0282-%3eSection%2034%230282.34 ~~<br>|
|~~**Florida Statute**~~<br>**282.041**<br>(Definitions)|~~Fl Senate Site~~<br>http://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statut<br>~~e&Search_String=&URL=Ch0282/SEC0041.HTM&Title=->2008-~~<br>~~>Ch0282->Section%200041#0282.0041  ~~|



9/17/2009 AEIT 5


|Enterprise E-mail|Version: 1.5|
|---|---|
|~~Customer (Functional) Requirements~~<br>|<br>~~ Created on 07/23/2009~~|


**7.** **Basic Functional Requirements**






















|Req.<br>#|Category|List the basic functional requirements – what capabilities<br>should the service provide.|
|---|---|---|
|~~**1.1**~~<br>|~~**E-mail, Calendar,**~~<br>**Contacts**<br>|~~Ability for the user to send, receive, and delete e-mail and~~<br>~~attachments.~~<br>|
|~~**1.2**~~<br> <br>|~~**E-mail, Calendar,**~~<br>**Contacts**<br>|~~Ability for the user to reply to e-mail and attachments.~~<br>|
|~~**1.3**~~<br>|~~**E-mail, Calendar,**~~<br>**Contacts**<br>|~~Ability for the user to forward e-mail and attachments.~~<br>|
|~~**1.4**~~<br>|~~**E-mail, Calendar,**~~<br>**Contacts**<br>|~~Ability for the user to print e-mail messages.~~<br>|
|~~**1.5**~~<br>|~~**E-mail, Calendar,**~~<br>**Contacts**<br>|~~Ability for the user to customize e-mail messages with word~~<br>~~processor like features for formatting of e-mail content.~~<br>|
|~~**1.6**~~<br>|~~**E-mail, Calendar,**~~<br>**Contacts**<br>|~~Ability for the user to establish rules (auto reply, out of office reply,~~<br>~~temporary transfer to another party, move files to inbox folders).~~<br>|
|~~**1.7**~~<br>|~~**E-mail, Calendar,**~~<br>**Contacts**<br>|~~Ability for the user to spell check.~~<br>|
|~~**1.8**~~<br>|<br>~~**E-mail, Calendar,**~~<br>**Contacts**<br>|~~Ability for the user to organize content into personal folders or~~<br>~~similar storage mechanism to aid with e-mail retrieval.~~<br>|
|~~**1.9**~~<br>|<br>~~**E-mail, Calendar,**~~<br>**Contacts**<br>|~~Ability for the agency admin to migrate existing public folders into~~<br>~~the statewide e-mail system.~~<br>|
|~~**1.10**~~<br>|~~**E-mail, Calendar,**~~<br>**Contacts**<br>|~~Ability for the agency admin to create and manage public folders~~<br>~~or similar storage mechanism to aid with the collection,~~<br>~~organization, and sharing of information with other peop~~le in their<br>~~individual agency or organization.~~<br>|
|~~**1.11**~~<br>|~~**E-mail, Calendar,**~~<br>**Contacts**<br>|<br>~~Ability for the user to create contact lists, including those imported~~<br>~~from other sources.~~<br>|
|~~**1.12**~~<br>|~~**E-mail, Calendar,**~~<br>**Contacts**<br>|~~Ability for the user to export contact lists.~~<br>|
|~~**1.13**~~<br>|~~**E-mail, Calendar,**~~<br>**Contacts**<br>|~~Ability for the user to share contact lists / address book.~~<br>|
|~~**1.14**~~<br>|~~**E-mail, Calendar,**~~<br>**Contacts**<br>|~~Ability for the agency admin to create and share distribution lists~~<br>~~(including the ability to create query based distribution lists from~~<br>~~LDAP-like directory services).~~<br>|
|~~**1.15**~~<br>|~~**E-mail, Calendar,**~~<br>**Contacts**<br>|~~Ability for the user to create calendars and customize calendar~~<br>~~views.~~<br>|
|~~**1.16**~~<br>|~~**E-mail, Calendar,**~~<br>**Contacts**<br>|~~Ability for the user to schedule resources such as conference~~<br>~~rooms, teleconference rooms, etc.~~<br>|
|~~**1.17**~~<br>|~~**E-mail, Calendar,**~~<br>**Contacts**<br>|~~Ability for the user to create reminders and tasks.~~<br>|
|~~**1.18**~~|~~**E-mail, Calendar,**~~<br>**Contacts**|~~Ability for the agency admin to accommodate programmer testing ~~<br>~~of e-mail functionality embedded in software applications.~~|



9/17/2009 AEIT 6


|Enterprise E-mail|Version: 1.5|
|---|---|
|~~Customer (Functional) Requirements~~<br>|<br>~~  Created on 07/23/2009~~|














|1.19|E-mail, Calendar,<br>Contacts|Ability for the user to share inbox, calendar, and files with users,<br>given permission.|
|---|---|---|
|~~**1.20**~~<br>|~~**E-mail, Calendar,**~~<br>**Contacts**<br>|~~Ability for the user to delegate their permissions to another user.~~<br>|
|~~**1.21**~~<br>|~~**E-mail, Calendar,**~~<br>**Contacts**<br>|~~Ability for the user to embed links to files and websites in e-mails.~~<br>|
|~~**1.22**~~<br>|~~**E-mail, Calendar,**~~<br>**Contacts**<br>|~~Ability for the agency admin to provision e-mail accounts for their~~<br>~~individual agency or organization (including the ability to integrate~~ <br>~~e-mail account provisioning with LDAP-like directory services).~~<br>|
|~~**1.23**~~<br>|~~**E-mail, Calendar,**~~<br>**Contacts**<br>|~~Ability for the user to search for e-mails based on age, size, ~~<br>~~sender, recipient, subject, key word, attachment content.~~<br>|
|~~**1.24**~~<br>|~~**E-mail, Calendar,**~~<br>**Contacts**<br>|~~Ability for the agency admin to auto-enforce standard conventions ~~<br>~~for creating accounts and distribution lists.~~<br>|
|~~**1.25**~~<br>|~~**E-mail, Calendar,**~~<br>**Contacts**<br>|~~Ability for the data center admin to control message size limits for~~<br>~~e-mail (inbound and outbound).~~<br>|
|~~**1.26**~~<br>|~~**E-mail, Calendar,**~~<br>**Contacts**<br>|~~Ability for the agency admin to create generic email ~~<br>~~accounts/addresses to be accessed by multiple use~~rs. <br>|
|~~**1.27**~~<br>|~~**E-mail, Calendar,**~~<br>**Contacts**<br>|~~Ability for the user to customize their view in the client application~~<br>~~(such as adding fields, arranging fields, and ordering emails by~~<br>~~fields).~~<br>|
|~~**1.28**~~<br>|<br>~~**Archiving,**~~<br>**Retention,**<br>**Discovery**<br>|<br>~~Ability for the user to archive at the desktop.~~<br>|
|~~**1.29**~~<br>|~~**Archiving,**~~<br>**Retention,**<br>**Discovery**<br>|~~Ability for the agency admin to provide a server based archiving~~<br>~~solution.~~<br>|
|~~**1.30**~~<br>|~~**Archiving,**~~<br>**Retention,**<br>**Discovery**<br>|~~Ability for the agency admin to archive at various regularly defined~~<br>~~intervals.~~<br>|
|~~**1.31**~~<br>|~~**Archiving,**~~<br>**Retention,**<br>**Discovery**<br>|~~Ability for the agency admin to search archive and forward, print~~<br>~~and restore in bulk items from archive.~~<br>|
|~~**1.32**~~<br>|~~**Archiving,**~~<br>**Retention,**<br>**Discovery**<br>|~~Ability for the agency admin to filter archive by sender, recipient,~~<br>~~date, subject, content, attachments, keyword, etc.~~<br>|
|~~**1.33**~~<br>|~~**Archiving,**~~<br>**Retention,**<br>**Discovery**<br>|~~Ability for the agency admin to provide long term retention~~<br>~~separate from active e-mail system.~~<br>|
|~~**1.34**~~<br>|~~**Archiving,**~~<br>**Retention,**<br>**Discovery**<br>|~~Ability for the agency admin to provide individual users the ability ~~<br>~~to search their portion of the archive repository.~~<br>|
|~~**1.35**~~|~~**Archiving,**~~<br>**Retention,**<br>**Discovery**|~~Ability for the agency admin to meet Federal regulations for ~~<br>~~retention (i.e. Sarbanes Oxley, Gramm-Leach-Bliley Act (GL~~B), <br>~~HIPAA, etc.)~~|



9/17/2009 AEIT 7


|Enterprise E-mail|Version: 1.5|
|---|---|
|~~Customer (Functional) Requirements~~<br>|<br>~~  Created on 07/23/2009~~|






|1.36|Archiving,<br>Retention,<br>Discovery|Ability for the agency admin to satisfy legal requests for e-mail<br>discovery and provide printed or digital results.|
|---|---|---|
|~~**1.37**~~<br>|~~**Archiving,**~~<br>**Retention,**<br>**Discovery**<br>|~~Ability for the agency admin to capture all sent and received e-~~<br>~~mails into the organization.~~<br>|
|~~**1.38**~~<br>|~~**Archiving,**~~<br>**Retention,**<br>**Discovery**<br>|~~Ability for the agency admin to select the e-mail retention period~~<br>~~for a specific e-mail (e.g. 1 year, 3 year, or 5 year).~~<br>|
|~~**1.39**~~<br>|~~**Archiving,**~~<br>**Retention,**<br>**Discovery**<br>|~~Ability for the agency admin to search the e-mail "header"~~<br>~~including Date: From, Subject, To, and CC.~~<br>|
|~~**1.40**~~<br>|~~**Archiving,**~~<br>**Retention,**<br>**Discovery**<br>|~~Ability for the agency admin to search the "body" of the e-mail~~<br>~~including the header and all text contained within the e-mail its~~elf.<br>|
|~~**1.41**~~<br>|~~**Archiving,**~~<br>**Retention,**<br>**Discovery**<br>|~~Ability for the agency admin to perform a "full text" search ~~<br>~~including the header, body and any attachments to the e-m~~ail.<br>|
|~~**1.42**~~<br>|~~**Archiving,**~~<br>**Retention,**<br>**Discovery**<br>|~~Ability for the agency admin to support litigation requests by~~<br>~~production of responsive e-mail in to a specified location, for~~ read<br>~~and redaction purposes.~~<br>|
|~~**1.43**~~<br>|<br>~~**Archiving,**~~<br>**Retention,**<br>**Discovery**<br>|~~Ability for the agency admin to move older data to tiered storage~~<br>~~(lower cost storage) while maintaining accessibility.~~<br>|
|~~**1.44**~~<br>|~~**Archiving,**~~<br>**Retention,**<br>**Discovery**<br>|~~Ability for the agency admin to import data from other sources~~<br>~~such as PST, NSF files into archiving solution.~~<br>|
|~~**1.45**~~<br>|~~**Archiving,**~~<br>**Retention,**<br>**Discovery**<br>|~~Ability for the agency admin to put discovery search results on~~<br>~~legal hold to suspend deletion.~~<br>|
|~~**1.46**~~<br>|~~**Archiving,**~~<br>**Retention,**<br>**Discovery**<br>|~~Ability for the user (Legal, OIG, etc.) to review and mark discovery~~<br>~~search results.~~<br>|
|~~**1.47**~~<br>|~~**Archiving,**~~<br>**Retention,**<br>**Discovery**<br>|~~Ability for the agency admin to search using Boolean fields.~~<br>|
|~~**1.48**~~<br>|~~**Archiving,**~~<br>**Retention,**<br>**Discovery**<br>|~~Ability for the agency admin to archive based on policy (i.e. e-mail~~<br>~~address, OU, group, organization, etc.)~~<br>|
|~~**1.49**~~|~~**Archiving,**~~<br>**Retention,**<br>**Discovery**|~~Ability for the user to delete, or flag for deletion by system~~<br>~~administrators, e-mails that have met their retention, in~~<br>~~accordance with s.119.021(2)(c) which requires agenci~~es to<br>~~“systematically dispose of records no longer needed.”~~~~_(Note:_~~ <br>~~_Deletion means complete removal/elimination of all copies of_~~_ an e-_<br>~~_mail from all portions of the system)” _~~<br>|



9/17/2009 AEIT 8


|Enterprise E-mail|Version: 1.5|
|---|---|
|~~Customer (Functional) Requirements~~<br>|<br>~~  Created on 07/23/2009~~|












|1.50|Archiving,<br>Retention,<br>Discovery|Ability for the user to flag individual e-mails to not be archived.|
|---|---|---|
|~~**1.51**~~<br>|~~**Backup, Restore**~~<br>|~~Ability for the data center admin to recover at the file level.~~<br>|
|~~**1.52**~~<br>|~~**Backup, Restore**~~<br>|~~Ability for the data center admin to recover all messages.~~<br>|
|~~**1.53**~~<br>|~~**Backup, Restore**~~<br>|~~Ability for the data center admin to recover a specific e-mail~~<br>~~message.~~<br>|
|~~**1.54**~~<br>|~~**Backup, Restore**~~<br>|~~Ability for the data center admin to recover by mailbox.~~<br>|
|~~**1.55**~~<br>|~~**Backup, Restore**~~<br>|~~Ability for the data center admin to recover by time.~~<br>|
|~~**1.56**~~<br>|~~**Backup, Restore**~~<br>|~~Ability for the data center admin to maintain backup and restore~~<br>~~event logs.~~<br>|
|~~**1.57**~~<br>|~~**Backup, Restore**~~<br>|~~Ability for the data center admin to restore previous backup~~<br>~~without service interruption.~~<br>|
|~~**1.58**~~<br>|~~**Security, Anti-**~~<br>**Virus, Filtering**<br>|~~Ability for the data center admin to provide pre-emptive e-mail~~<br>~~virus protection (scanning prior to delivery at the mail server).~~<br>|
|~~**1.59**~~<br>|~~**Security, Anti-**~~<br>**Virus, Filtering**<br>|~~Ability for the data center admin to provide pre-emptive e-mail~~<br>~~content filtering.~~<br>|
|~~**1.60**~~<br>|~~**Security, Anti-**~~<br>**Virus, Filtering**<br>|~~Ability for the data center admin to whitelist/blacklist senders by ~~<br>~~domain or IP address.~~<br>|
|~~**1.61**~~<br>|<br>~~**Security, Anti-**~~<br>**Virus, Filtering**<br>|~~Ability for the data center admin to block or allow e-mail based on~~<br>~~multiple message attributes.~~<br>|
|~~**1.62**~~<br>|~~**Security, Anti-**~~<br>**Virus, Filtering**<br>|~~Ability for the data center admin to integrate message hygiene~~<br>~~(antispam/antivirus) with LDAP.~~<br>|
|~~**1.63**~~<br>|~~**Security, Anti-**~~<br>**Virus, Filtering**<br>|~~Ability for the data center admin to provide message hygiene~~<br>~~(antispam/antivirus) statistical reports.~~<br>|
|~~**1.64**~~<br>|~~**Security, Anti-**~~<br>**Virus, Filtering**<br>|~~Ability for the user to encrypt outbound e-mail.~~<br>|
|~~**1.65**~~<br>|~~**Security, Anti-**~~<br>**Virus, Filtering**<br>|~~Ability for the user to establish TLS encryption with other~~<br>~~businesses or customers.~~<br>|
|~~**1.66**~~<br>|~~**Security, Anti-**~~<br>**Virus, Filtering**<br>|~~Ability for the data center admin to protect the reputation of~~<br>~~outbound mail gateways.~~<br>|
|~~**1.67**~~<br>|~~**Security, Anti-**~~<br>**Virus, Filtering**<br>|~~Ability for the data center admin to protect internal e-mail customer~~<br>~~identity.~~<br>|
|~~**1.68**~~<br>|~~**Remote Access,**~~<br>**Mobile**<br>**Messaging**<br>|~~Ability for the user to access e-mail by secure web or client.~~<br>~~(Calendar, Address book, Ability to send and receive).~~<br>|
|~~**1.69**~~<br>|~~**Remote Access,**~~<br>**Mobile**<br>**Messaging**<br>|~~Ability for the user to access e-mail with Blackberry services using~~<br>~~BlackBerry device.~~<br>|
|~~**1.70**~~|~~**Remote Access,**~~<br>**Mobile**<br>**Messaging**|~~Ability for the user to access e-mail with non-Blackberry mobile~~<br>~~data devices (iPhones, Treos, Pres. Etc.).~~|



9/17/2009 AEIT 9


|Enterprise E-mail|Version: 1.5|
|---|---|
|~~Customer (Functional) Requirements~~<br>|<br>~~  Created on 07/23/2009~~|






|1.71|Remote Access,<br>Mobile<br>Messaging|Ability for the agency admin to support other mobile device<br>protocols (ActiveSync).|
|---|---|---|
|~~**1.72**~~<br>|~~**Remote Access,**~~<br>**Mobile**<br>**Messaging**<br>|~~Ability for the agency admin to Create, Update and Delete~~<br>~~Blackberry accounts.~~<br>|
|~~**1.73**~~<br>|~~**Remote Access,**~~<br>**Mobile**<br>**Messaging**<br>|~~Ability for the user to access mailbox and components via a web ~~<br>~~browser over a secure (encrypted) connection.~~<br>|
|~~**1.74**~~<br>|~~**Additional E-mail**~~<br>**Services**<br>|~~Ability for the user to send/receive e-mails within workflow~~<br>~~applications.~~<br>|
|~~**1.75**~~<br>|~~**Additional E-mail**~~<br>**Services**<br>|~~Ability for the user to provide resource reservations integrated into~~<br>~~e-mail.~~<br>|
|~~**1.76**~~<br>|~~**Additional E-mail**~~<br>**Services**<br>|~~Ability for the user to access an SMTP bridgehead for agency~~<br>~~applications.~~<br>|
|~~**1.77**~~|~~**Additional E-mail**~~<br>**Services**|~~Ability for the user to integrate agency applications into the e-mail~~<br>~~and mobile messaging environments.~~|



**8.** **Extended Functional Requirements**










|Req.<br>#|Category|List the extended functional requirements – what additional<br>capabilities could the service provide.|
|---|---|---|
|~~**2.1**~~<br>|~~**Archiving,**~~<br>**Retention,**<br>**Discovery**<br>|~~Ability for the user to manually archive to server from their client.~~<br>|
|~~**2.2**~~<br>|~~**Archiving,**~~<br>**Retention,**<br>**Discovery**<br>|~~Ability for the agency admin to electronically redact information ~~<br>~~from archival storage.~~<br>|
|~~**2.3**~~<br>|~~**Archiving,**~~<br>**Retention,**<br>**Discovery**<br>|~~Ability for the agency admin to digitally certify search results.~~<br>|
|~~**2.4**~~<br>|~~**Archiving,**~~<br>**Retention,**<br>**Discovery**<br>|~~Ability for the agency admin to catalog responsive e-mail (by case)~~<br>~~so that e-mail can be electronically certified as complete to fulfill~~<br>~~the production.~~<br>|
|~~**2.5**~~<br>|~~**Archiving,**~~<br>**Retention,**<br>**Discovery**<br>|~~Ability for the agency admin to demonstrate due diligence and ~~<br>~~maintain markings for privileged and non-responsive search ~~<br>~~results.~~<br>|
|~~**2.6**~~<br>|~~**Archiving,**~~<br>**Retention,**<br>**Discovery**<br>|~~Ability for the agency admin to provide a full audit trail of discovery~~<br>~~and review.~~<br>|
|~~**2.7**~~<br>|~~**Disaster**~~<br>**Recovery**<br>|~~Ability for the data center admin to do real-time replication to~~<br>~~alternate site.~~<br>|
|~~**2.8**~~|~~**Disaster**~~<br>**Recovery**|~~Ability for the data center admin to do near-time replication to~~<br>~~alternate site.~~|



9/17/2009 AEIT 10


|Enterprise E-mail|Version: 1.5|
|---|---|
|~~Customer (Functional) Requirements~~<br>|<br>~~  Created on 07/23/2009~~|










|2.9|Disaster<br>Recovery|Ability for the data center admin to fail-over mail system and<br>clients to alternate site.|
|---|---|---|
|~~**2.10**~~<br>|~~**Security, Anti-**~~<br>**Virus, Filtering**<br>|~~Ability for the data center admin to retrieve quarantined messages.~~<br>|
|~~**2.11**~~<br>|~~**Security, Anti-**~~<br>**Virus, Filtering**<br>|~~Ability for the data center admin to add digital signatures to e-mail.~~<br>|
|~~**2.12**~~<br> <br>|~~**Remote Access,**~~<br>**Mobile**<br>**Messaging**<br>|~~Ability for the user to access e-mail archive.~~<br>|
|~~**2.13**~~<br> <br>|~~**Remote Access,**~~<br>**Mobile**<br>**Messaging**<br>|~~Ability for the user to use wireless service with GIS.~~<br>|
|~~**2.14**~~<br> <br>|~~**Additional E-mail**~~<br>**Services**<br>|~~Ability for the user to provide fax service integrated into e-mail.~~<br>|
|~~**2.15**~~<br> <br>|~~**Additional E-mail**~~<br>**Services**<br>|~~Ability for the user to integrate telephone messaging (VOIP) into e-~~<br>~~mail and vice/versa.~~<br>|
|~~**2.16**~~<br> <br>|~~**Additional E-mail**~~<br>**Services**<br>|~~Ability for the user to provide List Server option for internal and ~~<br>~~external publishing of information (report subscriptions).~~<br>|
|~~**2.17**~~<br> <br>|<br>~~**Additional E-mail**~~<br>**Services**<br>|~~Ability for the agency admin to integrate directory services with~~<br>~~other complimentary external systems for a unified client ~~<br>~~experience.~~<br>|
|~~**2.18**~~<br>|~~**Additional E-mail**~~<br>**Services**|~~Ability for the agency admin to provide RSS Feeds.~~|



9/17/2009 AEIT 11


|Enterprise E-mail|Version: 1.5|
|---|---|
|~~Customer (Functional) Requirements~~<br>|<br>~~ Created on 07/23/2009~~|


**9.** **Functional Requirements Summary**


**The functional requirements discovery and analysis process yielded the following results:**

      - **Email, Calendar, and Contacts** service category had a 97% “have and use” response average.

      - **Archiving, Retention, Discovery** service category had a 66% “have and use” response average and a

23% “would like to have” response average.

      - **Disaster Recovery** service category had a 59% “have and use” response average and a 34% “would like

to have” response average.

      - **Backup & Restore** service category had a 79% “have and use” response average and a 19% “would like

to have” response average.

      - **Security, Anti-Virus, Filtering** service category had a 67% “have and use” response average and a 24%

“would like to have” response average.

      - **Remote Access, Mobile Messaging** service category had a 71% “have and use” response average and

an 11% “would like to have” response average.

      - **Additional E-mail** service category had a 48% “have and use” response average and a 26% “would like

to have” response average.


Based on these results, the majority of requirements for each category made it into the basic requirements

recommendation. In each category except for email, calendar and contacts,

the survey showed that there is a potential need for extended services (varying service components, service

levels, and costs). This is especially likely for the archiving, disaster recovery, security, and remote – mobile

messaging categories. The survey also verified that more than half of agencies polled currently have and use a

document collaboration and workflow application. However, in keeping within the scope of the statewide “e-mail,

messaging, and calendaring” system proposal, it was agreed that collaboration services (such as shared

documents and workflows, instant messaging, and discussion forums) should remain out of scope for this project.

Finally, the technical and financial feasibility of each functional requirement will be further evaluated by the

Enterprise E-mail technical and financial workgroups prior to submitting the proposed plan for statewide e-mail by

December 31, 2009.


9/17/2009 AEIT 12


