# V11VmOpenApiServiceHour

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_hour_type** | **str** | Type of service hour. Valid values are: DaysOfTheWeek, Exceptional or OverMidnight.  In version 7 and older: Standard, Exception or Special. | 
**valid_from** | **datetime** | Date time where from this entry is valid. | [optional] 
**valid_to** | **datetime** | Date time to this entry is valid. | [optional] 
**is_closed** | **bool** | Set to true to present a time between the valid from and to times as closed. | [optional] 
**valid_for_now** | **bool** | Set to true to present that this entry is valid for now. | [optional] 
**is_always_open** | **bool** | Set to true to present a time between the valid from and to times as allways open. | [optional] 
**is_reservation** | **bool** | Gets or sets a value indicating whether this instance is open on reservation. | [optional] 
**additional_information** | [**list[VmOpenApiLanguageItem]**](VmOpenApiLanguageItem.md) | Localized list of additional information. (Max.Length: 150). | [optional] 
**opening_hour** | [**list[V8VmOpenApiDailyOpeningTime]**](V8VmOpenApiDailyOpeningTime.md) | Gets or sets the opening hour. | [optional] 
**order_number** | **int** | The order of service hours. | [optional] 
**owner_reference_id** | **str** | Gets or sets the owner reference identifier. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

