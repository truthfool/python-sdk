# swagger_client.GeneralDescriptionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v11_general_description_get**](GeneralDescriptionApi.md#api_v11_general_description_get) | **GET** /api/v11/GeneralDescription | Gets all the statutory service general descriptions within PTV as a list of ids and names.  General descriptions created/modified after certain date can be fetched by adding date as query string parameter.  General descriptions created/modified before certain date can be fetched by adding dateBefore as query string parameter.
[**api_v11_general_description_id_get**](GeneralDescriptionApi.md#api_v11_general_description_id_get) | **GET** /api/v11/GeneralDescription/{id} | Fetches all the information related to a single statutory service general description.
[**api_v11_general_description_id_put**](GeneralDescriptionApi.md#api_v11_general_description_id_put) | **PUT** /api/v11/GeneralDescription/{id} | Updates the defined general description with the data provided as input.
[**api_v11_general_description_list_get**](GeneralDescriptionApi.md#api_v11_general_description_list_get) | **GET** /api/v11/GeneralDescription/list | Fetches all the information related to requested statutory service general descriptions.
[**api_v11_general_description_new_gd_list_get**](GeneralDescriptionApi.md#api_v11_general_description_new_gd_list_get) | **GET** /api/v11/GeneralDescription/newGdList | Gets the new statutory service general descriptions within PTV as a list of ids and names.
[**api_v11_general_description_post**](GeneralDescriptionApi.md#api_v11_general_description_post) | **POST** /api/v11/GeneralDescription | Creates a new general description with the data provided as input.

# **api_v11_general_description_get**
> V3VmOpenApiGuidPage api_v11_general_description_get(_date=_date, date_before=date_before, page=page)

Gets all the statutory service general descriptions within PTV as a list of ids and names.  General descriptions created/modified after certain date can be fetched by adding date as query string parameter.  General descriptions created/modified before certain date can be fetched by adding dateBefore as query string parameter.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages. Below sample response.  <code>              {                  \"Names\": [                      \"Type - Required value 'Name' was not found!\"                  ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GeneralDescriptionApi()
_date = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
date_before = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
page = 1 # int | The page to be fetched. Page numbering starts from one. (optional) (default to 1)

try:
    # Gets all the statutory service general descriptions within PTV as a list of ids and names.  General descriptions created/modified after certain date can be fetched by adding date as query string parameter.  General descriptions created/modified before certain date can be fetched by adding dateBefore as query string parameter.
    api_response = api_instance.api_v11_general_description_get(_date=_date, date_before=date_before, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralDescriptionApi->api_v11_general_description_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **date_before** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **page** | **int**| The page to be fetched. Page numbering starts from one. | [optional] [default to 1]

### Return type

[**V3VmOpenApiGuidPage**](V3VmOpenApiGuidPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_general_description_id_get**
> V10VmOpenApiGeneralDescription api_v11_general_description_id_get(id, show_header=show_header)

Fetches all the information related to a single statutory service general description.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GeneralDescriptionApi()
id = 'id_example' # str | Statutory service general description guid (id of the entity) to fetch.
show_header = false # bool |  (optional) (default to false)

try:
    # Fetches all the information related to a single statutory service general description.
    api_response = api_instance.api_v11_general_description_id_get(id, show_header=show_header)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralDescriptionApi->api_v11_general_description_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Statutory service general description guid (id of the entity) to fetch. | 
 **show_header** | **bool**|  | [optional] [default to false]

### Return type

[**V10VmOpenApiGeneralDescription**](V10VmOpenApiGeneralDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_general_description_id_put**
> V10VmOpenApiGeneralDescription api_v11_general_description_id_put(id, body=body)

Updates the defined general description with the data provided as input.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages. Below sample response.  <code>              {                  \"Names\": [                      \"Type - Required value 'Name' was not found!\"                  ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.GeneralDescriptionApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Statutory service general description identifier
body = swagger_client.V10VmOpenApiGeneralDescriptionInBase() # V10VmOpenApiGeneralDescriptionInBase | The general description data. (optional)

try:
    # Updates the defined general description with the data provided as input.
    api_response = api_instance.api_v11_general_description_id_put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralDescriptionApi->api_v11_general_description_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Statutory service general description identifier | 
 **body** | [**V10VmOpenApiGeneralDescriptionInBase**](V10VmOpenApiGeneralDescriptionInBase.md)| The general description data. | [optional] 

### Return type

[**V10VmOpenApiGeneralDescription**](V10VmOpenApiGeneralDescription.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_general_description_list_get**
> list[V10VmOpenApiGeneralDescription] api_v11_general_description_list_get(guids=guids, show_header=show_header)

Fetches all the information related to requested statutory service general descriptions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GeneralDescriptionApi()
guids = 'guids_example' # str | Comma separated list of guids. Max 100 can be added into list. (optional)
show_header = false # bool |  (optional) (default to false)

try:
    # Fetches all the information related to requested statutory service general descriptions.
    api_response = api_instance.api_v11_general_description_list_get(guids=guids, show_header=show_header)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralDescriptionApi->api_v11_general_description_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guids** | **str**| Comma separated list of guids. Max 100 can be added into list. | [optional] 
 **show_header** | **bool**|  | [optional] [default to false]

### Return type

[**list[V10VmOpenApiGeneralDescription]**](V10VmOpenApiGeneralDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_general_description_new_gd_list_get**
> V3VmOpenApiGuidPage api_v11_general_description_new_gd_list_get(page=page)

Gets the new statutory service general descriptions within PTV as a list of ids and names.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GeneralDescriptionApi()
page = 1 # int | The page to be fetched. Page numbering starts from one. (optional) (default to 1)

try:
    # Gets the new statutory service general descriptions within PTV as a list of ids and names.
    api_response = api_instance.api_v11_general_description_new_gd_list_get(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralDescriptionApi->api_v11_general_description_new_gd_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page to be fetched. Page numbering starts from one. | [optional] [default to 1]

### Return type

[**V3VmOpenApiGuidPage**](V3VmOpenApiGuidPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_general_description_post**
> V10VmOpenApiGeneralDescription api_v11_general_description_post(body=body)

Creates a new general description with the data provided as input.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages. Below sample response.  <code>              {                  \"Names\": [                      \"Type - Required value 'Name' was not found!\"                  ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.GeneralDescriptionApi(swagger_client.ApiClient(configuration))
body = swagger_client.V10VmOpenApiGeneralDescriptionIn() # V10VmOpenApiGeneralDescriptionIn | The general description data. (optional)

try:
    # Creates a new general description with the data provided as input.
    api_response = api_instance.api_v11_general_description_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralDescriptionApi->api_v11_general_description_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V10VmOpenApiGeneralDescriptionIn**](V10VmOpenApiGeneralDescriptionIn.md)| The general description data. | [optional] 

### Return type

[**V10VmOpenApiGeneralDescription**](V10VmOpenApiGeneralDescription.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

