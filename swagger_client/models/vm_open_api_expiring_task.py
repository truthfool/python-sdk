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

class VmOpenApiExpiringTask(object):
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
        'statuses': 'list[VmOpenApiLanguageItem]',
        'modified_by': 'str',
        'expires': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'statuses': 'statuses',
        'modified_by': 'modifiedBy',
        'expires': 'expires'
    }

    def __init__(self, id=None, name=None, statuses=None, modified_by=None, expires=None):  # noqa: E501
        """VmOpenApiExpiringTask - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._statuses = None
        self._modified_by = None
        self._expires = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if statuses is not None:
            self.statuses = statuses
        if modified_by is not None:
            self.modified_by = modified_by
        if expires is not None:
            self.expires = expires

    @property
    def id(self):
        """Gets the id of this VmOpenApiExpiringTask.  # noqa: E501

        Id of the item.  # noqa: E501

        :return: The id of this VmOpenApiExpiringTask.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VmOpenApiExpiringTask.

        Id of the item.  # noqa: E501

        :param id: The id of this VmOpenApiExpiringTask.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this VmOpenApiExpiringTask.  # noqa: E501

        Name of the item.  # noqa: E501

        :return: The name of this VmOpenApiExpiringTask.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VmOpenApiExpiringTask.

        Name of the item.  # noqa: E501

        :param name: The name of this VmOpenApiExpiringTask.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def statuses(self):
        """Gets the statuses of this VmOpenApiExpiringTask.  # noqa: E501

        The statuses for available languages.  # noqa: E501

        :return: The statuses of this VmOpenApiExpiringTask.  # noqa: E501
        :rtype: list[VmOpenApiLanguageItem]
        """
        return self._statuses

    @statuses.setter
    def statuses(self, statuses):
        """Sets the statuses of this VmOpenApiExpiringTask.

        The statuses for available languages.  # noqa: E501

        :param statuses: The statuses of this VmOpenApiExpiringTask.  # noqa: E501
        :type: list[VmOpenApiLanguageItem]
        """

        self._statuses = statuses

    @property
    def modified_by(self):
        """Gets the modified_by of this VmOpenApiExpiringTask.  # noqa: E501

        User who has modified the item.  # noqa: E501

        :return: The modified_by of this VmOpenApiExpiringTask.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this VmOpenApiExpiringTask.

        User who has modified the item.  # noqa: E501

        :param modified_by: The modified_by of this VmOpenApiExpiringTask.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def expires(self):
        """Gets the expires of this VmOpenApiExpiringTask.  # noqa: E501

        Date when item is expiring (UTC).  # noqa: E501

        :return: The expires of this VmOpenApiExpiringTask.  # noqa: E501
        :rtype: datetime
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this VmOpenApiExpiringTask.

        Date when item is expiring (UTC).  # noqa: E501

        :param expires: The expires of this VmOpenApiExpiringTask.  # noqa: E501
        :type: datetime
        """

        self._expires = expires

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
        if issubclass(VmOpenApiExpiringTask, dict):
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
        if not isinstance(other, VmOpenApiExpiringTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
