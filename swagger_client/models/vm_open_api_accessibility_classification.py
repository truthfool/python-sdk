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

class VmOpenApiAccessibilityClassification(object):
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
        'accessibility_classification_level': 'str',
        'wcag_level': 'str',
        'accessibility_statement_web_page_name': 'str',
        'accessibility_statement_web_page': 'str',
        'language': 'str',
        'id': 'str',
        'owner_reference_id': 'str'
    }

    attribute_map = {
        'accessibility_classification_level': 'accessibilityClassificationLevel',
        'wcag_level': 'wcagLevel',
        'accessibility_statement_web_page_name': 'accessibilityStatementWebPageName',
        'accessibility_statement_web_page': 'accessibilityStatementWebPage',
        'language': 'language',
        'id': 'id',
        'owner_reference_id': 'ownerReferenceId'
    }

    def __init__(self, accessibility_classification_level=None, wcag_level=None, accessibility_statement_web_page_name=None, accessibility_statement_web_page=None, language=None, id=None, owner_reference_id=None):  # noqa: E501
        """VmOpenApiAccessibilityClassification - a model defined in Swagger"""  # noqa: E501
        self._accessibility_classification_level = None
        self._wcag_level = None
        self._accessibility_statement_web_page_name = None
        self._accessibility_statement_web_page = None
        self._language = None
        self._id = None
        self._owner_reference_id = None
        self.discriminator = None
        self.accessibility_classification_level = accessibility_classification_level
        if wcag_level is not None:
            self.wcag_level = wcag_level
        if accessibility_statement_web_page_name is not None:
            self.accessibility_statement_web_page_name = accessibility_statement_web_page_name
        if accessibility_statement_web_page is not None:
            self.accessibility_statement_web_page = accessibility_statement_web_page
        self.language = language
        if id is not None:
            self.id = id
        if owner_reference_id is not None:
            self.owner_reference_id = owner_reference_id

    @property
    def accessibility_classification_level(self):
        """Gets the accessibility_classification_level of this VmOpenApiAccessibilityClassification.  # noqa: E501

        Gets or sets the accessibility classification level.  # noqa: E501

        :return: The accessibility_classification_level of this VmOpenApiAccessibilityClassification.  # noqa: E501
        :rtype: str
        """
        return self._accessibility_classification_level

    @accessibility_classification_level.setter
    def accessibility_classification_level(self, accessibility_classification_level):
        """Sets the accessibility_classification_level of this VmOpenApiAccessibilityClassification.

        Gets or sets the accessibility classification level.  # noqa: E501

        :param accessibility_classification_level: The accessibility_classification_level of this VmOpenApiAccessibilityClassification.  # noqa: E501
        :type: str
        """
        if accessibility_classification_level is None:
            raise ValueError("Invalid value for `accessibility_classification_level`, must not be `None`")  # noqa: E501

        self._accessibility_classification_level = accessibility_classification_level

    @property
    def wcag_level(self):
        """Gets the wcag_level of this VmOpenApiAccessibilityClassification.  # noqa: E501

        Gets or sets the wcag level.  # noqa: E501

        :return: The wcag_level of this VmOpenApiAccessibilityClassification.  # noqa: E501
        :rtype: str
        """
        return self._wcag_level

    @wcag_level.setter
    def wcag_level(self, wcag_level):
        """Sets the wcag_level of this VmOpenApiAccessibilityClassification.

        Gets or sets the wcag level.  # noqa: E501

        :param wcag_level: The wcag_level of this VmOpenApiAccessibilityClassification.  # noqa: E501
        :type: str
        """

        self._wcag_level = wcag_level

    @property
    def accessibility_statement_web_page_name(self):
        """Gets the accessibility_statement_web_page_name of this VmOpenApiAccessibilityClassification.  # noqa: E501

        Gets or sets the accessibility classification web page name. (Max.Length: 100).  # noqa: E501

        :return: The accessibility_statement_web_page_name of this VmOpenApiAccessibilityClassification.  # noqa: E501
        :rtype: str
        """
        return self._accessibility_statement_web_page_name

    @accessibility_statement_web_page_name.setter
    def accessibility_statement_web_page_name(self, accessibility_statement_web_page_name):
        """Sets the accessibility_statement_web_page_name of this VmOpenApiAccessibilityClassification.

        Gets or sets the accessibility classification web page name. (Max.Length: 100).  # noqa: E501

        :param accessibility_statement_web_page_name: The accessibility_statement_web_page_name of this VmOpenApiAccessibilityClassification.  # noqa: E501
        :type: str
        """

        self._accessibility_statement_web_page_name = accessibility_statement_web_page_name

    @property
    def accessibility_statement_web_page(self):
        """Gets the accessibility_statement_web_page of this VmOpenApiAccessibilityClassification.  # noqa: E501

        Gets or sets the accessibility classification web page url. (Max.Length: 500).  # noqa: E501

        :return: The accessibility_statement_web_page of this VmOpenApiAccessibilityClassification.  # noqa: E501
        :rtype: str
        """
        return self._accessibility_statement_web_page

    @accessibility_statement_web_page.setter
    def accessibility_statement_web_page(self, accessibility_statement_web_page):
        """Sets the accessibility_statement_web_page of this VmOpenApiAccessibilityClassification.

        Gets or sets the accessibility classification web page url. (Max.Length: 500).  # noqa: E501

        :param accessibility_statement_web_page: The accessibility_statement_web_page of this VmOpenApiAccessibilityClassification.  # noqa: E501
        :type: str
        """

        self._accessibility_statement_web_page = accessibility_statement_web_page

    @property
    def language(self):
        """Gets the language of this VmOpenApiAccessibilityClassification.  # noqa: E501

        Language code.  # noqa: E501

        :return: The language of this VmOpenApiAccessibilityClassification.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this VmOpenApiAccessibilityClassification.

        Language code.  # noqa: E501

        :param language: The language of this VmOpenApiAccessibilityClassification.  # noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def id(self):
        """Gets the id of this VmOpenApiAccessibilityClassification.  # noqa: E501

        Gets or sets the identifier.  # noqa: E501

        :return: The id of this VmOpenApiAccessibilityClassification.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VmOpenApiAccessibilityClassification.

        Gets or sets the identifier.  # noqa: E501

        :param id: The id of this VmOpenApiAccessibilityClassification.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def owner_reference_id(self):
        """Gets the owner_reference_id of this VmOpenApiAccessibilityClassification.  # noqa: E501

        Gets or sets the owner reference identifier.  # noqa: E501

        :return: The owner_reference_id of this VmOpenApiAccessibilityClassification.  # noqa: E501
        :rtype: str
        """
        return self._owner_reference_id

    @owner_reference_id.setter
    def owner_reference_id(self, owner_reference_id):
        """Sets the owner_reference_id of this VmOpenApiAccessibilityClassification.

        Gets or sets the owner reference identifier.  # noqa: E501

        :param owner_reference_id: The owner_reference_id of this VmOpenApiAccessibilityClassification.  # noqa: E501
        :type: str
        """

        self._owner_reference_id = owner_reference_id

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
        if issubclass(VmOpenApiAccessibilityClassification, dict):
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
        if not isinstance(other, VmOpenApiAccessibilityClassification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
