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

class V4VmOpenApiLaw(object):
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
        'names': 'list[VmOpenApiLanguageItem]',
        'web_pages': 'list[V4VmOpenApiWebPage]',
        'owner_reference_id': 'str',
        'order_number': 'int'
    }

    attribute_map = {
        'id': 'id',
        'names': 'names',
        'web_pages': 'webPages',
        'owner_reference_id': 'ownerReferenceId',
        'order_number': 'orderNumber'
    }

    def __init__(self, id=None, names=None, web_pages=None, owner_reference_id=None, order_number=None):  # noqa: E501
        """V4VmOpenApiLaw - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._names = None
        self._web_pages = None
        self._owner_reference_id = None
        self._order_number = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if names is not None:
            self.names = names
        self.web_pages = web_pages
        if owner_reference_id is not None:
            self.owner_reference_id = owner_reference_id
        if order_number is not None:
            self.order_number = order_number

    @property
    def id(self):
        """Gets the id of this V4VmOpenApiLaw.  # noqa: E501

        Gets or sets the identifier.  # noqa: E501

        :return: The id of this V4VmOpenApiLaw.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V4VmOpenApiLaw.

        Gets or sets the identifier.  # noqa: E501

        :param id: The id of this V4VmOpenApiLaw.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def names(self):
        """Gets the names of this V4VmOpenApiLaw.  # noqa: E501

        List of localized law names. (Max.Length: 500).  # noqa: E501

        :return: The names of this V4VmOpenApiLaw.  # noqa: E501
        :rtype: list[VmOpenApiLanguageItem]
        """
        return self._names

    @names.setter
    def names(self, names):
        """Sets the names of this V4VmOpenApiLaw.

        List of localized law names. (Max.Length: 500).  # noqa: E501

        :param names: The names of this V4VmOpenApiLaw.  # noqa: E501
        :type: list[VmOpenApiLanguageItem]
        """

        self._names = names

    @property
    def web_pages(self):
        """Gets the web_pages of this V4VmOpenApiLaw.  # noqa: E501

        List of localized web page urls.  # noqa: E501

        :return: The web_pages of this V4VmOpenApiLaw.  # noqa: E501
        :rtype: list[V4VmOpenApiWebPage]
        """
        return self._web_pages

    @web_pages.setter
    def web_pages(self, web_pages):
        """Sets the web_pages of this V4VmOpenApiLaw.

        List of localized web page urls.  # noqa: E501

        :param web_pages: The web_pages of this V4VmOpenApiLaw.  # noqa: E501
        :type: list[V4VmOpenApiWebPage]
        """
        if web_pages is None:
            raise ValueError("Invalid value for `web_pages`, must not be `None`")  # noqa: E501

        self._web_pages = web_pages

    @property
    def owner_reference_id(self):
        """Gets the owner_reference_id of this V4VmOpenApiLaw.  # noqa: E501

        Gets or sets the owner reference identifier.  # noqa: E501

        :return: The owner_reference_id of this V4VmOpenApiLaw.  # noqa: E501
        :rtype: str
        """
        return self._owner_reference_id

    @owner_reference_id.setter
    def owner_reference_id(self, owner_reference_id):
        """Sets the owner_reference_id of this V4VmOpenApiLaw.

        Gets or sets the owner reference identifier.  # noqa: E501

        :param owner_reference_id: The owner_reference_id of this V4VmOpenApiLaw.  # noqa: E501
        :type: str
        """

        self._owner_reference_id = owner_reference_id

    @property
    def order_number(self):
        """Gets the order_number of this V4VmOpenApiLaw.  # noqa: E501

        Gets or sets the owner reference identifier.  # noqa: E501

        :return: The order_number of this V4VmOpenApiLaw.  # noqa: E501
        :rtype: int
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """Sets the order_number of this V4VmOpenApiLaw.

        Gets or sets the owner reference identifier.  # noqa: E501

        :param order_number: The order_number of this V4VmOpenApiLaw.  # noqa: E501
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
        if issubclass(V4VmOpenApiLaw, dict):
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
        if not isinstance(other, V4VmOpenApiLaw):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
