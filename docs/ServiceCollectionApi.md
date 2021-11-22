# swagger_client.ServiceCollectionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v11_service_collection_get**](ServiceCollectionApi.md#api_v11_service_collection_get) | **GET** /api/v11/ServiceCollection | Gets all the published service collections within PTV as a list of service collection ids and names.  Service collections created after certain date can be fetched by adding date as query string parameter.  Service collections created before certain date can be fetched by adding dateBefore as query string parameter.  Archived items can be fetched by setting parameter archived to true.
[**api_v11_service_collection_id_get**](ServiceCollectionApi.md#api_v11_service_collection_id_get) | **GET** /api/v11/ServiceCollection/{id} | Fetches all the information related to a single service collection.
[**api_v11_service_collection_id_put**](ServiceCollectionApi.md#api_v11_service_collection_id_put) | **PUT** /api/v11/ServiceCollection/{id} | Updates the defined service collection with the data provided as input.
[**api_v11_service_collection_organization_get**](ServiceCollectionApi.md#api_v11_service_collection_organization_get) | **GET** /api/v11/ServiceCollection/organization | Gets the published service collections within PTV related to certain organization. Either organizationId or code needs to be added as a parameter.
[**api_v11_service_collection_post**](ServiceCollectionApi.md#api_v11_service_collection_post) | **POST** /api/v11/ServiceCollection | Creates a new service collection with the data provided as input.
[**api_v11_service_collection_source_id_source_id_put**](ServiceCollectionApi.md#api_v11_service_collection_source_id_source_id_put) | **PUT** /api/v11/ServiceCollection/sourceId/{sourceId} | Updates the defined service collection with the data provided as input.

# **api_v11_service_collection_get**
> V3VmOpenApiGuidPage api_v11_service_collection_get(_date=_date, date_before=date_before, page=page, archived=archived)

Gets all the published service collections within PTV as a list of service collection ids and names.  Service collections created after certain date can be fetched by adding date as query string parameter.  Service collections created before certain date can be fetched by adding dateBefore as query string parameter.  Archived items can be fetched by setting parameter archived to true.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"date\": [                      \"The value 'rfsd' is not valid for Nullable`1.\",                      \"The date parameter is invalid.\"                  ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceCollectionApi()
_date = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
date_before = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC) (optional)
page = 1 # int | The page number to be fetched. (optional) (default to 1)
archived = false # bool | Get archived items by setting archived to true. (optional) (default to false)

try:
    # Gets all the published service collections within PTV as a list of service collection ids and names.  Service collections created after certain date can be fetched by adding date as query string parameter.  Service collections created before certain date can be fetched by adding dateBefore as query string parameter.  Archived items can be fetched by setting parameter archived to true.
    api_response = api_instance.api_v11_service_collection_get(_date=_date, date_before=date_before, page=page, archived=archived)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceCollectionApi->api_v11_service_collection_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **date_before** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC) | [optional] 
 **page** | **int**| The page number to be fetched. | [optional] [default to 1]
 **archived** | **bool**| Get archived items by setting archived to true. | [optional] [default to false]

### Return type

[**V3VmOpenApiGuidPage**](V3VmOpenApiGuidPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_collection_id_get**
> V11VmOpenApiServiceCollection api_v11_service_collection_id_get(id, show_header=show_header)

Fetches all the information related to a single service collection.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"id\": [                      \"Guid should contain 32 digits with 4 dashes (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx).\"                  ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceCollectionApi()
id = 'id_example' # str | Guid
show_header = false # bool |  (optional) (default to false)

try:
    # Fetches all the information related to a single service collection.
    api_response = api_instance.api_v11_service_collection_id_get(id, show_header=show_header)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceCollectionApi->api_v11_service_collection_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Guid | 
 **show_header** | **bool**|  | [optional] [default to false]

### Return type

[**V11VmOpenApiServiceCollection**](V11VmOpenApiServiceCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_collection_id_put**
> V11VmOpenApiServiceCollection api_v11_service_collection_id_put(id, body=body)

Updates the defined service collection with the data provided as input.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"ServiceCollectionNames[0].Type\": [                      \"The Type field is required.\"                  ]              }              </code>

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
api_instance = swagger_client.ServiceCollectionApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Service collection identifier
body = swagger_client.V11VmOpenApiServiceCollectionInBase() # V11VmOpenApiServiceCollectionInBase | The service collection data (optional)

try:
    # Updates the defined service collection with the data provided as input.
    api_response = api_instance.api_v11_service_collection_id_put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceCollectionApi->api_v11_service_collection_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Service collection identifier | 
 **body** | [**V11VmOpenApiServiceCollectionInBase**](V11VmOpenApiServiceCollectionInBase.md)| The service collection data | [optional] 

### Return type

[**V11VmOpenApiServiceCollection**](V11VmOpenApiServiceCollection.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_collection_organization_get**
> V10VmOpenApiServiceCollectionsWithPaging api_v11_service_collection_organization_get(organization_id=organization_id, code=code, page=page)

Gets the published service collections within PTV related to certain organization. Either organizationId or code needs to be added as a parameter.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"id\": [                      \"Guid should contain 32 digits with 4 dashes (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx).\"                  ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceCollectionApi()
organization_id = 'organization_id_example' # str | Organization guid. (optional)
code = 'code_example' # str | Organization business code. (optional)
page = 1 # int | The page to be fetched. (optional) (default to 1)

try:
    # Gets the published service collections within PTV related to certain organization. Either organizationId or code needs to be added as a parameter.
    api_response = api_instance.api_v11_service_collection_organization_get(organization_id=organization_id, code=code, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceCollectionApi->api_v11_service_collection_organization_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization guid. | [optional] 
 **code** | **str**| Organization business code. | [optional] 
 **page** | **int**| The page to be fetched. | [optional] [default to 1]

### Return type

[**V10VmOpenApiServiceCollectionsWithPaging**](V10VmOpenApiServiceCollectionsWithPaging.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_collection_post**
> V11VmOpenApiServiceCollection api_v11_service_collection_post(body=body)

Creates a new service collection with the data provided as input.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"ServiceCollectionNames\": [                      \"Type - Required value 'Name' was not found!\"                  ]              }              </code>

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
api_instance = swagger_client.ServiceCollectionApi(swagger_client.ApiClient(configuration))
body = swagger_client.V11VmOpenApiServiceCollectionIn() # V11VmOpenApiServiceCollectionIn | The service collection data. (optional)

try:
    # Creates a new service collection with the data provided as input.
    api_response = api_instance.api_v11_service_collection_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceCollectionApi->api_v11_service_collection_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V11VmOpenApiServiceCollectionIn**](V11VmOpenApiServiceCollectionIn.md)| The service collection data. | [optional] 

### Return type

[**V11VmOpenApiServiceCollection**](V11VmOpenApiServiceCollection.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_collection_source_id_source_id_put**
> V11VmOpenApiServiceCollection api_v11_service_collection_source_id_source_id_put(source_id, body=body)

Updates the defined service collection with the data provided as input.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"ServiceCollectionNames[0].Type\": [                      \"The Type field is required.\"                  ]              }              </code>

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
api_instance = swagger_client.ServiceCollectionApi(swagger_client.ApiClient(configuration))
source_id = 'source_id_example' # str | External source identifier
body = swagger_client.V11VmOpenApiServiceCollectionInBase() # V11VmOpenApiServiceCollectionInBase | The service collection data (optional)

try:
    # Updates the defined service collection with the data provided as input.
    api_response = api_instance.api_v11_service_collection_source_id_source_id_put(source_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceCollectionApi->api_v11_service_collection_source_id_source_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| External source identifier | 
 **body** | [**V11VmOpenApiServiceCollectionInBase**](V11VmOpenApiServiceCollectionInBase.md)| The service collection data | [optional] 

### Return type

[**V11VmOpenApiServiceCollection**](V11VmOpenApiServiceCollection.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

