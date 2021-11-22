# swagger_client.CommonApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v11_common_channels_without_services_get**](CommonApi.md#api_v11_common_channels_without_services_get) | **GET** /api/v11/Common/ChannelsWithoutServices | Gets information of user&#x27;s organization&#x27;s channels that have no connections to services.
[**api_v11_common_entities_by_organization_organization_id_get**](CommonApi.md#api_v11_common_entities_by_organization_organization_id_get) | **GET** /api/v11/Common/EntitiesByOrganization/{organizationId} | Gets a list of published services and service channels by organization.  Services/channels created/modified after certain date can be fetched by adding date as query string parameter.  Services/channels created/modified before certain date can be fetched by adding dateBefore as query string parameter.
[**api_v11_common_expiring_service_channels_get**](CommonApi.md#api_v11_common_expiring_service_channels_get) | **GET** /api/v11/Common/ExpiringServiceChannels | Gets information of user&#x27;s organization&#x27;s expiring service channels.
[**api_v11_common_not_maintained_service_channels_get**](CommonApi.md#api_v11_common_not_maintained_service_channels_get) | **GET** /api/v11/Common/NotMaintainedServiceChannels | Gets information of user&#x27;s organization&#x27;s not updated channels.
[**api_v11_common_not_maintained_services_get**](CommonApi.md#api_v11_common_not_maintained_services_get) | **GET** /api/v11/Common/NotMaintainedServices | Gets information of user&#x27;s organization&#x27;s not updated services.
[**api_v11_common_services_without_channels_get**](CommonApi.md#api_v11_common_services_without_channels_get) | **GET** /api/v11/Common/ServicesWithoutChannels | Gets information of user&#x27;s organization&#x27;s services that have no connections to channels.
[**api_v11_common_translation_get**](CommonApi.md#api_v11_common_translation_get) | **GET** /api/v11/Common/Translation | Gets information of translation processes within PTV.  Translation items created/modified after certain date can be fetched by adding date as query string parameter.  Translation items created/modified before certain date can be fetched by adding dateBefore as query string parameter.

# **api_v11_common_channels_without_services_get**
> VmOpenApiTasks api_v11_common_channels_without_services_get(page=page)

Gets information of user's organization's channels that have no connections to services.

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
api_instance = swagger_client.CommonApi(swagger_client.ApiClient(configuration))
page = 1 # int | The page number to be fetched. (optional) (default to 1)

try:
    # Gets information of user's organization's channels that have no connections to services.
    api_response = api_instance.api_v11_common_channels_without_services_get(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonApi->api_v11_common_channels_without_services_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page number to be fetched. | [optional] [default to 1]

### Return type

[**VmOpenApiTasks**](VmOpenApiTasks.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_common_entities_by_organization_organization_id_get**
> VmOpenApiEntityGuidPage api_v11_common_entities_by_organization_organization_id_get(organization_id, _date=_date, date_before=date_before, page=page)

Gets a list of published services and service channels by organization.  Services/channels created/modified after certain date can be fetched by adding date as query string parameter.  Services/channels created/modified before certain date can be fetched by adding dateBefore as query string parameter.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommonApi()
organization_id = 'organization_id_example' # str | Guid
_date = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
date_before = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
page = 1 # int | The page number to be fetched. (optional) (default to 1)

try:
    # Gets a list of published services and service channels by organization.  Services/channels created/modified after certain date can be fetched by adding date as query string parameter.  Services/channels created/modified before certain date can be fetched by adding dateBefore as query string parameter.
    api_response = api_instance.api_v11_common_entities_by_organization_organization_id_get(organization_id, _date=_date, date_before=date_before, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonApi->api_v11_common_entities_by_organization_organization_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Guid | 
 **_date** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **date_before** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **page** | **int**| The page number to be fetched. | [optional] [default to 1]

### Return type

[**VmOpenApiEntityGuidPage**](VmOpenApiEntityGuidPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_common_expiring_service_channels_get**
> VmOpenApiExpiringTask api_v11_common_expiring_service_channels_get(page=page, status=status)

Gets information of user's organization's expiring service channels.

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
api_instance = swagger_client.CommonApi(swagger_client.ApiClient(configuration))
page = 1 # int | The page number to be fetched. (optional) (default to 1)
status = 'Published' # str | Set status to get items either in published or draft state. (optional) (default to Published)

try:
    # Gets information of user's organization's expiring service channels.
    api_response = api_instance.api_v11_common_expiring_service_channels_get(page=page, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonApi->api_v11_common_expiring_service_channels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page number to be fetched. | [optional] [default to 1]
 **status** | **str**| Set status to get items either in published or draft state. | [optional] [default to Published]

### Return type

[**VmOpenApiExpiringTask**](VmOpenApiExpiringTask.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_common_not_maintained_service_channels_get**
> VmOpenApiNotUpdatedTask api_v11_common_not_maintained_service_channels_get(page=page, status=status)

Gets information of user's organization's not updated channels.

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
api_instance = swagger_client.CommonApi(swagger_client.ApiClient(configuration))
page = 1 # int | The page number to be fetched. (optional) (default to 1)
status = 'Published' # str | Set status to get items either in published or draft state. (optional) (default to Published)

try:
    # Gets information of user's organization's not updated channels.
    api_response = api_instance.api_v11_common_not_maintained_service_channels_get(page=page, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonApi->api_v11_common_not_maintained_service_channels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page number to be fetched. | [optional] [default to 1]
 **status** | **str**| Set status to get items either in published or draft state. | [optional] [default to Published]

### Return type

[**VmOpenApiNotUpdatedTask**](VmOpenApiNotUpdatedTask.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_common_not_maintained_services_get**
> VmOpenApiNotUpdatedTask api_v11_common_not_maintained_services_get(page=page, status=status)

Gets information of user's organization's not updated services.

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
api_instance = swagger_client.CommonApi(swagger_client.ApiClient(configuration))
page = 1 # int | The page number to be fetched. (optional) (default to 1)
status = 'Published' # str | Set status to get items either in published or draft state. (optional) (default to Published)

try:
    # Gets information of user's organization's not updated services.
    api_response = api_instance.api_v11_common_not_maintained_services_get(page=page, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonApi->api_v11_common_not_maintained_services_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page number to be fetched. | [optional] [default to 1]
 **status** | **str**| Set status to get items either in published or draft state. | [optional] [default to Published]

### Return type

[**VmOpenApiNotUpdatedTask**](VmOpenApiNotUpdatedTask.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_common_services_without_channels_get**
> VmOpenApiTasks api_v11_common_services_without_channels_get(page=page)

Gets information of user's organization's services that have no connections to channels.

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
api_instance = swagger_client.CommonApi(swagger_client.ApiClient(configuration))
page = 1 # int | The page number to be fetched. (optional) (default to 1)

try:
    # Gets information of user's organization's services that have no connections to channels.
    api_response = api_instance.api_v11_common_services_without_channels_get(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonApi->api_v11_common_services_without_channels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page number to be fetched. | [optional] [default to 1]

### Return type

[**VmOpenApiTasks**](VmOpenApiTasks.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v11_common_translation_get**
> VmOpenApiTranslationItemsPage api_v11_common_translation_get(_date=_date, date_before=date_before, page=page)

Gets information of translation processes within PTV.  Translation items created/modified after certain date can be fetched by adding date as query string parameter.  Translation items created/modified before certain date can be fetched by adding dateBefore as query string parameter.

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
api_instance = swagger_client.CommonApi(swagger_client.ApiClient(configuration))
_date = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
date_before = '2013-10-20T19:20:30+01:00' # datetime | Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC). (optional)
page = 1 # int | The page number to be fetched. (optional) (default to 1)

try:
    # Gets information of translation processes within PTV.  Translation items created/modified after certain date can be fetched by adding date as query string parameter.  Translation items created/modified before certain date can be fetched by adding dateBefore as query string parameter.
    api_response = api_instance.api_v11_common_translation_get(_date=_date, date_before=date_before, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonApi->api_v11_common_translation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **date_before** | **datetime**| Supports only format \&quot;yyyy-MM-ddTHH:mm:ss\&quot; (UTC). | [optional] 
 **page** | **int**| The page number to be fetched. | [optional] [default to 1]

### Return type

[**VmOpenApiTranslationItemsPage**](VmOpenApiTranslationItemsPage.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

