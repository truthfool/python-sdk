# V10VmOpenApiOrganization

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity identifier. | [optional] 
**oid** | **str** | Organization OID. - must match the regex @\&quot;^[A-Za-z0-9.-]*$\&quot; | [optional] 
**source_id** | **str** | Organization external system identifier. User needs to be logged in to be able to get/set value. | [optional] 
**organization_type** | **str** | Organization type (State, Municipality, RegionalOrganization, Organization, Company, SotePublic, SotePrivate, Region). | [optional] 
**business_code** | **str** | Organization business code (Y-tunnus). | [optional] 
**business_name** | **str** | Organization business name (name used for business code). This property is not used in the API anymore. Do not use. | [optional] 
**organization_names** | [**list[VmOpenApiLocalizedListItem]**](VmOpenApiLocalizedListItem.md) | List of organization names. Possible type values are: Name, AlternativeName (in version 7 AlternateName). | [optional] 
**display_name_type** | [**list[VmOpenApiNameTypeByLanguage]**](VmOpenApiNameTypeByLanguage.md) | List of Display name types (Name or AlternativeName) for each language version of OrganizationNames. | [optional] 
**area_type** | **str** | Area type (Nationwide, NationwideExceptAlandIslands, LimitedType). | [optional] 
**organization_descriptions** | [**list[VmOpenApiLocalizedListItem]**](VmOpenApiLocalizedListItem.md) | Localized list of organization descriptions. Possible type values are: Description, Summary (in version 7 ShortDescription). (Max.Length: 2500 Description). (Max.Length: 150 ShortDescription). | [optional] 
**emails** | [**list[V4VmOpenApiEmail]**](V4VmOpenApiEmail.md) | List of email addresses. | [optional] 
**phone_numbers** | [**list[V4VmOpenApiPhone]**](V4VmOpenApiPhone.md) | List of organizations phone numbers. | [optional] 
**web_pages** | [**list[V9VmOpenApiWebPage]**](V9VmOpenApiWebPage.md) | List of organizations web pages. | [optional] 
**electronic_invoicings** | [**list[VmOpenApiOrganizationEInvoicing]**](VmOpenApiOrganizationEInvoicing.md) | List of organizations electronic invoicing information. | [optional] 
**business_id** | **str** | Business code entity identifier. | [optional] 
**version_id** | **str** | The identifier for current version. | [optional] 
**parent_organization_id** | **str** | Organizations parent organization identifier if exists. | [optional] 
**organization_root_id** | **str** | Organizations root organization identifier if exists. | [optional] 
**municipality** | [**VmOpenApiMunicipality**](VmOpenApiMunicipality.md) |  | [optional] 
**areas** | [**list[VmOpenApiArea]**](VmOpenApiArea.md) | List of organization areas. | [optional] 
**area_municipalities** | [**list[VmOpenApiMunicipality]**](VmOpenApiMunicipality.md) | List of organization area municipalities | [optional] 
**addresses** | [**list[V9VmOpenApiAddress]**](V9VmOpenApiAddress.md) | List of organizations addresses. | [optional] 
**publishing_status** | **str** | Publishing status (Draft, Published, Deleted or Modified). | [optional] 
**services** | [**list[V10VmOpenApiOrganizationService]**](V10VmOpenApiOrganizationService.md) | List of organizations services. | [optional] 
**responsible_organization_services** | [**list[VmOpenApiItem]**](VmOpenApiItem.md) | List of organizations services where organization is main responsible. | [optional] 
**producer_organization_services** | [**list[V10VmOpenApiOrganizationService]**](V10VmOpenApiOrganizationService.md) | List of organizations services where organization is a producer. | [optional] 
**modified** | **datetime** | Date when item was modified/created (UTC). | [optional] 
**sub_organizations** | [**list[VmOpenApiItem]**](VmOpenApiItem.md) | The sub organizations | [optional] 
**available_languages** | **list[str]** | Gets or sets available languages | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

