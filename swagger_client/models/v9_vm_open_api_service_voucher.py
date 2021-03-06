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

class V9VmOpenApiServiceVoucher(object):
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
        'owner_reference_id': 'str',
        'order_number': 'int',
        'value': 'str',
        'language': 'str',
        'url': 'str',
        'additional_information': 'str'
    }

    attribute_map = {
        'id': 'id',
        'owner_reference_id': 'ownerReferenceId',
        'order_number': 'orderNumber',
        'value': 'value',
        'language': 'language',
        'url': 'url',
        'additional_information': 'additionalInformation'
    }

    def __init__(self, id=None, owner_reference_id=None, order_number=None, value=None, language=None, url=None, additional_information=None):  # noqa: E501
        """V9VmOpenApiServiceVoucher - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._owner_reference_id = None
        self._order_number = None
        self._value = None
        self._language = None
        self._url = None
        self._additional_information = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if owner_reference_id is not None:
            self.owner_reference_id = owner_reference_id
        if order_number is not None:
            self.order_number = order_number
        if value is not None:
            self.value = value
        self.language = language
        if url is not None:
            self.url = url
        if additional_information is not None:
            self.additional_information = additional_information

    @property
    def id(self):
        """Gets the id of this V9VmOpenApiServiceVoucher.  # noqa: E501

        Gets or sets the identifier.  # noqa: E501

        :return: The id of this V9VmOpenApiServiceVoucher.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V9VmOpenApiServiceVoucher.

        Gets or sets the identifier.  # noqa: E501

        :param id: The id of this V9VmOpenApiServiceVoucher.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def owner_reference_id(self):
        """Gets the owner_reference_id of this V9VmOpenApiServiceVoucher.  # noqa: E501

        Gets or sets the owner reference identifier.  # noqa: E501

        :return: The owner_reference_id of this V9VmOpenApiServiceVoucher.  # noqa: E501
        :rtype: str
        """
        return self._owner_reference_id

    @owner_reference_id.setter
    def owner_reference_id(self, owner_reference_id):
        """Sets the owner_reference_id of this V9VmOpenApiServiceVoucher.

        Gets or sets the owner reference identifier.  # noqa: E501

        :param owner_reference_id: The owner_reference_id of this V9VmOpenApiServiceVoucher.  # noqa: E501
        :type: str
        """

        self._owner_reference_id = owner_reference_id

    @property
    def order_number(self):
        """Gets the order_number of this V9VmOpenApiServiceVoucher.  # noqa: E501

        The order of service voucher.  # noqa: E501

        :return: The order_number of this V9VmOpenApiServiceVoucher.  # noqa: E501
        :rtype: int
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """Sets the order_number of this V9VmOpenApiServiceVoucher.

        The order of service voucher.  # noqa: E501

        :param order_number: The order_number of this V9VmOpenApiServiceVoucher.  # noqa: E501
        :type: int
        """

        self._order_number = order_number

    @property
    def value(self):
        """Gets the value of this V9VmOpenApiServiceVoucher.  # noqa: E501

        Name of the service voucher.  # noqa: E501

        :return: The value of this V9VmOpenApiServiceVoucher.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this V9VmOpenApiServiceVoucher.

        Name of the service voucher.  # noqa: E501

        :param value: The value of this V9VmOpenApiServiceVoucher.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def language(self):
        """Gets the language of this V9VmOpenApiServiceVoucher.  # noqa: E501

        Language code.  # noqa: E501

        :return: The language of this V9VmOpenApiServiceVoucher.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this V9VmOpenApiServiceVoucher.

        Language code.  # noqa: E501

        :param language: The language of this V9VmOpenApiServiceVoucher.  # noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def url(self):
        """Gets the url of this V9VmOpenApiServiceVoucher.  # noqa: E501

        Web page url. (Max.Length: 500).  # noqa: E501

        :return: The url of this V9VmOpenApiServiceVoucher.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this V9VmOpenApiServiceVoucher.

        Web page url. (Max.Length: 500).  # noqa: E501

        :param url: The url of this V9VmOpenApiServiceVoucher.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def additional_information(self):
        """Gets the additional_information of this V9VmOpenApiServiceVoucher.  # noqa: E501

        Service voucher additional information (Max.Length: 150).  # noqa: E501

        :return: The additional_information of this V9VmOpenApiServiceVoucher.  # noqa: E501
        :rtype: str
        """
        return self._additional_information

    @additional_information.setter
    def additional_information(self, additional_information):
        """Sets the additional_information of this V9VmOpenApiServiceVoucher.

        Service voucher additional information (Max.Length: 150).  # noqa: E501

        :param additional_information: The additional_information of this V9VmOpenApiServiceVoucher.  # noqa: E501
        :type: str
        """

        self._additional_information = additional_information

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
        if issubclass(V9VmOpenApiServiceVoucher, dict):
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
        if not isinstance(other, V9VmOpenApiServiceVoucher):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
