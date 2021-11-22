# V11VmOpenApiServiceLocationChannelInBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **str** | External system identifier for this service channel. User needs to be logged in to be able to get/set value. | [optional] 
**languages** | **list[str]** | List of languages the service channel is available in (two letter language code). | [optional] 
**web_pages** | [**list[V9VmOpenApiWebPage]**](V9VmOpenApiWebPage.md) | List of service channel web pages. | [optional] 
**is_visible_for_all** | **bool** | Indicates if channel can be used (referenced within services) by other users from other organizations. | [optional] 
**channel_id** | **str** | Gets or sets the special channel identifier. | [optional] 
**version_id** | **str** | The identifier for current version. | [optional] 
**id** | **str** | PTV identifier for the service channel. | [optional] 
**organization_id** | **str** | PTV organization identifier for organization responsible for this service channel. | [optional] 
**service_channel_names_with_type** | [**list[VmOpenApiLocalizedListItem]**](VmOpenApiLocalizedListItem.md) | Localized list of service channel names. | [optional] 
**delete_all_web_pages** | **bool** | Set to true to delete all existing web pages for the service channel. The WebPages collection should be empty when this property is set to true. | [optional] 
**delete_all_service_hours** | **bool** | Set to true to delete all existing service hours for the service channel. The ServiceHours collection should be empty when this property is set to true. | [optional] 
**valid_from** | **datetime** | Date when item should be published. | [optional] 
**valid_to** | **datetime** | Date when item should be archived. | [optional] 
**current_publishing_status** | **str** | Current version publishing status. | [optional] 
**service_channel_services** | **list[str]** | Internal property for adding service relations for a service channel. | [optional] 
**user_name** | **str** | User name. | [optional] 
**oid** | **str** | Service channel OID. Must match the regex @\&quot;^[A-Za-z0-9.-]*$\&quot;.  NOTICE! At the moment the property is only a placeholder. The data is not saved into database! | [optional] 
**emails** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | List email addresses for the service channel. | [optional] 
**support_emails** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | List email addresses for the service channel. | [optional] 
**fax_numbers** | [**list[V4VmOpenApiPhoneSimple]**](V4VmOpenApiPhoneSimple.md) | Service location contact fax numbers. | [optional] 
**addresses** | [**list[V9VmOpenApiAddressLocationIn]**](V9VmOpenApiAddressLocationIn.md) | List of service location addresses. | [optional] 
**delete_all_support_emails** | **bool** | Set to true to delete emails. The email property should be empty when this property is set to true. | [optional] 
**delete_all_phone_numbers** | **bool** | Set to true to delete phone number. The prohone property should be empty when this property is set to true. | [optional] 
**delete_all_fax_numbers** | **bool** | Set to true to delete fax number. The fax property should be empty when this property is set to true. | [optional] 
**delete_oid** | **bool** | Set to true to delete OID. The Oid property should be empty when this property is set to true. | [optional] 
**support_phones** | [**list[V4VmOpenApiPhone]**](V4VmOpenApiPhone.md) | List of support phone numbers for the service channel. | [optional] 
**delete_all_support_phones** | **bool** | Set to true to delete all existing support phone numbers for the service channel. The SupportPhones collection should be empty when this property is set to true. | [optional] 
**available_languages** | **list[str]** | Gets or sets available languages | [optional] 
**required_properties_available_languages** | **list[str]** | Internal property to check the languages within required lists: ServiceChannelNames, ServiceChannelDescriptions  and ChannelUrls lists. | [optional] 
**service_channel_names** | [**list[VmOpenApiLocalizedListItem]**](VmOpenApiLocalizedListItem.md) | List of organization names. Possible type values are: Name, AlternativeName. | [optional] 
**service_channel_descriptions** | [**list[VmOpenApiLocalizedListItem]**](VmOpenApiLocalizedListItem.md) | List of localized service channel descriptions. Possible type values are: Description, Summary. (Max.Length: 150 Summary). | [optional] 
**display_name_type** | [**list[VmOpenApiNameTypeByLanguage]**](VmOpenApiNameTypeByLanguage.md) | List of Display name types (Name or AlternativeName) for each language version of ServiceChannelNames. | [optional] 
**area_type** | **str** | Area type. Possible values are: Nationwide, NationwideExceptAlandIslands or LimitedType. | [optional] 
**areas** | [**list[VmOpenApiAreaIn]**](VmOpenApiAreaIn.md) | List of areas. List can contain different types of areas. | [optional] 
**phone_numbers** | [**list[V4VmOpenApiPhone]**](V4VmOpenApiPhone.md) | List of support phone numbers for the service channel. | [optional] 
**service_hours** | [**list[V11VmOpenApiServiceHour]**](V11VmOpenApiServiceHour.md) | List of service channel service hours. | [optional] 
**publishing_status** | **str** | Service channel publishing status. Values: Draft, Published, Deleted or Modified. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

