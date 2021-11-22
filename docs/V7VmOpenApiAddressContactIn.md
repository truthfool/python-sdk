# V7VmOpenApiAddressContactIn

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets the identifier. | [optional] 
**post_office_box_address** | [**VmOpenApiAddressPostOfficeBoxIn**](VmOpenApiAddressPostOfficeBoxIn.md) |  | [optional] 
**street_address** | [**VmOpenApiAddressStreetWithCoordinatesIn**](VmOpenApiAddressStreetWithCoordinatesIn.md) |  | [optional] 
**country** | **str** | Country code (ISO 3166-1 alpha-2), for example FI. | [optional] 
**owner_reference_id** | **str** | Gets or sets the owner reference identifier. | [optional] 
**unique_id** | **str** | Gets or sets the address unique id | [optional] 
**type** | **str** | Address type, only Postal accepted. | 
**sub_type** | **str** | Address sub type, Street, PostOfficeBox or Abroad. | 
**foreign_address** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | Localized list of foreign address information. | [optional] 
**location_abroad** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | Localized list of foreign address information. (Max.Length: 500). | [optional] 
**order_number** | **int** | Gets or sets the order number | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

