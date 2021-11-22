# V11VmOpenApiServiceServiceChannelInBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_channel_id** | **str** | PTV service channel identifier. | 
**service_charge_type** | **str** | Service charge type. Possible values are: Chargeable, FreeOfCharge or Other.  In version 7 and older: Charged, Free or Other | [optional] 
**description** | [**list[VmOpenApiLocalizedListItem]**](VmOpenApiLocalizedListItem.md) | List of localized service channel relationship descriptions. Possible type values are: Description, ChargeTypeAdditionalInfo. (Max.Length: 500 Description). (Max.Length: 500 ChargeTypeAdditionalInfo). | [optional] 
**service_hours** | [**list[V11VmOpenApiServiceHour]**](V11VmOpenApiServiceHour.md) | List of connection related service hours. | [optional] 
**contact_details** | [**V9VmOpenApiContactDetailsInBase**](V9VmOpenApiContactDetailsInBase.md) |  | [optional] 
**delete_service_charge_type** | **bool** | Indicates if value for property ServiceChargeType should be deleted. | [optional] 
**delete_all_descriptions** | **bool** | Indicates if all descriptions should be deleted. | [optional] 
**delete_all_service_hours** | **bool** | Gets or sets a value indicating whether all service hours should be delted. | [optional] 
**service_guid** | **str** | Gets or sets the service unique identifier. | [optional] 
**channel_guid** | **str** | Gets or sets the channel unique identifier. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

