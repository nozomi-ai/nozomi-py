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


class ComponentHistoricItemApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def component_historic_item_all_component_guid_get(self, component_guid, **kwargs):  # noqa: E501
        """Obtain all the component historical values created  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.component_historic_item_all_component_guid_get(component_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str component_guid: The unique identifier of the component. (required)
        :param int index: The 'page' of the list of results in 100s.
        :return: ComponentHistoricItemViewModelIEnumerablePaginatedViewModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.component_historic_item_all_component_guid_get_with_http_info(component_guid, **kwargs)  # noqa: E501
        else:
            (data) = self.component_historic_item_all_component_guid_get_with_http_info(component_guid, **kwargs)  # noqa: E501
            return data

    def component_historic_item_all_component_guid_get_with_http_info(self, component_guid, **kwargs):  # noqa: E501
        """Obtain all the component historical values created  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.component_historic_item_all_component_guid_get_with_http_info(component_guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str component_guid: The unique identifier of the component. (required)
        :param int index: The 'page' of the list of results in 100s.
        :return: ComponentHistoricItemViewModelIEnumerablePaginatedViewModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['component_guid', 'index']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method component_historic_item_all_component_guid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'component_guid' is set
        if ('component_guid' not in params or
                params['component_guid'] is None):
            raise ValueError("Missing the required parameter `component_guid` when calling `component_historic_item_all_component_guid_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'component_guid' in params:
            path_params['componentGuid'] = params['component_guid']  # noqa: E501

        query_params = []
        if 'index' in params:
            query_params.append(('index', params['index']))  # noqa: E501

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
            '/ComponentHistoricItem/All/{componentGuid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ComponentHistoricItemViewModelIEnumerablePaginatedViewModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)