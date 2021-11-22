# V10VmOpenApiGeneralDescriptionIn

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **str** | External system identifier. User needs to be logged in to be able to get/set value. | [optional] 
**requirements** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | Localized service usage requirements (description of requirement). (Max.Length: 2500). | [optional] 
**legislation** | [**list[V4VmOpenApiLaw]**](V4VmOpenApiLaw.md) | Laws that a general description is based on. | [optional] 
**general_description_type_id** | **str** | General description type id. Used internally to check the restrictions for usage.  In older versions: Default general description is Municipality. | [optional] 
**available_languages** | **list[str]** | Gets or sets available languages | [optional] 
**version_id** | **str** | The identifier for current version. | [optional] 
**id** | **str** | Entity Guid identifier. | [optional] 
**life_events** | **list[str]** | List of life event urls. Sample url: http://urn.fi/URN:NBN:fi:au:ptvl:v3017 | [optional] 
**industrial_classes** | **list[str]** | List of industrial class codes (see http://tilastokeskus.fi/meta/luokitukset/toimiala/001-2008/tekstitiedosto_en.txt). | [optional] 
**current_publishing_status** | **str** | Current version publishing status. | [optional] 
**required_properties_available_languages** | **list[str]** | Internal property to check the languages within required lists: Names and Descriptions | [optional] 
**type** | **str** | Service type. Possible values are: Service, PermitOrObligation or ProfessionalQualification. | [optional] 
**service_charge_type** | **str** | Service charge type. Possible values are:  Chargeable or FreeOfCharge. | [optional] 
**names** | [**list[VmOpenApiLocalizedListItem]**](VmOpenApiLocalizedListItem.md) | List of name entities. Possible type values are: Name, AlternativeName.   Sample single JSON object: {\&quot;language\&quot;: \&quot;fi\&quot;, \&quot;value\&quot;: \&quot;Perhepäivähoito esiopetusikäisille\&quot;, \&quot;type\&quot;: \&quot;Name\&quot;}. | 
**descriptions** | [**list[VmOpenApiLocalizedListItem]**](VmOpenApiLocalizedListItem.md) | List of description entities. Requires two entities where ones type is \&quot;Description\&quot; or \&quot;BackgroundDescription\&quot; and the other ones type is \&quot;Summary\&quot;.  Sample single JSON object: {\&quot;language\&quot;: \&quot;fi\&quot;, \&quot;value\&quot;: \&quot;Lyhyen kuvauksen kuvaus esimerkki teksti.\&quot;, \&quot;type\&quot;: \&quot;Summary\&quot;}.  Other optional description types are UserInstruction, ChargeTypeAdditionalInfo, DeadLine, ProcessingTime, ValidityTime, GeneralDescriptionTypeAdditionalInformation. | 
**service_classes** | **list[str]** | List of service class urls. Sample url: http://urn.fi/URN:NBN:fi:au:ptvl:v1065 | 
**ontology_terms** | **list[str]** | List of ontology term urls. Sample url: http://www.yso.fi/onto/koko/p2435 | 
**target_groups** | **list[str]** | List of target group urls. Sample url: http://urn.fi/URN:NBN:fi:au:ptvl:v2004 | 
**general_description_type** | **str** | General description type. Possible values are: Municipality, BusinessSubregion, Church. | 
**publishing_status** | **str** | Publishing status. Possible values are: Draft or Published. | 
**delete_all_industrial_classes** | **bool** | Set to true to delete all existing industrial classes (the IndustrialClasses collection for this object should be empty collection when this option is used). | [optional] 
**delete_all_laws** | **bool** | Set to true to delete all existing laws within legislation (the legislation collection for this object should be empty collection when this option is used). | [optional] 
**delete_all_life_events** | **bool** | Set to true to delete all existing life events (the LifeEvents collection for this object should be empty collection when this option is used). | [optional] 
**delete_service_charge_type** | **bool** | Set to true to delete service charge type (ServiceChargeType property for this object should be empty when this option is used). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

