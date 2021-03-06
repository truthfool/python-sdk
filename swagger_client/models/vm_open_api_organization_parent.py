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

class VmOpenApiOrganizationParent(object):
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
        'organization_names': 'list[VmOpenApiLocalizedListItem]',
        'parent': 'VmOpenApiOrganizationParent'
    }

    attribute_map = {
        'id': 'id',
        'organization_names': 'organizationNames',
        'parent': 'parent'
    }

    def __init__(self, id=None, organization_names=None, parent=None):  # noqa: E501
        """VmOpenApiOrganizationParent - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._organization_names = None
        self._parent = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if organization_names is not None:
            self.organization_names = organization_names
        if parent is not None:
            self.parent = parent

    @property
    def id(self):
        """Gets the id of this VmOpenApiOrganizationParent.  # noqa: E501

        Entity identifier.  # noqa: E501

        :return: The id of this VmOpenApiOrganizationParent.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VmOpenApiOrganizationParent.

        Entity identifier.  # noqa: E501

        :param id: The id of this VmOpenApiOrganizationParent.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def organization_names(self):
        """Gets the organization_names of this VmOpenApiOrganizationParent.  # noqa: E501

        List of organization names. Possible type values are: Name, AlternativeName.  # noqa: E501

        :return: The organization_names of this VmOpenApiOrganizationParent.  # noqa: E501
        :rtype: list[VmOpenApiLocalizedListItem]
        """
        return self._organization_names

    @organization_names.setter
    def organization_names(self, organization_names):
        """Sets the organization_names of this VmOpenApiOrganizationParent.

        List of organization names. Possible type values are: Name, AlternativeName.  # noqa: E501

        :param organization_names: The organization_names of this VmOpenApiOrganizationParent.  # noqa: E501
        :type: list[VmOpenApiLocalizedListItem]
        """

        self._organization_names = organization_names

    @property
    def parent(self):
        """Gets the parent of this VmOpenApiOrganizationParent.  # noqa: E501


        :return: The parent of this VmOpenApiOrganizationParent.  # noqa: E501
        :rtype: VmOpenApiOrganizationParent
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this VmOpenApiOrganizationParent.


        :param parent: The parent of this VmOpenApiOrganizationParent.  # noqa: E501
        :type: VmOpenApiOrganizationParent
        """

        self._parent = parent

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
        if issubclass(VmOpenApiOrganizationParent, dict):
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
        if not isinstance(other, VmOpenApiOrganizationParent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
