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

class V10VmOpenApiOrganizationService(object):
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
        'role_type': 'str',
        'provision_type': 'str',
        'additional_information': 'list[VmOpenApiLanguageItem]',
        'service': 'VmOpenApiItem',
        'organization_id': 'str'
    }

    attribute_map = {
        'role_type': 'roleType',
        'provision_type': 'provisionType',
        'additional_information': 'additionalInformation',
        'service': 'service',
        'organization_id': 'organizationId'
    }

    def __init__(self, role_type=None, provision_type=None, additional_information=None, service=None, organization_id=None):  # noqa: E501
        """V10VmOpenApiOrganizationService - a model defined in Swagger"""  # noqa: E501
        self._role_type = None
        self._provision_type = None
        self._additional_information = None
        self._service = None
        self._organization_id = None
        self.discriminator = None
        self.role_type = role_type
        if provision_type is not None:
            self.provision_type = provision_type
        if additional_information is not None:
            self.additional_information = additional_information
        if service is not None:
            self.service = service
        if organization_id is not None:
            self.organization_id = organization_id

    @property
    def role_type(self):
        """Gets the role_type of this V10VmOpenApiOrganizationService.  # noqa: E501

        Role type, valid values Responsible or Producer. In version 7 and upper also OtherResponsible role type is used.  # noqa: E501

        :return: The role_type of this V10VmOpenApiOrganizationService.  # noqa: E501
        :rtype: str
        """
        return self._role_type

    @role_type.setter
    def role_type(self, role_type):
        """Sets the role_type of this V10VmOpenApiOrganizationService.

        Role type, valid values Responsible or Producer. In version 7 and upper also OtherResponsible role type is used.  # noqa: E501

        :param role_type: The role_type of this V10VmOpenApiOrganizationService.  # noqa: E501
        :type: str
        """
        if role_type is None:
            raise ValueError("Invalid value for `role_type`, must not be `None`")  # noqa: E501

        self._role_type = role_type

    @property
    def provision_type(self):
        """Gets the provision_type of this V10VmOpenApiOrganizationService.  # noqa: E501

        Provision type, valid values SelfProduced, PurchaseServices, Other or VoucherServices. Required if RoleType value is Producer.  # noqa: E501

        :return: The provision_type of this V10VmOpenApiOrganizationService.  # noqa: E501
        :rtype: str
        """
        return self._provision_type

    @provision_type.setter
    def provision_type(self, provision_type):
        """Sets the provision_type of this V10VmOpenApiOrganizationService.

        Provision type, valid values SelfProduced, PurchaseServices, Other or VoucherServices. Required if RoleType value is Producer.  # noqa: E501

        :param provision_type: The provision_type of this V10VmOpenApiOrganizationService.  # noqa: E501
        :type: str
        """

        self._provision_type = provision_type

    @property
    def additional_information(self):
        """Gets the additional_information of this V10VmOpenApiOrganizationService.  # noqa: E501

        Localized list of additional information.  # noqa: E501

        :return: The additional_information of this V10VmOpenApiOrganizationService.  # noqa: E501
        :rtype: list[VmOpenApiLanguageItem]
        """
        return self._additional_information

    @additional_information.setter
    def additional_information(self, additional_information):
        """Sets the additional_information of this V10VmOpenApiOrganizationService.

        Localized list of additional information.  # noqa: E501

        :param additional_information: The additional_information of this V10VmOpenApiOrganizationService.  # noqa: E501
        :type: list[VmOpenApiLanguageItem]
        """

        self._additional_information = additional_information

    @property
    def service(self):
        """Gets the service of this V10VmOpenApiOrganizationService.  # noqa: E501


        :return: The service of this V10VmOpenApiOrganizationService.  # noqa: E501
        :rtype: VmOpenApiItem
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this V10VmOpenApiOrganizationService.


        :param service: The service of this V10VmOpenApiOrganizationService.  # noqa: E501
        :type: VmOpenApiItem
        """

        self._service = service

    @property
    def organization_id(self):
        """Gets the organization_id of this V10VmOpenApiOrganizationService.  # noqa: E501

        PTV organization identifier (organization related to the service).  # noqa: E501

        :return: The organization_id of this V10VmOpenApiOrganizationService.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this V10VmOpenApiOrganizationService.

        PTV organization identifier (organization related to the service).  # noqa: E501

        :param organization_id: The organization_id of this V10VmOpenApiOrganizationService.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

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
        if issubclass(V10VmOpenApiOrganizationService, dict):
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
        if not isinstance(other, V10VmOpenApiOrganizationService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
