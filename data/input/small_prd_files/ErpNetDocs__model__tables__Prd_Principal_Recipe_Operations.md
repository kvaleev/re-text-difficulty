---
project: model
repository: ErpNetDocs/model
license: Creative Commons Attribution 4.0 International
source_file: tables/Prd_Principal_Recipe_Operations.md
source_url: https://github.com/ErpNetDocs/model/blob/3e117f4548b5889de0f7bf7bfa887aac1576d37c/tables/Prd_Principal_Recipe_Operations.md
downloaded_at: 2025-12-05T10:33:41.823897+00:00
consensus_grade_level: 21.0
headings_per_sentence: 0.79
lists_per_sentence: 0.04
smao_sentences_pct: 0.0
vague_words_per_sentence: 0.77
anaphora_per_sentence: 0.33
sentence_cv: 2.11
cpre_terms_per_sentence: 1.17
---
# Table Prd_Principal_Recipe_Operations


## Entity

Entity: [Production.Technologies.PrincipalRecipeOperations](~/entities/Production.Technologies.PrincipalRecipeOperations.md)

Contains the operations within a principal recipe. Entity: Prd_Principal_Recipe_Operations

## Owner Tables Hierarchy

* [Prd_Principal_Recipes](Prd_Principal_Recipes.md)
* [Gen_Product_Groups](Gen_Product_Groups.md)

## Summary

| Name | Type | Description |
| - | - | --- |
|[Conditional_Property_Description](#conditional_property_description)|`nvarchar(254)` `ML`|The desired description of the Conditional Property. |
|[Conditional_Property_Id](#conditional_property_id)|`uniqueidentifier` |When not NULL, specifies that, when creating recipe, the operation will be added only if this property is set for the main product|
|[Conditional_Property_Value](#conditional_property_value)|`nvarchar(254)` |The desired value of the Conditional Property. |
|[Id](#id)|`uniqueidentifier` `PK`||
|[Line_Ord](#line_ord)|`int` |Consecutive line number within the principal recipe.|
|[Minimum_Concurrent_Start_Time_Minutes](#minimum_concurrent_start_time_minutes)|`int` |How many minutes after the start of the previous operation can this operation start. NULL means that this operation should wait the previous operation to finish before starting|
|[Move_Time_Minutes](#move_time_minutes)|`int` |Time to move the lot to the next operation in minutes|
|[Notes](#notes)|`nvarchar(254)` ||
|[Operation_Description](#operation_description)|`nvarchar(max)` |The description of the operation. Initially copied from the generic operation definition.|
|[Operation_Id](#operation_id)|`uniqueidentifier` |The generic operation definition. The data is copied locally and can be modified for this specific record.|
|[Operation_Instruction_Id](#operation_instruction_id)|`uniqueidentifier` |Link to additional data, containing instructions in external format|
|[Principal_Recipe_Id](#principal_recipe_id)|`uniqueidentifier` ||
|[Row_Version](#row_version)|`timestamp` ||
|[Run_Time_Minutes](#run_time_minutes)|`int` |Duration of the operation for one piece in the standard measurement unit of the product|
|[Scrap_Rate](#scrap_rate)|`decimal(7, 6)` |Standard rate of scrap during the operation|
|[Setup_Time_Minutes](#setup_time_minutes)|`int` |Time needed to setup the equipment|
|[Tooling](#tooling)|`nvarchar(254)` |The tools needed for the routing step|
|[Use_Quantity](#use_quantity)|`decimal(9, 3)` |Quantity of the workgroup resource that should be allocated for the operation|
|[Use_Quantity_Unit_Id](#use_quantity_unit_id)|`uniqueidentifier` |The measurement unit of Use_Quantity|
|[Wait_Time_Minutes](#wait_time_minutes)|`int` |Wait time (drying, cooling, etc.) after the operation in minutes|
|[Workgroup_Resource_Id](#workgroup_resource_id)|`uniqueidentifier` |Required workgroup resource for the operation. NULL means that no resource is required or the resource will be specified later|

## Columns

### Conditional_Property_Description


The desired description of the Conditional Property. 

| Property | Value |
| - | - |
|Auto Complete|no|
|Data Filter|no|
|Default Value|None|
|Enter Stop|no|
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
|Type|nvarchar(254) (MultiLanguage) (Allows NULL)|
|UI Memo Editor|no|
|UI Width|100|
|User Login|no|
|Visible|yes|

### Conditional_Property_Id


When not NULL, specifies that, when creating recipe, the operation will be added only if this property is set for the main product

| Property | Value |
| - | - |
|Auto Complete|no|
|Data Filter|no|
|Default Value|None|
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
|Referenced Table|[Gen_Properties](Gen_Properties.md)|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|yes|
|Type|uniqueidentifier (Allows NULL)|
|UI Memo Editor|no|
|UI Width|100|
|User Login|no|
|Visible|yes|

#### Conditional_Property_Id - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|Equals|`NULL`|yes|no|

### Conditional_Property_Value


The desired value of the Conditional Property. 

| Property | Value |
| - | - |
|Auto Complete|no|
|Data Filter|no|
|Default Value|None|
|Enter Stop|no|
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
|Type|nvarchar(254) (Allows NULL)|
|UI Memo Editor|no|
|UI Width|100|
|User Login|no|
|Visible|yes|

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

### Line_Ord


Consecutive line number within the principal recipe.

| Property | Value |
| - | - |
|Auto Complete|no|
|Autoincrement|1|
|Data Filter|no|
|Default Value|None|
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
|Type|int|
|UI Memo Editor|no|
|UI Width|Short|
|User Login|no|
|Visible|yes|

### Minimum_Concurrent_Start_Time_Minutes


How many minutes after the start of the previous operation can this operation start. NULL means that this operation should wait the previous operation to finish before starting

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
|Type|int (Allows NULL)|
|UI Memo Editor|no|
|UI Width|100|
|User Login|no|
|Visible|yes|

### Move_Time_Minutes


Time to move the lot to the next operation in minutes

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

#### Move_Time_Minutes - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|GreaterThanOrLessThan|None|yes|no|

### Notes

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
|Type|nvarchar(254) (Allows NULL)|
|UI Memo Editor|no|
|UI Width|Short|
|User Login|no|
|Visible|yes|

### Operation_Description


The description of the operation. Initially copied from the generic operation definition.

| Property | Value |
| - | - |
|Attributes|IsLongString|
|Auto Complete|no|
|Data Filter|no|
|Default Value|None|
|Enter Stop|no|
|Ignore for Insert Order|no|
|Is Entity Name|no|
|Max Length|2147483647|
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
|Type|nvarchar(max) (Allows NULL)|
|UI Memo Editor|no|
|UI Width|Medium|
|User Login|no|
|Visible|yes|

### Operation_Id


The generic operation definition. The data is copied locally and can be modified for this specific record.

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
|Referenced Table|[Prd_Operations](Prd_Operations.md)|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|yes|
|Type|uniqueidentifier (Allows NULL)|
|UI Memo Editor|no|
|UI Width|Medium|
|User Login|no|
|Visible|yes|

#### Operation_Id - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|Equals|`NULL`|yes|no|

### Operation_Instruction_Id


Link to additional data, containing instructions in external format

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
|Referenced Table|[Prd_Operation_Instructions](Prd_Operation_Instructions.md)|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|yes|
|Type|uniqueidentifier (Allows NULL)|
|UI Memo Editor|no|
|UI Width|Medium|
|User Login|no|
|Visible|no|

#### Operation_Instruction_Id - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|Equals|`NULL`|yes|no|

### Principal_Recipe_Id

| Property | Value |
| - | - |
|Auto Complete|no|
|Data Filter|no|
|Default Value|None|
|Enter Stop|no|
|Ignore for Insert Order|no|
|Is Entity Name|no|
|Max Length|-1|
|Order|2147483647|
|Ownership Reference|yes|
|Pasword|no|
|Picture|no|
|Primary Key|no|
|Readonly|no|
|Referenced Table|[Prd_Principal_Recipes](Prd_Principal_Recipes.md)|
|RTF|no|
|Sortable|no|
|Summary Type|None|
|Supports EQUALS_IN|yes|
|Type|uniqueidentifier|
|UI Memo Editor|no|
|UI Width|Long|
|User Login|no|
|Visible|yes|

#### Principal_Recipe_Id - Supported Filters

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

### Run_Time_Minutes


Duration of the operation for one piece in the standard measurement unit of the product

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

#### Run_Time_Minutes - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|GreaterThanOrLessThan|None|yes|no|

### Scrap_Rate


Standard rate of scrap during the operation

| Property | Value |
| - | - |
|Attributes|IsPercent|
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
|Type|decimal(7, 6)|
|UI Memo Editor|no|
|UI Width|Short|
|User Login|no|
|Visible|yes|

### Setup_Time_Minutes


Time needed to setup the equipment

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

#### Setup_Time_Minutes - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|GreaterThanOrLessThan|None|yes|no|

### Tooling


The tools needed for the routing step

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
|Type|nvarchar(254) (Allows NULL)|
|UI Memo Editor|no|
|UI Width|Short|
|User Login|no|
|Visible|yes|

### Use_Quantity


Quantity of the workgroup resource that should be allocated for the operation

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
|Type|decimal(9, 3)|
|UI Memo Editor|no|
|UI Width|Short|
|User Login|no|
|Visible|yes|

#### Use_Quantity - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|GreaterThanOrLessThan|None|yes|no|

### Use_Quantity_Unit_Id


The measurement unit of Use_Quantity

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

#### Use_Quantity_Unit_Id - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|Equals|`NULL`|no|no|

### Wait_Time_Minutes


Wait time (drying, cooling, etc.) after the operation in minutes

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

#### Wait_Time_Minutes - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|GreaterThanOrLessThan|None|yes|no|

### Workgroup_Resource_Id


Required workgroup resource for the operation. NULL means that no resource is required or the resource will be specified later

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
|UI Width|Medium|
|User Login|no|
|Visible|yes|

#### Workgroup_Resource_Id - Supported Filters

| Filter Type | Default | Include Nulls | Hidden by Default |
| - | - | - | - |
|Equals|`NULL`|no|no|


