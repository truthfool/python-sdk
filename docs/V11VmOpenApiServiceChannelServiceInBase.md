# V11VmOpenApiServiceChannelServiceInBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | PTV service identifier. | 
**service_charge_type** | **str** | Service charge type. Possible values are: Chargeable, FreeOfCharge or Other. | [optional] 
**description** | [**list[VmOpenApiLocalizedListItem]**](VmOpenApiLocalizedListItem.md) | List of localized service channel relationship descriptions. Possible type values are: Description, ChargeTypeAdditionalInfo. (Max.Length: 500 Description). (Max.Length: 500 ChargeTypeAdditionalInfo). | [optional] 
**extra_types** | [**list[VmOpenApiExtraType]**](VmOpenApiExtraType.md) | The extra types related to service and service channel connection. | [optional] 
**service_hours** | [**list[V11VmOpenApiServiceHour]**](V11VmOpenApiServiceHour.md) | List of connection related service hours. | [optional] 
**contact_details** | [**V9VmOpenApiContactDetailsInBase**](V9VmOpenApiContactDetailsInBase.md) |  | [optional] 
**delete_service_charge_type** | **bool** | Indicates if value for property ServiceChargeType should be deleted. | [optional] 
**delete_all_descriptions** | **bool** | Indicates if all descriptions should be deleted. | [optional] 
**delete_all_extra_types** | **bool** | Indicates if all extra types should be deleted. | [optional] 
**delete_all_service_hours** | **bool** | Gets or sets a value indicating whether all service hours should be delted. | [optional] 
**service_guid** | **str** | Gets or sets the service unique identifier. | [optional] 
**channel_guid** | **str** | Gets or sets the channel unique identifier. | [optional] 
**is_asti_connection** | **bool** | Indicates if connection between service and service channel is ASTI related. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

