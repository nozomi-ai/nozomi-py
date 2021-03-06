# coding: utf-8

"""
    Nozomi API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.request_property_api import RequestPropertyApi  # noqa: E501
from swagger_client.rest import ApiException


class TestRequestPropertyApi(unittest.TestCase):
    """RequestPropertyApi unit test stubs"""

    def setUp(self):
        self.api = RequestPropertyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_request_property_all_by_request_get(self):
        """Test case for request_property_all_by_request_get

        Obtain all analysed components you have created, relative to that specific request.  # noqa: E501
        """
        pass

    def test_request_property_all_get(self):
        """Test case for request_property_all_get

        Obtain all request properties you have created/own.  # noqa: E501
        """
        pass

    def test_request_property_create_post(self):
        """Test case for request_property_create_post

        Create a request property.  # noqa: E501
        """
        pass

    def test_request_property_delete_guid_delete(self):
        """Test case for request_property_delete_guid_delete

        Delete a request property  # noqa: E501
        """
        pass

    def test_request_property_update_put(self):
        """Test case for request_property_update_put

        Update a request property.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
