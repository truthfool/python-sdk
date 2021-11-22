# V11VmOpenApiPrintableFormChannel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | PTV identifier for the service channel. | [optional] 
**source_id** | **str** | External system identifier for this service channel. User needs to be logged in to be able to get/set value. | [optional] 
**service_channel_descriptions** | [**list[VmOpenApiLocalizedListItem]**](VmOpenApiLocalizedListItem.md) | List of localized service channel descriptions. Possible type values are: Description, Summary (in version 7 ShortDescription). (Max.Length: 2500 Description). | [optional] 
**area_type** | **str** | Area type. Possible values are: Nationwide, NationwideExceptAlandIslands or LimitedType.  In version 7 and older: WholeCountry, WholeCountryExceptAlandIslands, AreaType. | [optional] 
**support_phones** | [**list[V4VmOpenApiPhone]**](V4VmOpenApiPhone.md) | List of support phone numbers for the service channel. | [optional] 
**support_emails** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | List of support email addresses for the service channel. (Max.Length: 100). | [optional] 
**languages** | **list[str]** | List of languages the service channel is available in (two letter language code). | [optional] 
**web_pages** | [**list[V9VmOpenApiWebPage]**](V9VmOpenApiWebPage.md) | List of service channel web pages. | [optional] 
**service_hours** | [**list[V11VmOpenApiServiceHour]**](V11VmOpenApiServiceHour.md) | List of service channel service hours. | [optional] 
**channel_id** | **str** | Gets or sets the special channel identifier. | [optional] 
**version_id** | **str** | The identifier for current version. | [optional] 
**service_channel_type** | **str** | Type of the service channel. Channel types: EChannel, WebPage, PrintableForm, Phone or ServiceLocation. | [optional] 
**organization_id** | **str** | PTV organization identifier responsible for the channel. | [optional] 
**service_channel_names** | [**list[VmOpenApiLocalizedListItem]**](VmOpenApiLocalizedListItem.md) | Localized list of service channel names. Possible type values are: Name, AlternativeName (in version 7 AlternateName). | [optional] 
**areas** | [**list[VmOpenApiArea]**](VmOpenApiArea.md) | List of service channel areas. | [optional] 
**services** | [**list[V11VmOpenApiServiceChannelService]**](V11VmOpenApiServiceChannelService.md) | List of linked services including relationship data. | [optional] 
**service_collections** | [**list[VmOpenApiServiceServiceCollection]**](VmOpenApiServiceServiceCollection.md) |  | [optional] 
**publishing_status** | **str** | Publishing status. Possible values are: Draft, Published, Deleted or Modified. | [optional] 
**modified** | **datetime** | Date when item was modified/created (UTC). | [optional] 
**responsible_sote_organization** | **str** | Sote organization that is responsible for the service channel. Notice! At the moment always empty - the property is a placeholder for later use. | [optional] 
**ontology_terms** | [**list[V4VmOpenApiOntologyTerm]**](V4VmOpenApiOntologyTerm.md) | List of ontology terms related to the all service connections. | [optional] 
**area_municipalities** | [**list[VmOpenApiMunicipality]**](VmOpenApiMunicipality.md) | List of municipalities including municipality code and a localized list of municipality names. | [optional] 
**is_visible_for_all** | **bool** | Indicates if channel can be used (referenced within services) by other users from other organizations. | [optional] 
**security** | [**ISecurityOwnOrganization**](ISecurityOwnOrganization.md) |  | [optional] 
**available_languages** | **list[str]** | Gets or sets available languages | [optional] 
**form_identifier** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | List of localized form identifier. One per language. | [optional] 
**delivery_addresses** | [**list[V8VmOpenApiAddressDelivery]**](V8VmOpenApiAddressDelivery.md) | Form delivery addresses. | [optional] 
**channel_urls** | [**list[VmOpenApiLocalizedListItem]**](VmOpenApiLocalizedListItem.md) | List of localized channel urls. | [optional] 
**attachments** | [**list[VmOpenApiAttachmentWithType]**](VmOpenApiAttachmentWithType.md) | List of attachments. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

