# VmOpenApiAddressStreetWithCoordinates

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets the identifier. | [optional] 
**postal_code** | **str** | Postal code, for example 00100. | 
**post_office** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | List of localized Post offices, for example Helsinki, Helsingfors. | [optional] 
**municipality** | [**VmOpenApiMunicipality**](VmOpenApiMunicipality.md) |  | [optional] 
**additional_information** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | Localized list of additional information about the address. (Max.Length: 150). | [optional] 
**street** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | List of localized street addresses. (Max.Length: 100). | [optional] 
**street_number** | **str** | Street number for street address. (Max.Length: 30). | [optional] 
**latitude** | **str** | Location latitude coordinate. | [optional] 
**longitude** | **str** | Location longitude coordinate. | [optional] 
**coordinate_state** | **str** | State of coordinates. Coordinates are fetched from a service provided by Maanmittauslaitos (WFS).  Possible values are: Loading, Ok, Failed, NotReceived, EmptyInputReceived, MultipleResultsReceived, WrongFormatReceived or EnteredByUser. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

