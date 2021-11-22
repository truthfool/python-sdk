# V11VmOpenApiServiceCollection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | PTV service identifier. | [optional] 
**source_id** | **str** | External system identifier for the entity. User needs to be logged in to be able to get/set value. | [optional] 
**service_collection_names** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | List of localized service collection names. (Max.Length: 100). | [optional] 
**service_collection_descriptions** | [**list[VmOpenApiLocalizedListItem]**](VmOpenApiLocalizedListItem.md) | List of localized service collection descriptions. | [optional] 
**publishing_status** | **str** | Publishing status. Possible values are: Draft, Published, Deleted or Modified. | 
**available_languages** | **list[str]** | Gets or sets available languages | [optional] 
**version_id** | **str** | The identifier for current version. | [optional] 
**organization_id** | **str** | Main responsible organization Id. | [optional] 
**services** | [**list[VmOpenApiServiceCollectionService]**](VmOpenApiServiceCollectionService.md) | List of service collection services. | [optional] 
**service_channels** | [**list[VmOpenApiServiceCollectionChannel]**](VmOpenApiServiceCollectionChannel.md) |  | [optional] 
**modified** | **datetime** | Date when item was modified/created (UTC). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

