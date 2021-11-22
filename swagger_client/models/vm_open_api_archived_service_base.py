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

class VmOpenApiArchivedServiceBase(object):
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
        'organization_id': 'str',
        'type': 'str',
        'archiving_date': 'datetime',
        'service_names': 'list[VmOpenApiLocalizedListItem]'
    }

    attribute_map = {
        'id': 'id',
        'organization_id': 'organizationId',
        'type': 'type',
        'archiving_date': 'archivingDate',
        'service_names': 'serviceNames'
    }

    def __init__(self, id=None, organization_id=None, type=None, archiving_date=None, service_names=None):  # noqa: E501
        """VmOpenApiArchivedServiceBase - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._organization_id = None
        self._type = None
        self._archiving_date = None
        self._service_names = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if organization_id is not None:
            self.organization_id = organization_id
        if type is not None:
            self.type = type
        if archiving_date is not None:
            self.archiving_date = archiving_date
        if service_names is not None:
            self.service_names = service_names

    @property
    def id(self):
        """Gets the id of this VmOpenApiArchivedServiceBase.  # noqa: E501

        Service id.  # noqa: E501

        :return: The id of this VmOpenApiArchivedServiceBase.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VmOpenApiArchivedServiceBase.

        Service id.  # noqa: E501

        :param id: The id of this VmOpenApiArchivedServiceBase.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def organization_id(self):
        """Gets the organization_id of this VmOpenApiArchivedServiceBase.  # noqa: E501

        Organization id.  # noqa: E501

        :return: The organization_id of this VmOpenApiArchivedServiceBase.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this VmOpenApiArchivedServiceBase.

        Organization id.  # noqa: E501

        :param organization_id: The organization_id of this VmOpenApiArchivedServiceBase.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def type(self):
        """Gets the type of this VmOpenApiArchivedServiceBase.  # noqa: E501

        Service type  # noqa: E501

        :return: The type of this VmOpenApiArchivedServiceBase.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VmOpenApiArchivedServiceBase.

        Service type  # noqa: E501

        :param type: The type of this VmOpenApiArchivedServiceBase.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def archiving_date(self):
        """Gets the archiving_date of this VmOpenApiArchivedServiceBase.  # noqa: E501

        Archiving date (utc).  # noqa: E501

        :return: The archiving_date of this VmOpenApiArchivedServiceBase.  # noqa: E501
        :rtype: datetime
        """
        return self._archiving_date

    @archiving_date.setter
    def archiving_date(self, archiving_date):
        """Sets the archiving_date of this VmOpenApiArchivedServiceBase.

        Archiving date (utc).  # noqa: E501

        :param archiving_date: The archiving_date of this VmOpenApiArchivedServiceBase.  # noqa: E501
        :type: datetime
        """

        self._archiving_date = archiving_date

    @property
    def service_names(self):
        """Gets the service_names of this VmOpenApiArchivedServiceBase.  # noqa: E501

        Service names.  # noqa: E501

        :return: The service_names of this VmOpenApiArchivedServiceBase.  # noqa: E501
        :rtype: list[VmOpenApiLocalizedListItem]
        """
        return self._service_names

    @service_names.setter
    def service_names(self, service_names):
        """Sets the service_names of this VmOpenApiArchivedServiceBase.

        Service names.  # noqa: E501

        :param service_names: The service_names of this VmOpenApiArchivedServiceBase.  # noqa: E501
        :type: list[VmOpenApiLocalizedListItem]
        """

        self._service_names = service_names

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
        if issubclass(VmOpenApiArchivedServiceBase, dict):
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
        if not isinstance(other, VmOpenApiArchivedServiceBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
