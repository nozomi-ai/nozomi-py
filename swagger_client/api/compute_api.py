# coding: utf-8

"""
    Nozomi API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ComputeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def compute_all_index_get(self, index, **kwargs):  # noqa: E501
        """Obtains all of the relevant computes you own.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compute_all_index_get(index, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int index: The 'page' of the list of results of every x items. (required)
        :return: ComputeViewModelIEnumerablePaginatedViewModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.compute_all_index_get_with_http_info(index, **kwargs)  # noqa: E501
        else:
            (data) = self.compute_all_index_get_with_http_info(index, **kwargs)  # noqa: E501
            return data

    def compute_all_index_get_with_http_info(self, index, **kwargs):  # noqa: E501
        """Obtains all of the relevant computes you own.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compute_all_index_get_with_http_info(index, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int index: The 'page' of the list of results of every x items. (required)
        :return: ComputeViewModelIEnumerablePaginatedViewModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['index']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method compute_all_index_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'index' is set
        if ('index' not in params or
                params['index'] is None):
            raise ValueError("Missing the required parameter `index` when calling `compute_all_index_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'index' in params:
            path_params['index'] = params['index']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API Key']  # noqa: E501

        return self.api_client.call_api(
            '/Compute/All/{index}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ComputeViewModelIEnumerablePaginatedViewModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def compute_get_guid_get(self, guid, **kwargs):  # noqa: E501
        """Obtains the specific compute.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compute_get_guid_get(guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str guid: The Guid of the compute in question. (required)
        :return: ComputeViewModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.compute_get_guid_get_with_http_info(guid, **kwargs)  # noqa: E501
        else:
            (data) = self.compute_get_guid_get_with_http_info(guid, **kwargs)  # noqa: E501
            return data

    def compute_get_guid_get_with_http_info(self, guid, **kwargs):  # noqa: E501
        """Obtains the specific compute.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compute_get_guid_get_with_http_info(guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str guid: The Guid of the compute in question. (required)
        :return: ComputeViewModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['guid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method compute_get_guid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'guid' is set
        if ('guid' not in params or
                params['guid'] is None):
            raise ValueError("Missing the required parameter `guid` when calling `compute_get_guid_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'guid' in params:
            path_params['guid'] = params['guid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API Key']  # noqa: E501

        return self.api_client.call_api(
            '/Compute/Get/{guid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ComputeViewModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
