# V10VmOpenApiPrintableFormChannelIn

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
**form_identifier** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | List of localized form identifiers. One per language. (Max.Length: 100). | [optional] 
**delivery_addresses** | [**list[V8VmOpenApiAddressDeliveryIn]**](V8VmOpenApiAddressDeliveryIn.md) | Gets or sets the delivery addresses. | [optional] 
**attachments** | [**list[VmOpenApiAttachment]**](VmOpenApiAttachment.md) | List of attachments. | [optional] 
**web_pages** | [**list[V9VmOpenApiWebPage]**](V9VmOpenApiWebPage.md) | List of service channel web pages. | [optional] 
**service_hours** | [**list[V11VmOpenApiServiceHour]**](V11VmOpenApiServiceHour.md) | List of service channel service hours. | [optional] 
**delete_all_web_pages** | **bool** | Set to true to delete all existing web pages for the service channel. The WebPages collection should be empty when this property is set to true. | [optional] 
**delete_all_service_hours** | **bool** | Set to true to delete all existing service hours for the service channel. The ServiceHours collection should be empty when this property is set to true. | [optional] 
**available_languages** | **list[str]** | Gets or sets available languages | [optional] 
**required_properties_available_languages** | **list[str]** | Internal property to check the languages within required lists: ServiceChannelNames, ServiceChannelDescriptions  and ChannelUrls lists. | [optional] 
**area_type** | **str** | Area type. Possible values are: Nationwide, NationwideExceptAlandIslands or LimitedType. | [optional] 
**areas** | [**list[VmOpenApiAreaIn]**](VmOpenApiAreaIn.md) | List of areas. List can contain different types of areas. | [optional] 
**support_phones** | [**list[V4VmOpenApiPhone]**](V4VmOpenApiPhone.md) | List of support phone numbers for the service channel. | [optional] 
**channel_urls** | [**list[VmOpenApiLocalizedListItem]**](VmOpenApiLocalizedListItem.md) | List of localized urls. Possible type values are: PDF, DOC, Excel. | 
**organization_id** | **str** | PTV organization identifier of organization responsible for this channel. | 
**service_channel_names** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | List of localized service channel names. | 
**service_channel_descriptions** | [**list[VmOpenApiLocalizedListItem]**](VmOpenApiLocalizedListItem.md) | List of localized service channel descriptions. Possible type values are: Description, Summary. | 
**languages** | **list[str]** | List of languages the service channel is available in (two letter language code). | 
**publishing_status** | **str** | Service channel publishing status. Values: Draft or Published. | 
**services** | **list[str]** | List of related services (GUID). | [optional] 
**delete_all_delivery_addresses** | **bool** | Set to true to delete all existing delivery addresses for the service channel. The DeliveryAddresses should be empty when this property is set to true. | [optional] 
**delete_all_channel_urls** | **bool** | Set to true to delete all existing channel urls for the service channel. The ChannelUrls collection should be empty when this property is set to true. | [optional] 
**delete_all_attachments** | **bool** | Set to true to delete all existing attachments for the service channel. The Attachments collection should be empty when this property is set to true. | [optional] 
**delete_all_support_emails** | **bool** | Set to true to delete all existing support email addresses for the service channel. The SupportEmails collection should be empty when this property is set to true. | [optional] 
**delete_all_support_phones** | **bool** | Set to true to delete all existing support phone numbers for the service channel. The SupportPhones collection should be empty when this property is set to true. | [optional] 
**delete_all_form_identifiers** | **bool** | Set to true to delete all existing form identifiers for the service channel. The form identifiers collection should be empty when this property is set to true. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

