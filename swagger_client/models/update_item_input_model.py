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

class UpdateItemInputModel(object):
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
        'is_enabled': 'bool',
        'logo_path': 'str',
        'abbreviation': 'str',
        'slug': 'str',
        'name': 'str',
        'denominations': 'int',
        'denomination_name': 'str',
        'parent_item_guid': 'str',
        'types': 'list[UpdateTypeItemInputModel]',
        'properties': 'list[UpdateItemPropertyInputModel]',
        'requests': 'list[UpdateItemRequestInputModel]'
    }

    attribute_map = {
        'guid': 'guid',
        'is_enabled': 'isEnabled',
        'logo_path': 'logoPath',
        'abbreviation': 'abbreviation',
        'slug': 'slug',
        'name': 'name',
        'denominations': 'denominations',
        'denomination_name': 'denominationName',
        'parent_item_guid': 'parentItemGuid',
        'types': 'types',
        'properties': 'properties',
        'requests': 'requests'
    }

    def __init__(self, guid=None, is_enabled=None, logo_path=None, abbreviation=None, slug=None, name=None, denominations=None, denomination_name=None, parent_item_guid=None, types=None, properties=None, requests=None):  # noqa: E501
        """UpdateItemInputModel - a model defined in Swagger"""  # noqa: E501
        self._guid = None
        self._is_enabled = None
        self._logo_path = None
        self._abbreviation = None
        self._slug = None
        self._name = None
        self._denominations = None
        self._denomination_name = None
        self._parent_item_guid = None
        self._types = None
        self._properties = None
        self._requests = None
        self.discriminator = None
        if guid is not None:
            self.guid = guid
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if logo_path is not None:
            self.logo_path = logo_path
        if abbreviation is not None:
            self.abbreviation = abbreviation
        if slug is not None:
            self.slug = slug
        if name is not None:
            self.name = name
        if denominations is not None:
            self.denominations = denominations
        if denomination_name is not None:
            self.denomination_name = denomination_name
        if parent_item_guid is not None:
            self.parent_item_guid = parent_item_guid
        if types is not None:
            self.types = types
        if properties is not None:
            self.properties = properties
        if requests is not None:
            self.requests = requests

    @property
    def guid(self):
        """Gets the guid of this UpdateItemInputModel.  # noqa: E501


        :return: The guid of this UpdateItemInputModel.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this UpdateItemInputModel.


        :param guid: The guid of this UpdateItemInputModel.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def is_enabled(self):
        """Gets the is_enabled of this UpdateItemInputModel.  # noqa: E501


        :return: The is_enabled of this UpdateItemInputModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this UpdateItemInputModel.


        :param is_enabled: The is_enabled of this UpdateItemInputModel.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def logo_path(self):
        """Gets the logo_path of this UpdateItemInputModel.  # noqa: E501


        :return: The logo_path of this UpdateItemInputModel.  # noqa: E501
        :rtype: str
        """
        return self._logo_path

    @logo_path.setter
    def logo_path(self, logo_path):
        """Sets the logo_path of this UpdateItemInputModel.


        :param logo_path: The logo_path of this UpdateItemInputModel.  # noqa: E501
        :type: str
        """

        self._logo_path = logo_path

    @property
    def abbreviation(self):
        """Gets the abbreviation of this UpdateItemInputModel.  # noqa: E501


        :return: The abbreviation of this UpdateItemInputModel.  # noqa: E501
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """Sets the abbreviation of this UpdateItemInputModel.


        :param abbreviation: The abbreviation of this UpdateItemInputModel.  # noqa: E501
        :type: str
        """

        self._abbreviation = abbreviation

    @property
    def slug(self):
        """Gets the slug of this UpdateItemInputModel.  # noqa: E501


        :return: The slug of this UpdateItemInputModel.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this UpdateItemInputModel.


        :param slug: The slug of this UpdateItemInputModel.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def name(self):
        """Gets the name of this UpdateItemInputModel.  # noqa: E501


        :return: The name of this UpdateItemInputModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateItemInputModel.


        :param name: The name of this UpdateItemInputModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def denominations(self):
        """Gets the denominations of this UpdateItemInputModel.  # noqa: E501


        :return: The denominations of this UpdateItemInputModel.  # noqa: E501
        :rtype: int
        """
        return self._denominations

    @denominations.setter
    def denominations(self, denominations):
        """Sets the denominations of this UpdateItemInputModel.


        :param denominations: The denominations of this UpdateItemInputModel.  # noqa: E501
        :type: int
        """

        self._denominations = denominations

    @property
    def denomination_name(self):
        """Gets the denomination_name of this UpdateItemInputModel.  # noqa: E501


        :return: The denomination_name of this UpdateItemInputModel.  # noqa: E501
        :rtype: str
        """
        return self._denomination_name

    @denomination_name.setter
    def denomination_name(self, denomination_name):
        """Sets the denomination_name of this UpdateItemInputModel.


        :param denomination_name: The denomination_name of this UpdateItemInputModel.  # noqa: E501
        :type: str
        """

        self._denomination_name = denomination_name

    @property
    def parent_item_guid(self):
        """Gets the parent_item_guid of this UpdateItemInputModel.  # noqa: E501


        :return: The parent_item_guid of this UpdateItemInputModel.  # noqa: E501
        :rtype: str
        """
        return self._parent_item_guid

    @parent_item_guid.setter
    def parent_item_guid(self, parent_item_guid):
        """Sets the parent_item_guid of this UpdateItemInputModel.


        :param parent_item_guid: The parent_item_guid of this UpdateItemInputModel.  # noqa: E501
        :type: str
        """

        self._parent_item_guid = parent_item_guid

    @property
    def types(self):
        """Gets the types of this UpdateItemInputModel.  # noqa: E501


        :return: The types of this UpdateItemInputModel.  # noqa: E501
        :rtype: list[UpdateTypeItemInputModel]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this UpdateItemInputModel.


        :param types: The types of this UpdateItemInputModel.  # noqa: E501
        :type: list[UpdateTypeItemInputModel]
        """

        self._types = types

    @property
    def properties(self):
        """Gets the properties of this UpdateItemInputModel.  # noqa: E501


        :return: The properties of this UpdateItemInputModel.  # noqa: E501
        :rtype: list[UpdateItemPropertyInputModel]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this UpdateItemInputModel.


        :param properties: The properties of this UpdateItemInputModel.  # noqa: E501
        :type: list[UpdateItemPropertyInputModel]
        """

        self._properties = properties

    @property
    def requests(self):
        """Gets the requests of this UpdateItemInputModel.  # noqa: E501


        :return: The requests of this UpdateItemInputModel.  # noqa: E501
        :rtype: list[UpdateItemRequestInputModel]
        """
        return self._requests

    @requests.setter
    def requests(self, requests):
        """Sets the requests of this UpdateItemInputModel.


        :param requests: The requests of this UpdateItemInputModel.  # noqa: E501
        :type: list[UpdateItemRequestInputModel]
        """

        self._requests = requests

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
        if issubclass(UpdateItemInputModel, dict):
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
        if not isinstance(other, UpdateItemInputModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
