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

class V9VmOpenApiAddressLocationIn(object):
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
        'post_office_box_address': 'VmOpenApiAddressPostOfficeBoxIn',
        'country': 'str',
        'owner_reference_id': 'str',
        'unique_id': 'str',
        'type': 'str',
        'sub_type': 'str',
        'foreign_address': 'list[VmOpenApiLanguageItem]',
        'street_address': 'VmOpenApiAddressStreetWithCoordinatesIn',
        'other_address': 'VmOpenApiAddressOtherIn',
        'location_abroad': 'list[VmOpenApiLanguageItem]',
        'order_number': 'int'
    }

    attribute_map = {
        'id': 'id',
        'post_office_box_address': 'postOfficeBoxAddress',
        'country': 'country',
        'owner_reference_id': 'ownerReferenceId',
        'unique_id': 'uniqueId',
        'type': 'type',
        'sub_type': 'subType',
        'foreign_address': 'foreignAddress',
        'street_address': 'streetAddress',
        'other_address': 'otherAddress',
        'location_abroad': 'locationAbroad',
        'order_number': 'orderNumber'
    }

    def __init__(self, id=None, post_office_box_address=None, country=None, owner_reference_id=None, unique_id=None, type=None, sub_type=None, foreign_address=None, street_address=None, other_address=None, location_abroad=None, order_number=None):  # noqa: E501
        """V9VmOpenApiAddressLocationIn - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._post_office_box_address = None
        self._country = None
        self._owner_reference_id = None
        self._unique_id = None
        self._type = None
        self._sub_type = None
        self._foreign_address = None
        self._street_address = None
        self._other_address = None
        self._location_abroad = None
        self._order_number = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if post_office_box_address is not None:
            self.post_office_box_address = post_office_box_address
        if country is not None:
            self.country = country
        if owner_reference_id is not None:
            self.owner_reference_id = owner_reference_id
        if unique_id is not None:
            self.unique_id = unique_id
        self.type = type
        self.sub_type = sub_type
        if foreign_address is not None:
            self.foreign_address = foreign_address
        if street_address is not None:
            self.street_address = street_address
        if other_address is not None:
            self.other_address = other_address
        if location_abroad is not None:
            self.location_abroad = location_abroad
        if order_number is not None:
            self.order_number = order_number

    @property
    def id(self):
        """Gets the id of this V9VmOpenApiAddressLocationIn.  # noqa: E501

        Gets or sets the identifier.  # noqa: E501

        :return: The id of this V9VmOpenApiAddressLocationIn.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V9VmOpenApiAddressLocationIn.

        Gets or sets the identifier.  # noqa: E501

        :param id: The id of this V9VmOpenApiAddressLocationIn.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def post_office_box_address(self):
        """Gets the post_office_box_address of this V9VmOpenApiAddressLocationIn.  # noqa: E501


        :return: The post_office_box_address of this V9VmOpenApiAddressLocationIn.  # noqa: E501
        :rtype: VmOpenApiAddressPostOfficeBoxIn
        """
        return self._post_office_box_address

    @post_office_box_address.setter
    def post_office_box_address(self, post_office_box_address):
        """Sets the post_office_box_address of this V9VmOpenApiAddressLocationIn.


        :param post_office_box_address: The post_office_box_address of this V9VmOpenApiAddressLocationIn.  # noqa: E501
        :type: VmOpenApiAddressPostOfficeBoxIn
        """

        self._post_office_box_address = post_office_box_address

    @property
    def country(self):
        """Gets the country of this V9VmOpenApiAddressLocationIn.  # noqa: E501

        Country code (ISO 3166-1 alpha-2), for example FI.  # noqa: E501

        :return: The country of this V9VmOpenApiAddressLocationIn.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this V9VmOpenApiAddressLocationIn.

        Country code (ISO 3166-1 alpha-2), for example FI.  # noqa: E501

        :param country: The country of this V9VmOpenApiAddressLocationIn.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def owner_reference_id(self):
        """Gets the owner_reference_id of this V9VmOpenApiAddressLocationIn.  # noqa: E501

        Gets or sets the owner reference identifier.  # noqa: E501

        :return: The owner_reference_id of this V9VmOpenApiAddressLocationIn.  # noqa: E501
        :rtype: str
        """
        return self._owner_reference_id

    @owner_reference_id.setter
    def owner_reference_id(self, owner_reference_id):
        """Sets the owner_reference_id of this V9VmOpenApiAddressLocationIn.

        Gets or sets the owner reference identifier.  # noqa: E501

        :param owner_reference_id: The owner_reference_id of this V9VmOpenApiAddressLocationIn.  # noqa: E501
        :type: str
        """

        self._owner_reference_id = owner_reference_id

    @property
    def unique_id(self):
        """Gets the unique_id of this V9VmOpenApiAddressLocationIn.  # noqa: E501

        Gets or sets the address unique id  # noqa: E501

        :return: The unique_id of this V9VmOpenApiAddressLocationIn.  # noqa: E501
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        """Sets the unique_id of this V9VmOpenApiAddressLocationIn.

        Gets or sets the address unique id  # noqa: E501

        :param unique_id: The unique_id of this V9VmOpenApiAddressLocationIn.  # noqa: E501
        :type: str
        """

        self._unique_id = unique_id

    @property
    def type(self):
        """Gets the type of this V9VmOpenApiAddressLocationIn.  # noqa: E501

        Address type, Location or Postal.  # noqa: E501

        :return: The type of this V9VmOpenApiAddressLocationIn.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V9VmOpenApiAddressLocationIn.

        Address type, Location or Postal.  # noqa: E501

        :param type: The type of this V9VmOpenApiAddressLocationIn.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def sub_type(self):
        """Gets the sub_type of this V9VmOpenApiAddressLocationIn.  # noqa: E501

        Address sub type, Single, Street, PostOfficeBox, Abroad or Other.  # noqa: E501

        :return: The sub_type of this V9VmOpenApiAddressLocationIn.  # noqa: E501
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        """Sets the sub_type of this V9VmOpenApiAddressLocationIn.

        Address sub type, Single, Street, PostOfficeBox, Abroad or Other.  # noqa: E501

        :param sub_type: The sub_type of this V9VmOpenApiAddressLocationIn.  # noqa: E501
        :type: str
        """
        if sub_type is None:
            raise ValueError("Invalid value for `sub_type`, must not be `None`")  # noqa: E501

        self._sub_type = sub_type

    @property
    def foreign_address(self):
        """Gets the foreign_address of this V9VmOpenApiAddressLocationIn.  # noqa: E501

        Localized list of foreign address information.  # noqa: E501

        :return: The foreign_address of this V9VmOpenApiAddressLocationIn.  # noqa: E501
        :rtype: list[VmOpenApiLanguageItem]
        """
        return self._foreign_address

    @foreign_address.setter
    def foreign_address(self, foreign_address):
        """Sets the foreign_address of this V9VmOpenApiAddressLocationIn.

        Localized list of foreign address information.  # noqa: E501

        :param foreign_address: The foreign_address of this V9VmOpenApiAddressLocationIn.  # noqa: E501
        :type: list[VmOpenApiLanguageItem]
        """

        self._foreign_address = foreign_address

    @property
    def street_address(self):
        """Gets the street_address of this V9VmOpenApiAddressLocationIn.  # noqa: E501


        :return: The street_address of this V9VmOpenApiAddressLocationIn.  # noqa: E501
        :rtype: VmOpenApiAddressStreetWithCoordinatesIn
        """
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        """Sets the street_address of this V9VmOpenApiAddressLocationIn.


        :param street_address: The street_address of this V9VmOpenApiAddressLocationIn.  # noqa: E501
        :type: VmOpenApiAddressStreetWithCoordinatesIn
        """

        self._street_address = street_address

    @property
    def other_address(self):
        """Gets the other_address of this V9VmOpenApiAddressLocationIn.  # noqa: E501


        :return: The other_address of this V9VmOpenApiAddressLocationIn.  # noqa: E501
        :rtype: VmOpenApiAddressOtherIn
        """
        return self._other_address

    @other_address.setter
    def other_address(self, other_address):
        """Sets the other_address of this V9VmOpenApiAddressLocationIn.


        :param other_address: The other_address of this V9VmOpenApiAddressLocationIn.  # noqa: E501
        :type: VmOpenApiAddressOtherIn
        """

        self._other_address = other_address

    @property
    def location_abroad(self):
        """Gets the location_abroad of this V9VmOpenApiAddressLocationIn.  # noqa: E501

        Localized list of foreign address information. (Max.Length: 500).  # noqa: E501

        :return: The location_abroad of this V9VmOpenApiAddressLocationIn.  # noqa: E501
        :rtype: list[VmOpenApiLanguageItem]
        """
        return self._location_abroad

    @location_abroad.setter
    def location_abroad(self, location_abroad):
        """Sets the location_abroad of this V9VmOpenApiAddressLocationIn.

        Localized list of foreign address information. (Max.Length: 500).  # noqa: E501

        :param location_abroad: The location_abroad of this V9VmOpenApiAddressLocationIn.  # noqa: E501
        :type: list[VmOpenApiLanguageItem]
        """

        self._location_abroad = location_abroad

    @property
    def order_number(self):
        """Gets the order_number of this V9VmOpenApiAddressLocationIn.  # noqa: E501

        Gets or sets the order number  # noqa: E501

        :return: The order_number of this V9VmOpenApiAddressLocationIn.  # noqa: E501
        :rtype: int
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """Sets the order_number of this V9VmOpenApiAddressLocationIn.

        Gets or sets the order number  # noqa: E501

        :param order_number: The order_number of this V9VmOpenApiAddressLocationIn.  # noqa: E501
        :type: int
        """

        self._order_number = order_number

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
        if issubclass(V9VmOpenApiAddressLocationIn, dict):
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
        if not isinstance(other, V9VmOpenApiAddressLocationIn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
