---
consensus_grade_level: 6.7
headings_per_sentence: 0.23
lists_per_sentence: 0.17
smao_sentences_pct: 6.2
vague_words_per_sentence: 0.02
anaphora_per_sentence: 0.04
sentence_cv: 1.566
cpre_terms_per_sentence: 0.36
---
# **Software Requirements Specification**

## **for the**

# **Grid-BGC Application Version 1.0**

### **Version 1.0** **Prepared By: Nathan Wilhelmi** **Monday, September 13, 2004** **Status: Draft**


_**1**_ _**Introduction ______________________________________________________7**_

**1.1** **Purpose______________________________________________________7**


**1.2** **Project Scope and Project Features_______________________________7**


**1.3** **References ___________________________________________________7**


_**2**_ _**Overall Description ________________________________________________7**_

**2.1** **Product Perspective____________________________________________7**
2.1.1 Text Narrative ______________________________________________________ 7
2.1.2 Context Diagram____________________________________________________ 7


**2.2** **User Classes and Characteristics ________________________________7**
2.2.1 Scientists (Favored) _________________________________________________ 7
2.2.2 Portal Administrator _________________________________________________ 8
2.2.3 Data Users (Lowest Priority)___________________________________________ 8


**2.3** **Typical Usage Scenarios ________________________________________8**
2.3.1 Daymet Modeling Run _______________________________________________ 8
2.3.2 BiomeBGC Modeling Run_____________________________________________ 8
2.3.3 Visualization _______________________________________________________ 8
2.3.4 Analysis___________________________________________________________ 8
2.3.5 Data download _____________________________________________________ 8
2.3.6 Data Publication ____________________________________________________ 8

**2.4** **Operating Environment _________________________________________8**
2.4.1 Web Portal ________________________________________________________ 8
2.4.2 Compute Nodes ____________________________________________________ 8
2.4.3 Client User Interface _________________________________________________ 9


**2.5** **Design and Implementation Constraints ___________________________9**
2.5.1 The system shall use the Globus toolkit. _________________________________ 9
2.5.2 NCAR Security policies and constraints. _________________________________ 9


**2.6** **User Documentation ___________________________________________9**
2.6.1 Online Help Manual _________________________________________________ 9
2.6.2 Context sensitive online help manual ____________________________________ 9

**2.7** **Assumptions and Dependencies _________________________________9**
2.7.1 The system will use the NCAR Mass Storage System for all file based storage. __ 9


_**3**_ _**System Features __________________________________________________9**_

**3.1** **User Accounts ________________________________________________9**
3.1.1 Gatekeeper Accounts ________________________________________________ 9
3.1.2 User Account Information ____________________________________________ 10
3.1.3 User Roles _______________________________________________________ 10
3.1.4 Account Creation __________________________________________________ 11
3.1.5 User Functionality __________________________________________________ 11
3.1.6 Administrative Functions_____________________________________________ 12

**3.2** **Data Organization_____________________________________________13**
3.2.1 Objects __________________________________________________________ 14
3.2.2 Projects __________________________________________________________ 14
3.2.3 Data Element Relationships __________________________________________ 14
3.2.4 Data Integrity______________________________________________________ 15


**3.3** **Objects _____________________________________________________15**
3.3.1 The system shall support 3 types of objects______________________________ 15


Page 2 of 2


3.3.2 Sharing __________________________________________________________ 15
3.3.3 Merging Objects ___________________________________________________ 15


**3.4** **Projects _____________________________________________________16**
3.4.1 Project Type ______________________________________________________ 16
3.4.2 Collaboration______________________________________________________ 16
3.4.3 New Project Creation _______________________________________________ 16
3.4.4 Referenced Objects ________________________________________________ 16

**3.5** **Template Objects _____________________________________________16**
3.5.1 Object Types______________________________________________________ 17
3.5.2 ___________________________________________________________________ 17
3.5.3 Access Control ____________________________________________________ 17
3.5.4 Submission _______________________________________________________ 17
3.5.5 Editing ___________________________________________________________ 17
3.5.6 Deletion__________________________________________________________ 17
3.5.7 Display __________________________________________________________ 17
3.5.8 Template Use _____________________________________________________ 17

**3.6** **Projection Object _____________________________________________17**
3.6.1 Collaboration______________________________________________________ 18
3.6.2 Support Projection Types ____________________________________________ 18
3.6.3 Creation _________________________________________________________ 18
3.6.4 Read ____________________________________________________________ 18
3.6.5 Update __________________________________________________________ 18
3.6.6 Delete ___________________________________________________________ 18
3.6.7 Data Downloads ___________________________________________________ 18


**3.7** **Grid Registration Object _______________________________________18**
3.7.1 Collaboration______________________________________________________ 18
3.7.2 Creation _________________________________________________________ 19
3.7.3 Read ____________________________________________________________ 19
3.7.4 Update __________________________________________________________ 19
3.7.5 Delete ___________________________________________________________ 19
3.7.6 Data Downloads ___________________________________________________ 19


**3.8** **Surface Observation Object ____________________________________19**
3.8.1 Referenced Objects ________________________________________________ 19
3.8.2 Collaboration______________________________________________________ 19
3.8.3 Supported Object Types _____________________________________________ 19
3.8.4 Creation _________________________________________________________ 19
3.8.5 Read ____________________________________________________________ 20
3.8.6 Update __________________________________________________________ 20
3.8.7 Delete ___________________________________________________________ 20
3.8.8 Visualization (Low Priority) ___________________________________________ 20


**3.9** **Site Data Object ______________________________________________20**
3.9.1 Referenced Datasets _______________________________________________ 20
3.9.2 Collaboration______________________________________________________ 20
3.9.3 Supported Object Types _____________________________________________ 20
3.9.4 Creation _________________________________________________________ 21
3.9.5 Read ____________________________________________________________ 21
3.9.6 Update __________________________________________________________ 21
3.9.7 Delete ___________________________________________________________ 21
3.9.8 Visualization (Low Priority) ___________________________________________ 21


**3.10** **Daymet Parameterization Object ________________________________21**
3.10.1 Collaboration ___________________________________________________ 21
3.10.2 Creation _______________________________________________________ 22


Page 3 of 3


3.10.3 Read __________________________________________________________ 22
3.10.4 Update ________________________________________________________ 22
3.10.5 Delete _________________________________________________________ 22

**3.11** **DEM Object __________________________________________________22**
3.11.1 Collaboration ___________________________________________________ 22
3.11.2 Object Types ___________________________________________________ 22
3.11.3 Creation _______________________________________________________ 22
3.11.4 Read __________________________________________________________ 22
3.11.5 Update ________________________________________________________ 23
3.11.6 Delete _________________________________________________________ 23
3.11.7 Visualization (Low Priority) _________________________________________ 23


**3.12** **Analysis Mask Object _________________________________________23**
3.12.1 Collaboration ___________________________________________________ 23
3.12.2 Object Types ___________________________________________________ 23
3.12.3 Creation _______________________________________________________ 23
3.12.4 Read __________________________________________________________ 23
3.12.5 Update ________________________________________________________ 23
3.12.6 Delete _________________________________________________________ 23
3.12.7 Visualization (Low Priority) _________________________________________ 24


**3.13** **Daymet Project _______________________________________________24**
3.13.1 Referenced Objects ______________________________________________ 24
3.13.2 Templates______________________________________________________ 24
3.13.3 Sharing ________________________________________________________ 24
3.13.4 Creation _______________________________________________________ 24
3.13.5 Read __________________________________________________________ 24
3.13.6 Update ________________________________________________________ 24
3.13.7 Delete _________________________________________________________ 24
3.13.8 Model Runs ____________________________________________________ 25


**3.14** **Daymet Output Object _________________________________________25**
3.14.1 Collaboration ___________________________________________________ 25
3.14.2 Creation _______________________________________________________ 25
3.14.3 Read __________________________________________________________ 25
3.14.4 Contained datasets_______________________________________________ 25
3.14.5 Deletion________________________________________________________ 26
3.14.6 Data Downloading _______________________________________________ 26


**3.15** **Plant Functional Type Object ___________________________________26**
3.15.1 Sharing ________________________________________________________ 26
3.15.2 Templates______________________________________________________ 26
3.15.3 Creation _______________________________________________________ 26
3.15.4 PFT Id’s _______________________________________________________ 26
3.15.5 Read __________________________________________________________ 26
3.15.6 Update ________________________________________________________ 26
3.15.7 Delete _________________________________________________________ 26

**3.16** **BiomeBGC Site Data Object ____________________________________27**
3.16.1 Collaboration ___________________________________________________ 27


**3.17** **Output Specification Object ____________________________________27**
3.17.1 Collaboration ___________________________________________________ 27
3.17.2 User Interface ___________________________________________________ 27
3.17.3 Creation _______________________________________________________ 27
3.17.4 Read __________________________________________________________ 27
3.17.5 Update ________________________________________________________ 28
3.17.6 Delete _________________________________________________________ 28


Page 4 of 4


**3.18** **Nitrogen Deposition Object_____________________________________28**
3.18.1 Collaboration ___________________________________________________ 28
3.18.2 Object Types Supported___________________________________________ 28
3.18.3 Creation _______________________________________________________ 28
3.18.4 Read __________________________________________________________ 28
3.18.5 Update ________________________________________________________ 28
3.18.6 Delete _________________________________________________________ 28
3.18.7 Invalidated Objects _______________________________________________ 29


**3.19** **Disturbance Objects __________________________________________29**
3.19.1 Collaboration ___________________________________________________ 29
3.19.2 Creation _______________________________________________________ 29
3.19.3 Read __________________________________________________________ 29
3.19.4 Update ________________________________________________________ 29
3.19.5 Delete _________________________________________________________ 29


**3.20** **BiomeBGC Project ____________________________________________29**
3.20.1 Referenced Projects______________________________________________ 30
3.20.2 Simulation Topology______________________________________________ 30
3.20.3 Creation _______________________________________________________ 30
3.20.4 Read __________________________________________________________ 30
3.20.5 Update ________________________________________________________ 30
3.20.6 Delete _________________________________________________________ 30
3.20.7 Model Runs ____________________________________________________ 31
3.20.8 Invalidated Projects ______________________________________________ 31


**3.21** **BiomeBGC Output Object ______________________________________31**
3.21.1 Sharing ________________________________________________________ 31
3.21.2 Templates______________________________________________________ 31
3.21.3 Creation _______________________________________________________ 31
3.21.4 Read __________________________________________________________ 32
3.21.5 Deletion________________________________________________________ 32
3.21.6 Data Downloading _______________________________________________ 32


**3.22** **Daymet Visualization Project ___________________________________32**


**3.23** **BiomeBGC Visualization Project ________________________________32**


**3.24** **Evaluation Project ____________________________________________32**


**3.25** **Portal Administration__________________________________________32**
3.25.1 Portal Metrics ___________________________________________________ 32
3.25.2 System Consistency Check ________________________________________ 33


_**4**_ _**External Interface Requirements ____________________________________33**_


**4.1** **User Interfaces _______________________________________________33**
4.1.1 The web portal shall be usable in the following web browsers________________ 33


_**5**_ _**The system shall require the users enable cookies to use the system._____33**_

**5.1** **Hardware Interfaces___________________________________________34**
5.1.1 NCAR Mass Storage System (MSS) ___________________________________ 34


**5.2** **Software Interfaces ___________________________________________34**


**5.3** **Communication Interfaces _____________________________________34**


_**6**_ _**Other Nonfunctional Requirements __________________________________34**_


**6.1** **Performance Requirements ____________________________________34**


Page 5 of 5


**6.2** **Safety Requirements __________________________________________34**


**6.3** **Security Requirements ________________________________________34**


**6.4** **Software Quality Requirements _________________________________34**


_**7**_ _**To Be Determined (TBD) Items ______________________________________34**_


_**8**_ _**Appendix A: Data Dictionary and Data Model __________________________34**_


_**9**_ _**Appendix B: Analysis Models. ______________________________________34**_


Page 6 of 6


## **1 Introduction**

_**1.1**_ _**Purpose**_
_**1.2**_ _**Project Scope and Project Features**_
_**1.3**_ _**References**_

Reference the proposal document.

## **2 Overall Description**

_**2.1**_ _**Product Perspective**_


_2.1.1 Text Narrative_


This project is to develop a grid-based software infrastructure to support bio-geochemical modeling. The application will use the Daymet surface weather interpolation
engine for generating gridded surface weather datasets from observation data records.
The Biome-BGC model will be used to perform BGC modeling activities.

The system shall provide a graphical user interface to all functions of the system. Grid
technologies shall be utilized to provide secure and reliable communications to remote
computing resources.


_2.1.2 Context Diagram_


_**2.2**_ _**User Classes and Characteristics**_


_2.2.1 Scientists (Favored)_


Scientific users are the favored and primary user class for the system. Scientific users
will use the system to manage input data, run simulations, visualize results, and manage
output data.


Page 7 of 7


_2.2.2 Portal Administrator_


The portal administrator will be in charge of managing the day to day operations of the
system. This user will be responsible for managing user accounts, managing user runs if
needed, and general portal settings and monitoring.


_2.2.3 Data Users (Lowest Priority)_
### Data users are researchers who need to use simulation output but who do not have the

ability to initiate simulations.


_**2.3**_ _**Typical Usage Scenarios**_


_2.3.1 Daymet Modeling Run_


Scenario where the user goes to the portal to run a daymet run. This is the primary goal,
do we need to address the issue where the first thing the user does is setup the
supporting data?


_2.3.2 BiomeBGC Modeling Run_


Scenario where the user goes to the portal to run a BiomeBGC run. This is the primary
goal, do we need to address the issue where the first thing the user does is setup the
supporting data?


_2.3.3 Visualization_


Scenario where the users wants to visualize the output datasets


_2.3.4 Analysis_


Scenario where the user wants to perform post processing on the data, such as the
model performance evaluation studies on the output.


_2.3.5 Data download_


Scenario where the user wants to pull download the output data for further analysis etc.


_2.3.6 Data Publication_


Scenario where the user wants to publish output data for the community, i.e. directly
publish the data on dataportal.

_**2.4**_ _**Operating Environment**_


_2.4.1 Web Portal_


The web portal components shall integrate into the Dataportal Web Server at
NCAR


_2.4.2 Compute Nodes_


The compute node software shall be developed and deployed for the
Hemisphere Linux cluster at CU


Page 8 of 8


_2.4.3 Client User Interface_


The system shall provide a web based (portal) user interface for all aspects of
the system.

_**2.5**_ _**Design and Implementation Constraints**_


_2.5.1 The system shall use the Globus toolkit._


_2.5.2 NCAR Security policies and constraints._


_**2.6**_ _**User Documentation**_


_2.6.1 Online Help Manual_


1. Full online manual
2. Major sections listed in TOC


_2.6.2 Context sensitive online help manual_


1. Each page will have a context sensitive link to the help system
2. Each context sensitive help page will be displayed in a pop-up window.
3. The link will display the topic relevant for the page.
4. The TOC will not be displayed in the context sensitive view.

_**2.7**_ _**Assumptions and Dependencies**_


_2.7.1 The system will use the NCAR Mass Storage System for all file based storage._

## **3 System Features**


_**3.1**_ _**User Accounts**_

Access to the functional areas of the system will be controlled by user accounts.


_3.1.1 Gatekeeper Accounts_


1. All GridBGC users shall be required to have valid NCAR Gatekeeper accounts to use
the system.
2. Not all Gatekeeper account holders will have access to the GridBGC system. Users
must be approved by the GridBGC administrator(s) for access.

3.1.1.1 Passwords

1. NCAR Gatekeeper password policies will be governed by the NCAR Gatekeeper
tools and policies. Enforcement of these policies and procedures will NOT be
enforced through the GridBGC portal.
2. Users must use the existing Gatekeeper tools to manage their passwords.


Page 9 of 9


_3.1.2 User Account Information_


1. The system shall retrieve all user information from the Gatekeeper account system.

3.1.2.1 User accounts will have the following status states:

1. Pending Confirmation
2. Pending Approval
3. Active
4. Locked
5. Deleted (Place holder for deleted accounts but needed to maintain internal data
structures)


_3.1.3 User Roles_


1. The system shall support the following user roles:
1.1. User – General end user of the system
1.2. Administrator – Has additional permissions to administer the operation of the
system.


Page 10 of 10


_3.1.4 Account Creation_


_3.1.5 User Functionality_


3.1.5.1 Apply for an account

End users can apply for an account directly through the web portal.

1. Users must enter all required fields
2. The user must enter their NCAR Gatekeeper username.



Page 11 of 11


3.1.5.2 View account details

The user can view their current account details

1. User must be logged in to the portal
2. Display all the account properties
3. Password will not be displayed

3.1.5.3 Delete account

1. The system shall provide a means to request that the user account be deleted from
the system.
2. The system shall notify the portal admin(s) about the delete requests

3.1.5.4 Login to system

The system shall require the user to enter their username and password to login to the
system.

1. The user shall be prompted at the beginning of the session for their credentials, once
logged in they will not be prompted for additional or different credentials.
2. All login actions shall be protected by using secure data channels
3. The system shall lock the account after 3 login attempts. This will require portal
admin action to unlock the account.
4. Admin users will be authenticated against the portal database.
5. Users will be authenticated against the NCAR Gatekeeper system.


_3.1.6 Administrative Functions_


3.1.6.1 Approve Accounts

1. Portal Admin(s) will receive e-mail notification when new accounts are ready for
review.
2. Display a list of all accounts pending review
3. Approve specific account
4. Approve account
4.1. Add message
5. Reject account
5.1. Add message

3.1.6.2 Assign Template Submission Privileges

1. The system shall allow portal administrators the ability to control template
submissions rights.

3.1.6.3 List Accounts

The portal admin shall have the ability to list the user accounts in the system


Page 12 of 12


1. List all user accounts
2. List accounts pending approval
3. List all account deletion requests
4. List all locked accounts

3.1.6.4 Delete Accounts

1. Delete a specific user account
2. There operation will not be reversible
3. Data removal
3.1. Templates
3.1.1: All user submitted templates will NOT be deleted from disk
3.2. Shared Objects
3.2.1: All shared object that have NOT been referenced by dependant projects
will be deleted.
3.3. All other objects/projects
3.3.1: Will be deleted completely from the system.

3.1.6.5 Lock/Unlock accounts

1. The admin can lock accounts
1.1. The user will be notified via e-mail
1.2. Further logins will not be permitted until unlocked
1.3. Currently executing jobs will continue to run until the job ends or terminated by
the portal admin
2. The admin can unlock accounts
2.1. Once unlocked the user can login to the system and resume use

3.1.6.6 Job Management

1. The portal admin will have a display of all running jobs sorted by user
2. The status of each job and tile will be visible to the portal admin
3. The portal admin shall have the ability to terminate any user’s running jobs.

3.1.6.7 Assign User Roles

1. The system shall assign all user accounts to the scientist role by default.
2. The system shall allow the portal admin to change a user’s role in the system.

3.1.6.8 Resource Quotas (Lowest Priority)
_Review the need to implement resource quotas if time permits at the end of the project._

_**3.2**_ _**Data Organization**_

The system will organize the system in to types of logical grouping elements:
1. Objects


Page 13 of 13


2. Projects


_3.2.1 Objects_


Objects will be elements the group related data elements in the system. Objects will be
the mechanism by which data is shared and reused throughout the system.


_3.2.2 Projects_


Projects will be elements that group specific objects together to perform a unit of work.


_3.2.3 Data Element Relationships_


Page 14 of 14


_3.2.4 Data Integrity_


1. The system shall prevent the user from changing object/project values once that
project has been used in a model run. _This is to preserve the input values that_
_produced a certain set of output values._
2. Each object/project will have states which control when the user can change product
values.
3. The system shall support the following states
3.1. Unlocked – The user can make changes as desired.
3.2. Locked – The user can not make any changes
3.3. Invalidated – A dependency has been modified in someway and object/project
may no longer have valid inputs or outputs.

**NOTE:** See specific object/project details for the logic rules for each type.
_Go through the whole locked/invalidation sequence, try to do it at a very generic level._

_**3.3**_ _**Objects**_

Objects will manage datasets and references to other logically related datasets.


_3.3.1 The system shall support 3 types of objects_


3.3.1.1 List Objects

1. List objects will contain arbitrary points of data
2. The system will NOT enforce any spatial constraints on list datasets

3.3.1.2 Grid Objects

1. Grid objects will contain rectangular grid datasets.

3.3.1.3 Parameterization Objects

1. Parameterization projects will contain model specific parameter data


_3.3.2 Sharing_


1. Users can select to share specific objects with other users.
2. Users can specify which users to share the object with:
2.1. All users
2.2. Select specific users within the system
3. When a shared project is referenced in the system the underlying datasets will NOT
be copied.
4. Once a shared project has been referenced elsewhere in the system it will be in a
locked state.


_3.3.3 Merging Objects_


Users can create new dataset project by merging existing objects


Page 15 of 15


1. Project must be of the same type, list or grid
2. Merging operation will always be used to create new datasets from two existing
datasets.
3. Merge sources can be:
3.1. Current users existing projects
3.2. Other users projects that have been shared
4. No data validation will be done at this stage
4.1. Will not check for duplicate data
4.2. Will not check for spatial relationships of data.
4.3. Will not check for missing values
5. Full copies of the source datasets will be made during the creation of the merged
dataset.
6. The system shall display dataset metadata to allow users to screen data prior to
merging operations.

_**3.4**_ _**Projects**_

Project will have two main functions within the system; contain references to supporting
datasets and serve as the simulation run control element.


_3.4.1 Project Type_


1. The user shall specify the type of project during initial setup; either List or Grid
2. The system shall only allow the user to reference datasets of the same type as
specified in the project


_3.4.2 Collaboration_


1. Projects cannot be shared or be templates.


_3.4.3 New Project Creation_


1. The user can create new projects.

1. List data projects
2. Grid projects


_3.4.4 Referenced Objects_


1. The system shall allow the user to only select referenced objects that are of the
appropriate type
1.1. List and Grid types matching shall be enforced.

_**3.5**_ _**Template Objects**_

System templates will provide a means of sharing expert knowledge within the portal.


Page 16 of 16


_3.5.1 Object Types_


1. Not all Object types shall support templates, see specific object details for more
details.


_3.5.2_


_3.5.3 Access Control_


1. Any user of the system shall be able to use a template.


_3.5.4 Submission_


1. Only users with template submission privileges can submit new templates.


_3.5.5 Editing_


1. Once a template has been submitted it can no longer be edited.


_3.5.6 Deletion_


1. The system shall allow the following users to delete templates from the system:
1.1. Portal Admin(s)
1.2. The user who originally created the template


_3.5.7 Display_


1. The system shall provide portal admin(s) with a list of all system templates by project
type.
2. The system shall provide users with a list of their templates in the system.


_3.5.8 Template Use_


1. Any time a template is used the user shall get their own full private copy of the data
2. The user must supply a new project name when using a template before saving the
project.
3. If the template references a non-shared data resource the user must choose a new
dataset before saving the project.

### **Daymet Specific Objects and Projects**

_**3.6**_ _**Projection Object**_

This object defines the projection parameters for a dataset.


Page 17 of 17


_3.6.1 Collaboration_


1. Projection Objects can be templates.


_3.6.2 Support Projection Types_


The system shall support the following projection types
1. Geographic
2. UTM
3. Albers Conical Equal Area
4. Lambert Conformal Conic
5. Lambert Azimuthal Equal Area
6. Interrupted Goode Homolosine
7. Interrupted Mollweide


_3.6.3 Creation_


1. New Blank
2. Copied from system template.


_3.6.4 Read_


1. View List of projection projects
2. View Projection Details


_3.6.5 Update_


1. The project must be in an unlocked state
2. The user can change the parameter values
3. The user can NOT change the projection type


_3.6.6 Delete_


1. If the project is in an unlocked state
1.1. The project and all related data can be deleted.
2. If the project is in a locked state
2.1. The user shall be prompted to delete all projects that reference this project
following the candidate project deletion rules.


_3.6.7 Data Downloads_


1. This information will not be downloadable by the user.

_**3.7**_ _**Grid Registration Object**_


_3.7.1 Collaboration_


1. Projection Objects can be templates.


Page 18 of 18


_3.7.2 Creation_


1. New Blank
2. Copied from system template


_3.7.3 Read_


1. View List of Grid Registration objects
2. View Grid Registration Details


_3.7.4 Update_


1. The project must be in an unlocked state
2. The user can change the parameter values


_3.7.5 Delete_


1. If the object is in an unlocked state
1.1. The project and all related data can be deleted.
2. If the object is in a locked state
2.1. The user shall be prompted to delete all projects that reference this object
following the candidate object deletion rules.


_3.7.6 Data Downloads_


1. This information will not be downloadable by the user.

_**3.8**_ _**Surface Observation Object**_

This dataset contains observed surface weather data. This is one the primary input data
sets in the Daymet model.


_3.8.1 Referenced Objects_


None


_3.8.2 Collaboration_


1. Projection Objects can be shared.


_3.8.3 Supported Object Types_


1. List


_3.8.4 Creation_


1. New Blank Object
1.1. User must upload data files to the system
1.1.1: Reference required NetCDF file convention
1.1.2: Specify required archive structure
2. Merge existing objects
2.1. The user can combine 2 discrete objects into 1 new singular object
2.1.1: The system shall not perform any checking or conversion


Page 19 of 19


3. Subset existing object
3.1. The user can create a new object from a subset of a single existing object.
3.2. How is the subset performed specified?


_3.8.5 Read_


1. The system shall display a list of all the objects the user currently has in the system
2. The system shall display the object details
2.1. Display all metadata associated for the object
2.1.1: The system shall display all the stations for object
2.1.2: The system shall display all the data values for each station


_3.8.6 Update_


1. _Address the invalidation logic for locked state…._
2. Delete the project and start over.


_3.8.7 Delete_


1. The system shall allow the user to delete an unlocked project.
2. _Address the invalidation logic for locked state…._
3. The system shall allow the user to delete a locked project under the following
conditions:
3.1. The user has selected to delete all associated projects that reference the
project.
4. The system shall delete all associated input and model output data for this project
during deletion.


_3.8.8 Visualization (Low Priority)_


1. TBD - Later

_**3.9**_ _**Site Data Object**_

_Reference: Data model elements for this section_


_3.9.1 Referenced Datasets_


None


_3.9.2 Collaboration_


1. Site Data Objects can be shared.


_3.9.3 Supported Object Types_


1. List
2. Grid


Page 20 of 20


_3.9.4 Creation_


1. New Blank Object
1.1. User can upload files to the system
1.1.1: List File Formats
1.1.2: Specify required archive structure
2. Merge existing objects
3. Subset of existing object
3.1. Data extraction process
3.1.1: The user can enter a series of data points
3.1.2: The user can select a source object
3.1.3: The system shall extract the specified points from the dataset and store
them in a new dataset in the system.


_3.9.5 Read_


1. The system shall display a list of all the objects the user currently has in the system
2. The system shall display the object details
2.1. Display all metadata associated for the object


_3.9.6 Update_


1. Grid Type:
1.1. Delete and start over.
2. List Type:
2.1. The system shall provide user interface to manage the observation points
2.2. The system shall allow a user to add new data points
2.3. The system shall allow a user to edit existing data points
2.4. The system shall allow a user to delete existing data points


_3.9.7 Delete_


_3.9.8 Visualization (Low Priority)_


1. TBD - Later

_**3.10 Daymet Parameterization Object**_

This project contains all the parameterizations values for a daymet model run.


_3.10.1 Collaboration_


1. Daymet Parameterization Objects can be templates.


Page 21 of 21


_3.10.2 Creation_


1. New Blank Object
1.1. The system shall provide a user interface to manage all parameterization
values.


_3.10.3 Read_


1. The system shall display a list of all the objects the user currently has in the system
2. The system shall display the object details
2.1. Display all metadata associated for the object


_3.10.4 Update_


1. _Go through the locked / invalidation sequence_


_3.10.5 Delete_


1. Go through the locked / invalidation sequence

_**3.11 DEM Object**_

Object that contains DEM datasets and the associated Analysis mask data.


_3.11.1 Collaboration_


1. DEM Objects can be shared.


_3.11.2 Object Types_


_1._ List datasets
_2._ Grid datasets


_3.11.3 Creation_


1. New Blank Object
1.1. User can upload files to the system
1.1.1: DEM Datasets
1.1.1.1. NetCDF
1.1.1.2. _What is the native model format?_
1.1.2: Analysis Masks
1.1.2.1. NetCDF

2. Merge existing objects
3.


_3.11.4 Read_


1. The system shall display a list of all the objects the user currently has in the system
2. The system shall display the object details
2.1. Display all metadata associated for the object


Page 22 of 22


_3.11.5 Update_


1. _Go through the locked / invalidation sequence_


_3.11.6 Delete_


1. Go through the locked / invalidation sequence


_3.11.7 Visualization (Low Priority)_


1. TBD – Later

_**3.12 Analysis Mask Object**_


_3.12.1 Collaboration_


1. Analysis Mask objects can be shared.


_3.12.2 Object Types_


_1._ List datasets
_2._ Grid datasets


_3.12.3 Creation_


1. New Blank Object
1.1. User can upload files to the system
1.1.1: DEM Datasets
1.1.1.1. NetCDF
1.1.1.2. _What is the native model format?_
1.1.2: Analysis Masks
1.1.2.1. NetCDF

2. Merge existing objects


_3.12.4 Read_


1. The system shall display a list of all the objects the user currently has in the system
2. The system shall display the object details
2.1. Display all metadata associated for the object


_3.12.5 Update_


2. _Go through the locked / invalidation sequence_


_3.12.6 Delete_


2. Go through the locked / invalidation sequence


Page 23 of 23


_3.12.7 Visualization (Low Priority)_


2. TBD – Later

_**3.13 Daymet Project**_

This project aggregates all input objects and simulation control functions.

This project is the defining project for determining whether the project chain is list or grid
based.


_3.13.1 Referenced Objects_


1. Site Data Object
2. Surface Weather Data Object
3. Projection Object
_3.1. Must be the same as other input objects_
4. Registration
_4.1. Must be the same as other input objects_
_5._ DEM Object


_3.13.2 Templates_


1. This project can NOT be a template.


_3.13.3 Sharing_


1. This project can NOT be shared.


_3.13.4 Creation_


1. New Blank Project


_3.13.5 Read_


1. The system shall display a list of all the projects the user currently has in the system
2. The system shall display the project details
2.1. Display all metadata associated for the project


_3.13.6 Update_


1. The system shall allow the user to delete an unlocked data project.
2. _TODO – Reference the whole project dependency flow…._


_3.13.7 Delete_


1. The system shall allow the user to delete an unlocked project.
2. The system shall allow the user to delete a locked project under the following
conditions:
2.1. The user has selected to delete all associated projects that reference the
project.


Page 24 of 24


3. The system shall delete all associated input and model output data for this project
during deletion.


_3.13.8 Model Runs_


1. The system shall allow user to start a new model run.
1.1. The system shall display a list of computational resources to select from.
1.2. The system shall provide the user with an approximate execution time estimate
based on the computational resource selected.
2. The system shall allow the user to monitor and control model runs
2.1. The system shall display a list of runs currently active for the user
2.2. The system shall display the overall run status
2.3. Daymet model runs shall be monitored on a tile by tile basis.
2.3.1: The system shall display the list of tiles for a run.
2.3.2: The system shall maintain the following information for each tile:
2.3.2.1. Status – Queued, Running, Complete, Error
2.3.2.2. The system shall save and display Stdout messages.
2.3.2.3. The system shall save and display Stderr messages.
3. The system shall allow the user to terminate a model run.
3.1. The system shall delete all output data associated with the run
3.1.1: Cached input files
3.1.2: Temporary files
3.1.3: Output files
4. The system shall allow a user to restart a model run.
4.1. The system shall only permit a run to be restarted under the following
conditions:
4.1.1: The previous instance has completed
4.1.2: The previous instance has been terminated
4.2. The system shall delete all previous model output prior to starting the run.

_**3.14 Daymet Output Object**_

This is the object that will contain the output data for a daymet run……


_3.14.1 Collaboration_


1. Daymet Output Objects can be shared.


_3.14.2 Creation_


1. The systems shall automatically create this object for completed simulation runs


_3.14.3 Read_


1. Display a list of objects for a user
2. Display the details of each object
3. List all tiles for a object.


_3.14.4 Contained datasets_


1. Cross Validation Output


Page 25 of 25


2. Model Weather Data output


_3.14.5 Deletion_


1. _Reference: the invalidation logic flow…._


_3.14.6 Data Downloading_


1. The system shall allow the user to download the output data from the portal.
1.1. The system shall display a list of all the output tiles to the user.
1.2. The system shall allow the user to download the data files on a tile by tile basis.
1.3. The system shall allow the user to download the data in the native system
formats and conventions only.

### **BiomeBGC Specific Objects and Projects**

_**3.15 Plant Functional Type Object**_


_3.15.1 Sharing_


1. Plant Functional Type Objects can be shared.


_3.15.2 Templates_


1. Plant Functional Type Objects can NOT be templates.


_3.15.3 Creation_


1. New Blank Object
1.1. User can upload files to the system
1.1.1: EPC File Format
1.1.2: Raw ASCII file format, not archived.
1.2. User can hand enter the values


_3.15.4 PFT Id’s_


_1._ User can hand enter the PFT Id number. _This is so it can be related back to a site_
_data project._


_3.15.5 Read_


1. List user’s objects
2. List object values [list object only]


_3.15.6 Update_


_3.15.7 Delete_


Reference deletion logic.


Page 26 of 26


3.15.7.1 Download

1. The system shall allow the user to download the data in an EPC file format.

_**3.16 BiomeBGC Site Data Object**_

This will encapsulate the site data specific for the BiomeBGC runs….


_3.16.1 Collaboration_


1. Projection Objects can be shared.

References:
Projection
Registration

_**3.17 Output Specification Object**_

The biome bgc model has approximately 700 possible output variables. It is not
realistically possible to use all the 700 output variables to perform meaningful analysis.


_3.17.1 Collaboration_


1. Output Specification Objects can be templates.


_3.17.2 User Interface_


3.17.2.1 The system shall provide a graphical user interface to manage the output
parameters.

1. Parameter Categories
1.1. The system shall provide 1 level of parameter categorization
1.2. The system shall provide a list of all parameters for each category
1.3. The system shall allow the user to select individual parameters as needed.
2. Selected Categories
2.1. The system shall provide a display of the categories a user currently has
selected.
2.2. The system shall provide a method to add new categories to the project.
2.3. The system shall provide a method to remove categories from the project.


_3.17.3 Creation_


1. New Blank Object
2. Copy other user’s object


_3.17.4 Read_


1. The system shall display the list of objects the user currently has.
2. The system shall allow the user to view the details of a specific object.


Page 27 of 27


_3.17.5 Update_


1. The system shall allow the user to modify an unlocked object.


_3.17.6 Delete_


1. The system shall allow users to delete unlocked objects.
2. The system shall allow users to delete locked objects under the following conditions:
2.1. The user shall be able to choose to delete all objects referencing this object.

_**3.18 Nitrogen Deposition Object**_


_3.18.1 Collaboration_


1. Nitrogen Deposition Objects can be templates.


_3.18.2 Object Types Supported_


1. List Datasets
2. Grid Datasets


_3.18.3 Creation_


1. New Blank object
1.1. User can upload files to the system
1.1.1: List File Formats
1.1.2: Specify required archive structure
1.2. User can hand enter the values [list project only]
1.2.1: Provide GUI interface for entering values
2. Merge existing list objects


_3.18.4 Read_


1. List user’s objects in the system
2. List individual object details


_3.18.5 Update_


1. Grid objects
1.1. Cannot be updated, must delete/create new.
2. List Objects
2.1. Unlocked projects can be edited via online GUI


_3.18.6 Delete_


1. The system shall allow the user to delete unlocked objects.
2. The system shall allow the user to delete locked objects.
2.1. All dependant objects/projects shall be invalidated


Page 28 of 28


_3.18.7 Invalidated Objects_


1. The system shall change the project to an unlocked state.
2. Invalidate all dependant projects.

_**3.19 Disturbance Objects**_

A disturbance object contains the information representing climate factors that influence
the biome-BGC model. This includes information such as fires and deforestation events.

A disturbance project will have a series of events.
Each disturbance project can have an unlimited number of events
Each event will have a particular date in time associated with it.
An event occurs at a particular point in time, it does not have an associated duration.

The system shall support the following types of events:
1. Fire
2. Deforestation

The user shall specify the intensity value for the event
TBD – Is there a specific range we can check for here?


_3.19.1 Collaboration_


1. Projection Objects can be templates.


_3.19.2 Creation_


1. The user shall be able to create a new disturbance object


_3.19.3 Read_


1. The system shall list the user’s objects in the system
2. The system shall list the object details


_3.19.4 Update_


1. Unlocked Objects
1.1. The system shall allow users to edit unlocked objects
2. Locked Objects
2.1. The system shall allow users to edit locked objects
2.2. The system shall invalidate dependent objects


_3.19.5 Delete_


1. The system shall allow the user to delete unlocked objects.
2. The system shall allow the user to delete locked objects.
2.1. All dependant objects/projects shall be invalidated

_**3.20 BiomeBGC Project**_


Page 29 of 29


_3.20.1 Referenced Projects_


1. Daymet Output Object
2. BiomeBGC Site Data
3. PFT Object
4. Ouput Specification Project


_3.20.2 Simulation Topology_


1. The system shall allow the user to define a simulation topology
2. The user shall be able to create the following topology options
2.1. 1 Site x 1 PFT
2.2. 1 Site x all PFT’s
2.3. All Sites x 1 PFT’s
2.4. All Sites x All PFT’s
2.5. n Sites x 1 PFT
2.6. n Sites x All PFT’s
2.7. n Sites x n PFT’s
2.8. 1 Site x n PFT’s
2.9. All Sites x n PFT’s
2.10. Site Specific PFT List (number and weight) – _TBD - What is this?_


_3.20.3 Creation_


1. The system shall allow the user to create new blank projects


_3.20.4 Read_


2. The system shall list all the user’s projects in the system
3. The system shall display all the project details


_3.20.5 Update_


1. The system shall allow the user to change the project details for unlocked projects.
2. The system shall allow the user to ability to invalidate a locked project.
2.1. Will this trigger all running jobs to be terminated?
2.2. This will trigger all downstream projects to be invalidated.


_3.20.6 Delete_


3. The system shall allow the user to delete unlocked projects.
4. The system shall allow the user to delete locked projects.
4.1. All dependant objects/projects shall be invalidated


Page 30 of 30


_3.20.7 Model Runs_


1. The system shall allow user to start a new model run.
1.1. The system shall display a list of computational resources to select from.
2. The system shall allow the user to monitor and control model runs
2.1. The system shall display a list of runs currently active for the user
2.2. The system shall display the overall run status
2.3. BiomeBGC model runs shall be monitored on a tile by tile basis.
2.3.1: The system shall display the list of tiles for a run.
2.3.2: The system shall maintain the following information for each tile:
2.3.2.1. Status – Queued, Running, Complete, Errror
2.3.2.2. The system shall save and display Stdout messages.
2.3.2.3. The system shall save and display Stderr messages.
3. The system shall allow the user to terminate a model run.
3.1. The system shall delete all output data associated with the run
3.1.1: Cached input files
3.1.2: Temporary files
3.1.3: Output files
4. The system shall allow a user to restart a model run.
4.1. The system shall only permit a run to be restarted under the following
conditions:
4.1.1: The previous instance has completed
4.1.2: The previous instance has been terminated


_3.20.8 Invalidated Projects_


3. The system shall change the project to an unlocked state.
4. Invalidate all dependant projects.
5. The system shall delete the output data project if created
5.1. Delete all the files from disk storage as well.

_**3.21 BiomeBGC Output Object**_

This is the object that will contain the output data for a BiomeBGC run……


_3.21.1 Sharing_


2. BiomeBGC Output Objects can be shared.


_3.21.2 Templates_


1. BiomeBGC Output Objects can NOT be templates.


_3.21.3 Creation_


2. The systems shall automatically create this object for completed simulation runs


Page 31 of 31


_3.21.4 Read_


4. Display a list of projects for a user
5. Display the details of each project
6. List all tiles for a project.


_3.21.5 Deletion_


2. _Reference: the invalidation logic flow…._


_3.21.6 Data Downloading_


2. The system shall allow the user to download the output data from the portal.
2.1. The system shall display a list of all the output tiles to the user.
2.2. The system shall allow the user to download the data files on a tile by tile basis.
2.3. The system shall allow the user to download the data in the native system
formats and conventions only.

_**3.22 Daymet Visualization Project**_
TBD

_**3.23 BiomeBGC Visualization Project**_
TBD

_**3.24 Evaluation Project**_
TBD

_**3.25 Portal Administration**_


_3.25.1 Portal Metrics_


1. Currently Registered Users
2. Data Metrics
2.1. Number of files
2.2. Total storage size
2.3. Average File size
3. Computational Metrics
3.1. # of jobs completed
3.2. # of jobs running
3.3. # of jobs queued
4. Template Metrics
4.1. # of templates by object type
5. Objects/Projects Metrics
5.1. # of Objects/Projects by type
5.2. # of Objects/Projects by type and by user
6. Shared Objects/Projects
6.1. # of Objects/Projects by type
6.2. # of Objects/Projects by type and by user


Page 32 of 32


_3.25.2 System Consistency Check_


1. The system shall provide the portal admin a function to validate file references in the
system correspond to actual files on the storage system.
2. The system shall generate a listing of any missing files.
3. Error Correction


3.25.2.1 Compute Node Resources

1. The system shall list all the compute nodes
2. The system shall display the compute node resource details
3. The system shall allow the admin to manage compute resources
3.1. Add new nodes
3.2. Lock a node
3.3. Unlock a node
3.4. Delete nodes
4. The system shall allow the admin to change compute node settings

4.1. _TBD – Determine what the admin can change…._

3.25.2.2 System Settings

1. The system shall allow the portal admin to control the following system settings
1.1. _TBD – List all the general configuration settings the admin has control over._

## **4 External Interface Requirements**

_**4.1**_ _**User Interfaces**_


_4.1.1 The web portal shall be usable in the following web browsers_


1. Internet Explorer 6.0
2. Netscape 7.1
3. Safari 1.2.1?

## **5 The system shall require the users enable cookies** **to use the system.**


Page 33 of 33


_**5.1**_ _**Hardware Interfaces**_


_5.1.1 NCAR Mass Storage System (MSS)_


5.1.1.1 The system shall allow users the ability to store data on the NCAR Mass Storage
System.

_**5.2**_ _**Software Interfaces**_
_**5.3**_ _**Communication Interfaces**_

## **6 Other Nonfunctional Requirements**

_**6.1**_ _**Performance Requirements**_

_**6.2**_ _**Safety Requirements**_
_**6.3**_ _**Security Requirements**_
_**6.4**_ _**Software Quality Requirements**_

## **7 To Be Determined (TBD) Items** **8 Appendix A: Data Dictionary and Data Model**


_Do example data dictionary_

## **9 Appendix B: Analysis Models.**


_Workflows, GUI Maps, etc…._


Page 34 of 34


