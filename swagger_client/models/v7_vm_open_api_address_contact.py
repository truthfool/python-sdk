# coding: utf-8

"""
    PTV Open Api version 11

    Here you can see listed all the PTV Open Api methods.  # noqa: E501

    OpenAPI spec version: v11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class V7VmOpenApiAddressContact(object):
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
        'id': 'str',
        'post_office_box_address': 'VmOpenApiAddressPostOfficeBox',
        'street_address': 'VmOpenApiAddressStreetWithCoordinates',
        'country': 'str',
        'type': 'str',
        'sub_type': 'str',
        'location_abroad': 'list[VmOpenApiLanguageItem]'
    }

    attribute_map = {
        'id': 'id',
        'post_office_box_address': 'postOfficeBoxAddress',
        'street_address': 'streetAddress',
        'country': 'country',
        'type': 'type',
        'sub_type': 'subType',
        'location_abroad': 'locationAbroad'
    }

    def __init__(self, id=None, post_office_box_address=None, street_address=None, country=None, type=None, sub_type=None, location_abroad=None):  # noqa: E501
        """V7VmOpenApiAddressContact - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._post_office_box_address = None
        self._street_address = None
        self._country = None
        self._type = None
        self._sub_type = None
        self._location_abroad = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if post_office_box_address is not None:
            self.post_office_box_address = post_office_box_address
        if street_address is not None:
            self.street_address = street_address
        if country is not None:
            self.country = country
        if type is not None:
            self.type = type
        if sub_type is not None:
            self.sub_type = sub_type
        if location_abroad is not None:
            self.location_abroad = location_abroad

    @property
    def id(self):
        """Gets the id of this V7VmOpenApiAddressContact.  # noqa: E501

        Gets or sets the identifier.  # noqa: E501

        :return: The id of this V7VmOpenApiAddressContact.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V7VmOpenApiAddressContact.

        Gets or sets the identifier.  # noqa: E501

        :param id: The id of this V7VmOpenApiAddressContact.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def post_office_box_address(self):
        """Gets the post_office_box_address of this V7VmOpenApiAddressContact.  # noqa: E501


        :return: The post_office_box_address of this V7VmOpenApiAddressContact.  # noqa: E501
        :rtype: VmOpenApiAddressPostOfficeBox
        """
        return self._post_office_box_address

    @post_office_box_address.setter
    def post_office_box_address(self, post_office_box_address):
        """Sets the post_office_box_address of this V7VmOpenApiAddressContact.


        :param post_office_box_address: The post_office_box_address of this V7VmOpenApiAddressContact.  # noqa: E501
        :type: VmOpenApiAddressPostOfficeBox
        """

        self._post_office_box_address = post_office_box_address

    @property
    def street_address(self):
        """Gets the street_address of this V7VmOpenApiAddressContact.  # noqa: E501


        :return: The street_address of this V7VmOpenApiAddressContact.  # noqa: E501
        :rtype: VmOpenApiAddressStreetWithCoordinates
        """
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        """Sets the street_address of this V7VmOpenApiAddressContact.


        :param street_address: The street_address of this V7VmOpenApiAddressContact.  # noqa: E501
        :type: VmOpenApiAddressStreetWithCoordinates
        """

        self._street_address = street_address

    @property
    def country(self):
        """Gets the country of this V7VmOpenApiAddressContact.  # noqa: E501

        Country code (ISO 3166-1 alpha-2), for example FI.  # noqa: E501

        :return: The country of this V7VmOpenApiAddressContact.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this V7VmOpenApiAddressContact.

        Country code (ISO 3166-1 alpha-2), for example FI.  # noqa: E501

        :param country: The country of this V7VmOpenApiAddressContact.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def type(self):
        """Gets the type of this V7VmOpenApiAddressContact.  # noqa: E501

        Address type, Postal.  # noqa: E501

        :return: The type of this V7VmOpenApiAddressContact.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V7VmOpenApiAddressContact.

        Address type, Postal.  # noqa: E501

        :param type: The type of this V7VmOpenApiAddressContact.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def sub_type(self):
        """Gets the sub_type of this V7VmOpenApiAddressContact.  # noqa: E501

        Address sub type, Street, PostOfficeBox or Abroad.  # noqa: E501

        :return: The sub_type of this V7VmOpenApiAddressContact.  # noqa: E501
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        """Sets the sub_type of this V7VmOpenApiAddressContact.

        Address sub type, Street, PostOfficeBox or Abroad.  # noqa: E501

        :param sub_type: The sub_type of this V7VmOpenApiAddressContact.  # noqa: E501
        :type: str
        """

        self._sub_type = sub_type

    @property
    def location_abroad(self):
        """Gets the location_abroad of this V7VmOpenApiAddressContact.  # noqa: E501

        Localized list of foreign address information.  # noqa: E501

        :return: The location_abroad of this V7VmOpenApiAddressContact.  # noqa: E501
        :rtype: list[VmOpenApiLanguageItem]
        """
        return self._location_abroad

    @location_abroad.setter
    def location_abroad(self, location_abroad):
        """Sets the location_abroad of this V7VmOpenApiAddressContact.

        Localized list of foreign address information.  # noqa: E501

        :param location_abroad: The location_abroad of this V7VmOpenApiAddressContact.  # noqa: E501
        :type: list[VmOpenApiLanguageItem]
        """

        self._location_abroad = location_abroad

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
        if issubclass(V7VmOpenApiAddressContact, dict):
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
        if not isinstance(other, V7VmOpenApiAddressContact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other