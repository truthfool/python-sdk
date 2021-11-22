# V6VmOpenApiServiceServiceChannel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_charge_type** | **str** | Service charge type. Possible values are: Chargeable, FreeOfCharge or Other. | [optional] 
**description** | [**list[VmOpenApiLocalizedListItem]**](VmOpenApiLocalizedListItem.md) | List of localized service channel relationship descriptions. (Max.Length: 500 Description). (Max.Length: 500 ChargeTypeAdditionalInfo). | [optional] 
**is_asti_connection** | **bool** | Indicates if connection between service and service channel is ASTI related. | [optional] 
**owner_reference_id** | **str** | Contact details for connection. | [optional] 
**service_channel** | [**VmOpenApiItem**](VmOpenApiItem.md) |  | [optional] 
**digital_authorizations** | [**list[V4VmOpenApiFintoItem]**](V4VmOpenApiFintoItem.md) | List of digital authorizations related to the service. | [optional] 
**extra_types** | [**list[V9VmOpenApiExtraType]**](V9VmOpenApiExtraType.md) | The extra types related to service and service channel connection. | [optional] 
**service_hours** | [**list[V11VmOpenApiServiceHour]**](V11VmOpenApiServiceHour.md) | List of connection related service hours. | [optional] 
**contact_details** | [**V9VmOpenApiContactDetails**](V9VmOpenApiContactDetails.md) |  | [optional] 
**modified** | **datetime** | Date when connection was modified/created (UTC). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

