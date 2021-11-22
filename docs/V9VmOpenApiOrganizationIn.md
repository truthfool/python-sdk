# V9VmOpenApiOrganizationIn

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **str** | Organization external system identifier. User needs to be logged in to be able to get/set value. | [optional] 
**business_code** | **str** | Organization business code (Y-tunnus). | [optional] 
**business_name** | **str** | Organization business name (name used for business code). This property is not used in the API anymore. Do not use. | [optional] 
**emails** | [**list[V4VmOpenApiEmail]**](V4VmOpenApiEmail.md) | List of email addresses. | [optional] 
**web_pages** | [**list[V9VmOpenApiWebPage]**](V9VmOpenApiWebPage.md) | List of organizations web pages. | [optional] 
**electronic_invoicings** | [**list[VmOpenApiOrganizationEInvoicing]**](VmOpenApiOrganizationEInvoicing.md) | List of organizations electronic invoicing information. | [optional] 
**business_id** | **str** | Business code entity identifier. | [optional] 
**version_id** | **str** | The identifier for current version. | [optional] 
**oid** | **str** | Organization OID. - must match the regex @\&quot;^[A-Za-z0-9.-]*$\&quot; (Max.Length: 100). | [optional] 
**municipality** | **str** | Municipality code (like 491 or 091). | [optional] 
**addresses** | [**list[V9VmOpenApiAddressIn]**](V9VmOpenApiAddressIn.md) | List of addresses. | [optional] 
**parent_organization_id** | **str** | Parent organization identifier. | [optional] 
**valid_from** | **datetime** | Date when item should be published. | [optional] 
**valid_to** | **datetime** | Date when item should be archived. | [optional] 
**id** | **str** | Entity identifier. | [optional] 
**current_publishing_status** | **str** | Current version publishing status. | [optional] 
**user_name** | **str** | User name. | [optional] 
**available_languages** | **list[str]** | Gets or sets available languages | [optional] 
**required_properties_available_languages** | **list[str]** | Internal property to check the languages within required lists: OrganizationNames and OrganizationDescriptions | [optional] 
**sub_area_type** | **str** | Sub area type (Municipality, Region, BusinessSubRegion, HospitalDistrict). | [optional] 
**areas** | **list[str]** | Area codes related to sub area type. For example if SubAreaType &#x3D; Municipality, Areas-list need to include municipality codes like 491 or 091. | [optional] 
**phone_numbers** | [**list[V4VmOpenApiPhone]**](V4VmOpenApiPhone.md) | List of organizations phone numbers. | [optional] 
**organization_type** | **str** | Organization type (State, Municipality, RegionalOrganization, Organization, Company). | 
**organization_names** | [**list[VmOpenApiLocalizedListItem]**](VmOpenApiLocalizedListItem.md) | List of organization names. Possible type values are: Name, AlternativeName. | 
**organization_descriptions** | [**list[VmOpenApiLocalizedListItem]**](VmOpenApiLocalizedListItem.md) | Localized list of organization descriptions. Possible type values are: Description, Summary. | 
**display_name_type** | [**list[VmOpenApiNameTypeByLanguage]**](VmOpenApiNameTypeByLanguage.md) | List of Display name types (Name or AlternativeName) for each language version of OrganizationNames. | 
**area_type** | **str** | Area type (Nationwide, NationwideExceptAlandIslands, LimitedType). | [optional] 
**publishing_status** | **str** | Publishing status (Draft or Published). | 
**delete_all_emails** | **bool** | Set to true to delete all existing emails (the EmailAddresses collection for this object should be empty collection when this option is used). | [optional] 
**delete_all_phones** | **bool** | Set to true to delete all existing phone numbers (the PhoneNumbers collection for this object should be empty collection when this option is used). | [optional] 
**delete_all_web_pages** | **bool** | Set to true to delete all existing web pages (the WebPages collection for this object should be empty collection when this option is used). | [optional] 
**delete_all_addresses** | **bool** | Set to true to delete all existing addresses (the Addresses collection for this object should be empty collection when this option is used). | [optional] 
**delete_all_electronic_invoicings** | **bool** | Set to true to delete all existing electronic invoicing addresses (the ElectronicInvoicings collection for this object should be empty collection when this option is used). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

