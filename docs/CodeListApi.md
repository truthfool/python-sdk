# swagger_client.CodeListApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v11_code_list_get_area_codes_type_type_get**](CodeListApi.md#api_v11_code_list_get_area_codes_type_type_get) | **GET** /api/v11/CodeList/GetAreaCodes/type/{type} | Gets a list of area codes filtered by area type.
[**api_v11_code_list_get_country_codes_get**](CodeListApi.md#api_v11_code_list_get_country_codes_get) | **GET** /api/v11/CodeList/GetCountryCodes | Gets a list of country codes.
[**api_v11_code_list_get_language_codes_get**](CodeListApi.md#api_v11_code_list_get_language_codes_get) | **GET** /api/v11/CodeList/GetLanguageCodes | Gets a list of language codes.
[**api_v11_code_list_get_municipality_codes_get**](CodeListApi.md#api_v11_code_list_get_municipality_codes_get) | **GET** /api/v11/CodeList/GetMunicipalityCodes | Gets a list of municipality codes.
[**api_v11_code_list_get_postal_codes_get**](CodeListApi.md#api_v11_code_list_get_postal_codes_get) | **GET** /api/v11/CodeList/GetPostalCodes | Gets a list of postal codes.

# **api_v11_code_list_get_area_codes_type_type_get**
> list[VmOpenApiCodeListItem] api_v11_code_list_get_area_codes_type_type_get(type)

Gets a list of area codes filtered by area type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CodeListApi()
type = 'type_example' # str | Area type

try:
    # Gets a list of area codes filtered by area type.
    api_response = api_instance.api_v11_code_list_get_area_codes_type_type_get(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CodeListApi->api_v11_code_list_get_area_codes_type_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Area type | 

### Return type

[**list[VmOpenApiCodeListItem]**](VmOpenApiCodeListItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_code_list_get_country_codes_get**
> list[VmOpenApiDialCodeListItem] api_v11_code_list_get_country_codes_get()

Gets a list of country codes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CodeListApi()

try:
    # Gets a list of country codes.
    api_response = api_instance.api_v11_code_list_get_country_codes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CodeListApi->api_v11_code_list_get_country_codes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VmOpenApiDialCodeListItem]**](VmOpenApiDialCodeListItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_code_list_get_language_codes_get**
> list[VmOpenApiCodeListItem] api_v11_code_list_get_language_codes_get()

Gets a list of language codes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CodeListApi()

try:
    # Gets a list of language codes.
    api_response = api_instance.api_v11_code_list_get_language_codes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CodeListApi->api_v11_code_list_get_language_codes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VmOpenApiCodeListItem]**](VmOpenApiCodeListItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_code_list_get_municipality_codes_get**
> list[VmOpenApiCodeListItem] api_v11_code_list_get_municipality_codes_get()

Gets a list of municipality codes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CodeListApi()

try:
    # Gets a list of municipality codes.
    api_response = api_instance.api_v11_code_list_get_municipality_codes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CodeListApi->api_v11_code_list_get_municipality_codes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VmOpenApiCodeListItem]**](VmOpenApiCodeListItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_code_list_get_postal_codes_get**
> VmOpenApiCodeListPage api_v11_code_list_get_postal_codes_get(page=page)

Gets a list of postal codes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CodeListApi()
page = 1 # int | The page to be fetched. (optional) (default to 1)

try:
    # Gets a list of postal codes.
    api_response = api_instance.api_v11_code_list_get_postal_codes_get(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CodeListApi->api_v11_code_list_get_postal_codes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page to be fetched. | [optional] [default to 1]

### Return type

[**VmOpenApiCodeListPage**](VmOpenApiCodeListPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

