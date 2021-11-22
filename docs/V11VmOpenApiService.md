# V11VmOpenApiService

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity identifier. | [optional] 
**source_id** | **str** | External system identifier for the entity. User needs to be logged in to be able to get/set value. | [optional] 
**type** | **str** | Service type. Possible values are: Service, PermitOrObligation or ProfessionalQualification. In version 7 Service, PermissionAndObligation or ProfessionalQualifications. | [optional] 
**funding_type** | **str** | Service funding type. Possible values are: PubliclyFunded or MarketFunded. | [optional] 
**service_names** | [**list[VmOpenApiLocalizedListItem]**](VmOpenApiLocalizedListItem.md) | List of localized service names. Possible type values are: Name, AlternativeName (in version 7 AlternateName). (Max.Length: 100). | [optional] 
**service_charge_type** | **str** | Service charge type. Possible values are: Chargeable or FreeOfCharge.  In version 7: Charged or Free.  NOTE! If service charge type has been defined within attached statutory service general description, the charge type for service is ignored. | [optional] 
**area_type** | **str** | Area type. Possible values are: Nationwide, NationwideExceptAlandIslands or LimitedType.  In version 7: WholeCountry, WholeCountryExceptAlandIslands, AreaType. | [optional] 
**service_descriptions** | [**list[VmOpenApiLocalizedListItem]**](VmOpenApiLocalizedListItem.md) | List of localized service descriptions. Possible type values are: Description, Summary, UserInstruction, ValidityTime, ProcessingTime, DeadLine, ChargeTypeAdditionalInfo, ServiceType.  In version 7: Description, ShortDescription, ServiceUserInstruction, ValidityTimeAdditionalInfo, ProcessingTimeAdditionalInfo, DeadLineAdditionalInfo, ChargeTypeAdditionalInfo, ServiceTypeAdditionalInfo. | [optional] 
**languages** | **list[str]** | List of service languages. | [optional] 
**legislation** | [**list[V4VmOpenApiLaw]**](V4VmOpenApiLaw.md) | List of laws related to the service. | [optional] 
**keywords** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | List of localized service keywords. (Max.Length: 150). | [optional] 
**requirements** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | Localized service usage requirements (description of requirement). (Max.Length: 2500). | [optional] 
**service_vouchers_in_use** | **bool** | Indicates if service vouchers are used in the service. | [optional] 
**service_vouchers** | [**list[V9VmOpenApiServiceVoucher]**](V9VmOpenApiServiceVoucher.md) | List of service vouchers. | [optional] 
**version_id** | **str** | The identifier for current version. | [optional] 
**general_description_id** | **str** | PTV identifier for linked general description. | [optional] 
**sub_type** | **str** | Service sub-type. It is used for SOTE and its taken from GeneralDescription&#x27;s generalDescriptionType. Possible values are: PrescribedByFreedomOfChoiceAct, OtherPermissionGrantedSote. | [optional] 
**areas** | [**list[VmOpenApiArea]**](VmOpenApiArea.md) | List of service areas. | [optional] 
**service_classes** | [**list[V7VmOpenApiFintoItemWithDescription]**](V7VmOpenApiFintoItemWithDescription.md) | List of service classes related to the service. | [optional] 
**ontology_terms** | [**list[V4VmOpenApiOntologyTerm]**](V4VmOpenApiOntologyTerm.md) | List of ontology terms related to the service. | [optional] 
**target_groups** | [**list[V4VmOpenApiFintoItem]**](V4VmOpenApiFintoItem.md) | List of target groups related to the service. | [optional] 
**life_events** | [**list[V4VmOpenApiFintoItem]**](V4VmOpenApiFintoItem.md) | List of life events  related to the service. | [optional] 
**industrial_classes** | [**list[V4VmOpenApiFintoItem]**](V4VmOpenApiFintoItem.md) | List of industrial classes related to the service. | [optional] 
**service_channels** | [**list[V11VmOpenApiServiceServiceChannel]**](V11VmOpenApiServiceServiceChannel.md) | List of linked service channels including relationship data. | [optional] 
**organizations** | [**list[V6VmOpenApiServiceOrganization]**](V6VmOpenApiServiceOrganization.md) | List of organizations, responsible and producer organizations of the service. | [optional] 
**service_collections** | [**list[VmOpenApiServiceServiceCollection]**](VmOpenApiServiceServiceCollection.md) | List of service collections that the service has been linked to | [optional] 
**publishing_status** | **str** | Publishing status. Possible values are: Draft, Published, Deleted or Modified. | [optional] 
**modified** | **datetime** | Date when item was modified/created (UTC). | [optional] 
**responsible_sote_organization** | **str** | Sote organization that is responsible for the service. Notice! At the moment always empty - the property is a placeholder for later use. | [optional] 
**main_organization** | [**VmOpenApiItem**](VmOpenApiItem.md) |  | [optional] 
**service_producers** | [**list[VmOpenApiServiceProducer]**](VmOpenApiServiceProducer.md) | List of service producers | [optional] 
**security** | [**ISecurityOwnOrganization**](ISecurityOwnOrganization.md) |  | [optional] 
**municipalities** | [**list[VmOpenApiMunicipality]**](VmOpenApiMunicipality.md) | List of municipality codes and names that the service is available for. Used in conjunction with service coverage type Local. | [optional] 
**available_languages** | **list[str]** | Gets or sets available languages | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

