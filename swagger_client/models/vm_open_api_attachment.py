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

class VmOpenApiAttachment(object):
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
        'name': 'str',
        'description': 'str',
        'url': 'str',
        'language': 'str',
        'owner_reference_id': 'str',
        'order_number': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'url': 'url',
        'language': 'language',
        'owner_reference_id': 'ownerReferenceId',
        'order_number': 'orderNumber'
    }

    def __init__(self, id=None, name=None, description=None, url=None, language=None, owner_reference_id=None, order_number=None):  # noqa: E501
        """VmOpenApiAttachment - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._url = None
        self._language = None
        self._owner_reference_id = None
        self._order_number = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        self.url = url
        self.language = language
        if owner_reference_id is not None:
            self.owner_reference_id = owner_reference_id
        if order_number is not None:
            self.order_number = order_number

    @property
    def id(self):
        """Gets the id of this VmOpenApiAttachment.  # noqa: E501

        Gets or sets the identifier.  # noqa: E501

        :return: The id of this VmOpenApiAttachment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VmOpenApiAttachment.

        Gets or sets the identifier.  # noqa: E501

        :param id: The id of this VmOpenApiAttachment.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this VmOpenApiAttachment.  # noqa: E501

        Name of the attachment. (Max.Length: 100).  # noqa: E501

        :return: The name of this VmOpenApiAttachment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VmOpenApiAttachment.

        Name of the attachment. (Max.Length: 100).  # noqa: E501

        :param name: The name of this VmOpenApiAttachment.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this VmOpenApiAttachment.  # noqa: E501

        Description of the attachment. (Max.Length: 150).  # noqa: E501

        :return: The description of this VmOpenApiAttachment.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VmOpenApiAttachment.

        Description of the attachment. (Max.Length: 150).  # noqa: E501

        :param description: The description of this VmOpenApiAttachment.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def url(self):
        """Gets the url of this VmOpenApiAttachment.  # noqa: E501

        Url to the attachment. (Max.Length: 500).  # noqa: E501

        :return: The url of this VmOpenApiAttachment.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this VmOpenApiAttachment.

        Url to the attachment. (Max.Length: 500).  # noqa: E501

        :param url: The url of this VmOpenApiAttachment.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def language(self):
        """Gets the language of this VmOpenApiAttachment.  # noqa: E501

        Language of this object. Valid values are: fi, sv or en.  # noqa: E501

        :return: The language of this VmOpenApiAttachment.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this VmOpenApiAttachment.

        Language of this object. Valid values are: fi, sv or en.  # noqa: E501

        :param language: The language of this VmOpenApiAttachment.  # noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def owner_reference_id(self):
        """Gets the owner_reference_id of this VmOpenApiAttachment.  # noqa: E501

        Gets or sets the owner reference identifier.  # noqa: E501

        :return: The owner_reference_id of this VmOpenApiAttachment.  # noqa: E501
        :rtype: str
        """
        return self._owner_reference_id

    @owner_reference_id.setter
    def owner_reference_id(self, owner_reference_id):
        """Sets the owner_reference_id of this VmOpenApiAttachment.

        Gets or sets the owner reference identifier.  # noqa: E501

        :param owner_reference_id: The owner_reference_id of this VmOpenApiAttachment.  # noqa: E501
        :type: str
        """

        self._owner_reference_id = owner_reference_id

    @property
    def order_number(self):
        """Gets the order_number of this VmOpenApiAttachment.  # noqa: E501

        Gets or sets the order number.  # noqa: E501

        :return: The order_number of this VmOpenApiAttachment.  # noqa: E501
        :rtype: int
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """Sets the order_number of this VmOpenApiAttachment.

        Gets or sets the order number.  # noqa: E501

        :param order_number: The order_number of this VmOpenApiAttachment.  # noqa: E501
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
        if issubclass(VmOpenApiAttachment, dict):
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
        if not isinstance(other, VmOpenApiAttachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
