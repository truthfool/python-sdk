# VmOpenApiAddressStreetWithCoordinatesIn

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets the identifier. | [optional] 
**municipality** | **str** | Municipality code (e.g. 091). | [optional] 
**additional_information** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | Localized list of additional information about the address. (Max.Length: 150). | [optional] 
**owner_reference_id** | **str** | Gets or sets the owner reference identifier. | [optional] 
**street_number** | **str** | Street number for street address. (Max.Length: 30). | [optional] 
**postal_code** | **str** | Postal code, for example 00100. | 
**referenced_street_id** | **str** | Temporarily stored Id of assigned Street during translations | [optional] 
**street** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | List of localized street addresses. | [optional] 
**latitude** | **str** | Location latitude coordinate. | [optional] 
**longitude** | **str** | Location longitude coordinate. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

