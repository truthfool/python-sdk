# V8VmOpenApiAddressDeliveryIn

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets the identifier. | [optional] 
**sub_type** | **str** | Address sub type, Street, PostOfficeBox or NoAddress. | 
**post_office_box_address** | [**VmOpenApiAddressPostOfficeBoxIn**](VmOpenApiAddressPostOfficeBoxIn.md) |  | [optional] 
**street_address** | [**VmOpenApiAddressStreetIn**](VmOpenApiAddressStreetIn.md) |  | [optional] 
**delivery_address_in_text** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | Localized list of foreign address information. (Max.Length: 150). | [optional] 
**form_receiver** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | List of localized form receivers. One per language. (Max.Length: 100). | [optional] 
**order_number** | **int** | Gets or sets the order number | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

