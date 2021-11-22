# V11VmOpenApiPhoneChannelIn

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **str** | External system identifier for this service channel. User needs to be logged in to be able to get/set value. | [optional] 
**support_emails** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | List of support email addresses for the service channel. (Max.Length: 100). | [optional] 
**is_visible_for_all** | **bool** | Indicates if channel can be used (referenced within services) by other users from other organizations. | [optional] 
**channel_id** | **str** | Gets or sets the special channel identifier. | [optional] 
**version_id** | **str** | The identifier for current version. | [optional] 
**id** | **str** | PTV identifier for the service channel. | [optional] 
**service_channel_names_with_type** | [**list[VmOpenApiLocalizedListItem]**](VmOpenApiLocalizedListItem.md) | Localized list of service channel names. | [optional] 
**valid_from** | **datetime** | Date when item should be published. | [optional] 
**valid_to** | **datetime** | Date when item should be archived. | [optional] 
**current_publishing_status** | **str** | Current version publishing status. | [optional] 
**service_channel_services** | **list[str]** | Internal property for adding service relations for a service channel. | [optional] 
**user_name** | **str** | User name. | [optional] 
**web_page** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | List of localized urls. (Max.Length: 500). | [optional] 
**web_pages** | [**list[V9VmOpenApiWebPage]**](V9VmOpenApiWebPage.md) | List of service channel web pages. | [optional] 
**support_phones** | [**list[V4VmOpenApiPhone]**](V4VmOpenApiPhone.md) | List of support phone numbers for the service channel. | [optional] 
**available_languages** | **list[str]** | Gets or sets available languages | [optional] 
**required_properties_available_languages** | **list[str]** | Internal property to check the languages within required lists: ServiceChannelNames, ServiceChannelDescriptions  and PhoneNumbers lists. | [optional] 
**area_type** | **str** | Area type. Possible values are: Nationwide, NationwideExceptAlandIslands or LimitedType. | [optional] 
**areas** | [**list[VmOpenApiAreaIn]**](VmOpenApiAreaIn.md) | List of areas. List can contain different types of areas. | [optional] 
**phone_numbers** | [**list[V4VmOpenApiPhoneWithType]**](V4VmOpenApiPhoneWithType.md) | List of support phone numbers for the service channel. | [optional] 
**service_hours** | [**list[V11VmOpenApiServiceHour]**](V11VmOpenApiServiceHour.md) | List of service channel service hours. | [optional] 
**publishing_status** | **str** | Service channel publishing status. Values: Draft, Published, Deleted or Modified. | 
**languages** | **list[str]** | List of languages the service channel is available in (two letter language code). | 
**organization_id** | **str** | PTV organization identifier of organization responsible for this channel. | 
**service_channel_names** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | Localized list of service channel names. | 
**service_channel_descriptions** | [**list[VmOpenApiLocalizedListItem]**](VmOpenApiLocalizedListItem.md) | Localized list of service channel descriptions. Possible type values are: Description, Summary. | 
**services** | **list[str]** | List of related services (GUID). | [optional] 
**delete_all_service_hours** | **bool** | Set to true to delete all existing service hours for the service channel. The ServiceHours collection should be empty when this property is set to true. | [optional] 
**delete_all_web_pages** | **bool** | Set to true to delete all existing web pages for the service channel. The WebPages collection should be empty when this property is set to true. | [optional] 
**delete_all_support_emails** | **bool** | Set to true to delete all existing support emails for the service channel. The SupportEmails collection should be empty when this property is set to true. | [optional] 
**delete_all_support_phones** | **bool** | Set to true to delete all existing support phonesfor the service channel. The SupportPhones collection should be empty when this property is set to true. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

