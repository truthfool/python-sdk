# swagger_client.OrganizationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v11_organization_area_area_code_code_get**](OrganizationApi.md#api_v11_organization_area_area_code_code_get) | **GET** /api/v11/Organization/area/{area}/code/{code} | Gets a list of published organizations related to defined area and code.  Organizations created/modified after certain date can be fetched by adding date as query string parameter.  Organizations created/modified before certain date can be fetched by adding dateBefore as query string parameter.
[**api_v11_organization_businesscode_code_get**](OrganizationApi.md#api_v11_organization_businesscode_code_get) | **GET** /api/v11/Organization/businesscode/{code} | Fetches all the information related to organizations with defined business identity code.
[**api_v11_organization_get**](OrganizationApi.md#api_v11_organization_get) | **GET** /api/v11/Organization | Gets all the published organizations within PTV as a list of organization ids and names.  Organizations created/modified after certain date can be fetched by adding date as query string parameter.  Organizations created/modified before certain date can be fetched by adding dateBefore as query string parameter.  Archived items can be fetched by setting status parameter as &#x27;Archived&#x27; and withdrawn items can be fetched by setting status parameter as &#x27;Withdrawn&#x27;.
[**api_v11_organization_hierarchy_get**](OrganizationApi.md#api_v11_organization_hierarchy_get) | **GET** /api/v11/Organization/Hierarchy | Gets a list of published organizations that do not have a parent organization.  Organizations created/modified after certain date can be fetched by adding date as query string parameter.  Organizations created/modified before certain date can be fetched by adding dateBefore as query string parameter.
[**api_v11_organization_hierarchy_id_get**](OrganizationApi.md#api_v11_organization_hierarchy_id_get) | **GET** /api/v11/Organization/Hierarchy/{id} | Get a single organization hierarchy. Returns the complete hierarchy starting from  the root organization and including all the child and grandchild organizations.
[**api_v11_organization_id_get**](OrganizationApi.md#api_v11_organization_id_get) | **GET** /api/v11/Organization/{id} | Fetches all the information related to a single organization.
[**api_v11_organization_id_put**](OrganizationApi.md#api_v11_organization_id_put) | **PUT** /api/v11/Organization/{id} | Updates organization.
[**api_v11_organization_list_area_area_code_code_get**](OrganizationApi.md#api_v11_organization_list_area_area_code_code_get) | **GET** /api/v11/Organization/list/area/{area}/code/{code} | Fetches all the information of the organizations related to certain area.
[**api_v11_organization_list_get**](OrganizationApi.md#api_v11_organization_list_get) | **GET** /api/v11/Organization/list | Fetches all the information related to requested organizations.
[**api_v11_organization_oid_oid_get**](OrganizationApi.md#api_v11_organization_oid_oid_get) | **GET** /api/v11/Organization/oid/{oid} | Fetches all the information related to a single organization with defined Oid.
[**api_v11_organization_post**](OrganizationApi.md#api_v11_organization_post) | **POST** /api/v11/Organization | Creates a new organization with the data provided as input.
[**api_v11_organization_saha_get**](OrganizationApi.md#api_v11_organization_saha_get) | **GET** /api/v11/Organization/saha | Gets main organizations and two sub levels of organizations. Returns both published and archived organizations.  NOTE! This is a restricted endpoint.
[**api_v11_organization_saha_id_get**](OrganizationApi.md#api_v11_organization_saha_id_get) | **GET** /api/v11/Organization/saha/{id} | Fetches Saha related information of a single organization.  NOTE! This is a restricted endpoint.
[**api_v11_organization_source_id_source_id_put**](OrganizationApi.md#api_v11_organization_source_id_source_id_put) | **PUT** /api/v11/Organization/sourceId/{sourceId} | Updates organization.

# **api_v11_organization_area_area_code_code_get**
> V8VmOpenApiOrganizationGuidPage api_v11_organization_area_area_code_code_get(area, code, include_whole_country=include_whole_country, _date=_date, date_before=date_before, page=page)

Gets a list of published organizations related to defined area and code.  Organizations created/modified after certain date can be fetched by adding date as query string parameter.  Organizations created/modified before certain date can be fetched by adding dateBefore as query string parameter.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationApi()
area = 'area_example' # str | The area type.
code = 'code_example' # str | The code related to area
include_whole_country = true # bool | Indicates if organizations marked to provide services for whole country (or whole country except Åland) should be included. (optional)
_date = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
date_before = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
page = 1 # int | The page number to be fetched. (optional) (default to 1)

try:
    # Gets a list of published organizations related to defined area and code.  Organizations created/modified after certain date can be fetched by adding date as query string parameter.  Organizations created/modified before certain date can be fetched by adding dateBefore as query string parameter.
    api_response = api_instance.api_v11_organization_area_area_code_code_get(area, code, include_whole_country=include_whole_country, _date=_date, date_before=date_before, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->api_v11_organization_area_area_code_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area** | **str**| The area type. | 
 **code** | **str**| The code related to area | 
 **include_whole_country** | **bool**| Indicates if organizations marked to provide services for whole country (or whole country except Åland) should be included. | [optional] 
 **_date** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **date_before** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **page** | **int**| The page number to be fetched. | [optional] [default to 1]

### Return type

[**V8VmOpenApiOrganizationGuidPage**](V8VmOpenApiOrganizationGuidPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_organization_businesscode_code_get**
> list[V10VmOpenApiOrganization] api_v11_organization_businesscode_code_get(code, show_header=show_header)

Fetches all the information related to organizations with defined business identity code.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages. Below sample response.  <code>              {                 \"code\": [                   \"The field code must match the regular expression '^[0-9]{7}-[0-9]{1}$'.\"                 ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationApi()
code = 'code_example' # str | Finnish business identity code (Y-tunnus).
show_header = false # bool |  (optional) (default to false)

try:
    # Fetches all the information related to organizations with defined business identity code.
    api_response = api_instance.api_v11_organization_businesscode_code_get(code, show_header=show_header)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->api_v11_organization_businesscode_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Finnish business identity code (Y-tunnus). | 
 **show_header** | **bool**|  | [optional] [default to false]

### Return type

[**list[V10VmOpenApiOrganization]**](V10VmOpenApiOrganization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_organization_get**
> V8VmOpenApiOrganizationGuidPage api_v11_organization_get(_date=_date, date_before=date_before, page=page, status=status)

Gets all the published organizations within PTV as a list of organization ids and names.  Organizations created/modified after certain date can be fetched by adding date as query string parameter.  Organizations created/modified before certain date can be fetched by adding dateBefore as query string parameter.  Archived items can be fetched by setting status parameter as 'Archived' and withdrawn items can be fetched by setting status parameter as 'Withdrawn'.

NOTICE! When fetching published organizations, only organizations that have published services or published channels attached are returned!                <br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages. Below sample response.<code>  {     \"date\": [       \"The value '-2' is not valid for Nullable`1.\",       \"The date parameter is invalid.\"     ]  }  </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationApi()
_date = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
date_before = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
page = 1 # int | The page number to be fetched. (optional) (default to 1)
status = 'Published' # str | Set status to get items either in published, archived or withdrawn state. (optional) (default to Published)

try:
    # Gets all the published organizations within PTV as a list of organization ids and names.  Organizations created/modified after certain date can be fetched by adding date as query string parameter.  Organizations created/modified before certain date can be fetched by adding dateBefore as query string parameter.  Archived items can be fetched by setting status parameter as 'Archived' and withdrawn items can be fetched by setting status parameter as 'Withdrawn'.
    api_response = api_instance.api_v11_organization_get(_date=_date, date_before=date_before, page=page, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->api_v11_organization_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **date_before** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **page** | **int**| The page number to be fetched. | [optional] [default to 1]
 **status** | **str**| Set status to get items either in published, archived or withdrawn state. | [optional] [default to Published]

### Return type

[**V8VmOpenApiOrganizationGuidPage**](V8VmOpenApiOrganizationGuidPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_organization_hierarchy_get**
> V3VmOpenApiGuidPage api_v11_organization_hierarchy_get(_date=_date, date_before=date_before, page=page)

Gets a list of published organizations that do not have a parent organization.  Organizations created/modified after certain date can be fetched by adding date as query string parameter.  Organizations created/modified before certain date can be fetched by adding dateBefore as query string parameter.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationApi()
_date = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
date_before = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
page = 1 # int | The page number to be fetched. (optional) (default to 1)

try:
    # Gets a list of published organizations that do not have a parent organization.  Organizations created/modified after certain date can be fetched by adding date as query string parameter.  Organizations created/modified before certain date can be fetched by adding dateBefore as query string parameter.
    api_response = api_instance.api_v11_organization_hierarchy_get(_date=_date, date_before=date_before, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->api_v11_organization_hierarchy_get: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_organization_hierarchy_id_get**
> VmOpenApiOrganizationHierarchy api_v11_organization_hierarchy_id_get(id)

Get a single organization hierarchy. Returns the complete hierarchy starting from  the root organization and including all the child and grandchild organizations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationApi()
id = 'id_example' # str | Guid

try:
    # Get a single organization hierarchy. Returns the complete hierarchy starting from  the root organization and including all the child and grandchild organizations.
    api_response = api_instance.api_v11_organization_hierarchy_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->api_v11_organization_hierarchy_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Guid | 

### Return type

[**VmOpenApiOrganizationHierarchy**](VmOpenApiOrganizationHierarchy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_organization_id_get**
> V10VmOpenApiOrganization api_v11_organization_id_get(id, show_header=show_header)

Fetches all the information related to a single organization.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages. Below sample response.  <code>              {                 \"id\": [                   \"Guid should contain 32 digits with 4 dashes (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx).\"                 ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationApi()
id = 'id_example' # str | Guid
show_header = false # bool |  (optional) (default to false)

try:
    # Fetches all the information related to a single organization.
    api_response = api_instance.api_v11_organization_id_get(id, show_header=show_header)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->api_v11_organization_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Guid | 
 **show_header** | **bool**|  | [optional] [default to false]

### Return type

[**V10VmOpenApiOrganization**](V10VmOpenApiOrganization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_organization_id_put**
> V10VmOpenApiOrganization api_v11_organization_id_put(id, body=body)

Updates organization.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages. Below sample response.  <code>              {                 \"propertyname\": [                   \"The field propertyname has invalid characters.\"                 ]              }              </code>

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
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | organization entity id
body = swagger_client.V9VmOpenApiOrganizationInBase() # V9VmOpenApiOrganizationInBase | organization values (optional)

try:
    # Updates organization.
    api_response = api_instance.api_v11_organization_id_put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->api_v11_organization_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| organization entity id | 
 **body** | [**V9VmOpenApiOrganizationInBase**](V9VmOpenApiOrganizationInBase.md)| organization values | [optional] 

### Return type

[**V10VmOpenApiOrganization**](V10VmOpenApiOrganization.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_organization_list_area_area_code_code_get**
> V10VmOpenApiOrganizationsWithPaging api_v11_organization_list_area_area_code_code_get(area, code, include_whole_country=include_whole_country, page=page, show_header=show_header)

Fetches all the information of the organizations related to certain area.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages. Below sample response.  <code>              {                 \"id\": [                   \"Guid should contain 32 digits with 4 dashes (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx).\"                 ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationApi()
area = 'area_example' # str | The area type.
code = 'code_example' # str | The code related to area
include_whole_country = true # bool | Indicates if organizations marked to provide services for whole country (or whole country except Åland) should be included. (optional)
page = 1 # int | The page number to be fetched. (optional) (default to 1)
show_header = false # bool |  (optional) (default to false)

try:
    # Fetches all the information of the organizations related to certain area.
    api_response = api_instance.api_v11_organization_list_area_area_code_code_get(area, code, include_whole_country=include_whole_country, page=page, show_header=show_header)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->api_v11_organization_list_area_area_code_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area** | **str**| The area type. | 
 **code** | **str**| The code related to area | 
 **include_whole_country** | **bool**| Indicates if organizations marked to provide services for whole country (or whole country except Åland) should be included. | [optional] 
 **page** | **int**| The page number to be fetched. | [optional] [default to 1]
 **show_header** | **bool**|  | [optional] [default to false]

### Return type

[**V10VmOpenApiOrganizationsWithPaging**](V10VmOpenApiOrganizationsWithPaging.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_organization_list_get**
> list[V10VmOpenApiOrganization] api_v11_organization_list_get(guids=guids, show_header=show_header)

Fetches all the information related to requested organizations.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages. Below sample response.  <code>              {                 \"id\": [                   \"Guid should contain 32 digits with 4 dashes (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx).\"                 ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationApi()
guids = 'guids_example' # str | Comma separated list of guids. Max 100 can be added into list. (optional)
show_header = false # bool |  (optional) (default to false)

try:
    # Fetches all the information related to requested organizations.
    api_response = api_instance.api_v11_organization_list_get(guids=guids, show_header=show_header)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->api_v11_organization_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guids** | **str**| Comma separated list of guids. Max 100 can be added into list. | [optional] 
 **show_header** | **bool**|  | [optional] [default to false]

### Return type

[**list[V10VmOpenApiOrganization]**](V10VmOpenApiOrganization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_organization_oid_oid_get**
> V10VmOpenApiOrganization api_v11_organization_oid_oid_get(oid, show_header=show_header)

Fetches all the information related to a single organization with defined Oid.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages. Below sample response.  <code>              {                 \"oid\": [                   \"The field oid must match the regular expression '^[A-Za-z0-9.-]*$'.\"                 ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationApi()
oid = 'oid_example' # str | Oid identifier
show_header = false # bool |  (optional) (default to false)

try:
    # Fetches all the information related to a single organization with defined Oid.
    api_response = api_instance.api_v11_organization_oid_oid_get(oid, show_header=show_header)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->api_v11_organization_oid_oid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Oid identifier | 
 **show_header** | **bool**|  | [optional] [default to false]

### Return type

[**V10VmOpenApiOrganization**](V10VmOpenApiOrganization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_organization_post**
> V10VmOpenApiOrganization api_v11_organization_post(body=body)

Creates a new organization with the data provided as input.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"Addresses[1].StreetAddress\": [                      \"The StreetAddress field is required.\"                  ]              }              </code>

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
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
body = swagger_client.V9VmOpenApiOrganizationIn() # V9VmOpenApiOrganizationIn | The organization data. (optional)

try:
    # Creates a new organization with the data provided as input.
    api_response = api_instance.api_v11_organization_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->api_v11_organization_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V9VmOpenApiOrganizationIn**](V9VmOpenApiOrganizationIn.md)| The organization data. | [optional] 

### Return type

[**V10VmOpenApiOrganization**](V10VmOpenApiOrganization.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_organization_saha_get**
> VmOpenApiOrganizationSahaGuidPage api_v11_organization_saha_get(_date=_date, date_before=date_before, page=page)

Gets main organizations and two sub levels of organizations. Returns both published and archived organizations.  NOTE! This is a restricted endpoint.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages. Below sample response.  <code>              {                 \"date\": [                   \"The value '-2' is not valid for Nullable`1.\",                   \"The date parameter is invalid.\"                 ]              }              </code>

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
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
_date = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
date_before = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC) (optional)
page = 1 # int | The page number to be fetched. (optional) (default to 1)

try:
    # Gets main organizations and two sub levels of organizations. Returns both published and archived organizations.  NOTE! This is a restricted endpoint.
    api_response = api_instance.api_v11_organization_saha_get(_date=_date, date_before=date_before, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->api_v11_organization_saha_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **date_before** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC) | [optional] 
 **page** | **int**| The page number to be fetched. | [optional] [default to 1]

### Return type

[**VmOpenApiOrganizationSahaGuidPage**](VmOpenApiOrganizationSahaGuidPage.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_organization_saha_id_get**
> VmOpenApiOrganizationSaha api_v11_organization_saha_id_get(id)

Fetches Saha related information of a single organization.  NOTE! This is a restricted endpoint.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages. Below sample response.  <code>              {                 \"id\": [                   \"Guid should contain 32 digits with 4 dashes (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx).\"                 ]              }              </code>

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
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Guid

try:
    # Fetches Saha related information of a single organization.  NOTE! This is a restricted endpoint.
    api_response = api_instance.api_v11_organization_saha_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->api_v11_organization_saha_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Guid | 

### Return type

[**VmOpenApiOrganizationSaha**](VmOpenApiOrganizationSaha.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_organization_source_id_source_id_put**
> V10VmOpenApiOrganization api_v11_organization_source_id_source_id_put(source_id, body=body)

Updates organization.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages. Below sample response.  <code>              {                 \"propertyname\": [                   \"The field propertyname has invalid characters.\"                 ]              }              </code>

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
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
source_id = 'source_id_example' # str | organization external id
body = swagger_client.V9VmOpenApiOrganizationInBase() # V9VmOpenApiOrganizationInBase | organization values (optional)

try:
    # Updates organization.
    api_response = api_instance.api_v11_organization_source_id_source_id_put(source_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->api_v11_organization_source_id_source_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| organization external id | 
 **body** | [**V9VmOpenApiOrganizationInBase**](V9VmOpenApiOrganizationInBase.md)| organization values | [optional] 

### Return type

[**V10VmOpenApiOrganization**](V10VmOpenApiOrganization.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

