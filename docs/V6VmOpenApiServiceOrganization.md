# V6VmOpenApiServiceOrganization

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_type** | **str** | Role type, valid values Responsible or Producer. In version 7 and upper also OtherResponsible role type is used. | 
**additional_information** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | Localized list of additional information. | [optional] 
**organization** | [**VmOpenApiItem**](VmOpenApiItem.md) |  | [optional] 
**provision_type** | **str** | Provision type, valid values for version 8 are SelfProducedServices, ProcuredServices or Other.  For older versions valid values are SelfProduced, PurchaseServices or Other. | [optional] 
**service_id** | **str** | Gets or sets the service identifier. | [optional] 
**owner_reference_id** | **str** | Gets or sets the owner reference identifier. | [optional] 
**organization_id** | **str** | Organization identifier | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

