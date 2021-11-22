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

class V8VmOpenApiOrganizationItem(object):
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
        'parent_organization_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'parent_organization_id': 'parentOrganizationId'
    }

    def __init__(self, id=None, name=None, parent_organization_id=None):  # noqa: E501
        """V8VmOpenApiOrganizationItem - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._parent_organization_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if parent_organization_id is not None:
            self.parent_organization_id = parent_organization_id

    @property
    def id(self):
        """Gets the id of this V8VmOpenApiOrganizationItem.  # noqa: E501

        Id of the item.  # noqa: E501

        :return: The id of this V8VmOpenApiOrganizationItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V8VmOpenApiOrganizationItem.

        Id of the item.  # noqa: E501

        :param id: The id of this V8VmOpenApiOrganizationItem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this V8VmOpenApiOrganizationItem.  # noqa: E501

        Name of the item.  # noqa: E501

        :return: The name of this V8VmOpenApiOrganizationItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V8VmOpenApiOrganizationItem.

        Name of the item.  # noqa: E501

        :param name: The name of this V8VmOpenApiOrganizationItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parent_organization_id(self):
        """Gets the parent_organization_id of this V8VmOpenApiOrganizationItem.  # noqa: E501

        Organizations parent organization identifier if exists.  # noqa: E501

        :return: The parent_organization_id of this V8VmOpenApiOrganizationItem.  # noqa: E501
        :rtype: str
        """
        return self._parent_organization_id

    @parent_organization_id.setter
    def parent_organization_id(self, parent_organization_id):
        """Sets the parent_organization_id of this V8VmOpenApiOrganizationItem.

        Organizations parent organization identifier if exists.  # noqa: E501

        :param parent_organization_id: The parent_organization_id of this V8VmOpenApiOrganizationItem.  # noqa: E501
        :type: str
        """

        self._parent_organization_id = parent_organization_id

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
        if issubclass(V8VmOpenApiOrganizationItem, dict):
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
        if not isinstance(other, V8VmOpenApiOrganizationItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
