# VmOpenApiArea

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the area. Possible values are: Municipality, Region, BusinessSubRegion, HospitalDistrict.  In version 7 and older: Municipality, Province, BusinessRegions, HospitalRegions. | [optional] 
**code** | **str** | Code of the area. | [optional] 
**name** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | Localized list of names for the area | [optional] 
**municipalities** | [**list[VmOpenApiMunicipality]**](VmOpenApiMunicipality.md) | List of municipalities including municipality code and a localized list of municipality names. | [optional] 
**owner_reference_id** | **str** | Gets or sets the owner reference identifier. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

