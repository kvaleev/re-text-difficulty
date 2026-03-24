---
consensus_grade_level: 11.9
headings_per_sentence: 0.0
lists_per_sentence: 0.0
smao_sentences_pct: 1.0
vague_words_per_sentence: 0.04
anaphora_per_sentence: 0.18
sentence_cv: 1.425
cpre_terms_per_sentence: 0.34
---
The address of this document is:
<http://www.perceptek.com.au/kteam/docs/srs.html>

------------------------------------------------------------------------

+-----------------------------------------------------------------------+
| # Software Requirements Specification                                 |
+-----------------------------------------------------------------------+

------------------------------------------------------------------------

+-----------------------------------------------------------------------+
| # The MultiMahjong Project                                            |
|                                                                       |
| # K-Team                                                              |
|                                                                       |
| -------------------------------------------------------------------   |
|                                                                       |
|                                                                       |
|                                                                       |
| ::: {align="left"}                                                    |
| ### Team Members:                                                     |
|                                                                       |
| ###                                                                   |
|                                                                       |
| +--------------------------------+--------------------------------+   |
| | 1.  **Joanna Araminta**        | **(Project Manager)\           |   |
| |     ::: {align="left"}         | (Technical Researcher)\        |   |
| |     **Victor Leung**           | (Client Liaison Officer, Web   |   |
| |     **Joel Brakey**            | Site Manager)\                 |   |
| |     **Michael Hart**           | (Secretary, Web Site Manager,  |   |
| |     **Dean Cortinovis**        | Backup Manager)\               |   |
| |     **Long Tang**              | (Technical Researcher)\        |   |
| |     :::                        | (Technical Researcher and Risk |   |
| |                                | Manager)**                     |   |
| +--------------------------------+--------------------------------+   |
|                                                                       |
| ### **Abstract:**                                                     |
|                                                                       |
| ### Maintainer:                                                       |
|                                                                       |
| ### Version Control:                                                  |
| :::                                                                   |
|                                                                       |
|                                                                       |
|                                                                       |
|                                                                       |
|                                                                       |
| ## Table Of Contents                                                  |
|                                                                       |
| 1.  [**Introduction**](#Anchor-1)                                     |
| 2.  [**The Existing Logical System**](#Anchor-2)                      |
| 3.  [**The Proposed Logical System**](#Anchor-3)**\                   |
|     **[3.1 Data Flow Diagrams (DFDs)](#Anchor-3.1)\                   |
|     [3.2 Data Dictionary](#Anchor-3.2)                                |
| 4.  [**Functional Requirements\                                       |
|     **](#Anchor-4)[4.1 The MultiMahjongServer](#Anchor-4.1)[**\       |
|     **](#Anchor-4)[4.2 Beginning the Game](#Anchor-4.2)[**\           |
|     **](#Anchor-4)[4.3 Playing the Game](#Anchor-4.3)**\              |
|     **[4.4 Ending the Game](#Anchor-4.4)**\                           |
|     **[4.5 Computer Opponent (CO)](#Anchor-4.5)                       |
| 5.  [**Non-Functional Requirements**](#Anchor-5)**\                   |
|     **[5.1 Nature of the Users](#Anchor-5.1)\                         |
|     [5.2 Error Handling](#Anchor-5.2)\                                |
|     [5.3 Implementation Constraints](#Anchor-5.3)\                    |
|     [5.4](#Anchor-5.4) [Hardware Constraints](#Anchor-5.4)\           |
|     [5.5 Performance Constraints](#Anchor-5.5)\                       |
|     [5.6 Security Requirements](#Anchor-5.6)                          |
| 6.  [**User Interface Requirements\                                   |
|     **](#Anchor-6)[6.1 User Interface -                               |
|     MultiMahjongServer](#Anchor-6.1)[**\                              |
|     **](#Anchor-6)[6.2 User Interface -                               |
|     MultiMahjongClient](#Anchor-6.2)[**\                              |
|     **](#Anchor-6)[6.3 Graphical User Interface -                     |
|     MultiMahjongClient](#Anchor-6.3)                                  |
| 7.  [**Document/Training Requirements\                                |
|     **](#Anchor-7)[7.1 MultiMahjongServer                             |
|     Documentation](#Anchor-7.1)[**\                                   |
|     **](#Anchor-7)[7.2 MultiMahjongClient                             |
|     Documentation](#Anchor-7.2)[**\                                   |
|     **](#Anchor-7)[7.3 Coding and Design Documentation](#Anchor-7.3)  |
| 8.  [**Acceptance Criteria**](#Anchor-8)                              |
| 9.  [**Examples of Behaviour\                                         |
|     **](#Anchor-9)[9.1 Beginning the Game](#Anchor-9.1)[**\           |
|     **9.2 Playing the Game](#Anchor-9.2)[**\                          |
|     **](#Anchor-9)[9.3 Ending the Game](#Anchor-9.3)                  |
| 10. [**Glossary**](#Anchor-10)                                        |
| 11. [**Customer Sign-Off**](#Anchor-11)                               |
|                                                                       |
| ##  Table Of Figures                                                  |
|                                                                       |
| 1.  [**Figure 3.1.1 - Level 0 DFD of the MultiMahjong                 |
|     System**](#Anchor-3.1.1)                                          |
| 2.  [**Figure 3.1.2 - Level 1 DFD of the MultiMahjong                 |
|     System**](#Anchor-3.1.2)                                          |
| 3.  [**Figure 6.3.1 - Draft of the Proposed Main                      |
|     Window**](#Anchor-6.3.1)                                          |
|                                                                       |
| ### []{#Anchor-1}1. Introduction                                      |
|                                                                       |
| 1.  *Essential*\                                                      |
|     The minimum set of requirements for the product to be accepted    |
|     (see [Section 8](#Anchor-8)).                                     |
| 2.  *Highly Desirable*\                                               |
|     Requirements that are considered to be likely inclusions to the   |
|     product, time permitting.                                         |
| 3.  *Desirable*\                                                      |
|     Requirements that are not likely to be added in this version, but |
|     should be considered for future modifications.                    |
|                                                                       |
| MultiMahjong is a product consisting of two programs - a              |
| MultiMahjongServer and a MultiMahjongClient. This Server/Client       |
| architecture will allow up to 4 players to play Mahjong against each  |
| other over a TCP/IP network. The MultiMahjongClient program will also |
| allow 1 player to play in a stand-alone mode.                         |
|                                                                       |
| As any game of Mahjong requires 4 players to play, and there may not  |
| be 4 people available for a network game, the game will allow users   |
| to choose enough computer opponents to make up the required 4         |
| players. In a single player game, the user will play against 3        |
| computer opponents.                                                   |
|                                                                       |
| To play the game, users will use the MultiMahjongClient. The          |
| MultiMahjongServer is to reside on a TCP/IP server and will           |
| communicate with MultiMahjongClients.                                 |
|                                                                       |
| The client requires the product for commercial purposes. The          |
| MultiMahjongClient program is to be sold to potential users (see      |
| [Section 5.1.1](#Anchor-5.1)) and the MultiMahjongServer is to        |
| initially reside on a server owned or operated by the client.         |
|                                                                       |
| The client for this project is:                                       |
|                                                                       |
| Our team for the project is called K-Team and consists of:            |
|                                                                       |
| The supervisor for the project is:                                    |
|                                                                       |
| []{#Anchor-Rules}This document contains many references to the rules  |
| of Mahjong, specifically the Chinese rules of Mahjong. It is assumed  |
| that the reader of this document is familiar with these rules as many |
| of the requirements are Mahjong specific. These rules can be found in |
| the following book:                                                   |
|                                                                       |
|                                                                       |
|                                                                       |
| ### []{#Anchor-2}2. The Existing Logical System                       |
|                                                                       |
|                                                                       |
|                                                                       |
| ### []{#Anchor-3}3. The Proposed Logical System                       |
|                                                                       |
| As this is only a *suggestion* for the proposed logical system, all   |
| requirements mentioned in this section are Level 2 requirements.      |
|                                                                       |
| #### []{#Anchor-3.1}3.1 Data Flow Diagrams (DFDs)                     |
|                                                                       |
|                                                                       |
|                                                                       |
| []{#Anchor-3.1.2}**![](srs_files/level1_dfd.gif){width="520"          |
| height="367"}**                                                       |
|                                                                       |
| #### []{#Anchor-3.2}3.2 Data Dictionary                               |
|                                                                       |
|                                                                       |
|                                                                       |
| ### []{#Anchor-4}4. Functional Requirements                           |
|                                                                       |
| This section states the requirements that relate to the functionality |
| of the MultiMahjong system. Each requirement has been prioritised     |
| according to the levels set out in the Introduction ([see Section     |
| 1](#Anchor-1)). Requirements that relate to what is displayed on the  |
| user\'s screen are defined in [Section 6](#Anchor-6).                 |
|                                                                       |
| Note that for single player games, the MultiMahjongServer will not be |
| required and the player need not be connected to a TCP/IP network.    |
| Although many requirements mention that the MultiMahjongClient will   |
| send certain information to the MultiMahjongServer, in the single     |
| player game, this is not the case. In a single player game, the       |
| MultiMahjongClient will intercept this information and process it     |
| internally. The reference to the MultiMahjongServer is made to reduce |
| duplicate requirements.                                               |
|                                                                       |
| #### []{#Anchor-4.1}4.1 The MultiMahjongServer                        |
|                                                                       |
| *Level 1 Requirements:*                                               |
|                                                                       |
| *Level 2 Requirements:*                                               |
|                                                                       |
| *Level 3 Requirements:*                                               |
|                                                                       |
| Note that all requirements hereafter are concerned with the           |
| MultiMahjongClient program.                                           |
|                                                                       |
| #### []{#Anchor-4.2}4.2 Beginning the Game                            |
|                                                                       |
| *Level 1 Requirements:*                                               |
|                                                                       |
| *Level 2 Requirements:*                                               |
|                                                                       |
| *Level 3 Requirements:*                                               |
|                                                                       |
| #### []{#Anchor-4.3}4.3 Playing the Game                              |
|                                                                       |
| *Level 1 Requirements:*                                               |
|                                                                       |
| *Level 2 Requirements:*                                               |
|                                                                       |
| *Level 3 Requirements:*                                               |
|                                                                       |
| #### []{#Anchor-4.4}4.4 Ending the Game                               |
|                                                                       |
| *Level 1 Requirements:*                                               |
|                                                                       |
| *Level 2 Requirements:*                                               |
|                                                                       |
| *Level 3 Requirements:*                                               |
|                                                                       |
| #### []{#Anchor-4.5}4.5 Computer Opponent (CO)                        |
|                                                                       |
| *Level 1 Requirements:*                                               |
|                                                                       |
| *Level 2 Requirements:*                                               |
|                                                                       |
| *Level 3 Requirements:*                                               |
|                                                                       |
|                                                                       |
|                                                                       |
| ### []{#Anchor-5}5. Non-Functional Requirements                       |
|                                                                       |
| This section states all the requirements of the MultiMahjong system   |
| that are not related to the functionality of the MultiMahjong system. |
|                                                                       |
| #### []{#Anchor-5.1}5.1 Nature of the Users                           |
|                                                                       |
| #### 5.1.1 MultiMahjongClient                                         |
|                                                                       |
| ```{=html}                                                            |
| <!-- -->                                                              |
| ```                                                                   |
|                                                                       |
| #### 5.1.2 MultiMahjongServer                                         |
|                                                                       |
| *Level 1 Requirements:*                                               |
|                                                                       |
| #### []{#Anchor-5.2}5.2 Error Handling                                |
|                                                                       |
| Every error that occurs during program execution can be classified    |
| into two types - fatal and nonfatal errors. The distinction between   |
| the two is that the program is unable to continue to execute upon     |
| encountering a fatal error.                                           |
|                                                                       |
| #### 5.2.1 Nonfatal errors:                                           |
|                                                                       |
| *Level 1 Requirements:*                                               |
|                                                                       |
| *Level 2 Requirements:*                                               |
|                                                                       |
| #### 5.2.2 Fatal errors:                                              |
|                                                                       |
| *Level 1 Requirements:*                                               |
|                                                                       |
| #### []{#Anchor-5.3}5.3 Implementation Constraints                    |
|                                                                       |
| *Level 1 Requirements:*                                               |
|                                                                       |
| *Level 3 Requirements:*                                               |
|                                                                       |
| #### []{#Anchor-5.4}5.4 Hardware Constraints                          |
|                                                                       |
| *Level 1 Requirements:*                                               |
|                                                                       |
| *Level 2 Requirements:*                                               |
|                                                                       |
| #### []{#Anchor-5.5}5.5 Performance Constraints                       |
|                                                                       |
| *Level 1 Requirements:*                                               |
|                                                                       |
| #### []{#Anchor-5.6}5.6 Security Requirements                         |
|                                                                       |
| ###                                                                   |
|                                                                       |
|                                                                       |
|                                                                       |
| ### []{#Anchor-6}6. User Interface Requirements                       |
|                                                                       |
| This section states all the requirements of the MultiMahjong system   |
| that are related to what the user sees and how the user interacts     |
| with the MultiMahjong system.                                         |
|                                                                       |
| #### []{#Anchor-6.1}6.1 User Interface - MultiMahjongServer           |
|                                                                       |
| *Level 1 Requirements:*                                               |
|                                                                       |
| *Level 2 Requirements:*                                               |
|                                                                       |
| #### []{#Anchor-6.2}6.2 User Interface - MultiMahjongClient           |
|                                                                       |
| *Level 1 Requirements:*                                               |
|                                                                       |
| *Level 2 Requirements:*                                               |
|                                                                       |
| *Level 3 Requirements:*                                               |
|                                                                       |
| #### []{#Anchor-6.3}6.3 Graphical User Interface - MultiMahjongClient |
|                                                                       |
| The graphical user interface (GUI) described below only applies to    |
| the MultiMahjongClient program. As the validity of these requirements |
| will not be determined until the design phase, most of them are Level |
| 2 or Level 3 requirements. As described in [Section                   |
| 6.2.1](#Anchor-6.2), the *existence* of the GUI is a Level 1          |
| requirement, however, the *detail* of the GUI is not necessarily so.  |
|                                                                       |
| *Level 1 Requirements:*                                               |
|                                                                       |
| *Level 2 Requirements:*                                               |
|                                                                       |
| *Level 3 Requirements:*                                               |
|                                                                       |
| []{#Anchor-6.3.1}![Main Window Image](srs_files/gui.gif){width="536"  |
| height="396"}                                                         |
|                                                                       |
| ###                                                                   |
|                                                                       |
|                                                                       |
|                                                                       |
| ### []{#Anchor-7}7. Document/Training Requirements                    |
|                                                                       |
| This section states all the documentation which is required to be     |
| included with the MultiMahjong product. There will be no formal       |
| training sessions arranged. The documentation included with the       |
| MultiMahjongClient and MultiMahjongServer applications will be of     |
| sufficient quality for users (see [Section 5.1](#Anchor-5.1)) to      |
| learn how to use the programs without any further explanation.        |
|                                                                       |
| #### []{#Anchor-7.1}7.1 MultiMahjongServer Documentation              |
|                                                                       |
| *Level 1 Requirements:*                                               |
|                                                                       |
| *Level 2 Requirements:*                                               |
|                                                                       |
| *Level 3 Requirements:*                                               |
|                                                                       |
| #### []{#Anchor-7.2}7.2 MultiMahjongClient Documentation              |
|                                                                       |
| *Level 1 Requirements:*                                               |
|                                                                       |
| *Level 2 Requirements:*                                               |
|                                                                       |
| #### []{#Anchor-7.3}7.3 Coding and Design Documentation               |
|                                                                       |
| *Level 1 Requirements:*                                               |
|                                                                       |
| *Level 2 Requirements:*                                               |
|                                                                       |
| ###                                                                   |
|                                                                       |
|                                                                       |
|                                                                       |
| ###                                                                   |
|                                                                       |
| []{#Anchor-8}8. Acceptance Criteria                                   |
|                                                                       |
|                                                                       |
|                                                                       |
| ### []{#Anchor-9}9. Examples of Behaviour                             |
|                                                                       |
| This section describes a possible scenario that incorporates some of  |
| the requirements mentioned in this document. As some of the           |
| requirements used are Level 2 and Level 3 requirements, the actual    |
| implementation of the product may not reflect this scenario exactly.  |
|                                                                       |
| #### []{#Anchor-9.1}9.1 Beginning the Game                            |
|                                                                       |
| #### []{#Anchor-9.2}9.2 Playing the Game                              |
|                                                                       |
| #### []{#Anchor-9.3}9.3 Ending the Game                               |
|                                                                       |
|                                                                       |
|                                                                       |
| ### []{#Anchor-10}10. Glossary                                        |
|                                                                       |
| ###                                                                   |
|                                                                       |
|                                                                       |
|                                                                       |
| ### []{#Anchor-11}11. Customer Sign-Off                               |
|                                                                       |
| I (the client), hereby agree that the requirements specified within   |
| this document agree with my own requirements and expectations of the  |
| product, and abide by the Acceptance Criteria ([Section               |
| 8](#Anchor-8)).                                                       |
|                                                                       |
| Any alterations to any of the Acceptance Criteria specified above,    |
| are to be negotiated between myself and the team.                     |
|                                                                       |
| Team Members:                                                         |
|                                                                       |
| Date: \_\_\_/\_\_\_/\_\_\_                                            |
+-----------------------------------------------------------------------+

------------------------------------------------------------------------

[**Other Documentation**](http://www.perceptek.com.au/kteam/docs/)

------------------------------------------------------------------------
