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

class V9VmOpenApiExtraType(object):
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
        'type': 'str',
        'code': 'str',
        'description': 'list[VmOpenApiLanguageItem]',
        'service_guid': 'str',
        'channel_guid': 'str',
        'name': 'list[VmOpenApiLanguageItem]'
    }

    attribute_map = {
        'type': 'type',
        'code': 'code',
        'description': 'description',
        'service_guid': 'serviceGuid',
        'channel_guid': 'channelGuid',
        'name': 'name'
    }

    def __init__(self, type=None, code=None, description=None, service_guid=None, channel_guid=None, name=None):  # noqa: E501
        """V9VmOpenApiExtraType - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._code = None
        self._description = None
        self._service_guid = None
        self._channel_guid = None
        self._name = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if code is not None:
            self.code = code
        if description is not None:
            self.description = description
        if service_guid is not None:
            self.service_guid = service_guid
        if channel_guid is not None:
            self.channel_guid = channel_guid
        if name is not None:
            self.name = name

    @property
    def type(self):
        """Gets the type of this V9VmOpenApiExtraType.  # noqa: E501

        Type of the area (Asti).  # noqa: E501

        :return: The type of this V9VmOpenApiExtraType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V9VmOpenApiExtraType.

        Type of the area (Asti).  # noqa: E501

        :param type: The type of this V9VmOpenApiExtraType.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def code(self):
        """Gets the code of this V9VmOpenApiExtraType.  # noqa: E501

        Code of the extra type.  In Asti case the code can be DocumentReceived, GuidanceToOnlineSelfService, LostAndFound, OnlineSelfServicePoint,  OnsiteGuidance, OnsiteGuidanceByServiceAuthor or RemoteGuidance  # noqa: E501

        :return: The code of this V9VmOpenApiExtraType.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this V9VmOpenApiExtraType.

        Code of the extra type.  In Asti case the code can be DocumentReceived, GuidanceToOnlineSelfService, LostAndFound, OnlineSelfServicePoint,  OnsiteGuidance, OnsiteGuidanceByServiceAuthor or RemoteGuidance  # noqa: E501

        :param code: The code of this V9VmOpenApiExtraType.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def description(self):
        """Gets the description of this V9VmOpenApiExtraType.  # noqa: E501

        List of localized extra type descriptions.  # noqa: E501

        :return: The description of this V9VmOpenApiExtraType.  # noqa: E501
        :rtype: list[VmOpenApiLanguageItem]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V9VmOpenApiExtraType.

        List of localized extra type descriptions.  # noqa: E501

        :param description: The description of this V9VmOpenApiExtraType.  # noqa: E501
        :type: list[VmOpenApiLanguageItem]
        """

        self._description = description

    @property
    def service_guid(self):
        """Gets the service_guid of this V9VmOpenApiExtraType.  # noqa: E501

        Gets or sets the service unique identifier.  # noqa: E501

        :return: The service_guid of this V9VmOpenApiExtraType.  # noqa: E501
        :rtype: str
        """
        return self._service_guid

    @service_guid.setter
    def service_guid(self, service_guid):
        """Sets the service_guid of this V9VmOpenApiExtraType.

        Gets or sets the service unique identifier.  # noqa: E501

        :param service_guid: The service_guid of this V9VmOpenApiExtraType.  # noqa: E501
        :type: str
        """

        self._service_guid = service_guid

    @property
    def channel_guid(self):
        """Gets the channel_guid of this V9VmOpenApiExtraType.  # noqa: E501

        Gets or sets the channel unique identifier.  # noqa: E501

        :return: The channel_guid of this V9VmOpenApiExtraType.  # noqa: E501
        :rtype: str
        """
        return self._channel_guid

    @channel_guid.setter
    def channel_guid(self, channel_guid):
        """Sets the channel_guid of this V9VmOpenApiExtraType.

        Gets or sets the channel unique identifier.  # noqa: E501

        :param channel_guid: The channel_guid of this V9VmOpenApiExtraType.  # noqa: E501
        :type: str
        """

        self._channel_guid = channel_guid

    @property
    def name(self):
        """Gets the name of this V9VmOpenApiExtraType.  # noqa: E501

        List of localized entity names.  # noqa: E501

        :return: The name of this V9VmOpenApiExtraType.  # noqa: E501
        :rtype: list[VmOpenApiLanguageItem]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V9VmOpenApiExtraType.

        List of localized entity names.  # noqa: E501

        :param name: The name of this V9VmOpenApiExtraType.  # noqa: E501
        :type: list[VmOpenApiLanguageItem]
        """

        self._name = name

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
        if issubclass(V9VmOpenApiExtraType, dict):
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
        if not isinstance(other, V9VmOpenApiExtraType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other