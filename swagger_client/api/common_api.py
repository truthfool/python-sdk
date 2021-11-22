# coding: utf-8

"""
    PTV Open Api version 11

    Here you can see listed all the PTV Open Api methods.  # noqa: E501

    OpenAPI spec version: v11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class CommonApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v11_common_channels_without_services_get(self, **kwargs):  # noqa: E501
        """Gets information of user's organization's channels that have no connections to services.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v11_common_channels_without_services_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page number to be fetched.
        :return: VmOpenApiTasks
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v11_common_channels_without_services_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v11_common_channels_without_services_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v11_common_channels_without_services_get_with_http_info(self, **kwargs):  # noqa: E501
        """Gets information of user's organization's channels that have no connections to services.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v11_common_channels_without_services_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page number to be fetched.
        :return: VmOpenApiTasks
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v11_common_channels_without_services_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/v11/Common/ChannelsWithoutServices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VmOpenApiTasks',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v11_common_entities_by_organization_organization_id_get(self, organization_id, **kwargs):  # noqa: E501
        """Gets a list of published services and service channels by organization.  Services/channels created/modified after certain date can be fetched by adding date as query string parameter.  Services/channels created/modified before certain date can be fetched by adding dateBefore as query string parameter.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v11_common_entities_by_organization_organization_id_get(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_id: Guid (required)
        :param datetime _date: Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC).
        :param datetime date_before: Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC).
        :param int page: The page number to be fetched.
        :return: VmOpenApiEntityGuidPage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v11_common_entities_by_organization_organization_id_get_with_http_info(organization_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v11_common_entities_by_organization_organization_id_get_with_http_info(organization_id, **kwargs)  # noqa: E501
            return data

    def api_v11_common_entities_by_organization_organization_id_get_with_http_info(self, organization_id, **kwargs):  # noqa: E501
        """Gets a list of published services and service channels by organization.  Services/channels created/modified after certain date can be fetched by adding date as query string parameter.  Services/channels created/modified before certain date can be fetched by adding dateBefore as query string parameter.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v11_common_entities_by_organization_organization_id_get_with_http_info(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization_id: Guid (required)
        :param datetime _date: Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC).
        :param datetime date_before: Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC).
        :param int page: The page number to be fetched.
        :return: VmOpenApiEntityGuidPage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization_id', '_date', 'date_before', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v11_common_entities_by_organization_organization_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization_id' is set
        if ('organization_id' not in params or
                params['organization_id'] is None):
            raise ValueError("Missing the required parameter `organization_id` when calling `api_v11_common_entities_by_organization_organization_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_id' in params:
            path_params['organizationId'] = params['organization_id']  # noqa: E501

        query_params = []
        if '_date' in params:
            query_params.append(('date', params['_date']))  # noqa: E501
        if 'date_before' in params:
            query_params.append(('dateBefore', params['date_before']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v11/Common/EntitiesByOrganization/{organizationId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VmOpenApiEntityGuidPage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v11_common_expiring_service_channels_get(self, **kwargs):  # noqa: E501
        """Gets information of user's organization's expiring service channels.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v11_common_expiring_service_channels_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page number to be fetched.
        :param str status: Set status to get items either in published or draft state.
        :return: VmOpenApiExpiringTask
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v11_common_expiring_service_channels_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v11_common_expiring_service_channels_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v11_common_expiring_service_channels_get_with_http_info(self, **kwargs):  # noqa: E501
        """Gets information of user's organization's expiring service channels.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v11_common_expiring_service_channels_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page number to be fetched.
        :param str status: Set status to get items either in published or draft state.
        :return: VmOpenApiExpiringTask
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'status']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v11_common_expiring_service_channels_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/v11/Common/ExpiringServiceChannels', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VmOpenApiExpiringTask',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v11_common_not_maintained_service_channels_get(self, **kwargs):  # noqa: E501
        """Gets information of user's organization's not updated channels.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v11_common_not_maintained_service_channels_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page number to be fetched.
        :param str status: Set status to get items either in published or draft state.
        :return: VmOpenApiNotUpdatedTask
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v11_common_not_maintained_service_channels_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v11_common_not_maintained_service_channels_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v11_common_not_maintained_service_channels_get_with_http_info(self, **kwargs):  # noqa: E501
        """Gets information of user's organization's not updated channels.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v11_common_not_maintained_service_channels_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page number to be fetched.
        :param str status: Set status to get items either in published or draft state.
        :return: VmOpenApiNotUpdatedTask
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'status']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v11_common_not_maintained_service_channels_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/v11/Common/NotMaintainedServiceChannels', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VmOpenApiNotUpdatedTask',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v11_common_not_maintained_services_get(self, **kwargs):  # noqa: E501
        """Gets information of user's organization's not updated services.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v11_common_not_maintained_services_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page number to be fetched.
        :param str status: Set status to get items either in published or draft state.
        :return: VmOpenApiNotUpdatedTask
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v11_common_not_maintained_services_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v11_common_not_maintained_services_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v11_common_not_maintained_services_get_with_http_info(self, **kwargs):  # noqa: E501
        """Gets information of user's organization's not updated services.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v11_common_not_maintained_services_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page number to be fetched.
        :param str status: Set status to get items either in published or draft state.
        :return: VmOpenApiNotUpdatedTask
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'status']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v11_common_not_maintained_services_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/v11/Common/NotMaintainedServices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VmOpenApiNotUpdatedTask',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v11_common_services_without_channels_get(self, **kwargs):  # noqa: E501
        """Gets information of user's organization's services that have no connections to channels.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v11_common_services_without_channels_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page number to be fetched.
        :return: VmOpenApiTasks
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v11_common_services_without_channels_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v11_common_services_without_channels_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v11_common_services_without_channels_get_with_http_info(self, **kwargs):  # noqa: E501
        """Gets information of user's organization's services that have no connections to channels.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v11_common_services_without_channels_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page number to be fetched.
        :return: VmOpenApiTasks
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v11_common_services_without_channels_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/v11/Common/ServicesWithoutChannels', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VmOpenApiTasks',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v11_common_translation_get(self, **kwargs):  # noqa: E501
        """Gets information of translation processes within PTV.  Translation items created/modified after certain date can be fetched by adding date as query string parameter.  Translation items created/modified before certain date can be fetched by adding dateBefore as query string parameter.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v11_common_translation_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime _date: Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC).
        :param datetime date_before: Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC).
        :param int page: The page number to be fetched.
        :return: VmOpenApiTranslationItemsPage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v11_common_translation_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v11_common_translation_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v11_common_translation_get_with_http_info(self, **kwargs):  # noqa: E501
        """Gets information of translation processes within PTV.  Translation items created/modified after certain date can be fetched by adding date as query string parameter.  Translation items created/modified before certain date can be fetched by adding dateBefore as query string parameter.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v11_common_translation_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime _date: Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC).
        :param datetime date_before: Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC).
        :param int page: The page number to be fetched.
        :return: VmOpenApiTranslationItemsPage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['_date', 'date_before', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v11_common_translation_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if '_date' in params:
            query_params.append(('date', params['_date']))  # noqa: E501
        if 'date_before' in params:
            query_params.append(('dateBefore', params['date_before']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/v11/Common/Translation', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VmOpenApiTranslationItemsPage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
