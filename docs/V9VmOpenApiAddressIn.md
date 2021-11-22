# V9VmOpenApiAddressIn

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets the identifier. | [optional] 
**post_office_box_address** | [**VmOpenApiAddressPostOfficeBoxIn**](VmOpenApiAddressPostOfficeBoxIn.md) |  | [optional] 
**street_address** | [**VmOpenApiAddressStreetWithCoordinatesIn**](VmOpenApiAddressStreetWithCoordinatesIn.md) |  | [optional] 
**country** | **str** | Country code (ISO 3166-1 alpha-2), for example FI. | [optional] 
**owner_reference_id** | **str** | Gets or sets the owner reference identifier. | [optional] 
**unique_id** | **str** | Gets or sets the address unique id | [optional] 
**type** | **str** | Address type, Visiting or Postal. | 
**sub_type** | **str** | Address sub type, Street, PostOfficeBox, Foreign or Other. | 
**other_address** | [**VmOpenApiAddressOtherIn**](VmOpenApiAddressOtherIn.md) |  | [optional] 
**foreign_address** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | Localized list of foreign address information. | [optional] 
**order_number** | **int** | Gets or sets the order number | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

