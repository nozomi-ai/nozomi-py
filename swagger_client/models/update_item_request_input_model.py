# coding: utf-8

"""
    Nozomi API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UpdateItemRequestInputModel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'guid': 'str',
        'request_id': 'int',
        'request': 'RequestViewModel',
        'item_guid': 'str',
        'item': 'ItemViewModel',
        'is_enabled': 'bool',
        'is_deleted': 'bool',
        'permanent_deletion': 'bool'
    }

    attribute_map = {
        'guid': 'guid',
        'request_id': 'requestId',
        'request': 'request',
        'item_guid': 'itemGuid',
        'item': 'item',
        'is_enabled': 'isEnabled',
        'is_deleted': 'isDeleted',
        'permanent_deletion': 'permanentDeletion'
    }

    def __init__(self, guid=None, request_id=None, request=None, item_guid=None, item=None, is_enabled=None, is_deleted=None, permanent_deletion=None):  # noqa: E501
        """UpdateItemRequestInputModel - a model defined in Swagger"""  # noqa: E501
        self._guid = None
        self._request_id = None
        self._request = None
        self._item_guid = None
        self._item = None
        self._is_enabled = None
        self._is_deleted = None
        self._permanent_deletion = None
        self.discriminator = None
        if guid is not None:
            self.guid = guid
        if request_id is not None:
            self.request_id = request_id
        if request is not None:
            self.request = request
        if item_guid is not None:
            self.item_guid = item_guid
        if item is not None:
            self.item = item
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if permanent_deletion is not None:
            self.permanent_deletion = permanent_deletion

    @property
    def guid(self):
        """Gets the guid of this UpdateItemRequestInputModel.  # noqa: E501


        :return: The guid of this UpdateItemRequestInputModel.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this UpdateItemRequestInputModel.


        :param guid: The guid of this UpdateItemRequestInputModel.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def request_id(self):
        """Gets the request_id of this UpdateItemRequestInputModel.  # noqa: E501


        :return: The request_id of this UpdateItemRequestInputModel.  # noqa: E501
        :rtype: int
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this UpdateItemRequestInputModel.


        :param request_id: The request_id of this UpdateItemRequestInputModel.  # noqa: E501
        :type: int
        """

        self._request_id = request_id

    @property
    def request(self):
        """Gets the request of this UpdateItemRequestInputModel.  # noqa: E501


        :return: The request of this UpdateItemRequestInputModel.  # noqa: E501
        :rtype: RequestViewModel
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this UpdateItemRequestInputModel.


        :param request: The request of this UpdateItemRequestInputModel.  # noqa: E501
        :type: RequestViewModel
        """

        self._request = request

    @property
    def item_guid(self):
        """Gets the item_guid of this UpdateItemRequestInputModel.  # noqa: E501


        :return: The item_guid of this UpdateItemRequestInputModel.  # noqa: E501
        :rtype: str
        """
        return self._item_guid

    @item_guid.setter
    def item_guid(self, item_guid):
        """Sets the item_guid of this UpdateItemRequestInputModel.


        :param item_guid: The item_guid of this UpdateItemRequestInputModel.  # noqa: E501
        :type: str
        """

        self._item_guid = item_guid

    @property
    def item(self):
        """Gets the item of this UpdateItemRequestInputModel.  # noqa: E501


        :return: The item of this UpdateItemRequestInputModel.  # noqa: E501
        :rtype: ItemViewModel
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this UpdateItemRequestInputModel.


        :param item: The item of this UpdateItemRequestInputModel.  # noqa: E501
        :type: ItemViewModel
        """

        self._item = item

    @property
    def is_enabled(self):
        """Gets the is_enabled of this UpdateItemRequestInputModel.  # noqa: E501


        :return: The is_enabled of this UpdateItemRequestInputModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this UpdateItemRequestInputModel.


        :param is_enabled: The is_enabled of this UpdateItemRequestInputModel.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def is_deleted(self):
        """Gets the is_deleted of this UpdateItemRequestInputModel.  # noqa: E501


        :return: The is_deleted of this UpdateItemRequestInputModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this UpdateItemRequestInputModel.


        :param is_deleted: The is_deleted of this UpdateItemRequestInputModel.  # noqa: E501
        :type: bool
        """

        self._is_deleted = is_deleted

    @property
    def permanent_deletion(self):
        """Gets the permanent_deletion of this UpdateItemRequestInputModel.  # noqa: E501


        :return: The permanent_deletion of this UpdateItemRequestInputModel.  # noqa: E501
        :rtype: bool
        """
        return self._permanent_deletion

    @permanent_deletion.setter
    def permanent_deletion(self, permanent_deletion):
        """Sets the permanent_deletion of this UpdateItemRequestInputModel.


        :param permanent_deletion: The permanent_deletion of this UpdateItemRequestInputModel.  # noqa: E501
        :type: bool
        """

        self._permanent_deletion = permanent_deletion

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UpdateItemRequestInputModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateItemRequestInputModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
