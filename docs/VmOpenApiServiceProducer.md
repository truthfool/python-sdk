# VmOpenApiServiceProducer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets the identifier. | [optional] 
**owner_reference_id** | **str** | Gets or sets the owner reference identifier. | [optional] 
**order_number** | **int** | The order of service voucher. | [optional] 
**provision_type** | **str** | Provision type, valid values for version 8 are SelfProducedServices, ProcuredServices or Other.  For older versions valid values are SelfProduced, PurchaseServices or Other. | 
**additional_information** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | Localized list of additional information. (Max.Length: 150). | [optional] 
**organizations** | [**list[VmOpenApiItem]**](VmOpenApiItem.md) | Gets or sets the organization information. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

