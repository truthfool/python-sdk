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

class V9VmOpenApiContactDetails(object):
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
        'emails': 'list[VmOpenApiLanguageItem]',
        'phone_numbers': 'list[V4VmOpenApiPhoneWithType]',
        'web_pages': 'list[V9VmOpenApiWebPage]',
        'addresses': 'list[V7VmOpenApiAddressContact]'
    }

    attribute_map = {
        'emails': 'emails',
        'phone_numbers': 'phoneNumbers',
        'web_pages': 'webPages',
        'addresses': 'addresses'
    }

    def __init__(self, emails=None, phone_numbers=None, web_pages=None, addresses=None):  # noqa: E501
        """V9VmOpenApiContactDetails - a model defined in Swagger"""  # noqa: E501
        self._emails = None
        self._phone_numbers = None
        self._web_pages = None
        self._addresses = None
        self.discriminator = None
        if emails is not None:
            self.emails = emails
        if phone_numbers is not None:
            self.phone_numbers = phone_numbers
        if web_pages is not None:
            self.web_pages = web_pages
        if addresses is not None:
            self.addresses = addresses

    @property
    def emails(self):
        """Gets the emails of this V9VmOpenApiContactDetails.  # noqa: E501

        List of connection related email addresses.  # noqa: E501

        :return: The emails of this V9VmOpenApiContactDetails.  # noqa: E501
        :rtype: list[VmOpenApiLanguageItem]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this V9VmOpenApiContactDetails.

        List of connection related email addresses.  # noqa: E501

        :param emails: The emails of this V9VmOpenApiContactDetails.  # noqa: E501
        :type: list[VmOpenApiLanguageItem]
        """

        self._emails = emails

    @property
    def phone_numbers(self):
        """Gets the phone_numbers of this V9VmOpenApiContactDetails.  # noqa: E501

        List of connection related phone numbers.  # noqa: E501

        :return: The phone_numbers of this V9VmOpenApiContactDetails.  # noqa: E501
        :rtype: list[V4VmOpenApiPhoneWithType]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """Sets the phone_numbers of this V9VmOpenApiContactDetails.

        List of connection related phone numbers.  # noqa: E501

        :param phone_numbers: The phone_numbers of this V9VmOpenApiContactDetails.  # noqa: E501
        :type: list[V4VmOpenApiPhoneWithType]
        """

        self._phone_numbers = phone_numbers

    @property
    def web_pages(self):
        """Gets the web_pages of this V9VmOpenApiContactDetails.  # noqa: E501

        List of connection related web pages.  # noqa: E501

        :return: The web_pages of this V9VmOpenApiContactDetails.  # noqa: E501
        :rtype: list[V9VmOpenApiWebPage]
        """
        return self._web_pages

    @web_pages.setter
    def web_pages(self, web_pages):
        """Sets the web_pages of this V9VmOpenApiContactDetails.

        List of connection related web pages.  # noqa: E501

        :param web_pages: The web_pages of this V9VmOpenApiContactDetails.  # noqa: E501
        :type: list[V9VmOpenApiWebPage]
        """

        self._web_pages = web_pages

    @property
    def addresses(self):
        """Gets the addresses of this V9VmOpenApiContactDetails.  # noqa: E501

        List of service location addresses.  # noqa: E501

        :return: The addresses of this V9VmOpenApiContactDetails.  # noqa: E501
        :rtype: list[V7VmOpenApiAddressContact]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this V9VmOpenApiContactDetails.

        List of service location addresses.  # noqa: E501

        :param addresses: The addresses of this V9VmOpenApiContactDetails.  # noqa: E501
        :type: list[V7VmOpenApiAddressContact]
        """

        self._addresses = addresses

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
        if issubclass(V9VmOpenApiContactDetails, dict):
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
        if not isinstance(other, V9VmOpenApiContactDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
