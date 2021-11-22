# swagger_client.ServiceChannelApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v11_service_channel_active_get**](ServiceChannelApi.md#api_v11_service_channel_active_get) | **GET** /api/v11/ServiceChannel/active | Gets all service channels within PTV as a list of service channel ids and names. Also service channels with draft and modified versions are included.  Service channels created/modified after certain date can be fetched by adding date as query string parameter.  Service channels created/modified before certain date can be fetched by adding dateBefore as query string parameter.  Certain type of service channels can be fetched by setting query string parameter type.  NOTE! This is a restricted endpoint.
[**api_v11_service_channel_active_id_get**](ServiceChannelApi.md#api_v11_service_channel_active_id_get) | **GET** /api/v11/ServiceChannel/active/{id} | Fetches all the information related to a single service channel. Also service channels with only draft or modified versions are returned.  NOTE! This is a restricted endpoint.
[**api_v11_service_channel_archived_list_get**](ServiceChannelApi.md#api_v11_service_channel_archived_list_get) | **GET** /api/v11/ServiceChannel/archived/list | Fetches automatically/manually archived service channels
[**api_v11_service_channel_area_area_code_code_get**](ServiceChannelApi.md#api_v11_service_channel_area_area_code_code_get) | **GET** /api/v11/ServiceChannel/area/{area}/code/{code} | Gets a list of service channels related to defined area and code.  Service channels created/modified after certain date can be fetched by adding date as query string parameter.  Service channels created/modified before certain date can be fetched by adding dateBefore as query string parameter.
[**api_v11_service_channel_e_channel_id_put**](ServiceChannelApi.md#api_v11_service_channel_e_channel_id_put) | **PUT** /api/v11/ServiceChannel/EChannel/{id} | Updates electronic channel with the data provided as input.
[**api_v11_service_channel_e_channel_post**](ServiceChannelApi.md#api_v11_service_channel_e_channel_post) | **POST** /api/v11/ServiceChannel/EChannel | Creates a new electronic channel with the data provided as input.
[**api_v11_service_channel_e_channel_source_id_source_id_put**](ServiceChannelApi.md#api_v11_service_channel_e_channel_source_id_source_id_put) | **PUT** /api/v11/ServiceChannel/EChannel/sourceId/{sourceId} | Updates electronic channel with the data provided as input.
[**api_v11_service_channel_get**](ServiceChannelApi.md#api_v11_service_channel_get) | **GET** /api/v11/ServiceChannel | Gets all published service channels within PTV as a list of service channel ids and names.  Service channels created/modified after certain date can be fetched by adding date as query string parameter  Service channels created/modified before certain date can be fetched by adding dateBefore as query string parameter.  Archived items can be fetched by setting status parameter as &#x27;Archived&#x27; and withdrawn items can be fetched by setting status parameter as &#x27;Withdrawn&#x27;.
[**api_v11_service_channel_id_get**](ServiceChannelApi.md#api_v11_service_channel_id_get) | **GET** /api/v11/ServiceChannel/{id} | Fetches all the information related to a single service channel.
[**api_v11_service_channel_list_area_area_code_code_get**](ServiceChannelApi.md#api_v11_service_channel_list_area_area_code_code_get) | **GET** /api/v11/ServiceChannel/list/area/{area}/code/{code} | Gets a list of service channels related to defined area and code.  Service channels created/modified after certain date can be fetched by adding date as query string parameter.  Service channels created/modified before certain date can be fetched by adding dateBefore as query string parameter.
[**api_v11_service_channel_list_get**](ServiceChannelApi.md#api_v11_service_channel_list_get) | **GET** /api/v11/ServiceChannel/list | Fetches all the information related to requested service channels.
[**api_v11_service_channel_list_organization_get**](ServiceChannelApi.md#api_v11_service_channel_list_organization_get) | **GET** /api/v11/ServiceChannel/list/organization | Fetches all the information of service channels related to certain organization. Either organizationId, code or oid needs to be added as a parameter.
[**api_v11_service_channel_organization_organization_id_get**](ServiceChannelApi.md#api_v11_service_channel_organization_organization_id_get) | **GET** /api/v11/ServiceChannel/organization/{organizationId} | Gets a list of published service channels for defined organization.  Service channels created/modified after certain date can be fetched by adding date as query string parameter.  Service channels created/modified before certain date can be fetched by adding dateBefore as query string parameter.
[**api_v11_service_channel_organization_organization_id_type_type_get**](ServiceChannelApi.md#api_v11_service_channel_organization_organization_id_type_type_get) | **GET** /api/v11/ServiceChannel/organization/{organizationId}/type/{type} | Gets a list of certain type of published service channels for defined organization.  Service channels created/modified after certain date can be fetched by adding date as query string parameter.  Service channels created/modified before certain date can be fetched by adding dateBefore as query string parameter.
[**api_v11_service_channel_phone_id_put**](ServiceChannelApi.md#api_v11_service_channel_phone_id_put) | **PUT** /api/v11/ServiceChannel/Phone/{id} | Updates phone channel with the data provided as input.
[**api_v11_service_channel_phone_post**](ServiceChannelApi.md#api_v11_service_channel_phone_post) | **POST** /api/v11/ServiceChannel/Phone | Creates a new phone channel with the data provided as input.
[**api_v11_service_channel_phone_source_id_source_id_put**](ServiceChannelApi.md#api_v11_service_channel_phone_source_id_source_id_put) | **PUT** /api/v11/ServiceChannel/Phone/sourceId/{sourceId} | Updates phone channel with the data provided as input.
[**api_v11_service_channel_printable_form_id_put**](ServiceChannelApi.md#api_v11_service_channel_printable_form_id_put) | **PUT** /api/v11/ServiceChannel/PrintableForm/{id} | Updates printable form channel with the data provided as input.
[**api_v11_service_channel_printable_form_post**](ServiceChannelApi.md#api_v11_service_channel_printable_form_post) | **POST** /api/v11/ServiceChannel/PrintableForm | Creates a new printable form channel with the data provided as input.
[**api_v11_service_channel_printable_form_source_id_source_id_put**](ServiceChannelApi.md#api_v11_service_channel_printable_form_source_id_source_id_put) | **PUT** /api/v11/ServiceChannel/PrintableForm/sourceId/{sourceId} | Updates printable form channel with the data provided as input.
[**api_v11_service_channel_service_location_id_put**](ServiceChannelApi.md#api_v11_service_channel_service_location_id_put) | **PUT** /api/v11/ServiceChannel/ServiceLocation/{id} | Updates service location channel with the data provided as input.
[**api_v11_service_channel_service_location_post**](ServiceChannelApi.md#api_v11_service_channel_service_location_post) | **POST** /api/v11/ServiceChannel/ServiceLocation | Creates a new service location channel with the data provided as input.
[**api_v11_service_channel_service_location_source_id_source_id_put**](ServiceChannelApi.md#api_v11_service_channel_service_location_source_id_source_id_put) | **PUT** /api/v11/ServiceChannel/ServiceLocation/sourceId/{sourceId} | Updates service location channel with the data provided as input.
[**api_v11_service_channel_type_type_get**](ServiceChannelApi.md#api_v11_service_channel_type_type_get) | **GET** /api/v11/ServiceChannel/type/{type} | Gets a list of certain type of published service channels.  Service channels created/modified after certain date can be fetched by adding date as query string parameter.  Service channels created/modified before certain date can be fetched by adding dateBefore as query string parameter.
[**api_v11_service_channel_web_page_id_put**](ServiceChannelApi.md#api_v11_service_channel_web_page_id_put) | **PUT** /api/v11/ServiceChannel/WebPage/{id} | Updates webpage channel with the data provided as input.
[**api_v11_service_channel_web_page_post**](ServiceChannelApi.md#api_v11_service_channel_web_page_post) | **POST** /api/v11/ServiceChannel/WebPage | Creates a new web page channel with the data provided as input.
[**api_v11_service_channel_web_page_source_id_source_id_put**](ServiceChannelApi.md#api_v11_service_channel_web_page_source_id_source_id_put) | **PUT** /api/v11/ServiceChannel/WebPage/sourceId/{sourceId} | Updates webpage channel with the data provided as input.

# **api_v11_service_channel_active_get**
> V3VmOpenApiGuidPage api_v11_service_channel_active_get(_date=_date, date_before=date_before, type=type, page=page)

Gets all service channels within PTV as a list of service channel ids and names. Also service channels with draft and modified versions are included.  Service channels created/modified after certain date can be fetched by adding date as query string parameter.  Service channels created/modified before certain date can be fetched by adding dateBefore as query string parameter.  Certain type of service channels can be fetched by setting query string parameter type.  NOTE! This is a restricted endpoint.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages. Below sample response.  <code>              {                 \"date\": [                   \"The value '-5' is not valid for Nullable`1.\",                   \"The date parameter is invalid.\"                 ]              }              </code>

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
api_instance = swagger_client.ServiceChannelApi(swagger_client.ApiClient(configuration))
_date = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
date_before = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
type = 'type_example' # str | Service channel type (optional)
page = 1 # int | The page to be fetched. (optional) (default to 1)

try:
    # Gets all service channels within PTV as a list of service channel ids and names. Also service channels with draft and modified versions are included.  Service channels created/modified after certain date can be fetched by adding date as query string parameter.  Service channels created/modified before certain date can be fetched by adding dateBefore as query string parameter.  Certain type of service channels can be fetched by setting query string parameter type.  NOTE! This is a restricted endpoint.
    api_response = api_instance.api_v11_service_channel_active_get(_date=_date, date_before=date_before, type=type, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceChannelApi->api_v11_service_channel_active_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **date_before** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **type** | **str**| Service channel type | [optional] 
 **page** | **int**| The page to be fetched. | [optional] [default to 1]

### Return type

[**V3VmOpenApiGuidPage**](V3VmOpenApiGuidPage.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_channel_active_id_get**
> V11VmOpenApiServiceChannels api_v11_service_channel_active_id_get(id, show_header=show_header)

Fetches all the information related to a single service channel. Also service channels with only draft or modified versions are returned.  NOTE! This is a restricted endpoint.

<br>Notice! The returned object is one of the following: <i>V11VmOpenApiElectronicChannel</i> or <i>V11VmOpenApiPhoneChannel</i> or               <i>V11VmOpenApiPrintableFormChannel</i> or <i>V11VmOpenApiServiceLocationChannel</i> or <i>V11mOpenApiWebPageChannel</i>  <br>The returned object depends on the type of the channel. For example if the channel is phone channel then V11VmOpenApiPhoneChannel object is returned.  <br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                 \"id\": [                     \"Guid should contain 32 digits with 4 dashes (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx).\"                 ]              }              </code>

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
api_instance = swagger_client.ServiceChannelApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Guid
show_header = false # bool |  (optional) (default to false)

try:
    # Fetches all the information related to a single service channel. Also service channels with only draft or modified versions are returned.  NOTE! This is a restricted endpoint.
    api_response = api_instance.api_v11_service_channel_active_id_get(id, show_header=show_header)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceChannelApi->api_v11_service_channel_active_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Guid | 
 **show_header** | **bool**|  | [optional] [default to false]

### Return type

[**V11VmOpenApiServiceChannels**](V11VmOpenApiServiceChannels.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_channel_archived_list_get**
> list[VmOpenApiArchivedServiceChannelBase] api_v11_service_channel_archived_list_get(archiving_type, organization_id, take, min_archiving_date=min_archiving_date, max_archiving_date=max_archiving_date, skip=skip)

Fetches automatically/manually archived service channels

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"id\": [                      \"Guid should contain 32 digits with 4 dashes (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx).\"                  ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceChannelApi()
archiving_type = swagger_client.ArchivingType() # ArchivingType | How channel was archived.
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Return only channels belonging to this organization.
take = 56 # int | How many channels to return.
min_archiving_date = '2013-10-20T19:20:30+01:00' # datetime | Return only channels archived after this time.  ISO 8601 format (e.g. 2020-10-26T05:24:11+00:00). (optional)
max_archiving_date = '2013-10-20T19:20:30+01:00' # datetime | Return only channels archived before this time.  ISO 8601 format (e.g. 2020-10-26T05:24:11+00:00). (optional)
skip = 56 # int | Skip the first n channels. (optional)

try:
    # Fetches automatically/manually archived service channels
    api_response = api_instance.api_v11_service_channel_archived_list_get(archiving_type, organization_id, take, min_archiving_date=min_archiving_date, max_archiving_date=max_archiving_date, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceChannelApi->api_v11_service_channel_archived_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **archiving_type** | [**ArchivingType**](.md)| How channel was archived. | 
 **organization_id** | [**str**](.md)| Return only channels belonging to this organization. | 
 **take** | **int**| How many channels to return. | 
 **min_archiving_date** | **datetime**| Return only channels archived after this time.  ISO 8601 format (e.g. 2020-10-26T05:24:11+00:00). | [optional] 
 **max_archiving_date** | **datetime**| Return only channels archived before this time.  ISO 8601 format (e.g. 2020-10-26T05:24:11+00:00). | [optional] 
 **skip** | **int**| Skip the first n channels. | [optional] 

### Return type

[**list[VmOpenApiArchivedServiceChannelBase]**](VmOpenApiArchivedServiceChannelBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_channel_area_area_code_code_get**
> V3VmOpenApiGuidPage api_v11_service_channel_area_area_code_code_get(area, code, include_whole_country=include_whole_country, _date=_date, date_before=date_before, page=page)

Gets a list of service channels related to defined area and code.  Service channels created/modified after certain date can be fetched by adding date as query string parameter.  Service channels created/modified before certain date can be fetched by adding dateBefore as query string parameter.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                 \"type\": [                     \"The field is invalid. Please use one of these: 'EChannel, WebPage, PrintableForm, Phone, ServiceLocation'.\"                 ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceChannelApi()
area = 'area_example' # str | The area type
code = 'code_example' # str | The area code
include_whole_country = true # bool | Indicates if service channels marked for whole country (or whole country except Åland) should be included. (optional)
_date = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
date_before = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
page = 1 # int | The page to be fetched. (optional) (default to 1)

try:
    # Gets a list of service channels related to defined area and code.  Service channels created/modified after certain date can be fetched by adding date as query string parameter.  Service channels created/modified before certain date can be fetched by adding dateBefore as query string parameter.
    api_response = api_instance.api_v11_service_channel_area_area_code_code_get(area, code, include_whole_country=include_whole_country, _date=_date, date_before=date_before, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceChannelApi->api_v11_service_channel_area_area_code_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area** | **str**| The area type | 
 **code** | **str**| The area code | 
 **include_whole_country** | **bool**| Indicates if service channels marked for whole country (or whole country except Åland) should be included. | [optional] 
 **_date** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **date_before** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **page** | **int**| The page to be fetched. | [optional] [default to 1]

### Return type

[**V3VmOpenApiGuidPage**](V3VmOpenApiGuidPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_channel_e_channel_id_put**
> V11VmOpenApiElectronicChannel api_v11_service_channel_e_channel_id_put(id, body=body)

Updates electronic channel with the data provided as input.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"ServiceChannelNames\":[                      \"The ServiceChannelNames field is required.\"                  ]              }              </code>

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
api_instance = swagger_client.ServiceChannelApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | electronic channel id
body = swagger_client.V11VmOpenApiElectronicChannelInBase() # V11VmOpenApiElectronicChannelInBase | electronic channel data (optional)

try:
    # Updates electronic channel with the data provided as input.
    api_response = api_instance.api_v11_service_channel_e_channel_id_put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceChannelApi->api_v11_service_channel_e_channel_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| electronic channel id | 
 **body** | [**V11VmOpenApiElectronicChannelInBase**](V11VmOpenApiElectronicChannelInBase.md)| electronic channel data | [optional] 

### Return type

[**V11VmOpenApiElectronicChannel**](V11VmOpenApiElectronicChannel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_channel_e_channel_post**
> V11VmOpenApiElectronicChannel api_v11_service_channel_e_channel_post(body=body)

Creates a new electronic channel with the data provided as input.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"ServiceChannelNames\":[                      \"The ServiceChannelNames field is required.\"                  ]              }              </code>

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
api_instance = swagger_client.ServiceChannelApi(swagger_client.ApiClient(configuration))
body = swagger_client.V11VmOpenApiElectronicChannelIn() # V11VmOpenApiElectronicChannelIn | The electronic channel data. (optional)

try:
    # Creates a new electronic channel with the data provided as input.
    api_response = api_instance.api_v11_service_channel_e_channel_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceChannelApi->api_v11_service_channel_e_channel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V11VmOpenApiElectronicChannelIn**](V11VmOpenApiElectronicChannelIn.md)| The electronic channel data. | [optional] 

### Return type

[**V11VmOpenApiElectronicChannel**](V11VmOpenApiElectronicChannel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_channel_e_channel_source_id_source_id_put**
> V11VmOpenApiElectronicChannel api_v11_service_channel_e_channel_source_id_source_id_put(source_id, body=body)

Updates electronic channel with the data provided as input.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"ServiceChannelNames\":[                      \"The ServiceChannelNames field is required.\"                  ]              }              </code>

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
api_instance = swagger_client.ServiceChannelApi(swagger_client.ApiClient(configuration))
source_id = 'source_id_example' # str | electronic channel external source id
body = swagger_client.V11VmOpenApiElectronicChannelInBase() # V11VmOpenApiElectronicChannelInBase | electronic channel data (optional)

try:
    # Updates electronic channel with the data provided as input.
    api_response = api_instance.api_v11_service_channel_e_channel_source_id_source_id_put(source_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceChannelApi->api_v11_service_channel_e_channel_source_id_source_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| electronic channel external source id | 
 **body** | [**V11VmOpenApiElectronicChannelInBase**](V11VmOpenApiElectronicChannelInBase.md)| electronic channel data | [optional] 

### Return type

[**V11VmOpenApiElectronicChannel**](V11VmOpenApiElectronicChannel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_channel_get**
> V3VmOpenApiGuidPage api_v11_service_channel_get(_date=_date, date_before=date_before, organization_id=organization_id, code=code, oid=oid, is_visible_for_all=is_visible_for_all, page=page, status=status)

Gets all published service channels within PTV as a list of service channel ids and names.  Service channels created/modified after certain date can be fetched by adding date as query string parameter  Service channels created/modified before certain date can be fetched by adding dateBefore as query string parameter.  Archived items can be fetched by setting status parameter as 'Archived' and withdrawn items can be fetched by setting status parameter as 'Withdrawn'.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages. Below sample response.  <code>              {                 \"date\": [                   \"The value '-5' is not valid for Nullable`1.\",                   \"The date parameter is invalid.\"                 ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceChannelApi()
_date = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
date_before = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC) (optional)
organization_id = 'organization_id_example' # str | You can restrict the result set by setting organization guid. (optional)
code = 'code_example' # str | You can restrict the result set by setting organization business code. (optional)
oid = 'oid_example' # str | You can restrict the result set by setting organization oid. (optional)
is_visible_for_all = false # bool | When set to true only service channels marked as isVisibleForAll are returned. (optional) (default to false)
page = 1 # int | The page to be fetched. (optional) (default to 1)
status = 'Published' # str | Set status to get items either in published, archived or withdrawn state. (optional) (default to Published)

try:
    # Gets all published service channels within PTV as a list of service channel ids and names.  Service channels created/modified after certain date can be fetched by adding date as query string parameter  Service channels created/modified before certain date can be fetched by adding dateBefore as query string parameter.  Archived items can be fetched by setting status parameter as 'Archived' and withdrawn items can be fetched by setting status parameter as 'Withdrawn'.
    api_response = api_instance.api_v11_service_channel_get(_date=_date, date_before=date_before, organization_id=organization_id, code=code, oid=oid, is_visible_for_all=is_visible_for_all, page=page, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceChannelApi->api_v11_service_channel_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **date_before** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC) | [optional] 
 **organization_id** | **str**| You can restrict the result set by setting organization guid. | [optional] 
 **code** | **str**| You can restrict the result set by setting organization business code. | [optional] 
 **oid** | **str**| You can restrict the result set by setting organization oid. | [optional] 
 **is_visible_for_all** | **bool**| When set to true only service channels marked as isVisibleForAll are returned. | [optional] [default to false]
 **page** | **int**| The page to be fetched. | [optional] [default to 1]
 **status** | **str**| Set status to get items either in published, archived or withdrawn state. | [optional] [default to Published]

### Return type

[**V3VmOpenApiGuidPage**](V3VmOpenApiGuidPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_channel_id_get**
> V11VmOpenApiServiceChannels api_v11_service_channel_id_get(id, show_header=show_header)

Fetches all the information related to a single service channel.

<br>Notice! The returned object is one of the following: <i>V11VmOpenApiElectronicChannel</i> or <i>V11VmOpenApiPhoneChannel</i> or               <i>V11VmOpenApiPrintableFormChannel</i> or <i>V11VmOpenApiServiceLocationChannel</i> or <i>V11VmOpenApiWebPageChannel</i>  <br>The returned object depends on the type of the channel. For example if the channel is phone channel then V11VmOpenApiPhoneChannel object is returned.  <br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                 \"id\": [                     \"Guid should contain 32 digits with 4 dashes (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx).\"                 ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceChannelApi()
id = 'id_example' # str | Guid
show_header = false # bool |  (optional) (default to false)

try:
    # Fetches all the information related to a single service channel.
    api_response = api_instance.api_v11_service_channel_id_get(id, show_header=show_header)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceChannelApi->api_v11_service_channel_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Guid | 
 **show_header** | **bool**|  | [optional] [default to false]

### Return type

[**V11VmOpenApiServiceChannels**](V11VmOpenApiServiceChannels.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_channel_list_area_area_code_code_get**
> V11VmOpenApiServiceChannelsWithPaging api_v11_service_channel_list_area_area_code_code_get(area, code, include_whole_country=include_whole_country, page=page, show_header=show_header)

Gets a list of service channels related to defined area and code.  Service channels created/modified after certain date can be fetched by adding date as query string parameter.  Service channels created/modified before certain date can be fetched by adding dateBefore as query string parameter.

<br>Notice! The returned itemList object includes items which can be one of the following: <i>V11VmOpenApiElectronicChannel</i> or <i>V11VmOpenApiPhoneChannel</i> or               <i>V11VmOpenApiPrintableFormChannel</i> or <i>V11VmOpenApiServiceLocationChannel</i> or <i>V11VmOpenApiWebPageChannel</i>  <br>The returned item type within itemList depends on the type of the channel. For example if the channel is phone channel then V11VmOpenApiPhoneChannel object is returned.  <br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                 \"type\": [                     \"The field is invalid. Please use one of these: 'EChannel, WebPage, PrintableForm, Phone, ServiceLocation'.\"                 ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceChannelApi()
area = 'area_example' # str | The area type
code = 'code_example' # str | The area code
include_whole_country = true # bool | Indicates if service channels marked for whole country (or whole country except Åland) should be included. (optional)
page = 1 # int | The page to be fetched. (optional) (default to 1)
show_header = false # bool |  (optional) (default to false)

try:
    # Gets a list of service channels related to defined area and code.  Service channels created/modified after certain date can be fetched by adding date as query string parameter.  Service channels created/modified before certain date can be fetched by adding dateBefore as query string parameter.
    api_response = api_instance.api_v11_service_channel_list_area_area_code_code_get(area, code, include_whole_country=include_whole_country, page=page, show_header=show_header)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceChannelApi->api_v11_service_channel_list_area_area_code_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area** | **str**| The area type | 
 **code** | **str**| The area code | 
 **include_whole_country** | **bool**| Indicates if service channels marked for whole country (or whole country except Åland) should be included. | [optional] 
 **page** | **int**| The page to be fetched. | [optional] [default to 1]
 **show_header** | **bool**|  | [optional] [default to false]

### Return type

[**V11VmOpenApiServiceChannelsWithPaging**](V11VmOpenApiServiceChannelsWithPaging.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_channel_list_get**
> list[V11VmOpenApiServiceChannels] api_v11_service_channel_list_get(guids=guids, show_header=show_header)

Fetches all the information related to requested service channels.

<br>Notice! The returned object is one of the following: <i>V11VmOpenApiElectronicChannel</i> or <i>V11VmOpenApiPhoneChannel</i> or               <i>V11VmOpenApiPrintableFormChannel</i> or <i>V11VmOpenApiServiceLocationChannel</i> or <i>V11VmOpenApiWebPageChannel</i>  <br>The returned object depends on the type of the channel. For example if the channel is phone channel then V11VmOpenApiPhoneChannel object is returned.  <br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                 \"id\": [                     \"Guid should contain 32 digits with 4 dashes (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx).\"                 ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceChannelApi()
guids = 'guids_example' # str | Comma separated list of guids. Max 100 can be added into list. (optional)
show_header = false # bool |  (optional) (default to false)

try:
    # Fetches all the information related to requested service channels.
    api_response = api_instance.api_v11_service_channel_list_get(guids=guids, show_header=show_header)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceChannelApi->api_v11_service_channel_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guids** | **str**| Comma separated list of guids. Max 100 can be added into list. | [optional] 
 **show_header** | **bool**|  | [optional] [default to false]

### Return type

[**list[V11VmOpenApiServiceChannels]**](V11VmOpenApiServiceChannels.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_channel_list_organization_get**
> V11VmOpenApiServiceChannelsWithPaging api_v11_service_channel_list_organization_get(organization_id=organization_id, code=code, oid=oid, page=page, show_header=show_header)

Fetches all the information of service channels related to certain organization. Either organizationId, code or oid needs to be added as a parameter.

<br>Notice! The returned itemList object includes items which can be one of the following: <i>V11VmOpenApiElectronicChannel</i> or <i>V11VmOpenApiPhoneChannel</i> or               <i>V11VmOpenApiPrintableFormChannel</i> or <i>V11VmOpenApiServiceLocationChannel</i> or <i>V11VmOpenApiWebPageChannel</i>  <br>The returned item type within itemList depends on the type of the channel. For example if the channel is phone channel then V11VmOpenApiPhoneChannel object is returned.  <br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                 \"id\": [                     \"Guid should contain 32 digits with 4 dashes (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx).\"                 ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceChannelApi()
organization_id = 'organization_id_example' # str | Organization guid. (optional)
code = 'code_example' # str | Organization business code. (optional)
oid = 'oid_example' # str | Organization oid. (optional)
page = 1 # int | The page to be fetched. (optional) (default to 1)
show_header = false # bool |  (optional) (default to false)

try:
    # Fetches all the information of service channels related to certain organization. Either organizationId, code or oid needs to be added as a parameter.
    api_response = api_instance.api_v11_service_channel_list_organization_get(organization_id=organization_id, code=code, oid=oid, page=page, show_header=show_header)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceChannelApi->api_v11_service_channel_list_organization_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization guid. | [optional] 
 **code** | **str**| Organization business code. | [optional] 
 **oid** | **str**| Organization oid. | [optional] 
 **page** | **int**| The page to be fetched. | [optional] [default to 1]
 **show_header** | **bool**|  | [optional] [default to false]

### Return type

[**V11VmOpenApiServiceChannelsWithPaging**](V11VmOpenApiServiceChannelsWithPaging.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_channel_organization_organization_id_get**
> V3VmOpenApiGuidPage api_v11_service_channel_organization_organization_id_get(organization_id, _date=_date, date_before=date_before, page=page)

Gets a list of published service channels for defined organization.  Service channels created/modified after certain date can be fetched by adding date as query string parameter.  Service channels created/modified before certain date can be fetched by adding dateBefore as query string parameter.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                 \"date\": [                     \"The value '-2' is not valid for Nullable`1.\",                     \"The date parameter is invalid.\"                 ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceChannelApi()
organization_id = 'organization_id_example' # str | Guid
_date = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
date_before = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
page = 1 # int | The page to be fetched. (optional) (default to 1)

try:
    # Gets a list of published service channels for defined organization.  Service channels created/modified after certain date can be fetched by adding date as query string parameter.  Service channels created/modified before certain date can be fetched by adding dateBefore as query string parameter.
    api_response = api_instance.api_v11_service_channel_organization_organization_id_get(organization_id, _date=_date, date_before=date_before, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceChannelApi->api_v11_service_channel_organization_organization_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Guid | 
 **_date** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **date_before** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **page** | **int**| The page to be fetched. | [optional] [default to 1]

### Return type

[**V3VmOpenApiGuidPage**](V3VmOpenApiGuidPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_channel_organization_organization_id_type_type_get**
> V3VmOpenApiGuidPage api_v11_service_channel_organization_organization_id_type_type_get(organization_id, type, _date=_date, date_before=date_before, page=page)

Gets a list of certain type of published service channels for defined organization.  Service channels created/modified after certain date can be fetched by adding date as query string parameter.  Service channels created/modified before certain date can be fetched by adding dateBefore as query string parameter.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                 \"type\": [                     \"The field is invalid. Please use one of these: 'EChannel, WebPage, PrintableForm, Phone, ServiceLocation'.\"                 ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceChannelApi()
organization_id = 'organization_id_example' # str | Guid
type = 'type_example' # str | Service channel type
_date = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
date_before = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
page = 1 # int | The page to be fetched. (optional) (default to 1)

try:
    # Gets a list of certain type of published service channels for defined organization.  Service channels created/modified after certain date can be fetched by adding date as query string parameter.  Service channels created/modified before certain date can be fetched by adding dateBefore as query string parameter.
    api_response = api_instance.api_v11_service_channel_organization_organization_id_type_type_get(organization_id, type, _date=_date, date_before=date_before, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceChannelApi->api_v11_service_channel_organization_organization_id_type_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Guid | 
 **type** | **str**| Service channel type | 
 **_date** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **date_before** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **page** | **int**| The page to be fetched. | [optional] [default to 1]

### Return type

[**V3VmOpenApiGuidPage**](V3VmOpenApiGuidPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_channel_phone_id_put**
> V11VmOpenApiPhoneChannel api_v11_service_channel_phone_id_put(id, body=body)

Updates phone channel with the data provided as input.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"ServiceChannelNames\":[                      \"The ServiceChannelNames field is required.\"                  ]              }              </code>

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
api_instance = swagger_client.ServiceChannelApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | phone channel id
body = swagger_client.V11VmOpenApiPhoneChannelInBase() # V11VmOpenApiPhoneChannelInBase | phone channel data (optional)

try:
    # Updates phone channel with the data provided as input.
    api_response = api_instance.api_v11_service_channel_phone_id_put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceChannelApi->api_v11_service_channel_phone_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| phone channel id | 
 **body** | [**V11VmOpenApiPhoneChannelInBase**](V11VmOpenApiPhoneChannelInBase.md)| phone channel data | [optional] 

### Return type

[**V11VmOpenApiPhoneChannel**](V11VmOpenApiPhoneChannel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_channel_phone_post**
> V11VmOpenApiPhoneChannel api_v11_service_channel_phone_post(body=body)

Creates a new phone channel with the data provided as input.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"ServiceChannelNames\":[                      \"The ServiceChannelNames field is required.\"                  ]              }              </code>

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
api_instance = swagger_client.ServiceChannelApi(swagger_client.ApiClient(configuration))
body = swagger_client.V11VmOpenApiPhoneChannelIn() # V11VmOpenApiPhoneChannelIn | The phone channel data. (optional)

try:
    # Creates a new phone channel with the data provided as input.
    api_response = api_instance.api_v11_service_channel_phone_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceChannelApi->api_v11_service_channel_phone_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V11VmOpenApiPhoneChannelIn**](V11VmOpenApiPhoneChannelIn.md)| The phone channel data. | [optional] 

### Return type

[**V11VmOpenApiPhoneChannel**](V11VmOpenApiPhoneChannel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_channel_phone_source_id_source_id_put**
> V11VmOpenApiPhoneChannel api_v11_service_channel_phone_source_id_source_id_put(source_id, body=body)

Updates phone channel with the data provided as input.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"ServiceChannelNames\":[                      \"The ServiceChannelNames field is required.\"                  ]              }              </code>

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
api_instance = swagger_client.ServiceChannelApi(swagger_client.ApiClient(configuration))
source_id = 'source_id_example' # str | phone channel external id
body = swagger_client.V11VmOpenApiPhoneChannelInBase() # V11VmOpenApiPhoneChannelInBase | phone channel data (optional)

try:
    # Updates phone channel with the data provided as input.
    api_response = api_instance.api_v11_service_channel_phone_source_id_source_id_put(source_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceChannelApi->api_v11_service_channel_phone_source_id_source_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| phone channel external id | 
 **body** | [**V11VmOpenApiPhoneChannelInBase**](V11VmOpenApiPhoneChannelInBase.md)| phone channel data | [optional] 

### Return type

[**V11VmOpenApiPhoneChannel**](V11VmOpenApiPhoneChannel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_channel_printable_form_id_put**
> V11VmOpenApiPrintableFormChannel api_v11_service_channel_printable_form_id_put(id, body=body)

Updates printable form channel with the data provided as input.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"ServiceChannelNames\":[                      \"The ServiceChannelNames field is required.\"                  ]              }              </code>

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
api_instance = swagger_client.ServiceChannelApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | printable form channel id
body = swagger_client.V10VmOpenApiPrintableFormChannelInBase() # V10VmOpenApiPrintableFormChannelInBase | printable form channel data (optional)

try:
    # Updates printable form channel with the data provided as input.
    api_response = api_instance.api_v11_service_channel_printable_form_id_put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceChannelApi->api_v11_service_channel_printable_form_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| printable form channel id | 
 **body** | [**V10VmOpenApiPrintableFormChannelInBase**](V10VmOpenApiPrintableFormChannelInBase.md)| printable form channel data | [optional] 

### Return type

[**V11VmOpenApiPrintableFormChannel**](V11VmOpenApiPrintableFormChannel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_channel_printable_form_post**
> V11VmOpenApiPrintableFormChannel api_v11_service_channel_printable_form_post(body=body)

Creates a new printable form channel with the data provided as input.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"ServiceChannelNames\":[                      \"The ServiceChannelNames field is required.\"                  ]              }              </code>

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
api_instance = swagger_client.ServiceChannelApi(swagger_client.ApiClient(configuration))
body = swagger_client.V10VmOpenApiPrintableFormChannelIn() # V10VmOpenApiPrintableFormChannelIn | The printable form channel data. (optional)

try:
    # Creates a new printable form channel with the data provided as input.
    api_response = api_instance.api_v11_service_channel_printable_form_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceChannelApi->api_v11_service_channel_printable_form_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V10VmOpenApiPrintableFormChannelIn**](V10VmOpenApiPrintableFormChannelIn.md)| The printable form channel data. | [optional] 

### Return type

[**V11VmOpenApiPrintableFormChannel**](V11VmOpenApiPrintableFormChannel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_channel_printable_form_source_id_source_id_put**
> V11VmOpenApiPrintableFormChannel api_v11_service_channel_printable_form_source_id_source_id_put(source_id, body=body)

Updates printable form channel with the data provided as input.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"ServiceChannelNames\":[                      \"The ServiceChannelNames field is required.\"                  ]              }              </code>

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
api_instance = swagger_client.ServiceChannelApi(swagger_client.ApiClient(configuration))
source_id = 'source_id_example' # str | printable form channel external source id
body = swagger_client.V10VmOpenApiPrintableFormChannelInBase() # V10VmOpenApiPrintableFormChannelInBase | printable form channel data (optional)

try:
    # Updates printable form channel with the data provided as input.
    api_response = api_instance.api_v11_service_channel_printable_form_source_id_source_id_put(source_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceChannelApi->api_v11_service_channel_printable_form_source_id_source_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| printable form channel external source id | 
 **body** | [**V10VmOpenApiPrintableFormChannelInBase**](V10VmOpenApiPrintableFormChannelInBase.md)| printable form channel data | [optional] 

### Return type

[**V11VmOpenApiPrintableFormChannel**](V11VmOpenApiPrintableFormChannel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_channel_service_location_id_put**
> V11VmOpenApiServiceLocationChannel api_v11_service_channel_service_location_id_put(id, body=body)

Updates service location channel with the data provided as input.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"ServiceChannelNames\":[                      \"The ServiceChannelNames field is required.\"                  ]              }              </code>

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
api_instance = swagger_client.ServiceChannelApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | service location channel id
body = swagger_client.V11VmOpenApiServiceLocationChannelInBase() # V11VmOpenApiServiceLocationChannelInBase | service location channel data. (optional)

try:
    # Updates service location channel with the data provided as input.
    api_response = api_instance.api_v11_service_channel_service_location_id_put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceChannelApi->api_v11_service_channel_service_location_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| service location channel id | 
 **body** | [**V11VmOpenApiServiceLocationChannelInBase**](V11VmOpenApiServiceLocationChannelInBase.md)| service location channel data. | [optional] 

### Return type

[**V11VmOpenApiServiceLocationChannel**](V11VmOpenApiServiceLocationChannel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_channel_service_location_post**
> V11VmOpenApiServiceLocationChannel api_v11_service_channel_service_location_post(body=body)

Creates a new service location channel with the data provided as input.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"ServiceChannelNames\":[                      \"The ServiceChannelNames field is required.\"                  ]              }              </code>

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
api_instance = swagger_client.ServiceChannelApi(swagger_client.ApiClient(configuration))
body = swagger_client.V11VmOpenApiServiceLocationChannelIn() # V11VmOpenApiServiceLocationChannelIn | The service location channel data. (optional)

try:
    # Creates a new service location channel with the data provided as input.
    api_response = api_instance.api_v11_service_channel_service_location_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceChannelApi->api_v11_service_channel_service_location_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V11VmOpenApiServiceLocationChannelIn**](V11VmOpenApiServiceLocationChannelIn.md)| The service location channel data. | [optional] 

### Return type

[**V11VmOpenApiServiceLocationChannel**](V11VmOpenApiServiceLocationChannel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_channel_service_location_source_id_source_id_put**
> V11VmOpenApiServiceLocationChannel api_v11_service_channel_service_location_source_id_source_id_put(source_id, body=body)

Updates service location channel with the data provided as input.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"ServiceChannelNames\":[                      \"The ServiceChannelNames field is required.\"                  ]              }              </code>

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
api_instance = swagger_client.ServiceChannelApi(swagger_client.ApiClient(configuration))
source_id = 'source_id_example' # str | service location channel external source id
body = swagger_client.V11VmOpenApiServiceLocationChannelInBase() # V11VmOpenApiServiceLocationChannelInBase | service location channel data (optional)

try:
    # Updates service location channel with the data provided as input.
    api_response = api_instance.api_v11_service_channel_service_location_source_id_source_id_put(source_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceChannelApi->api_v11_service_channel_service_location_source_id_source_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| service location channel external source id | 
 **body** | [**V11VmOpenApiServiceLocationChannelInBase**](V11VmOpenApiServiceLocationChannelInBase.md)| service location channel data | [optional] 

### Return type

[**V11VmOpenApiServiceLocationChannel**](V11VmOpenApiServiceLocationChannel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_channel_type_type_get**
> V3VmOpenApiGuidPage api_v11_service_channel_type_type_get(type, _date=_date, date_before=date_before, page=page)

Gets a list of certain type of published service channels.  Service channels created/modified after certain date can be fetched by adding date as query string parameter.  Service channels created/modified before certain date can be fetched by adding dateBefore as query string parameter.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                 \"type\": [                     \"The field is invalid. Please use one of these: 'EChannel, WebPage, PrintableForm, Phone, ServiceLocation'.\"                 ]              }              </code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceChannelApi()
type = 'type_example' # str | Service channel type
_date = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
date_before = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
page = 1 # int | The page to be fetched. (optional) (default to 1)

try:
    # Gets a list of certain type of published service channels.  Service channels created/modified after certain date can be fetched by adding date as query string parameter.  Service channels created/modified before certain date can be fetched by adding dateBefore as query string parameter.
    api_response = api_instance.api_v11_service_channel_type_type_get(type, _date=_date, date_before=date_before, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceChannelApi->api_v11_service_channel_type_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Service channel type | 
 **_date** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **date_before** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **page** | **int**| The page to be fetched. | [optional] [default to 1]

### Return type

[**V3VmOpenApiGuidPage**](V3VmOpenApiGuidPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_channel_web_page_id_put**
> V11VmOpenApiWebPageChannel api_v11_service_channel_web_page_id_put(id, body=body)

Updates webpage channel with the data provided as input.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"ServiceChannelNames\":[                      \"The ServiceChannelNames field is required.\"                  ]              }              </code>

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
api_instance = swagger_client.ServiceChannelApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | web page channel id
body = swagger_client.V10VmOpenApiWebPageChannelInBase() # V10VmOpenApiWebPageChannelInBase | web page channel data (optional)

try:
    # Updates webpage channel with the data provided as input.
    api_response = api_instance.api_v11_service_channel_web_page_id_put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceChannelApi->api_v11_service_channel_web_page_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| web page channel id | 
 **body** | [**V10VmOpenApiWebPageChannelInBase**](V10VmOpenApiWebPageChannelInBase.md)| web page channel data | [optional] 

### Return type

[**V11VmOpenApiWebPageChannel**](V11VmOpenApiWebPageChannel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_channel_web_page_post**
> V11VmOpenApiWebPageChannel api_v11_service_channel_web_page_post(body=body)

Creates a new web page channel with the data provided as input.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"ServiceChannelNames\":[                      \"The ServiceChannelNames field is required.\"                  ]              }              </code>

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
api_instance = swagger_client.ServiceChannelApi(swagger_client.ApiClient(configuration))
body = swagger_client.V10VmOpenApiWebPageChannelIn() # V10VmOpenApiWebPageChannelIn | The web page channel data. (optional)

try:
    # Creates a new web page channel with the data provided as input.
    api_response = api_instance.api_v11_service_channel_web_page_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceChannelApi->api_v11_service_channel_web_page_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V10VmOpenApiWebPageChannelIn**](V10VmOpenApiWebPageChannelIn.md)| The web page channel data. | [optional] 

### Return type

[**V11VmOpenApiWebPageChannel**](V11VmOpenApiWebPageChannel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_service_channel_web_page_source_id_source_id_put**
> V11VmOpenApiWebPageChannel api_v11_service_channel_web_page_source_id_source_id_put(source_id, body=body)

Updates webpage channel with the data provided as input.

<br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages.  <code>              {                  \"ServiceChannelNames\":[                      \"The ServiceChannelNames field is required.\"                  ]              }              </code>

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
api_instance = swagger_client.ServiceChannelApi(swagger_client.ApiClient(configuration))
source_id = 'source_id_example' # str | web page channel external source id
body = swagger_client.V10VmOpenApiWebPageChannelInBase() # V10VmOpenApiWebPageChannelInBase | web page channel data (optional)

try:
    # Updates webpage channel with the data provided as input.
    api_response = api_instance.api_v11_service_channel_web_page_source_id_source_id_put(source_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceChannelApi->api_v11_service_channel_web_page_source_id_source_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| web page channel external source id | 
 **body** | [**V10VmOpenApiWebPageChannelInBase**](V10VmOpenApiWebPageChannelInBase.md)| web page channel data | [optional] 

### Return type

[**V11VmOpenApiWebPageChannel**](V11VmOpenApiWebPageChannel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

