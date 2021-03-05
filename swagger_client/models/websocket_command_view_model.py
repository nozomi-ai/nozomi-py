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

class WebsocketCommandViewModel(object):
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
        'type': 'CommandType',
        'name': 'str',
        'delay': 'int',
        'request_guid': 'str',
        'is_enabled': 'bool',
        'id': 'int',
        'guid': 'str',
        'properties': 'list[WebsocketCommandPropertyViewModel]'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'delay': 'delay',
        'request_guid': 'requestGuid',
        'is_enabled': 'isEnabled',
        'id': 'id',
        'guid': 'guid',
        'properties': 'properties'
    }

    def __init__(self, type=None, name=None, delay=None, request_guid=None, is_enabled=None, id=None, guid=None, properties=None):  # noqa: E501
        """WebsocketCommandViewModel - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._name = None
        self._delay = None
        self._request_guid = None
        self._is_enabled = None
        self._id = None
        self._guid = None
        self._properties = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if delay is not None:
            self.delay = delay
        if request_guid is not None:
            self.request_guid = request_guid
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if id is not None:
            self.id = id
        if guid is not None:
            self.guid = guid
        if properties is not None:
            self.properties = properties

    @property
    def type(self):
        """Gets the type of this WebsocketCommandViewModel.  # noqa: E501


        :return: The type of this WebsocketCommandViewModel.  # noqa: E501
        :rtype: CommandType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WebsocketCommandViewModel.


        :param type: The type of this WebsocketCommandViewModel.  # noqa: E501
        :type: CommandType
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this WebsocketCommandViewModel.  # noqa: E501


        :return: The name of this WebsocketCommandViewModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WebsocketCommandViewModel.


        :param name: The name of this WebsocketCommandViewModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def delay(self):
        """Gets the delay of this WebsocketCommandViewModel.  # noqa: E501


        :return: The delay of this WebsocketCommandViewModel.  # noqa: E501
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this WebsocketCommandViewModel.


        :param delay: The delay of this WebsocketCommandViewModel.  # noqa: E501
        :type: int
        """

        self._delay = delay

    @property
    def request_guid(self):
        """Gets the request_guid of this WebsocketCommandViewModel.  # noqa: E501


        :return: The request_guid of this WebsocketCommandViewModel.  # noqa: E501
        :rtype: str
        """
        return self._request_guid

    @request_guid.setter
    def request_guid(self, request_guid):
        """Sets the request_guid of this WebsocketCommandViewModel.


        :param request_guid: The request_guid of this WebsocketCommandViewModel.  # noqa: E501
        :type: str
        """

        self._request_guid = request_guid

    @property
    def is_enabled(self):
        """Gets the is_enabled of this WebsocketCommandViewModel.  # noqa: E501


        :return: The is_enabled of this WebsocketCommandViewModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this WebsocketCommandViewModel.


        :param is_enabled: The is_enabled of this WebsocketCommandViewModel.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def id(self):
        """Gets the id of this WebsocketCommandViewModel.  # noqa: E501


        :return: The id of this WebsocketCommandViewModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebsocketCommandViewModel.


        :param id: The id of this WebsocketCommandViewModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def guid(self):
        """Gets the guid of this WebsocketCommandViewModel.  # noqa: E501


        :return: The guid of this WebsocketCommandViewModel.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this WebsocketCommandViewModel.


        :param guid: The guid of this WebsocketCommandViewModel.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def properties(self):
        """Gets the properties of this WebsocketCommandViewModel.  # noqa: E501


        :return: The properties of this WebsocketCommandViewModel.  # noqa: E501
        :rtype: list[WebsocketCommandPropertyViewModel]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this WebsocketCommandViewModel.


        :param properties: The properties of this WebsocketCommandViewModel.  # noqa: E501
        :type: list[WebsocketCommandPropertyViewModel]
        """

        self._properties = properties

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
        if issubclass(WebsocketCommandViewModel, dict):
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
        if not isinstance(other, WebsocketCommandViewModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other