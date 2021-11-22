# V9VmOpenApiAddressLocation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets the identifier. | [optional] 
**post_office_box_address** | [**VmOpenApiAddressPostOfficeBox**](VmOpenApiAddressPostOfficeBox.md) |  | [optional] 
**street_address** | [**VmOpenApiAddressStreetWithCoordinates**](VmOpenApiAddressStreetWithCoordinates.md) |  | [optional] 
**country** | **str** | Country code (ISO 3166-1 alpha-2), for example FI. | [optional] 
**type** | **str** | Address type, Location or Postal. | [optional] 
**sub_type** | **str** | Address sub type, Single, Street, PostOfficeBox, Abroad or Other. | [optional] 
**other_address** | [**VmOpenApiAddressOther**](VmOpenApiAddressOther.md) |  | [optional] 
**location_abroad** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | Localized list of foreign address information. | [optional] 
**entrances** | [**list[V9VmOpenApiEntrance]**](V9VmOpenApiEntrance.md) | Entrances for an address. Includes accessibility sentences. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

