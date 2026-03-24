---
project: model
repository: ErpNetDocs/model
license: Creative Commons Attribution 4.0 International
source_file: tables/Prd_Load.md
source_url: https://github.com/ErpNetDocs/model/blob/3e117f4548b5889de0f7bf7bfa887aac1576d37c/tables/Prd_Load.md
downloaded_at: 2025-12-05T10:50:09.120998+00:00
consensus_grade_level: 16.2
headings_per_sentence: 0.63
lists_per_sentence: 0.11
smao_sentences_pct: 0.0
vague_words_per_sentence: 0.5
anaphora_per_sentence: 0.05
sentence_cv: 2.158
cpre_terms_per_sentence: 0.87
---
# Table Prd_Load


## Entity

Entity: [Production.Resources.Load](~/entities/Production.Resources.Load.md)

Contains scheduled operations usage of the resources. Entity: Prd_Load

## Owner Tables Hierarchy

* [Prd_Work_Order_Item_Operations](Prd_Work_Order_Item_Operations.md)
* [Prd_Work_Order_Items](Prd_Work_Order_Items.md)
* [Prd_Work_Orders](Prd_Work_Orders.md)
* [Gen_Documents](Gen_Documents.md)

## Summary

| Name | Type | Description |
| - | - | --- |
|[Calendar_Date](#calendar_date)|`datetime` |Date of the scheduled load. This is date only. Start_Time and End_Time specify time of day|
|[Id](#id)|`uniqueidentifier` `PK`||
|[Priority](#priority)|`smallint` Allowed: `1`, `2`, `3`, `4`, `5`|Priority of the allocation. 1=Lowest ... 5=Highest|
|[Row_Version](#row_version)|`timestamp` ||
|[Time_Type](#time_type)|`char(1)` Allowed: `M`, `R`, `S`, `W`|S=Setup; R=Run; W=Wait; M=Move|
|[Usage_End_Time](#usage_end_time)|`datetime` |The ending time of the planned usage.|
|[Usage_Quantity](#usage_quantity)|`decimal(9, 0)` |Quantity of the resource, which will be used for production|
|[Usage_Start_Time](#usage_start_time)|`datetime` |The starting time of the planned usage.|
|[Usage_Time_Minutes](#usage_time_minutes)|`int` |Time allocated for the operation in minutes|
|[Work_Order_Item_Operation_Id](#work_order_item_operation_id)|`uniqueidentifier` ||
|[Workgroup_Resource_Id](#workgroup_resource_id)|`uniqueidentifier` |The exact resource being utilised|

## Columns

### Calendar_Date


Date of the scheduled load. This is date only. Start_Time and End_Time specify time of day

| Property | Value |
| - | - |
|Auto Complete|no|
|Data Filter|no|
|Default Value|None|
|Enter Stop|yes|
|Ignore for Insert Order|no|
|Is Entity Name|no|
|Max Length|-1|
|Order|2147483647|
|Ownership Reference|no|
|Pasword|no|
|Picture|no|
|Primary Key|no|
|Readonly|no|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|no|
|Type|datetime|
|UI Memo Editor|no|
|UI Width|Medium|
|User Login|no|
|Visible|yes|

#### Calendar_Date - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|GreaterThanOrLessThan|None|no|no|

### Id

| Property | Value |
| - | - |
|Auto Complete|no|
|Data Filter|no|
|Default Value|NewGuid|
|Enter Stop|yes|
|Ignore for Insert Order|no|
|Is Entity Name|no|
|Max Length|-1|
|Order|2147483647|
|Ownership Reference|no|
|Pasword|no|
|Picture|no|
|Primary Key|yes (order: 1)|
|Readonly|no|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|yes|
|Type|uniqueidentifier|
|UI Memo Editor|no|
|UI Width|Medium|
|User Login|no|
|Visible|no|

#### Id - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|Equals|`NULL`|no|no|

### Priority


Priority of the allocation. 1=Lowest ... 5=Highest

| Property | Value |
| - | - |
|Allowed Values|`1`, `2`, `3`, `4`, `5`|
|Auto Complete|no|
|Data Filter|no|
|Default Value|3|
|Enter Stop|yes|
|Ignore for Insert Order|no|
|Is Entity Name|no|
|Max Length|-1|
|Order|2147483647|
|Ownership Reference|no|
|Pasword|no|
|Picture|no|
|Primary Key|no|
|Readonly|no|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|no|
|Type|smallint|
|UI Memo Editor|no|
|UI Width|Short|
|User Login|no|
|Visible|yes|

### Row_Version

| Property | Value |
| - | - |
|Auto Complete|no|
|Data Filter|no|
|Default Value|None|
|Enter Stop|yes|
|Ignore for Insert Order|no|
|Is Entity Name|no|
|Max Length|-1|
|Order|2147483647|
|Ownership Reference|no|
|Pasword|no|
|Picture|no|
|Primary Key|no|
|Readonly|no|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|no|
|Type|timestamp|
|UI Memo Editor|no|
|UI Width|Medium|
|User Login|no|
|Visible|no|

### Time_Type


S=Setup; R=Run; W=Wait; M=Move

| Property | Value |
| - | - |
|Allowed Values|`M`, `R`, `S`, `W`|
|Auto Complete|no|
|Data Filter|no|
|Default Value|R|
|Enter Stop|yes|
|Ignore for Insert Order|no|
|Is Entity Name|no|
|Max Length|1|
|Order|2147483647|
|Ownership Reference|no|
|Pasword|no|
|Picture|no|
|Primary Key|no|
|Readonly|no|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|no|
|Type|char(1)|
|UI Memo Editor|no|
|UI Width|Medium|
|User Login|no|
|Visible|yes|

### Usage_End_Time


The ending time of the planned usage.

| Property | Value |
| - | - |
|Auto Complete|no|
|Data Filter|no|
|Default Value|None|
|Enter Stop|yes|
|Ignore for Insert Order|no|
|Is Entity Name|no|
|Max Length|-1|
|Order|2147483647|
|Ownership Reference|no|
|Pasword|no|
|Picture|no|
|Primary Key|no|
|Readonly|no|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|no|
|Type|datetime|
|UI Memo Editor|no|
|UI Width|Medium|
|User Login|no|
|Visible|yes|

#### Usage_End_Time - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|GreaterThanOrLessThan|None|no|no|

### Usage_Quantity


Quantity of the resource, which will be used for production

| Property | Value |
| - | - |
|Auto Complete|no|
|Data Filter|no|
|Default Value|1|
|Enter Stop|yes|
|Ignore for Insert Order|no|
|Is Entity Name|no|
|Max Length|-1|
|Order|2147483647|
|Ownership Reference|no|
|Pasword|no|
|Picture|no|
|Primary Key|no|
|Readonly|no|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|no|
|Type|decimal(9, 0)|
|UI Memo Editor|no|
|UI Width|Short|
|User Login|no|
|Visible|yes|

#### Usage_Quantity - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|GreaterThanOrLessThan|None|no|no|

### Usage_Start_Time


The starting time of the planned usage.

| Property | Value |
| - | - |
|Auto Complete|no|
|Data Filter|no|
|Default Value|None|
|Enter Stop|yes|
|Ignore for Insert Order|no|
|Is Entity Name|no|
|Max Length|-1|
|Order|2147483647|
|Ownership Reference|no|
|Pasword|no|
|Picture|no|
|Primary Key|no|
|Readonly|no|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|no|
|Type|datetime|
|UI Memo Editor|no|
|UI Width|Medium|
|User Login|no|
|Visible|yes|

#### Usage_Start_Time - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|GreaterThanOrLessThan|None|no|no|

### Usage_Time_Minutes


Time allocated for the operation in minutes

| Property | Value |
| - | - |
|Auto Complete|no|
|Data Filter|no|
|Default Value|0|
|Enter Stop|yes|
|Ignore for Insert Order|no|
|Is Entity Name|no|
|Max Length|-1|
|Order|2147483647|
|Ownership Reference|no|
|Pasword|no|
|Picture|no|
|Primary Key|no|
|Readonly|no|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|no|
|Type|int|
|UI Memo Editor|no|
|UI Width|Short|
|User Login|no|
|Visible|yes|

#### Usage_Time_Minutes - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|GreaterThanOrLessThan|None|no|no|

### Work_Order_Item_Operation_Id

| Property | Value |
| - | - |
|Auto Complete|no|
|Data Filter|no|
|Default Value|None|
|Enter Stop|yes|
|Ignore for Insert Order|no|
|Is Entity Name|no|
|Max Length|-1|
|Order|2147483647|
|Ownership Reference|yes|
|Pasword|no|
|Picture|no|
|Primary Key|no|
|Readonly|no|
|Referenced Table|[Prd_Work_Order_Item_Operations](Prd_Work_Order_Item_Operations.md)|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|yes|
|Type|uniqueidentifier|
|UI Memo Editor|no|
|UI Width|Long|
|User Login|no|
|Visible|yes|

#### Work_Order_Item_Operation_Id - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|Equals|`NULL`|no|no|

### Workgroup_Resource_Id


The exact resource being utilised

| Property | Value |
| - | - |
|Auto Complete|no|
|Data Filter|no|
|Default Value|None|
|Enter Stop|yes|
|Ignore for Insert Order|no|
|Is Entity Name|no|
|Max Length|-1|
|Order|2147483647|
|Ownership Reference|no|
|Pasword|no|
|Picture|no|
|Primary Key|no|
|Readonly|no|
|Referenced Table|[Prd_Workgroup_Resources](Prd_Workgroup_Resources.md)|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|yes|
|Type|uniqueidentifier|
|UI Memo Editor|no|
|UI Width|Long|
|User Login|no|
|Visible|yes|

#### Workgroup_Resource_Id - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|Equals|`NULL`|no|no|


