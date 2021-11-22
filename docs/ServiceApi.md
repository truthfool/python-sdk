# swagger_client.ServiceApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v11_service_active_get**](ServiceApi.md#api_v11_service_active_get) | **GET** /api/v11/Service/active | Gets all services within PTV as a list of service ids and names. Also services with draft and modified versions are included.  Services created/modified after certain date can be fetched by adding date as query string parameter.  Services created/modified before certain date can be fetched by adding dateBefore as query string parameter.  NOTE! This is a restricted endpoint.
[**api_v11_service_active_id_get**](ServiceApi.md#api_v11_service_active_id_get) | **GET** /api/v11/Service/active/{id} | Fetches all the information related to a single service. Also services with only draft or modified versions are returned.  NOTE! This is a restricted endpoint.
[**api_v11_service_archived_list_get**](ServiceApi.md#api_v11_service_archived_list_get) | **GET** /api/v11/Service/archived/list | Fetches automatically/manually archived services
[**api_v11_service_area_area_code_code_get**](ServiceApi.md#api_v11_service_area_area_code_code_get) | **GET** /api/v11/Service/area/{area}/code/{code} | Gets a list of published services related to defined area and code.  Services created/modified after certain date can be fetched by adding date as query string parameter.  Services created/modified before certain date can be fetched by adding dateBefore as query string parameter.
[**api_v11_service_get**](ServiceApi.md#api_v11_service_get) | **GET** /api/v11/Service | Gets all the published services within PTV as a list of service ids and names.  Services created/modified after certain date can be fetched by adding date as query string parameter.  Services created/modified before certain date can be fetched by adding dateBefore as query string parameter.  Archived items can be fetched by setting status parameter as &#x27;Archived&#x27; and withdrawn items can be fetched by setting status parameter as &#x27;Withdrawn&#x27;.
[**api_v11_service_id_get**](ServiceApi.md#api_v11_service_id_get) | **GET** /api/v11/Service/{id} | Fetches all the information related to a single service.
[**api_v11_service_id_put**](ServiceApi.md#api_v11_service_id_put) | **PUT** /api/v11/Service/{id} | Updates the defined service with the data provided as input.
[**api_v11_service_industrial_class_get**](ServiceApi.md#api_v11_service_industrial_class_get) | **GET** /api/v11/Service/industrialClass | Gets a list of published services for defined industrial class.  Services created/modified after certain date can be fetched by adding date as query string parameter.  Services created/modified before certain date can be fetched by adding dateBefore as query string parameter.
[**api_v11_service_list_area_area_code_code_get**](ServiceApi.md#api_v11_service_list_area_area_code_code_get) | **GET** /api/v11/Service/list/area/{area}/code/{code} | Fetches all the information of published services related to certain area and code.  User can set serviceWithGD parameter to true to include possible attached general description data into the service data.  In this case general description related descriptions are marked with prefix &#x27;GD_&#x27; to separate them from service related descriptions.
[**api_v11_service_list_get**](ServiceApi.md#api_v11_service_list_get) | **GET** /api/v11/Service/list | Fetches all the information related to requested services.
[**api_v11_service_list_organization_get**](ServiceApi.md#api_v11_service_list_organization_get) | **GET** /api/v11/Service/list/organization | Fetches all the information of the services related to certain organization. Either organizationId, code or oid needs to be added as a parameter.  User can also set serviceWithGD parameter to true to include possible attached general description data into the service data.  In this case general description related descriptions are marked with prefix &#x27;GD_&#x27; to separate them from service related descriptions.
[**api_v11_service_post**](ServiceApi.md#api_v11_service_post) | **POST** /api/v11/Service | Creates a new service with the data provided as input.
[**api_v11_service_service_channel_service_channel_id_get**](ServiceApi.md#api_v11_service_service_channel_service_channel_id_get) | **GET** /api/v11/Service/serviceChannel/{serviceChannelId} | Gets a list of published services for defined service channel.  Services joined to service channel after certain date can be fetched by adding date as query string parameter.  Services joined to service channel before certain date can be fetched by adding dateBefore as query string parameter.
[**api_v11_service_service_class_get**](ServiceApi.md#api_v11_service_service_class_get) | **GET** /api/v11/Service/serviceClass | Gets a list of published services for defined service class.  Services created/modified after certain date can be fetched by adding date as query string parameter.  Services created/modified before certain date can be fetched by adding dateBefore as query string parameter.
[**api_v11_service_service_with_gd_id_get**](ServiceApi.md#api_v11_service_service_with_gd_id_get) | **GET** /api/v11/Service/serviceWithGD/{id} | Fetches all the information related to a single service. If general description is attached also general description data is returned within the service data.  General description related descriptions are marked with prefix &#x27;GD_&#x27; to separate them from service related descriptions.
[**api_v11_service_service_with_gd_list_get**](ServiceApi.md#api_v11_service_service_with_gd_list_get) | **GET** /api/v11/Service/serviceWithGD/list | Fetches all the information related to requests services. If general description is attached to a service also general description data is returned within the service data.  General description related descriptions are marked with prefix &#x27;GD_&#x27; to separate them from service related descriptions.
[**api_v11_service_source_id_source_id_put**](ServiceApi.md#api_v11_service_source_id_source_id_put) | **PUT** /api/v11/Service/sourceId/{sourceId} | Updates the defined service with the data provided as input.
[**api_v11_service_target_group_get**](ServiceApi.md#api_v11_service_target_group_get) | **GET** /api/v11/Service/targetGroup | Gets a list of published services for defined target group.  Services created/modified after certain date can be fetched by adding date as query string parameter.  Services created/modified before certain date can be fetched by adding dateBefore as query string parameter.
[**api_v11_service_type_type_get**](ServiceApi.md#api_v11_service_type_type_get) | **GET** /api/v11/Service/type/{type} | Gets a list of published services of defined service type.  Services created/modified after certain date can be fetched by adding date as query string parameter.  Services created/modified before certain date can be fetched by adding dateBefore as query string parameter.

# **api_v11_service_active_get**
> V3VmOpenApiGuidPage api_v11_service_active_get(_date=_date, date_before=date_before, page=page)

Gets all services within PTV as a list of service ids and names. Also services with draft and modified versions are included.  Services created/modified after certain date can be fetched by adding date as query string parameter.  Services created/modified before certain date can be fetched by adding dateBefore as query string parameter.  NOTE! This is a restricted endpoint.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"date\": [                      \"The value 'rfsd' is not valid for Nullable`1.\",                      \"The date parameter is invalid.\"                  ]              }              </code>

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
api_instance = swagger_client.ServiceApi(swagger_client.ApiClient(configuration))
_date = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
date_before = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
page = 1 # int | The page number to be fetched. (optional) (default to 1)

try:
    # Gets all services within PTV as a list of service ids and names. Also services with draft and modified versions are included.  Services created/modified after certain date can be fetched by adding date as query string parameter.  Services created/modified before certain date can be fetched by adding dateBefore as query string parameter.  NOTE! This is a restricted endpoint.
    api_response = api_instance.api_v11_service_active_get(_date=_date, date_before=date_before, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->api_v11_service_active_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **date_before** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **page** | **int**| The page number to be fetched. | [optional] [default to 1]

### Return type

[**V3VmOpenApiGuidPage**](V3VmOpenApiGuidPage.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_active_id_get**
> V11VmOpenApiService api_v11_service_active_id_get(id, show_header=show_header)

Fetches all the information related to a single service. Also services with only draft or modified versions are returned.  NOTE! This is a restricted endpoint.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"id\": [                      \"Guid should contain 32 digits with 4 dashes (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx).\"                  ]              }              </code>

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
api_instance = swagger_client.ServiceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Guid
show_header = false # bool |  (optional) (default to false)

try:
    # Fetches all the information related to a single service. Also services with only draft or modified versions are returned.  NOTE! This is a restricted endpoint.
    api_response = api_instance.api_v11_service_active_id_get(id, show_header=show_header)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->api_v11_service_active_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Guid | 
 **show_header** | **bool**|  | [optional] [default to false]

### Return type

[**V11VmOpenApiService**](V11VmOpenApiService.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_archived_list_get**
> list[VmOpenApiArchivedServiceBase] api_v11_service_archived_list_get(archiving_type, organization_id, take, min_archiving_date=min_archiving_date, max_archiving_date=max_archiving_date, skip=skip)

Fetches automatically/manually archived services

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"id\": [                      \"Guid should contain 32 digits with 4 dashes (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx).\"                  ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()
archiving_type = swagger_client.ArchivingType() # ArchivingType | How service was archived.
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Return only services belonging to this organization.
take = 56 # int | How many services to return.
min_archiving_date = '2013-10-20T19:20:30+01:00' # datetime | Return only services archived after this time.  ISO 8601 format (e.g. 2020-10-26T05:24:11+00:00). (optional)
max_archiving_date = '2013-10-20T19:20:30+01:00' # datetime | Return only services archived before this time.  ISO 8601 format (e.g. 2020-10-26T05:24:11+00:00). (optional)
skip = 56 # int | Skip the first n services. (optional)

try:
    # Fetches automatically/manually archived services
    api_response = api_instance.api_v11_service_archived_list_get(archiving_type, organization_id, take, min_archiving_date=min_archiving_date, max_archiving_date=max_archiving_date, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->api_v11_service_archived_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **archiving_type** | [**ArchivingType**](.md)| How service was archived. | 
 **organization_id** | [**str**](.md)| Return only services belonging to this organization. | 
 **take** | **int**| How many services to return. | 
 **min_archiving_date** | **datetime**| Return only services archived after this time.  ISO 8601 format (e.g. 2020-10-26T05:24:11+00:00). | [optional] 
 **max_archiving_date** | **datetime**| Return only services archived before this time.  ISO 8601 format (e.g. 2020-10-26T05:24:11+00:00). | [optional] 
 **skip** | **int**| Skip the first n services. | [optional] 

### Return type

[**list[VmOpenApiArchivedServiceBase]**](VmOpenApiArchivedServiceBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_area_area_code_code_get**
> V3VmOpenApiGuidPage api_v11_service_area_area_code_code_get(area, code, include_whole_country=include_whole_country, _date=_date, date_before=date_before, page=page)

Gets a list of published services related to defined area and code.  Services created/modified after certain date can be fetched by adding date as query string parameter.  Services created/modified before certain date can be fetched by adding dateBefore as query string parameter.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()
area = 'area_example' # str | The area type
code = 'code_example' # str | The code related to area
include_whole_country = true # bool | Indicates if services marked for whole country (or whole country except Åland) should be included. (optional)
_date = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
date_before = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
page = 1 # int | The page number to be fetched. (optional) (default to 1)

try:
    # Gets a list of published services related to defined area and code.  Services created/modified after certain date can be fetched by adding date as query string parameter.  Services created/modified before certain date can be fetched by adding dateBefore as query string parameter.
    api_response = api_instance.api_v11_service_area_area_code_code_get(area, code, include_whole_country=include_whole_country, _date=_date, date_before=date_before, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->api_v11_service_area_area_code_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area** | **str**| The area type | 
 **code** | **str**| The code related to area | 
 **include_whole_country** | **bool**| Indicates if services marked for whole country (or whole country except Åland) should be included. | [optional] 
 **_date** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **date_before** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **page** | **int**| The page number to be fetched. | [optional] [default to 1]

### Return type

[**V3VmOpenApiGuidPage**](V3VmOpenApiGuidPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_get**
> V3VmOpenApiGuidPage api_v11_service_get(_date=_date, date_before=date_before, page=page, status=status)

Gets all the published services within PTV as a list of service ids and names.  Services created/modified after certain date can be fetched by adding date as query string parameter.  Services created/modified before certain date can be fetched by adding dateBefore as query string parameter.  Archived items can be fetched by setting status parameter as 'Archived' and withdrawn items can be fetched by setting status parameter as 'Withdrawn'.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"date\": [                      \"The value 'rfsd' is not valid for Nullable`1.\",                      \"The date parameter is invalid.\"                  ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()
_date = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
date_before = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
page = 1 # int | The page number to be fetched. (optional) (default to 1)
status = 'Published' # str | Set status to get items either in published, archived or withdrawn state. (optional) (default to Published)

try:
    # Gets all the published services within PTV as a list of service ids and names.  Services created/modified after certain date can be fetched by adding date as query string parameter.  Services created/modified before certain date can be fetched by adding dateBefore as query string parameter.  Archived items can be fetched by setting status parameter as 'Archived' and withdrawn items can be fetched by setting status parameter as 'Withdrawn'.
    api_response = api_instance.api_v11_service_get(_date=_date, date_before=date_before, page=page, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->api_v11_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **date_before** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **page** | **int**| The page number to be fetched. | [optional] [default to 1]
 **status** | **str**| Set status to get items either in published, archived or withdrawn state. | [optional] [default to Published]

### Return type

[**V3VmOpenApiGuidPage**](V3VmOpenApiGuidPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_id_get**
> V11VmOpenApiService api_v11_service_id_get(id, show_header=show_header)

Fetches all the information related to a single service.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"id\": [                      \"Guid should contain 32 digits with 4 dashes (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx).\"                  ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()
id = 'id_example' # str | Guid
show_header = false # bool |  (optional) (default to false)

try:
    # Fetches all the information related to a single service.
    api_response = api_instance.api_v11_service_id_get(id, show_header=show_header)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->api_v11_service_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Guid | 
 **show_header** | **bool**|  | [optional] [default to false]

### Return type

[**V11VmOpenApiService**](V11VmOpenApiService.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_id_put**
> V11VmOpenApiService api_v11_service_id_put(id, body=body, attach_proposed_channels=attach_proposed_channels)

Updates the defined service with the data provided as input.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"ServiceNames[0].Type\": [                      \"The Type field is required.\"                  ]              }              </code>

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
api_instance = swagger_client.ServiceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Service identifier
body = swagger_client.V9VmOpenApiServiceInBase() # V9VmOpenApiServiceInBase | The service data (optional)
attach_proposed_channels = true # bool | Indicates if service channels attached into general description should automatically be attached into the service. (optional)

try:
    # Updates the defined service with the data provided as input.
    api_response = api_instance.api_v11_service_id_put(id, body=body, attach_proposed_channels=attach_proposed_channels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->api_v11_service_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Service identifier | 
 **body** | [**V9VmOpenApiServiceInBase**](V9VmOpenApiServiceInBase.md)| The service data | [optional] 
 **attach_proposed_channels** | **bool**| Indicates if service channels attached into general description should automatically be attached into the service. | [optional] 

### Return type

[**V11VmOpenApiService**](V11VmOpenApiService.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_industrial_class_get**
> V3VmOpenApiGuidPage api_v11_service_industrial_class_get(uri=uri, _date=_date, date_before=date_before, page=page)

Gets a list of published services for defined industrial class.  Services created/modified after certain date can be fetched by adding date as query string parameter.  Services created/modified before certain date can be fetched by adding dateBefore as query string parameter.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()
uri = 'uri_example' # str | Industrial class uri, e.g. http://www.stat.fi/meta/luokitukset/toimiala/001-2008/46909 (optional)
_date = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
date_before = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
page = 1 # int | The page number to be fetched. (optional) (default to 1)

try:
    # Gets a list of published services for defined industrial class.  Services created/modified after certain date can be fetched by adding date as query string parameter.  Services created/modified before certain date can be fetched by adding dateBefore as query string parameter.
    api_response = api_instance.api_v11_service_industrial_class_get(uri=uri, _date=_date, date_before=date_before, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->api_v11_service_industrial_class_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Industrial class uri, e.g. http://www.stat.fi/meta/luokitukset/toimiala/001-2008/46909 | [optional] 
 **_date** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **date_before** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **page** | **int**| The page number to be fetched. | [optional] [default to 1]

### Return type

[**V3VmOpenApiGuidPage**](V3VmOpenApiGuidPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_list_area_area_code_code_get**
> V11VmOpenApiServicesWithPaging api_v11_service_list_area_area_code_code_get(area, code, include_whole_country=include_whole_country, service_with_gd=service_with_gd, page=page, show_header=show_header)

Fetches all the information of published services related to certain area and code.  User can set serviceWithGD parameter to true to include possible attached general description data into the service data.  In this case general description related descriptions are marked with prefix 'GD_' to separate them from service related descriptions.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"id\": [                      \"Guid should contain 32 digits with 4 dashes (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx).\"                  ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()
area = 'area_example' # str | The area type.
code = 'code_example' # str | The code related to area.
include_whole_country = false # bool | Indicates if services marked to provide services for whole country (or whole country except Åland) should be included. (optional) (default to false)
service_with_gd = false # bool | Indicates if general description data should be attached within the service data. (optional) (default to false)
page = 1 # int | The page to be fetched. (optional) (default to 1)
show_header = false # bool |  (optional) (default to false)

try:
    # Fetches all the information of published services related to certain area and code.  User can set serviceWithGD parameter to true to include possible attached general description data into the service data.  In this case general description related descriptions are marked with prefix 'GD_' to separate them from service related descriptions.
    api_response = api_instance.api_v11_service_list_area_area_code_code_get(area, code, include_whole_country=include_whole_country, service_with_gd=service_with_gd, page=page, show_header=show_header)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->api_v11_service_list_area_area_code_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area** | **str**| The area type. | 
 **code** | **str**| The code related to area. | 
 **include_whole_country** | **bool**| Indicates if services marked to provide services for whole country (or whole country except Åland) should be included. | [optional] [default to false]
 **service_with_gd** | **bool**| Indicates if general description data should be attached within the service data. | [optional] [default to false]
 **page** | **int**| The page to be fetched. | [optional] [default to 1]
 **show_header** | **bool**|  | [optional] [default to false]

### Return type

[**V11VmOpenApiServicesWithPaging**](V11VmOpenApiServicesWithPaging.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_list_get**
> list[V11VmOpenApiService] api_v11_service_list_get(guids=guids, show_header=show_header)

Fetches all the information related to requested services.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"id\": [                      \"Guid should contain 32 digits with 4 dashes (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx).\"                  ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()
guids = 'guids_example' # str | Comma separated list of guids. Max 100 can be added into list. (optional)
show_header = false # bool |  (optional) (default to false)

try:
    # Fetches all the information related to requested services.
    api_response = api_instance.api_v11_service_list_get(guids=guids, show_header=show_header)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->api_v11_service_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guids** | **str**| Comma separated list of guids. Max 100 can be added into list. | [optional] 
 **show_header** | **bool**|  | [optional] [default to false]

### Return type

[**list[V11VmOpenApiService]**](V11VmOpenApiService.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_list_organization_get**
> V11VmOpenApiServicesWithPaging api_v11_service_list_organization_get(organization_id=organization_id, code=code, oid=oid, service_with_gd=service_with_gd, page=page, show_header=show_header)

Fetches all the information of the services related to certain organization. Either organizationId, code or oid needs to be added as a parameter.  User can also set serviceWithGD parameter to true to include possible attached general description data into the service data.  In this case general description related descriptions are marked with prefix 'GD_' to separate them from service related descriptions.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"id\": [                      \"Guid should contain 32 digits with 4 dashes (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx).\"                  ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()
organization_id = 'organization_id_example' # str | Organization guid. (optional)
code = 'code_example' # str | Organization business code. (optional)
oid = 'oid_example' # str | Organization oid. (optional)
service_with_gd = false # bool | Indicates if general description data should be attached within the service data. (optional) (default to false)
page = 1 # int | The page to be fetched. (optional) (default to 1)
show_header = false # bool |  (optional) (default to false)

try:
    # Fetches all the information of the services related to certain organization. Either organizationId, code or oid needs to be added as a parameter.  User can also set serviceWithGD parameter to true to include possible attached general description data into the service data.  In this case general description related descriptions are marked with prefix 'GD_' to separate them from service related descriptions.
    api_response = api_instance.api_v11_service_list_organization_get(organization_id=organization_id, code=code, oid=oid, service_with_gd=service_with_gd, page=page, show_header=show_header)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->api_v11_service_list_organization_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization guid. | [optional] 
 **code** | **str**| Organization business code. | [optional] 
 **oid** | **str**| Organization oid. | [optional] 
 **service_with_gd** | **bool**| Indicates if general description data should be attached within the service data. | [optional] [default to false]
 **page** | **int**| The page to be fetched. | [optional] [default to 1]
 **show_header** | **bool**|  | [optional] [default to false]

### Return type

[**V11VmOpenApiServicesWithPaging**](V11VmOpenApiServicesWithPaging.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_post**
> V11VmOpenApiService api_v11_service_post(body=body, attach_proposed_channels=attach_proposed_channels)

Creates a new service with the data provided as input.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"ServiceNames\": [                      \"Type - Required value 'Name' was not found!\"                  ]              }              </code>

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
api_instance = swagger_client.ServiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.V9VmOpenApiServiceIn() # V9VmOpenApiServiceIn | The service data. (optional)
attach_proposed_channels = true # bool | Indicates if service channels attached into general description should automatically be attached into the service. (optional)

try:
    # Creates a new service with the data provided as input.
    api_response = api_instance.api_v11_service_post(body=body, attach_proposed_channels=attach_proposed_channels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->api_v11_service_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V9VmOpenApiServiceIn**](V9VmOpenApiServiceIn.md)| The service data. | [optional] 
 **attach_proposed_channels** | **bool**| Indicates if service channels attached into general description should automatically be attached into the service. | [optional] 

### Return type

[**V11VmOpenApiService**](V11VmOpenApiService.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_service_channel_service_channel_id_get**
> V3VmOpenApiGuidPage api_v11_service_service_channel_service_channel_id_get(service_channel_id, _date=_date, date_before=date_before, page=page)

Gets a list of published services for defined service channel.  Services joined to service channel after certain date can be fetched by adding date as query string parameter.  Services joined to service channel before certain date can be fetched by adding dateBefore as query string parameter.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()
service_channel_id = 'service_channel_id_example' # str | Guid
_date = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
date_before = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
page = 1 # int | The page number to be fetched. (optional) (default to 1)

try:
    # Gets a list of published services for defined service channel.  Services joined to service channel after certain date can be fetched by adding date as query string parameter.  Services joined to service channel before certain date can be fetched by adding dateBefore as query string parameter.
    api_response = api_instance.api_v11_service_service_channel_service_channel_id_get(service_channel_id, _date=_date, date_before=date_before, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->api_v11_service_service_channel_service_channel_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_channel_id** | **str**| Guid | 
 **_date** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **date_before** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **page** | **int**| The page number to be fetched. | [optional] [default to 1]

### Return type

[**V3VmOpenApiGuidPage**](V3VmOpenApiGuidPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_service_class_get**
> V3VmOpenApiGuidPage api_v11_service_service_class_get(uri=uri, _date=_date, date_before=date_before, page=page)

Gets a list of published services for defined service class.  Services created/modified after certain date can be fetched by adding date as query string parameter.  Services created/modified before certain date can be fetched by adding dateBefore as query string parameter.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()
uri = 'uri_example' # str | Service class uri, e.g. http://urn.fi/URN:NBN:fi:au:ptvl:v1065 (optional)
_date = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
date_before = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
page = 1 # int | The page number to be fetched. (optional) (default to 1)

try:
    # Gets a list of published services for defined service class.  Services created/modified after certain date can be fetched by adding date as query string parameter.  Services created/modified before certain date can be fetched by adding dateBefore as query string parameter.
    api_response = api_instance.api_v11_service_service_class_get(uri=uri, _date=_date, date_before=date_before, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->api_v11_service_service_class_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Service class uri, e.g. http://urn.fi/URN:NBN:fi:au:ptvl:v1065 | [optional] 
 **_date** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **date_before** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **page** | **int**| The page number to be fetched. | [optional] [default to 1]

### Return type

[**V3VmOpenApiGuidPage**](V3VmOpenApiGuidPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_service_with_gd_id_get**
> V11VmOpenApiService api_v11_service_service_with_gd_id_get(id, show_header=show_header)

Fetches all the information related to a single service. If general description is attached also general description data is returned within the service data.  General description related descriptions are marked with prefix 'GD_' to separate them from service related descriptions.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"id\": [                      \"Guid should contain 32 digits with 4 dashes (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx).\"                  ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()
id = 'id_example' # str | Guid
show_header = false # bool |  (optional) (default to false)

try:
    # Fetches all the information related to a single service. If general description is attached also general description data is returned within the service data.  General description related descriptions are marked with prefix 'GD_' to separate them from service related descriptions.
    api_response = api_instance.api_v11_service_service_with_gd_id_get(id, show_header=show_header)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->api_v11_service_service_with_gd_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Guid | 
 **show_header** | **bool**|  | [optional] [default to false]

### Return type

[**V11VmOpenApiService**](V11VmOpenApiService.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_service_with_gd_list_get**
> list[V11VmOpenApiService] api_v11_service_service_with_gd_list_get(guids=guids, show_header=show_header)

Fetches all the information related to requests services. If general description is attached to a service also general description data is returned within the service data.  General description related descriptions are marked with prefix 'GD_' to separate them from service related descriptions.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"id\": [                      \"Guid should contain 32 digits with 4 dashes (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx).\"                  ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()
guids = 'guids_example' # str | Comma separated list of guids. Max 100 can be added into list. (optional)
show_header = false # bool |  (optional) (default to false)

try:
    # Fetches all the information related to requests services. If general description is attached to a service also general description data is returned within the service data.  General description related descriptions are marked with prefix 'GD_' to separate them from service related descriptions.
    api_response = api_instance.api_v11_service_service_with_gd_list_get(guids=guids, show_header=show_header)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->api_v11_service_service_with_gd_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guids** | **str**| Comma separated list of guids. Max 100 can be added into list. | [optional] 
 **show_header** | **bool**|  | [optional] [default to false]

### Return type

[**list[V11VmOpenApiService]**](V11VmOpenApiService.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_source_id_source_id_put**
> V11VmOpenApiService api_v11_service_source_id_source_id_put(source_id, body=body, attach_proposed_channels=attach_proposed_channels)

Updates the defined service with the data provided as input.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"ServiceNames[0].Type\": [                      \"The Type field is required.\"                  ]              }              </code>

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
api_instance = swagger_client.ServiceApi(swagger_client.ApiClient(configuration))
source_id = 'source_id_example' # str | External source identifier
body = swagger_client.V9VmOpenApiServiceInBase() # V9VmOpenApiServiceInBase | The service data (optional)
attach_proposed_channels = true # bool | Indicates if service channels attached into general description should automatically be attached into the service. (optional)

try:
    # Updates the defined service with the data provided as input.
    api_response = api_instance.api_v11_service_source_id_source_id_put(source_id, body=body, attach_proposed_channels=attach_proposed_channels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->api_v11_service_source_id_source_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| External source identifier | 
 **body** | [**V9VmOpenApiServiceInBase**](V9VmOpenApiServiceInBase.md)| The service data | [optional] 
 **attach_proposed_channels** | **bool**| Indicates if service channels attached into general description should automatically be attached into the service. | [optional] 

### Return type

[**V11VmOpenApiService**](V11VmOpenApiService.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_target_group_get**
> V3VmOpenApiGuidPage api_v11_service_target_group_get(uri=uri, _date=_date, date_before=date_before, page=page)

Gets a list of published services for defined target group.  Services created/modified after certain date can be fetched by adding date as query string parameter.  Services created/modified before certain date can be fetched by adding dateBefore as query string parameter.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()
uri = 'uri_example' # str | Target group uri, e.g. http://urn.fi/URN:NBN:fi:au:ptvl:v2001 (optional)
_date = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
date_before = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
page = 1 # int | The page number to be fetched. (optional) (default to 1)

try:
    # Gets a list of published services for defined target group.  Services created/modified after certain date can be fetched by adding date as query string parameter.  Services created/modified before certain date can be fetched by adding dateBefore as query string parameter.
    api_response = api_instance.api_v11_service_target_group_get(uri=uri, _date=_date, date_before=date_before, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->api_v11_service_target_group_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Target group uri, e.g. http://urn.fi/URN:NBN:fi:au:ptvl:v2001 | [optional] 
 **_date** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **date_before** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **page** | **int**| The page number to be fetched. | [optional] [default to 1]

### Return type

[**V3VmOpenApiGuidPage**](V3VmOpenApiGuidPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_type_type_get**
> V3VmOpenApiGuidPage api_v11_service_type_type_get(type, _date=_date, date_before=date_before, page=page)

Gets a list of published services of defined service type.  Services created/modified after certain date can be fetched by adding date as query string parameter.  Services created/modified before certain date can be fetched by adding dateBefore as query string parameter.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()
type = 'type_example' # str | Service type
_date = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
date_before = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
page = 1 # int | The page number to be fetched. (optional) (default to 1)

try:
    # Gets a list of published services of defined service type.  Services created/modified after certain date can be fetched by adding date as query string parameter.  Services created/modified before certain date can be fetched by adding dateBefore as query string parameter.
    api_response = api_instance.api_v11_service_type_type_get(type, _date=_date, date_before=date_before, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->api_v11_service_type_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Service type | 
 **_date** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **date_before** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **page** | **int**| The page number to be fetched. | [optional] [default to 1]

### Return type

[**V3VmOpenApiGuidPage**](V3VmOpenApiGuidPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

