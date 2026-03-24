---
consensus_grade_level: 12.2
headings_per_sentence: 0.0
lists_per_sentence: 0.0
smao_sentences_pct: 0.9
vague_words_per_sentence: 0.12
anaphora_per_sentence: 0.17
sentence_cv: 1.389
cpre_terms_per_sentence: 0.88
---
### **_Central Trading System_**
## **_— subsystem of Stock Trading_**
#### **_System_**

# **_Software_** **_Requirements_** **_Specification_**

###### Team leader : 陈徐希 Author : 陈徐希、管铮、 刘世林、赖剑、 吴玉书 Version ：    1.0 Date ： 9.27.2007


**TABLE CONTENTS**

**1** **INTRODUCTION......................................................................................................... 3**

1.1 GOALS AND OBJECTIVES .......................................................................................... 3
1.2 SYSTEM CONTEXT.................................................................................................... 3
1.3 Potential Users’ Specification ................................................................................ 3

**2** **USER SCENARIO........................................................................................................ 3**

2.1 USER PROFILES ......................................................................................................... 3
2.2 USER SCENARIOS SPECIFICATION ............................................................................. 4
_2.2.1_ _personal opinion ............................................................................................. 4_
_2.2.2_ _Develop use-cases within which user-secnarios are specified .................... 4_
_2.2.3_ _Use-case diagram for Central Trading System function.............................. 8_


**3** **DATA FLOW DIAGRAM........................................................................................... 9**

3.1 CONTEXT_LEVEL DFD............................................................................................. 9
3.2 LEVEL 1 DFD OF CENTRAL TRADING SYSTEM ....................................................... 9
3.3 LEVEL 2 DFD OF THE INSTRUCTION PRETRETEMENT ...........................................10
3.4 LEVEL 2 DFD OF THE INSTRUCTION INSTRUCTION MANAGER .............................11

**4** **DATA DICTIONARY................................................................................................12**

**5** **STATE DIAGRAM.....................................................................................................13**

**6** **CRC INDEX CARDS .................................................................................................15**

**7** **VALIDATION CRITERIA.......................................................................................16**

7.1 INTERFACE CEITERIA..............................................................................................16
7.2 FUNCTION CEITERIA ...............................................................................................17


**2** **Version 1.0**


##### **1. Introduction**

**1.1** **Goals and objectives**

The central trading system (CTS) is to complete the trading of stock. It analyses the
instructions that enter the central trading system and divides them into several kinds of
instructions. System will make a match between them under specifically prescripts. Also
central trading system provides some interfaces to send messages to other modules.

**1.2** **System Context**

The CTS is just a subsystem of the whole stock trading system (STS) system. There
are mainly six subsystems involved, stock account operation, financing account operation,
trade client serve, network message promulgating, centeral trading system and trading
system manage. Communications exist among these subsystems which complicates the
relationships between subsystems.
The CTS receive instructions from trade client serve. Then the CTS produce new
messages which to be sent to network message promulgating after deal with the
instructions from trade client serve. Also the system manager is authorization to access
the information in CTS.

**1.3** **Potential Users’ Specification**

There are mainly two kinds of users. The CTS provides the terminal users easy
Operations that are confined to a series of mouse clicks and keyboard, which compared to
other systems are really much simplified. However, for another user, things are
different .the maintainers of this CTS must be familiar with java programming and the
socket. When the system crashes down, they can find the cause and fix it. When new
requirements should be supported, they can modify the program to make it fit.
As the instruction is frequently operated in CTS such as fetch, deal with, repeal and
so on, the CTS is heavily transferred. The program must take this into consideration. The
maintainers of CTS should have good strategies to overcome crash of the system when
overhead exceeds the capacity of it.

##### **2. User Scenario**

**2.1** **User Profiles**

There are mainly five kinds of actors, which here consist of other related sub-systems,
involved with our Central Trading System. They are Transaction User Interface, Security


**3** **Version 1.0**


Account Management, Trading Management System, Trading Information Release.

**2.2** **User Scenarios Specification**

**2.2.1** **Personal Opinion**

Often, user-scenario is considered the same to use-case. They both can help our team
understand how system functions and features will be used by different classes of
end-users (actors). However, I prefer to understand it like this: a user scenario is a
particular environment within a specified use case. So, I will specify user-scenarios going
along with developing use cases in the next session.

**2.2.2** **Develop Use-Cases within which User-Scenarios are specified**







|Use-case|Buy stock|
|---|---|
|**Primary actor**|Transaction User Interface|
|**Goal in context**|To fulfill the buy transaction|
|**Preconditions**|Customer has successfully logged into UI and submit the buy<br>information|
|**Trigger**|The ‘buy’ button on UI been clicked|
|**Scenario**|1. transaction user interface: give the buy instruction<br>2. central trading system: save the buy instruction<br>3. central trading system: match the instructions with the<br>same stock id<br>4. central trading system: make a trade by matching<br>5. central trading system: modify the information of matched<br>instructions|
|**Exception**|1. all the operations have been suspended<br>2. some trade exceptions come up<br>3. no matched stock with the buy instruction|
|**Priority**|Essential, must be implemented|
|**When available**|First increment|
|**Frequency of use**|Frequent|
|**Channel to actor**|Via transaction user interface|
|**Secondary actors**|Trading System Management|
|**Channels to**<br>**secondary actors**|Via central trading system interface|


**4** **Version 1.0**


|Use-case|Sell stock|
|---|---|
|**Primary actor**|Transaction User Interface|
|**Goal in context**|To fulfill the sell transaction|
|**Preconditions**|Customer has successfully logged into UI and submit the sell<br>information|
|**Trigger**|The ‘sell’ button on UI been clicked|
|**Scenario**|1. transaction user interface: give the sell instruction<br>2. central trading system: save the sell instruction<br>3. central trading system: match the instructions with the<br>same stock id<br>4. central trading system: make a trade by matching<br>5. central trading system: modify the information of matched<br>instructions|
|**Exception**|1. all the operations have been suspended<br>2. some deal exceptions come up<br>3. no matched stock with the buy instruction|
|**Priority**|Essential, must be implemented|
|**When available**|First increment|
|**Frequency of use**|Frequent|
|**Channel to actor**|Via transaction user interface|
|**Secondary actors**|Trading System Management|
|**Channels to**<br>**secondary actors**|Via central trading system interface|
|**Open issues**|1. Should the trade information return to Transaction User<br>Interface immediately when the deal is done?<br>2. Should the failure of trade return to Transaction User<br>Interface the next day?<br>3. If exception happens, is exception log needed?<br>4. security issue|



**5** **Version 1.0**


|Use-case|Cancel trading instruction|
|---|---|
|**Primary actor**|Transaction User Interface|
|**Goal in context**|To fulfill the cancel transaction|
|**Preconditions**|Customer has successfully logged into UI and submit the<br>cancel information|
|**Trigger**|The ‘cancel’ button on UI been clicked|
|**Scenario**|1. transaction user interface: give the cancel instruction<br>2. central trading system: save the cancel instruction<br>3. central trading system: cancel the correlative instruction|
|**Exception**|1. all the operations have been suspended<br>2. the instruction concerned has been implemented<br>3. no matched instruction to be cancelled|
|**Priority**|Moderate, to be implemented after basic functions|
|**When available**|Second increment|
|**Frequency of use**|Many times per day|
|**Channel to actor**|Via transaction user interface|
|**Secondary actors**|Trading System Management|
|**Channels to**<br>**secondary actors**|Via central trading system interface|
|**Open issues**|1. Is it necessary to return the status of cancel transaction?<br>2. If exception happens, is exception log needed?<br>3. security issue|


|Use-case|Save trade information|
|---|---|
|**Primary actor**|Security Account Management|
|**Goal in context**|To save all successful trade information|
|**Preconditions**|The correlative trade transactions have been successfully<br>conducted|
|**Trigger**|Any trade transaction been conducted|
|**Scenario**|1. central trading system: give out the successful trade<br>information<br>2. security account management: save the trade information|


**6** **Version 1.0**


|Exception|1. all the operations have been suspended<br>2. no matched stock with the buy instruction|
|---|---|
|**Priority**|Essential, must be implemented|
|**When available**|First increment|
|**Frequency of use**|Frequent|
|**Channel to actor**|Via central trading system interface|
|**Secondary actors**|Trading System Management|
|**Channels to**<br>**secondary actors**|Via central trading system interface|
|**Open issues**|1. If exception happens, is exception log needed?<br>2. Will we develop a media (ie. Web page) where any<br>customer can look up the latest trade records which have<br>been saved?<br>3. security issue|









|Use-case|Query trade information|
|---|---|
|**Primary actor**|Trading Information Release|
|**Goal in context**|To query the trading information which needed to be<br>statistically analyzed and released on a web site|
|**Preconditions**|Central Trading System deal transactions well|
|**Trigger**|Trading Information Release System send a query|
|**Scenario**|1. trading information release system: send a query<br>2. central trading system: implement the query<br>3. central trading system: structuralize the queried data<br>4. central trading system: send the data to release|
|**Exception**|1. all the operations have been suspended<br>2. the query is invalid<br>3. no matched data|
|**Priority**|Essential, must be implemented|
|**When available**|First increment|
|**Frequency of use**|Frequent|
|**Channel to actor**|Via central trading system interface|
|**Secondary actors**|Trading System Management|


**7** **Version 1.0**


|Channels to<br>secondary actors|Via central trading system interface|
|---|---|
|**Open issues**|1. If exception happens, is exception log needed?<br>2. How frequent the release system is to send a query?<br>3. Do we need a warning if any query failed?<br>4. security issue|



**2.2.3** **Use-case diagram for Central Trading System function**


**8** **Version 1.0**


##### **3 Data Flow Diagram**

**3.1** **Context-level DFD for the stock trade system**


Hint: we only indicate the flow that involved the central trading system.

**3.2** **Level-1 DFD for the central trade system**


**9** **Version 1.0**


The instructions first arrive at the instruction pretreatment modular which will judge
the validity of the instruction and freeze the fund and write the log files. Then the
instructions will go to the instructions manager modular. This modular will deal with all
the three kinds of instructions. Then it will send the results to the Trading client serve and
information releasing modular as well as keep a log file.

**3.3** **Level 2 DFD for the instruction pretreatment**


**10** **Version 1.0**


The instructions analysis will identify the kind of the instructions. Then it will deal
with the illegal instructions like the raising limit and freezing the fund in the Data Base.
In addition, it will keep log file about the instructions.


**3.4** **Level-2 DFD of the instructions manager**


**11** **Version 1.0**


In this level the three kinds of instructions will go to three different modules. The
query instruction will refer to the Data Base or the instructions list. The cancel instruction
will delete the instruction the instruction in the instructions list. And the trade instruction
will go to the trade manager to make a match in the instructions list.

##### **4 Data Dictionary**


**12** **Version 1.0**


|Name|Alias|When /how to use|Description|
|---|---|---|---|
|central trading<br>system|CTS|receive the instructions and<br>return the result.|to accomplish the matching work of the stock<br>trading system as well as the query.|
|user instruction||trading client serve(output)<br>CTS(input)|Indicate the users’ instruction (buy、sell、query),<br>also include the trading quantity, and the time<br>stamp.|
|instruction<br>result||CTS(output)<br>|Indicate the handled result and return to the<br>other three sub system of the whole stock<br>trading system.|
|DB instruction||Data Base(input)|Include the query and writing and modifying<br>instructions to the Data Base|
|newest trading<br>result||CTS(output)<br>Information<br>releasing module(input)|Send the newest trading result and status to the<br>information releasing module.|
|Instruction<br>pretreatment||deal the instruction for first<br>step|Judge the validity of the instruction<br>Write the log file<br>Freeze the fund of user’s account|
|instruction<br>manager||deal the instruction in detail.|has the instruction input and deal with it.|
|log instruction||trading client serve (output)<br>CTS (input)|Indicate the users’ instruction (buy、sell、query),<br>also include the trading quantity, and the time<br>stamp.|
|freezing fund||instruction<br>pretreatment(output)<br>DB (input)|Freeze the user’s corresponding account accord<br>to the trade instruction.|
|list instruction||instruction manager(output)<br>instruction list(input)|The instruction that involve the several<br>operations of the list as well as the making<br>match of the instructions.|

##### **5 State Diagram**





**13** **Version 1.0**


Here is the state diagram. There are several states in the diagram, which are decoding,
researching, canceling, analyzing, rejecting, queuing, storing, matching, queue modifying,
responding. The flow between the adjacent states goes their way according to specific
conditions which are displayed on the flow line.


**14** **Version 1.0**


##### 6 CRC index cards

|Class: PretreatmentOfInstruction|Col2|
|---|---|
|Description:|Description:|
|After a new instruction come, we must get key information from instruction and solve some<br>simple problems by necessary constraints and some key rules|After a new instruction come, we must get key information from instruction and solve some<br>simple problems by necessary constraints and some key rules|
|Responsibility:|Collaborator:|
|Determination<br>of<br>prices’increments<br>and<br>decrements constraints of Instruction||
|Freeze account of buyers|ManagementOfDatabase|
|Prededuct commission charge and tax|ManagementOfDatabase|
|Log instruction||
|Send to Management of instruction|ManagementOfInstruction|


|Class: ManagementOfInstruction|Col2|
|---|---|
|Description:|Description:|
|Manage and maintain the instructions of buyers and sellers|Manage and maintain the instructions of buyers and sellers|
|Responsibility:|Collaborator:|
|Add instructions||
|Cancel instructions||
|Search instructions||
|Sort instructions||
|Class: ManagementOfInstruction||


|Class: ManagementOfDealing|Col2|
|---|---|
|Description:|Description:|
|Deal business following the key rules, and some operations are executed after the deals|Deal business following the key rules, and some operations are executed after the deals|
|Responsibility:|Collaborator:|



**15** **Version 1.0**


|Deal the business|Col2|
|---|---|
|Log the results of business||
|Store some key data to database|ManagementOfDatabase|
|Determine the commission charge and tax||


|Class: ManagementOfDatabase|Col2|
|---|---|
|Description:|Description:|
|Support the basic operations interface of database for other modules|Support the basic operations interface of database for other modules|
|Responsibility:|Collaborator:|
|Operations of account, insert, delete, update||
|Operations of stock, insert, delete, update||

##### 7 Validation Criteria

**7.1** **Interface criteria**

The central trading system has relation with three modules that are trading client
serve、trading manager system、information releasing module. These modules have
contact with CTS using the interface supplied by CTS.

**7.1.1** **Transaction User Interface**

The Transaction User Interface has to input the instructions. The input instruction is
divided into three kinds: buy instruction, sell instruction and query instruction.

_a) buy instruction_
This instruction should have five parameters: user ID, stock ID, quantity,
respected price, timestamp.

_b) sell instruction_
This instruction should have five parameters: user ID, stock ID, quantity,
respected price, timestamp.

_c) query instruction_
This instruction can be divided into two kinds: user query instruction and
the stock query instruction. The user query instruction should have three


**16** **Version 1.0**


parameters: user ID, query content, some restrict parameters. The stock query
instruction should has three parameters: stock ID，query content, some restrict
parameter。

**7.1.2** **Information Releasing Module**

The information releasing module use the interface to find the price of the stocks.
The input should has two parameters including the stock name and the restrict
parameter.

**7.1.3** **Trading manager system**

The trading manager system uses the interface to find the user’s trading instruction.
The input should has two parameters including the trading instruction type(buy or
sell),and the restrict parameter.

**7.2** **Function Criteria**

The CTS deals with trading instruction, query instruction and some cancel
instruction. The functions are as follows:

_1)_ _instruction matching_
When the client serve get a trading instruction, it will send the instruction to the
CTS to trade with other trading instructions. The process of the trading includes the
following two main principles: price first principle and the time first principle. If the
trading fails when these two principles have been applied, we should refer to another
principle. If the lowest buy price is higher than the highest sell price, then the CTS
will make a match of this trading.

_2)_ _rising and falling limit_
If the trading price is higher(lower) than the rising limit (falling limit), the CTS
will reject this trading instruction.

_3)_ _return the result_
The CTS will return the result to the client serve for any trading instructions than
go into the CTS.
The trading states are divided into two kinds: totally finished and the partially
finished.

_4)_ _outdated instruction_
If a instruction haven’t finished it’s trading in one day, then it will be removed
form the CTS for out of date.


**17** **Version 1.0**


