# swagger_client.ConnectionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v11_connection_asti_service_channel_id_service_channel_id_put**](ConnectionApi.md#api_v11_connection_asti_service_channel_id_service_channel_id_put) | **PUT** /api/v11/Connection/ASTI/serviceChannelId/{serviceChannelId} | Updates connections between a service channel and services with extra data.  Request includes services for one certain service channel and missing ASTI connections are removed. Regular connections are left as they are.  To delete all ASTI connections for a service channel set &#x27;deleteAllServiceRelations&#x27; property to true.  This is special endpoint for ASTI and users need to have special access right to be able use it.
[**api_v11_connection_asti_service_id_service_id_put**](ConnectionApi.md#api_v11_connection_asti_service_id_service_id_put) | **PUT** /api/v11/Connection/ASTI/serviceId/{serviceId} | Updates connections between a service and service channels with extra data.  Request includes service channels for one certain service and missing ASTI connections are removed. Regular connections are left as they are.  To delete all ASTI service channel connections for a service, set &#x27;deleteAllChannelRelations&#x27; property to true.  This is special endpoint for ASTI and users need to have special access right to be able use it.
[**api_v11_connection_asti_service_source_id_service_source_id_put**](ConnectionApi.md#api_v11_connection_asti_service_source_id_service_source_id_put) | **PUT** /api/v11/Connection/ASTI/serviceSourceId/{serviceSourceId} | Updates connections between a service and service channels with extra data. External source ids are used.  Request includes service channels for one certain service and missing ASTI connections are removed. Regular connections are left as they are.  To delete all ASTI service channel connections for a service set &#x27;deleteAllChannelRelations&#x27; property to true.  This is special endpoint for ASTI and users need to have special access right to be able use it.
[**api_v11_connection_post**](ConnectionApi.md#api_v11_connection_post) | **POST** /api/v11/Connection | Creates a connections between services and service channels with extra data.
[**api_v11_connection_service_id_service_id_put**](ConnectionApi.md#api_v11_connection_service_id_service_id_put) | **PUT** /api/v11/Connection/serviceId/{serviceId} | Updates connections between a service and service channels with extra data.  Request includes service channels for one certain service so regular connections missing from request are removed.  ASTI connections are left as they are.  To delete all regular service channel connections for a service, set &#x27;deleteAllChannelRelations&#x27; property to true.
[**api_v11_connection_service_source_id_service_source_id_put**](ConnectionApi.md#api_v11_connection_service_source_id_service_source_id_put) | **PUT** /api/v11/Connection/serviceSourceId/{serviceSourceId} | Updates connections between a service and service channels with extra data. External source ids are used.  Request includes service channels for one certain service so service channels missing from request are removed.  To delete all service channel connections for a service set &#x27;deleteAllChannelRelations&#x27; property to true.  ASTI connections are not removed - data for those connections can be updated though.
[**api_v11_connection_source_post**](ConnectionApi.md#api_v11_connection_source_post) | **POST** /api/v11/Connection/Source | Creates a connections between services and service channels with extra data. External source ids are used.

# **api_v11_connection_asti_service_channel_id_service_channel_id_put**
> V11VmOpenApiServiceChannels api_v11_connection_asti_service_channel_id_service_channel_id_put(service_channel_id, body=body)

Updates connections between a service channel and services with extra data.  Request includes services for one certain service channel and missing ASTI connections are removed. Regular connections are left as they are.  To delete all ASTI connections for a service channel set 'deleteAllServiceRelations' property to true.  This is special endpoint for ASTI and users need to have special access right to be able use it.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"Service with id '00000000-0000-0000-0000-00000000' not found!\"              }              </code>

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
api_instance = swagger_client.ConnectionApi(swagger_client.ApiClient(configuration))
service_channel_id = 'service_channel_id_example' # str | Service channel identifier
body = swagger_client.V11VmOpenApiChannelServicesIn() # V11VmOpenApiChannelServicesIn | A list of service channels. (optional)

try:
    # Updates connections between a service channel and services with extra data.  Request includes services for one certain service channel and missing ASTI connections are removed. Regular connections are left as they are.  To delete all ASTI connections for a service channel set 'deleteAllServiceRelations' property to true.  This is special endpoint for ASTI and users need to have special access right to be able use it.
    api_response = api_instance.api_v11_connection_asti_service_channel_id_service_channel_id_put(service_channel_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->api_v11_connection_asti_service_channel_id_service_channel_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_channel_id** | **str**| Service channel identifier | 
 **body** | [**V11VmOpenApiChannelServicesIn**](V11VmOpenApiChannelServicesIn.md)| A list of service channels. | [optional] 

### Return type

[**V11VmOpenApiServiceChannels**](V11VmOpenApiServiceChannels.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_connection_asti_service_id_service_id_put**
> V11VmOpenApiService api_v11_connection_asti_service_id_service_id_put(service_id, body=body)

Updates connections between a service and service channels with extra data.  Request includes service channels for one certain service and missing ASTI connections are removed. Regular connections are left as they are.  To delete all ASTI service channel connections for a service, set 'deleteAllChannelRelations' property to true.  This is special endpoint for ASTI and users need to have special access right to be able use it.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"Service with id '00000000-0000-0000-0000-00000000' not found!\"              }              </code>

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
api_instance = swagger_client.ConnectionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | Service identifier
body = swagger_client.V11VmOpenApiServiceAndChannelRelationAstiInBase() # V11VmOpenApiServiceAndChannelRelationAstiInBase | A list of service channels. (optional)

try:
    # Updates connections between a service and service channels with extra data.  Request includes service channels for one certain service and missing ASTI connections are removed. Regular connections are left as they are.  To delete all ASTI service channel connections for a service, set 'deleteAllChannelRelations' property to true.  This is special endpoint for ASTI and users need to have special access right to be able use it.
    api_response = api_instance.api_v11_connection_asti_service_id_service_id_put(service_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->api_v11_connection_asti_service_id_service_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Service identifier | 
 **body** | [**V11VmOpenApiServiceAndChannelRelationAstiInBase**](V11VmOpenApiServiceAndChannelRelationAstiInBase.md)| A list of service channels. | [optional] 

### Return type

[**V11VmOpenApiService**](V11VmOpenApiService.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_connection_asti_service_source_id_service_source_id_put**
> V11VmOpenApiService api_v11_connection_asti_service_source_id_service_source_id_put(service_source_id, body=body)

Updates connections between a service and service channels with extra data. External source ids are used.  Request includes service channels for one certain service and missing ASTI connections are removed. Regular connections are left as they are.  To delete all ASTI service channel connections for a service set 'deleteAllChannelRelations' property to true.  This is special endpoint for ASTI and users need to have special access right to be able use it.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"Service with id '00000000-0000-0000-0000-00000000' not found!\"              }              </code>

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
api_instance = swagger_client.ConnectionApi(swagger_client.ApiClient(configuration))
service_source_id = 'service_source_id_example' # str | External source identifier for service
body = swagger_client.V11VmOpenApiServiceAndChannelRelationBySourceAsti() # V11VmOpenApiServiceAndChannelRelationBySourceAsti | A list of service channels. (optional)

try:
    # Updates connections between a service and service channels with extra data. External source ids are used.  Request includes service channels for one certain service and missing ASTI connections are removed. Regular connections are left as they are.  To delete all ASTI service channel connections for a service set 'deleteAllChannelRelations' property to true.  This is special endpoint for ASTI and users need to have special access right to be able use it.
    api_response = api_instance.api_v11_connection_asti_service_source_id_service_source_id_put(service_source_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->api_v11_connection_asti_service_source_id_service_source_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_source_id** | **str**| External source identifier for service | 
 **body** | [**V11VmOpenApiServiceAndChannelRelationBySourceAsti**](V11VmOpenApiServiceAndChannelRelationBySourceAsti.md)| A list of service channels. | [optional] 

### Return type

[**V11VmOpenApiService**](V11VmOpenApiService.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_connection_post**
> list[str] api_v11_connection_post(body=body)

Creates a connections between services and service channels with extra data.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"Service with id '00000000-0000-0000-0000-00000000' not found!\"              }              </code>

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
api_instance = swagger_client.ConnectionApi(swagger_client.ApiClient(configuration))
body = [swagger_client.V11VmOpenApiServiceAndChannelIn()] # list[V11VmOpenApiServiceAndChannelIn] | A list of services and service channels. (optional)

try:
    # Creates a connections between services and service channels with extra data.
    api_response = api_instance.api_v11_connection_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->api_v11_connection_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[V11VmOpenApiServiceAndChannelIn]**](V11VmOpenApiServiceAndChannelIn.md)| A list of services and service channels. | [optional] 

### Return type

**list[str]**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_connection_service_id_service_id_put**
> V11VmOpenApiService api_v11_connection_service_id_service_id_put(service_id, body=body)

Updates connections between a service and service channels with extra data.  Request includes service channels for one certain service so regular connections missing from request are removed.  ASTI connections are left as they are.  To delete all regular service channel connections for a service, set 'deleteAllChannelRelations' property to true.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"Service with id '00000000-0000-0000-0000-00000000' not found!\"              }              </code>

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
api_instance = swagger_client.ConnectionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | Service identifier
body = swagger_client.V11VmOpenApiServiceAndChannelRelationInBase() # V11VmOpenApiServiceAndChannelRelationInBase | A list of service channels. (optional)

try:
    # Updates connections between a service and service channels with extra data.  Request includes service channels for one certain service so regular connections missing from request are removed.  ASTI connections are left as they are.  To delete all regular service channel connections for a service, set 'deleteAllChannelRelations' property to true.
    api_response = api_instance.api_v11_connection_service_id_service_id_put(service_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->api_v11_connection_service_id_service_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Service identifier | 
 **body** | [**V11VmOpenApiServiceAndChannelRelationInBase**](V11VmOpenApiServiceAndChannelRelationInBase.md)| A list of service channels. | [optional] 

### Return type

[**V11VmOpenApiService**](V11VmOpenApiService.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_connection_service_source_id_service_source_id_put**
> V11VmOpenApiService api_v11_connection_service_source_id_service_source_id_put(service_source_id, body=body)

Updates connections between a service and service channels with extra data. External source ids are used.  Request includes service channels for one certain service so service channels missing from request are removed.  To delete all service channel connections for a service set 'deleteAllChannelRelations' property to true.  ASTI connections are not removed - data for those connections can be updated though.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"Service with id '00000000-0000-0000-0000-00000000' not found!\"              }              </code>

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
api_instance = swagger_client.ConnectionApi(swagger_client.ApiClient(configuration))
service_source_id = 'service_source_id_example' # str | External source identifier for service
body = swagger_client.V11VmOpenApiServiceAndChannelRelationBySourceInBase() # V11VmOpenApiServiceAndChannelRelationBySourceInBase | A list of service channels. (optional)

try:
    # Updates connections between a service and service channels with extra data. External source ids are used.  Request includes service channels for one certain service so service channels missing from request are removed.  To delete all service channel connections for a service set 'deleteAllChannelRelations' property to true.  ASTI connections are not removed - data for those connections can be updated though.
    api_response = api_instance.api_v11_connection_service_source_id_service_source_id_put(service_source_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->api_v11_connection_service_source_id_service_source_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_source_id** | **str**| External source identifier for service | 
 **body** | [**V11VmOpenApiServiceAndChannelRelationBySourceInBase**](V11VmOpenApiServiceAndChannelRelationBySourceInBase.md)| A list of service channels. | [optional] 

### Return type

[**V11VmOpenApiService**](V11VmOpenApiService.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_connection_source_post**
> list[str] api_v11_connection_source_post(body=body)

Creates a connections between services and service channels with extra data. External source ids are used.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"Service with id '00000000-0000-0000-0000-00000000' not found!\"              }              </code>

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
api_instance = swagger_client.ConnectionApi(swagger_client.ApiClient(configuration))
body = [swagger_client.V11VmOpenApiServiceAndChannelRelationBySource()] # list[V11VmOpenApiServiceAndChannelRelationBySource] | A list of services and service channels. (optional)

try:
    # Creates a connections between services and service channels with extra data. External source ids are used.
    api_response = api_instance.api_v11_connection_source_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->api_v11_connection_source_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[V11VmOpenApiServiceAndChannelRelationBySource]**](V11VmOpenApiServiceAndChannelRelationBySource.md)| A list of services and service channels. | [optional] 

### Return type

**list[str]**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

