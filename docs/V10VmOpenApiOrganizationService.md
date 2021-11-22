# V10VmOpenApiOrganizationService

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_type** | **str** | Role type, valid values Responsible or Producer. In version 7 and upper also OtherResponsible role type is used. | 
**provision_type** | **str** | Provision type, valid values SelfProduced, PurchaseServices, Other or VoucherServices. Required if RoleType value is Producer. | [optional] 
**additional_information** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | Localized list of additional information. | [optional] 
**service** | [**VmOpenApiItem**](VmOpenApiItem.md) |  | [optional] 
**organization_id** | **str** | PTV organization identifier (organization related to the service). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

