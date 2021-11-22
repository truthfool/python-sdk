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

class V9VmOpenApiEntrance(object):
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
        'name': 'list[VmOpenApiLanguageItem]',
        'is_main_entrance': 'bool',
        'coordinates': 'VmOpenApiCoordinates',
        'accessibility_sentences': 'list[VmOpenApiAccessibilitySentence]',
        'contact_info': 'VmOpenApiAccessibilityContactInfo'
    }

    attribute_map = {
        'name': 'name',
        'is_main_entrance': 'isMainEntrance',
        'coordinates': 'coordinates',
        'accessibility_sentences': 'accessibilitySentences',
        'contact_info': 'contactInfo'
    }

    def __init__(self, name=None, is_main_entrance=None, coordinates=None, accessibility_sentences=None, contact_info=None):  # noqa: E501
        """V9VmOpenApiEntrance - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._is_main_entrance = None
        self._coordinates = None
        self._accessibility_sentences = None
        self._contact_info = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if is_main_entrance is not None:
            self.is_main_entrance = is_main_entrance
        if coordinates is not None:
            self.coordinates = coordinates
        if accessibility_sentences is not None:
            self.accessibility_sentences = accessibility_sentences
        if contact_info is not None:
            self.contact_info = contact_info

    @property
    def name(self):
        """Gets the name of this V9VmOpenApiEntrance.  # noqa: E501

        List of localized service names.  # noqa: E501

        :return: The name of this V9VmOpenApiEntrance.  # noqa: E501
        :rtype: list[VmOpenApiLanguageItem]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V9VmOpenApiEntrance.

        List of localized service names.  # noqa: E501

        :param name: The name of this V9VmOpenApiEntrance.  # noqa: E501
        :type: list[VmOpenApiLanguageItem]
        """

        self._name = name

    @property
    def is_main_entrance(self):
        """Gets the is_main_entrance of this V9VmOpenApiEntrance.  # noqa: E501

        Indicates if entrance is main entrance.  # noqa: E501

        :return: The is_main_entrance of this V9VmOpenApiEntrance.  # noqa: E501
        :rtype: bool
        """
        return self._is_main_entrance

    @is_main_entrance.setter
    def is_main_entrance(self, is_main_entrance):
        """Sets the is_main_entrance of this V9VmOpenApiEntrance.

        Indicates if entrance is main entrance.  # noqa: E501

        :param is_main_entrance: The is_main_entrance of this V9VmOpenApiEntrance.  # noqa: E501
        :type: bool
        """

        self._is_main_entrance = is_main_entrance

    @property
    def coordinates(self):
        """Gets the coordinates of this V9VmOpenApiEntrance.  # noqa: E501


        :return: The coordinates of this V9VmOpenApiEntrance.  # noqa: E501
        :rtype: VmOpenApiCoordinates
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this V9VmOpenApiEntrance.


        :param coordinates: The coordinates of this V9VmOpenApiEntrance.  # noqa: E501
        :type: VmOpenApiCoordinates
        """

        self._coordinates = coordinates

    @property
    def accessibility_sentences(self):
        """Gets the accessibility_sentences of this V9VmOpenApiEntrance.  # noqa: E501

        List of accessibility sentences.  # noqa: E501

        :return: The accessibility_sentences of this V9VmOpenApiEntrance.  # noqa: E501
        :rtype: list[VmOpenApiAccessibilitySentence]
        """
        return self._accessibility_sentences

    @accessibility_sentences.setter
    def accessibility_sentences(self, accessibility_sentences):
        """Sets the accessibility_sentences of this V9VmOpenApiEntrance.

        List of accessibility sentences.  # noqa: E501

        :param accessibility_sentences: The accessibility_sentences of this V9VmOpenApiEntrance.  # noqa: E501
        :type: list[VmOpenApiAccessibilitySentence]
        """

        self._accessibility_sentences = accessibility_sentences

    @property
    def contact_info(self):
        """Gets the contact_info of this V9VmOpenApiEntrance.  # noqa: E501


        :return: The contact_info of this V9VmOpenApiEntrance.  # noqa: E501
        :rtype: VmOpenApiAccessibilityContactInfo
        """
        return self._contact_info

    @contact_info.setter
    def contact_info(self, contact_info):
        """Sets the contact_info of this V9VmOpenApiEntrance.


        :param contact_info: The contact_info of this V9VmOpenApiEntrance.  # noqa: E501
        :type: VmOpenApiAccessibilityContactInfo
        """

        self._contact_info = contact_info

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
        if issubclass(V9VmOpenApiEntrance, dict):
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
        if not isinstance(other, V9VmOpenApiEntrance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
