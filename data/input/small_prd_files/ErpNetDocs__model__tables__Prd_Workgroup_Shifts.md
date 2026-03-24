---
project: model
repository: ErpNetDocs/model
license: Creative Commons Attribution 4.0 International
source_file: tables/Prd_Workgroup_Shifts.md
source_url: https://github.com/ErpNetDocs/model/blob/3e117f4548b5889de0f7bf7bfa887aac1576d37c/tables/Prd_Workgroup_Shifts.md
downloaded_at: 2025-12-05T10:33:06.554178+00:00
consensus_grade_level: 15.5
headings_per_sentence: 0.59
lists_per_sentence: 0.03
smao_sentences_pct: 0.0
vague_words_per_sentence: 0.41
anaphora_per_sentence: 0.07
sentence_cv: 2.093
cpre_terms_per_sentence: 0.76
---
# Table Prd_Workgroup_Shifts


## Entity

Entity: [Production.Resources.WorkgroupShifts](~/entities/Production.Resources.WorkgroupShifts.md)

Contains the working shifts of the wrokgroups. Entity: Prd_Workgroup_Shifts

## Owner Tables Hierarchy

* [Prd_Workgroups](Prd_Workgroups.md)

## Summary

| Name | Type | Description |
| - | - | --- |
|[Efficiency_Factor_Percent](#efficiency_factor_percent)|`decimal(3, 2)` |Efficiency factor of the routing steps for this shift, expressed as percentage|
|[Establishment_Date](#establishment_date)|`datetime` |When the workgroup shift was established. Used as minimum date when generating calendar|
|[Id](#id)|`uniqueidentifier` `PK`|Unique workgroup shift Id|
|[Row_Version](#row_version)|`timestamp` ||
|[Shift_Name](#shift_name)|`nvarchar(254)` |The name of the workgroup shift.|
|[Work_Schedule_Id](#work_schedule_id)|`uniqueidentifier` |The work schedule used to calculate the working time for the shift.|
|[Workgroup_Id](#workgroup_id)|`uniqueidentifier` ||

## Columns

### Efficiency_Factor_Percent


Efficiency factor of the routing steps for this shift, expressed as percentage

| Property | Value |
| - | - |
|Attributes|IsPercent|
|Auto Complete|no|
|Data Filter|no|
|Default Value|1|
|Enter Stop|no|
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
|Type|decimal(3, 2)|
|UI Memo Editor|no|
|UI Width|Short|
|User Login|no|
|Visible|yes|

### Establishment_Date


When the workgroup shift was established. Used as minimum date when generating calendar

| Property | Value |
| - | - |
|Auto Complete|no|
|Data Filter|no|
|Default Value|CurrentDate|
|Enter Stop|no|
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

#### Establishment_Date - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|GreaterThanOrLessThan|None|no|no|

### Id


Unique workgroup shift Id

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

### Shift_Name


The name of the workgroup shift.

| Property | Value |
| - | - |
|Auto Complete|no|
|Data Filter|no|
|Default Value|None|
|Enter Stop|yes|
|Ignore for Insert Order|no|
|Is Entity Name|no|
|Max Length|254|
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
|Type|nvarchar(254)|
|UI Memo Editor|no|
|UI Width|Long|
|User Login|no|
|Visible|yes|

#### Shift_Name - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|Like|None|no|no|

### Work_Schedule_Id


The work schedule used to calculate the working time for the shift.

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
|Referenced Table|[Gen_Work_Schedules](Gen_Work_Schedules.md)|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|yes|
|Type|uniqueidentifier|
|UI Memo Editor|no|
|UI Width|Medium|
|User Login|no|
|Visible|yes|

#### Work_Schedule_Id - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|Equals|`NULL`|no|no|

### Workgroup_Id

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
|Referenced Table|[Prd_Workgroups](Prd_Workgroups.md)|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|yes|
|Type|uniqueidentifier|
|UI Memo Editor|no|
|UI Width|Medium|
|User Login|no|
|Visible|yes|

#### Workgroup_Id - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|Equals|`NULL`|no|no|


