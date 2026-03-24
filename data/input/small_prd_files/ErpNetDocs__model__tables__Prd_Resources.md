---
project: model
repository: ErpNetDocs/model
license: Creative Commons Attribution 4.0 International
source_file: tables/Prd_Resources.md
source_url: https://github.com/ErpNetDocs/model/blob/3e117f4548b5889de0f7bf7bfa887aac1576d37c/tables/Prd_Resources.md
downloaded_at: 2025-12-05T10:50:22.380597+00:00
consensus_grade_level: 17.1
headings_per_sentence: 0.61
lists_per_sentence: 0.02
smao_sentences_pct: 0.0
vague_words_per_sentence: 0.49
anaphora_per_sentence: 0.29
sentence_cv: 1.991
cpre_terms_per_sentence: 1.07
---
# Table Prd_Resources


## Entity

Entity: [Production.Resources.Resources](~/entities/Production.Resources.Resources.md)

Resource types available to production. Entity: Prd_Resources

## Owner Tables Hierarchy

* [Prd_Resource_Groups](Prd_Resource_Groups.md)

## Summary

| Name | Type | Description |
| - | - | --- |
|[Active](#active)|`bit` |Indicates whether the current resource is active.|
|[Id](#id)|`uniqueidentifier` `PK`|Unique resource id|
|[Notes](#notes)|`nvarchar(254)` |User notes for the resource|
|[Primary_Unit_Id](#primary_unit_id)|`uniqueidentifier` |Primary measurement unit for quantities of the resource|
|[Resource_Currency_Id](#resource_currency_id)|`uniqueidentifier` |Currency for this resource. This currency applies for the standard price and cost per hour.|
|[Resource_Group_Id](#resource_group_id)|`uniqueidentifier` |The Id of the containing resource group|
|[Resource_Name](#resource_name)|`nvarchar(64)` |Name of the resource|
|[Row_Version](#row_version)|`timestamp` ||
|[Setup_Duration_Hours](#setup_duration_hours)|`decimal(6, 2)` |The usual duration of setup when changing production|
|[Setup_Scrap_Quantity](#setup_scrap_quantity)|`decimal(18, 3)` |The usual quantity of fixed scrap occurring when changing production. |
|[Setup_Scrap_Unit](#setup_scrap_unit)|`uniqueidentifier` |The measurement units of Setup_Scrap_Quantity|
|[Standard_Cost_Per_Hour](#standard_cost_per_hour)|`decimal(18, 6)` |Standard cost per hour for this resource. It participates in the calculation of standard cost for production recipes in which the current resource is used.|
|[Standard_Price_Per_Hour](#standard_price_per_hour)|`decimal(18, 6)` |Standard price per hour for this resource. It participates in the calculation of standard price for production recipes in which the current resource is used.|

## Columns

### Active


Indicates whether the current resource is active.

| Property | Value |
| - | - |
|Auto Complete|no|
|Data Filter|no|
|Default Value|True|
|Enter Stop|yes|
|Ignore for Insert Order|no|
|Is Entity Name|no|
|Max Length|-1|
|Order|12|
|Ownership Reference|no|
|Pasword|no|
|Picture|no|
|Primary Key|no|
|Readonly|no|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|no|
|Type|bit|
|UI Memo Editor|no|
|UI Width|Medium|
|User Login|no|
|Visible|yes|

#### Active - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|Equals|`True`|no|no|

### Id


Unique resource id

| Property | Value |
| - | - |
|Auto Complete|no|
|Data Filter|no|
|Default Value|NewGuid|
|Enter Stop|no|
|Ignore for Insert Order|no|
|Is Entity Name|no|
|Max Length|-1|
|Order|0|
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
|UI Width|100|
|User Login|no|
|Visible|no|

#### Id - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|Equals|`NULL`|no|no|

### Notes


User notes for the resource

| Property | Value |
| - | - |
|Attributes|IsLongString|
|Auto Complete|no|
|Data Filter|no|
|Default Value|None|
|Enter Stop|no|
|Ignore for Insert Order|no|
|Is Entity Name|no|
|Max Length|254|
|Order|7|
|Ownership Reference|no|
|Pasword|no|
|Picture|no|
|Primary Key|no|
|Readonly|no|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|no|
|Type|nvarchar(254) (Allows NULL)|
|UI Memo Editor|no|
|UI Width|100|
|User Login|no|
|Visible|yes|

### Primary_Unit_Id


Primary measurement unit for quantities of the resource

| Property | Value |
| - | - |
|Auto Complete|no|
|Data Filter|no|
|Default Value|None|
|Enter Stop|yes|
|Ignore for Insert Order|no|
|Is Entity Name|no|
|Max Length|-1|
|Order|3|
|Ownership Reference|no|
|Pasword|no|
|Picture|no|
|Primary Key|no|
|Readonly|no|
|Referenced Table|[Gen_Measurement_Units](Gen_Measurement_Units.md)|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|yes|
|Type|uniqueidentifier|
|UI Memo Editor|no|
|UI Width|Short|
|User Login|no|
|Visible|yes|

#### Primary_Unit_Id - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|Equals|`NULL`|no|no|

### Resource_Currency_Id


Currency for this resource. This currency applies for the standard price and cost per hour.

| Property | Value |
| - | - |
|Auto Complete|no|
|Data Filter|no|
|Default Value|None|
|Enter Stop|yes|
|Ignore for Insert Order|no|
|Is Entity Name|no|
|Max Length|-1|
|Order|9|
|Ownership Reference|no|
|Pasword|no|
|Picture|no|
|Primary Key|no|
|Readonly|no|
|Referenced Table|[Gen_Currencies](Gen_Currencies.md)|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|yes|
|Type|uniqueidentifier (Allows NULL)|
|UI Memo Editor|no|
|UI Width|Medium|
|User Login|no|
|Visible|yes|

#### Resource_Currency_Id - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|Equals|`NULL`|yes|no|

### Resource_Group_Id


The Id of the containing resource group

| Property | Value |
| - | - |
|Auto Complete|no|
|Data Filter|no|
|Default Value|None|
|Enter Stop|yes|
|Ignore for Insert Order|no|
|Is Entity Name|no|
|Max Length|-1|
|Order|1|
|Ownership Reference|yes|
|Pasword|no|
|Picture|no|
|Primary Key|no|
|Readonly|no|
|Referenced Table|[Prd_Resource_Groups](Prd_Resource_Groups.md)|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|yes|
|Type|uniqueidentifier|
|UI Memo Editor|no|
|UI Width|Medium|
|User Login|no|
|Visible|yes|

#### Resource_Group_Id - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|Equals|`NULL`|no|no|

### Resource_Name


Name of the resource

| Property | Value |
| - | - |
|Auto Complete|no|
|Data Filter|no|
|Default Value|None|
|Enter Stop|yes|
|Ignore for Insert Order|no|
|Is Entity Name|no|
|Max Length|64|
|Order|2|
|Ownership Reference|no|
|Pasword|no|
|Picture|no|
|Primary Key|no|
|Readonly|no|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|no|
|Type|nvarchar(64)|
|UI Memo Editor|no|
|UI Width|Long|
|User Login|no|
|Visible|yes|

#### Resource_Name - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|Like|None|no|no|

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
|Order|11|
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

### Setup_Duration_Hours


The usual duration of setup when changing production

| Property | Value |
| - | - |
|Auto Complete|no|
|Data Filter|no|
|Default Value|0|
|Enter Stop|yes|
|Ignore for Insert Order|no|
|Is Entity Name|no|
|Max Length|-1|
|Order|6|
|Ownership Reference|no|
|Pasword|no|
|Picture|no|
|Primary Key|no|
|Readonly|no|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|no|
|Type|decimal(6, 2)|
|UI Memo Editor|no|
|UI Width|Short|
|User Login|no|
|Visible|yes|

### Setup_Scrap_Quantity


The usual quantity of fixed scrap occurring when changing production. 

| Property | Value |
| - | - |
|Auto Complete|no|
|Data Filter|no|
|Default Value|0|
|Enter Stop|yes|
|Ignore for Insert Order|no|
|Is Entity Name|no|
|Max Length|-1|
|Order|4|
|Ownership Reference|no|
|Pasword|no|
|Picture|no|
|Primary Key|no|
|Readonly|no|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|no|
|Type|decimal(18, 3)|
|UI Memo Editor|no|
|UI Width|Short|
|User Login|no|
|Visible|yes|

### Setup_Scrap_Unit


The measurement units of Setup_Scrap_Quantity

| Property | Value |
| - | - |
|Auto Complete|no|
|Data Filter|no|
|Default Value|None|
|Enter Stop|yes|
|Ignore for Insert Order|no|
|Is Entity Name|no|
|Max Length|-1|
|Order|5|
|Ownership Reference|no|
|Pasword|no|
|Picture|no|
|Primary Key|no|
|Readonly|no|
|Referenced Table|[Gen_Measurement_Units](Gen_Measurement_Units.md)|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|yes|
|Type|uniqueidentifier|
|UI Memo Editor|no|
|UI Width|Short|
|User Login|no|
|Visible|yes|

#### Setup_Scrap_Unit - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|Equals|`NULL`|no|no|

### Standard_Cost_Per_Hour


Standard cost per hour for this resource. It participates in the calculation of standard cost for production recipes in which the current resource is used.

| Property | Value |
| - | - |
|Auto Complete|no|
|Data Filter|no|
|Default Value|None|
|Enter Stop|yes|
|Ignore for Insert Order|no|
|Is Entity Name|no|
|Max Length|-1|
|Order|10|
|Ownership Reference|no|
|Pasword|no|
|Picture|no|
|Primary Key|no|
|Readonly|no|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|no|
|Type|decimal(18, 6) (Allows NULL)|
|UI Memo Editor|no|
|UI Width|Medium|
|User Login|no|
|Visible|yes|

### Standard_Price_Per_Hour


Standard price per hour for this resource. It participates in the calculation of standard price for production recipes in which the current resource is used.

| Property | Value |
| - | - |
|Auto Complete|no|
|Data Filter|no|
|Default Value|None|
|Enter Stop|yes|
|Ignore for Insert Order|no|
|Is Entity Name|no|
|Max Length|-1|
|Order|8|
|Ownership Reference|no|
|Pasword|no|
|Picture|no|
|Primary Key|no|
|Readonly|no|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|no|
|Type|decimal(18, 6) (Allows NULL)|
|UI Memo Editor|no|
|UI Width|Medium|
|User Login|no|
|Visible|yes|


