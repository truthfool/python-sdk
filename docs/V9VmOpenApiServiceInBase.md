# V9VmOpenApiServiceInBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **str** | External system identifier for the entity. User needs to be logged in to be able to get/set value. | [optional] 
**funding_type** | **str** | Service funding type. Possible values are: PubliclyFunded or MarketFunded. | [optional] 
**languages** | **list[str]** | List of service languages. | [optional] 
**legislation** | [**list[V4VmOpenApiLaw]**](V4VmOpenApiLaw.md) | List of laws related to the service. | [optional] 
**keywords** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | List of localized service keywords. (Max.Length: 150). | [optional] 
**requirements** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | Localized service usage requirements (description of requirement). (Max.Length: 2500). | [optional] 
**service_vouchers_in_use** | **bool** | Indicates if service vouchers are used in the service. | [optional] 
**service_vouchers** | [**list[V9VmOpenApiServiceVoucher]**](V9VmOpenApiServiceVoucher.md) | List of service vouchers. | [optional] 
**version_id** | **str** | The identifier for current version. | [optional] 
**id** | **str** | PTV service identifier. | [optional] 
**general_description_id** | **str** | Valid PTV statutory service general description identifier that this service will be linked to. List of valid identifiers can be retrieved from the endpoint /api/GeneralDescription | [optional] 
**life_events** | **list[str]** | List of life event urls. Sample url: http://urn.fi/URN:NBN:fi:au:ptvl:v3017  NOTE! If life event has been defined within attached statutory service general description, the life event is not added for service. | [optional] 
**industrial_classes** | **list[str]** | List of industrial class codes (see http://tilastokeskus.fi/meta/luokitukset/toimiala/001-2008/tekstitiedosto_en.txt).  NOTE! If industrial class has been defined within attached statutory service general description, the industrial class is not added for service. | [optional] 
**other_responsible_organizations** | **list[str]** | List of other responsible organizations for the service. | [optional] 
**publishing_status** | **str** | Publishing status. Possible values are: Draft, Published, Deleted or Modified. | 
**delete_all_life_events** | **bool** | Set to true to delete all existing life events (the LifeEvents collection for this object should be empty collection when this option is used). | [optional] 
**delete_all_industrial_classes** | **bool** | Set to true to delete all existing industrial classes (the IndustrialClasses collection for this object should be empty collection when this option is used). | [optional] 
**delete_all_laws** | **bool** | Set to true to delete all existing laws within legislation (the legislation collection for this object should be empty collection when this option is used). | [optional] 
**delete_all_keywords** | **bool** | Set to true to delete all existing keywords (the Keywords collection for this object should be empty collection when this option is used). | [optional] 
**delete_service_charge_type** | **bool** | Set to true to delete service charge type (ServiceChargeType property for this object should be empty when this option is used). | [optional] 
**delete_general_description_id** | **bool** | Set to true to delete statutory service general description (GeneralDescriptionId property for this object should be empty when this option is used). | [optional] 
**main_responsible_organization** | **str** | Main responsible organization Id | [optional] 
**valid_from** | **datetime** | Date when item should be published. | [optional] 
**valid_to** | **datetime** | Date when item should be archived. | [optional] 
**current_publishing_status** | **str** | Current version publishing status. | [optional] 
**service_service_channels** | [**list[V11VmOpenApiServiceServiceChannelAstiInBase]**](V11VmOpenApiServiceServiceChannelAstiInBase.md) | Internal property for adding service channel connections for a service.  This property is also used when attaching general description propsed channels into service (PTV-2315). | [optional] 
**user_name** | **str** | User name. | [optional] 
**available_languages** | **list[str]** | Gets or sets available languages | [optional] 
**required_properties_available_languages** | **list[str]** | Internal property to check the languages within required lists: ServiceNames and ServiceDescriptions | [optional] 
**type** | **str** | Service type. Possible values are: Service, PermitOrObligation or ProfessionalQualification.  NOTE! If service type has been defined within attached statutory service general description, the type for service is ignored. | [optional] 
**service_names** | [**list[VmOpenApiLocalizedListItem]**](VmOpenApiLocalizedListItem.md) | List of localized service names. Possible type values are: Name, AlternativeName. | [optional] 
**service_charge_type** | **str** | Service charge type. Possible values are: Chargeable or FreeOfCharge.  NOTE! If service charge type has been defined within attached statutory service general description, the charge type for service is ignored. | [optional] 
**area_type** | **str** | Area type (Nationwide, NationwideExceptAlandIslands, LimitedType). | [optional] 
**areas** | [**list[VmOpenApiAreaIn]**](VmOpenApiAreaIn.md) | List of areas. List can contain different types of areas. | [optional] 
**service_descriptions** | [**list[VmOpenApiLocalizedListItem]**](VmOpenApiLocalizedListItem.md) | List of localized service descriptions. Possible type values are: Description, Summary, UserInstruction, ValidityTime, ProcessingTime, DeadLine, ChargeTypeAdditionalInfo, ServiceType. (Max.Length: 2500 Description). (Max.Length: 2500 UserInstruction). (Max.Length: 150 Summary). (Max.Length: 500 ProcessingTime). (Max.Length: 500 DeadLine). (Max.Length: 500 ChargeTypeAdditionalInfo). (Max.Length: 500 ValidityTime). (Max.Length: 500 ServiceType). | [optional] 
**service_classes** | **list[str]** | List of service class urls (see http://finto.fi/ptvl/fi/).  NOTE! If service class has been defined within attached statutory service general description, the service class is not added for service. | [optional] 
**ontology_terms** | **list[str]** | List of ontology term urls (see http://finto.fi/koko/fi/).  NOTE! If ontology term has been defined within attached statutory service general description, the ontology term is not added for service. | [optional] 
**target_groups** | **list[str]** | List of target group urls (see http://finto.fi/ptvl/fi/page/?uri&#x3D;http://urn.fi/URN:NBN:fi:au:ptvl:KR).  NOTE! If target group has been defined within attached statutory service general description, the target group is not added for service. | [optional] 
**service_producers** | [**list[V9VmOpenApiServiceProducerIn]**](V9VmOpenApiServiceProducerIn.md) | List of service producers | [optional] 
**delete_all_municipalities** | **bool** | Set to true to delete all existing municipalities (the Municipalities collection for this object should be empty collection when this option is used). | [optional] 
**delete_all_service_vouchers** | **bool** | Set to true to delete all existing service vouchers (the ServiceVouchers collection for this object should be empty collection when this option is used). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

