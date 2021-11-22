# V11VmOpenApiServiceAndChannelRelationBySource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_source_id** | **str** | The external source id for service. | 
**service_channel_source_id** | **str** | The external source id for service channel. | 
**service_charge_type** | **str** | Service charge type. Possible values are: Chargeable, FreeOfCharge or Other | [optional] 
**description** | [**list[VmOpenApiLocalizedListItem]**](VmOpenApiLocalizedListItem.md) | List of localized service channel relationship descriptions. Possible type values are: Description, ChargeTypeAdditionalInfo. (Max.Length: 500 Description). (Max.Length: 500 ChargeTypeAdditionalInfo). | [optional] 
**service_hours** | [**list[V11VmOpenApiServiceHour]**](V11VmOpenApiServiceHour.md) | List of connection related service hours. | [optional] 
**contact_details** | [**V9VmOpenApiContactDetailsIn**](V9VmOpenApiContactDetailsIn.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

