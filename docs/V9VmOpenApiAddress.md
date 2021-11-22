# V9VmOpenApiAddress

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets the identifier. | [optional] 
**type** | **str** | Address type, Visiting or Postal. | [optional] 
**post_office_box_address** | [**VmOpenApiAddressPostOfficeBox**](VmOpenApiAddressPostOfficeBox.md) |  | [optional] 
**street_address** | [**VmOpenApiAddressStreetWithCoordinates**](VmOpenApiAddressStreetWithCoordinates.md) |  | [optional] 
**country** | **str** | Country code (ISO 3166-1 alpha-2), for example FI. | [optional] 
**sub_type** | **str** | Address sub type, Street, PostOfficeBox, Foreign or Other. | [optional] 
**other_address** | [**VmOpenApiAddressOther**](VmOpenApiAddressOther.md) |  | [optional] 
**foreign_address** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | Localized list of foreign address information. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

