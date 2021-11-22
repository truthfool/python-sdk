# V11VmOpenApiServiceCollectionIn

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **str** | External system identifier for the entity. User needs to be logged in to be able to get/set value. | [optional] 
**available_languages** | **list[str]** | Gets or sets available languages | [optional] 
**version_id** | **str** | The identifier for current version. | [optional] 
**id** | **str** | PTV service identifier. | [optional] 
**current_publishing_status** | **str** | Current version publishing status. | [optional] 
**services** | **list[str]** | List of service collection services. | [optional] 
**service_collection_services** | **list[str]** | Internal property for adding service collection services for service collection. | [optional] 
**service_collection_channels** | **list[str]** | Internal property for adding service collection services for service collection. | [optional] 
**delete_all_channels** | **bool** | Set to true to delete all existing channels (the services collection for this object should be empty collection when this option is used). | [optional] 
**required_properties_available_languages** | **list[str]** | Internal property to check the languages within required lists: ServiceCollectionNames and ServiceCollectionDescriptions | [optional] 
**service_collection_descriptions** | [**list[VmOpenApiLocalizedListItem]**](VmOpenApiLocalizedListItem.md) | List of localized service colections descriptions. Possible type values are: Description, Summary. (Max.Length: 150 Summary). (Max.Length: 2500 Description). | [optional] 
**service_channels** | **list[str]** | List of service collection channels. | [optional] 
**service_collection_names** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | List of localized service collection names. | 
**organization_id** | **str** | Main responsible organization Id. | 
**publishing_status** | **str** | Publishing status. Possible values are: Draft or Published. | 
**delete_all_services** | **bool** | Set to true to delete all existing services (the services collection for this object should be empty collection when this option is used). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

