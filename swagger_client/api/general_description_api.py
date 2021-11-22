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


class GeneralDescriptionApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v11_general_description_get(self, **kwargs):  # noqa: E501
        """Gets all the statutory service general descriptions within PTV as a list of ids and names.  General descriptions created/modified after certain date can be fetched by adding date as query string parameter.  General descriptions created/modified before certain date can be fetched by adding dateBefore as query string parameter.  # noqa: E501

        <br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages. Below sample response.  <code>              {                  \"Names\": [                      \"Type - Required value 'Name' was not found!\"                  ]              }              </code>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v11_general_description_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime _date: Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC).
        :param datetime date_before: Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC).
        :param int page: The page to be fetched. Page numbering starts from one.
        :return: V3VmOpenApiGuidPage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v11_general_description_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v11_general_description_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v11_general_description_get_with_http_info(self, **kwargs):  # noqa: E501
        """Gets all the statutory service general descriptions within PTV as a list of ids and names.  General descriptions created/modified after certain date can be fetched by adding date as query string parameter.  General descriptions created/modified before certain date can be fetched by adding dateBefore as query string parameter.  # noqa: E501

        <br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages. Below sample response.  <code>              {                  \"Names\": [                      \"Type - Required value 'Name' was not found!\"                  ]              }              </code>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v11_general_description_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime _date: Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC).
        :param datetime date_before: Supports only format \"yyyy-MM-ddTHH:mm:ss\" (UTC).
        :param int page: The page to be fetched. Page numbering starts from one.
        :return: V3VmOpenApiGuidPage
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
                    " to method api_v11_general_description_get" % key
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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v11/GeneralDescription', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V3VmOpenApiGuidPage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v11_general_description_id_get(self, id, **kwargs):  # noqa: E501
        """Fetches all the information related to a single statutory service general description.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v11_general_description_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Statutory service general description guid (id of the entity) to fetch. (required)
        :param bool show_header:
        :return: V10VmOpenApiGeneralDescription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v11_general_description_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v11_general_description_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def api_v11_general_description_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Fetches all the information related to a single statutory service general description.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v11_general_description_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Statutory service general description guid (id of the entity) to fetch. (required)
        :param bool show_header:
        :return: V10VmOpenApiGeneralDescription
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'show_header']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v11_general_description_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_v11_general_description_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'show_header' in params:
            query_params.append(('showHeader', params['show_header']))  # noqa: E501

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
            '/api/v11/GeneralDescription/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V10VmOpenApiGeneralDescription',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v11_general_description_id_put(self, id, **kwargs):  # noqa: E501
        """Updates the defined general description with the data provided as input.  # noqa: E501

        <br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages. Below sample response.  <code>              {                  \"Names\": [                      \"Type - Required value 'Name' was not found!\"                  ]              }              </code>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v11_general_description_id_put(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Statutory service general description identifier (required)
        :param V10VmOpenApiGeneralDescriptionInBase body: The general description data.
        :return: V10VmOpenApiGeneralDescription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v11_general_description_id_put_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v11_general_description_id_put_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def api_v11_general_description_id_put_with_http_info(self, id, **kwargs):  # noqa: E501
        """Updates the defined general description with the data provided as input.  # noqa: E501

        <br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages. Below sample response.  <code>              {                  \"Names\": [                      \"Type - Required value 'Name' was not found!\"                  ]              }              </code>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v11_general_description_id_put_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Statutory service general description identifier (required)
        :param V10VmOpenApiGeneralDescriptionInBase body: The general description data.
        :return: V10VmOpenApiGeneralDescription
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v11_general_description_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_v11_general_description_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/v11/GeneralDescription/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V10VmOpenApiGeneralDescription',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v11_general_description_list_get(self, **kwargs):  # noqa: E501
        """Fetches all the information related to requested statutory service general descriptions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v11_general_description_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str guids: Comma separated list of guids. Max 100 can be added into list.
        :param bool show_header:
        :return: list[V10VmOpenApiGeneralDescription]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v11_general_description_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v11_general_description_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v11_general_description_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """Fetches all the information related to requested statutory service general descriptions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v11_general_description_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str guids: Comma separated list of guids. Max 100 can be added into list.
        :param bool show_header:
        :return: list[V10VmOpenApiGeneralDescription]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['guids', 'show_header']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v11_general_description_list_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'guids' in params:
            query_params.append(('guids', params['guids']))  # noqa: E501
        if 'show_header' in params:
            query_params.append(('showHeader', params['show_header']))  # noqa: E501

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
            '/api/v11/GeneralDescription/list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[V10VmOpenApiGeneralDescription]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v11_general_description_new_gd_list_get(self, **kwargs):  # noqa: E501
        """Gets the new statutory service general descriptions within PTV as a list of ids and names.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v11_general_description_new_gd_list_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page to be fetched. Page numbering starts from one.
        :return: V3VmOpenApiGuidPage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v11_general_description_new_gd_list_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v11_general_description_new_gd_list_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v11_general_description_new_gd_list_get_with_http_info(self, **kwargs):  # noqa: E501
        """Gets the new statutory service general descriptions within PTV as a list of ids and names.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v11_general_description_new_gd_list_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page to be fetched. Page numbering starts from one.
        :return: V3VmOpenApiGuidPage
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
                    " to method api_v11_general_description_new_gd_list_get" % key
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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v11/GeneralDescription/newGdList', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V3VmOpenApiGuidPage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v11_general_description_post(self, **kwargs):  # noqa: E501
        """Creates a new general description with the data provided as input.  # noqa: E501

        <br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages. Below sample response.  <code>              {                  \"Names\": [                      \"Type - Required value 'Name' was not found!\"                  ]              }              </code>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v11_general_description_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V10VmOpenApiGeneralDescriptionIn body: The general description data.
        :return: V10VmOpenApiGeneralDescription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v11_general_description_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v11_general_description_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v11_general_description_post_with_http_info(self, **kwargs):  # noqa: E501
        """Creates a new general description with the data provided as input.  # noqa: E501

        <br>HTTP status code 400 response model is a dictionary where key is property name and value is a list of error messages. Below sample response.  <code>              {                  \"Names\": [                      \"Type - Required value 'Name' was not found!\"                  ]              }              </code>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v11_general_description_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V10VmOpenApiGeneralDescriptionIn body: The general description data.
        :return: V10VmOpenApiGeneralDescription
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v11_general_description_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/v11/GeneralDescription', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V10VmOpenApiGeneralDescription',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
