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


class ComputeValueApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def compute_value_all_index_get(self, index, **kwargs):  # noqa: E501
        """Obtain all compute value generated.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compute_value_all_index_get(index, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int index: The 'page' of the list of results in x (required)
        :param str compute_guid: The compute guid relating to the values in question, optional.
        :return: ComputeValueViewModelIEnumerablePaginatedViewModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.compute_value_all_index_get_with_http_info(index, **kwargs)  # noqa: E501
        else:
            (data) = self.compute_value_all_index_get_with_http_info(index, **kwargs)  # noqa: E501
            return data

    def compute_value_all_index_get_with_http_info(self, index, **kwargs):  # noqa: E501
        """Obtain all compute value generated.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compute_value_all_index_get_with_http_info(index, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int index: The 'page' of the list of results in x (required)
        :param str compute_guid: The compute guid relating to the values in question, optional.
        :return: ComputeValueViewModelIEnumerablePaginatedViewModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['index', 'compute_guid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method compute_value_all_index_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'index' is set
        if ('index' not in params or
                params['index'] is None):
            raise ValueError("Missing the required parameter `index` when calling `compute_value_all_index_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'index' in params:
            path_params['index'] = params['index']  # noqa: E501

        query_params = []
        if 'compute_guid' in params:
            query_params.append(('computeGuid', params['compute_guid']))  # noqa: E501

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
            '/ComputeValue/All/{index}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ComputeValueViewModelIEnumerablePaginatedViewModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def compute_value_get_guid_get(self, guid, **kwargs):  # noqa: E501
        """Obtain the compute value specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compute_value_get_guid_get(guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str guid: The guid of the compute value in question. (required)
        :return: ComputeValueViewModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.compute_value_get_guid_get_with_http_info(guid, **kwargs)  # noqa: E501
        else:
            (data) = self.compute_value_get_guid_get_with_http_info(guid, **kwargs)  # noqa: E501
            return data

    def compute_value_get_guid_get_with_http_info(self, guid, **kwargs):  # noqa: E501
        """Obtain the compute value specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compute_value_get_guid_get_with_http_info(guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str guid: The guid of the compute value in question. (required)
        :return: ComputeValueViewModel
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
                    " to method compute_value_get_guid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'guid' is set
        if ('guid' not in params or
                params['guid'] is None):
            raise ValueError("Missing the required parameter `guid` when calling `compute_value_get_guid_get`")  # noqa: E501

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
            '/ComputeValue/Get/{guid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ComputeValueViewModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def compute_value_last_compute_guid_get(self, compute_guid, **kwargs):  # noqa: E501
        """Obtain the last compute value of the compute in question.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compute_value_last_compute_guid_get(compute_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str compute_guid: The compute in question. (required)
        :return: ComputeValueViewModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.compute_value_last_compute_guid_get_with_http_info(compute_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.compute_value_last_compute_guid_get_with_http_info(compute_guid, **kwargs)  # noqa: E501
            return data

    def compute_value_last_compute_guid_get_with_http_info(self, compute_guid, **kwargs):  # noqa: E501
        """Obtain the last compute value of the compute in question.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compute_value_last_compute_guid_get_with_http_info(compute_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str compute_guid: The compute in question. (required)
        :return: ComputeValueViewModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['compute_guid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method compute_value_last_compute_guid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'compute_guid' is set
        if ('compute_guid' not in params or
                params['compute_guid'] is None):
            raise ValueError("Missing the required parameter `compute_guid` when calling `compute_value_last_compute_guid_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'compute_guid' in params:
            path_params['computeGuid'] = params['compute_guid']  # noqa: E501

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
            '/ComputeValue/Last/{computeGuid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ComputeValueViewModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
