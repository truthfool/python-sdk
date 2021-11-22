# V4VmOpenApiPhoneWithType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets the identifier. | [optional] 
**number** | **str** | Phone number. | 
**language** | **str** | Language of this object. Valid values are: fi, sv or en. | 
**owner_reference_id** | **str** | Gets or sets the owner reference identifier. | [optional] 
**owner_reference_id2** | **str** | Gets or sets the owner reference identifier. | [optional] 
**order_number** | **int** | The order of phone number. | [optional] 
**prefix_number** | **str** | Prefix for the phone number. | [optional] 
**is_finnish_service_number** | **bool** | Defines if number is Finnish service number. If true prefix number can be left empty. | [optional] 
**additional_information** | **str** | Additional information. (Max.Length: 150). | [optional] 
**service_charge_type** | **str** | Service charge type. Possible values are: Chargeable, FreeOfCharge or Other.  In version 7 and older: Charged, Free or Other. | [optional] 
**charge_description** | **str** | Charge description. (Max.Length: 150). | [optional] 
**type** | **str** | Phone number type (Phone, Sms or Fax). | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

