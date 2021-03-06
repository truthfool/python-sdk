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

class V4VmOpenApiPhoneWithType(object):
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
        'number': 'str',
        'language': 'str',
        'owner_reference_id': 'str',
        'owner_reference_id2': 'str',
        'order_number': 'int',
        'prefix_number': 'str',
        'is_finnish_service_number': 'bool',
        'additional_information': 'str',
        'service_charge_type': 'str',
        'charge_description': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'number': 'number',
        'language': 'language',
        'owner_reference_id': 'ownerReferenceId',
        'owner_reference_id2': 'ownerReferenceId2',
        'order_number': 'orderNumber',
        'prefix_number': 'prefixNumber',
        'is_finnish_service_number': 'isFinnishServiceNumber',
        'additional_information': 'additionalInformation',
        'service_charge_type': 'serviceChargeType',
        'charge_description': 'chargeDescription',
        'type': 'type'
    }

    def __init__(self, id=None, number=None, language=None, owner_reference_id=None, owner_reference_id2=None, order_number=None, prefix_number=None, is_finnish_service_number=None, additional_information=None, service_charge_type=None, charge_description=None, type=None):  # noqa: E501
        """V4VmOpenApiPhoneWithType - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._number = None
        self._language = None
        self._owner_reference_id = None
        self._owner_reference_id2 = None
        self._order_number = None
        self._prefix_number = None
        self._is_finnish_service_number = None
        self._additional_information = None
        self._service_charge_type = None
        self._charge_description = None
        self._type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.number = number
        self.language = language
        if owner_reference_id is not None:
            self.owner_reference_id = owner_reference_id
        if owner_reference_id2 is not None:
            self.owner_reference_id2 = owner_reference_id2
        if order_number is not None:
            self.order_number = order_number
        if prefix_number is not None:
            self.prefix_number = prefix_number
        if is_finnish_service_number is not None:
            self.is_finnish_service_number = is_finnish_service_number
        if additional_information is not None:
            self.additional_information = additional_information
        if service_charge_type is not None:
            self.service_charge_type = service_charge_type
        if charge_description is not None:
            self.charge_description = charge_description
        self.type = type

    @property
    def id(self):
        """Gets the id of this V4VmOpenApiPhoneWithType.  # noqa: E501

        Gets or sets the identifier.  # noqa: E501

        :return: The id of this V4VmOpenApiPhoneWithType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V4VmOpenApiPhoneWithType.

        Gets or sets the identifier.  # noqa: E501

        :param id: The id of this V4VmOpenApiPhoneWithType.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def number(self):
        """Gets the number of this V4VmOpenApiPhoneWithType.  # noqa: E501

        Phone number.  # noqa: E501

        :return: The number of this V4VmOpenApiPhoneWithType.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this V4VmOpenApiPhoneWithType.

        Phone number.  # noqa: E501

        :param number: The number of this V4VmOpenApiPhoneWithType.  # noqa: E501
        :type: str
        """
        if number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def language(self):
        """Gets the language of this V4VmOpenApiPhoneWithType.  # noqa: E501

        Language of this object. Valid values are: fi, sv or en.  # noqa: E501

        :return: The language of this V4VmOpenApiPhoneWithType.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this V4VmOpenApiPhoneWithType.

        Language of this object. Valid values are: fi, sv or en.  # noqa: E501

        :param language: The language of this V4VmOpenApiPhoneWithType.  # noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def owner_reference_id(self):
        """Gets the owner_reference_id of this V4VmOpenApiPhoneWithType.  # noqa: E501

        Gets or sets the owner reference identifier.  # noqa: E501

        :return: The owner_reference_id of this V4VmOpenApiPhoneWithType.  # noqa: E501
        :rtype: str
        """
        return self._owner_reference_id

    @owner_reference_id.setter
    def owner_reference_id(self, owner_reference_id):
        """Sets the owner_reference_id of this V4VmOpenApiPhoneWithType.

        Gets or sets the owner reference identifier.  # noqa: E501

        :param owner_reference_id: The owner_reference_id of this V4VmOpenApiPhoneWithType.  # noqa: E501
        :type: str
        """

        self._owner_reference_id = owner_reference_id

    @property
    def owner_reference_id2(self):
        """Gets the owner_reference_id2 of this V4VmOpenApiPhoneWithType.  # noqa: E501

        Gets or sets the owner reference identifier.  # noqa: E501

        :return: The owner_reference_id2 of this V4VmOpenApiPhoneWithType.  # noqa: E501
        :rtype: str
        """
        return self._owner_reference_id2

    @owner_reference_id2.setter
    def owner_reference_id2(self, owner_reference_id2):
        """Sets the owner_reference_id2 of this V4VmOpenApiPhoneWithType.

        Gets or sets the owner reference identifier.  # noqa: E501

        :param owner_reference_id2: The owner_reference_id2 of this V4VmOpenApiPhoneWithType.  # noqa: E501
        :type: str
        """

        self._owner_reference_id2 = owner_reference_id2

    @property
    def order_number(self):
        """Gets the order_number of this V4VmOpenApiPhoneWithType.  # noqa: E501

        The order of phone number.  # noqa: E501

        :return: The order_number of this V4VmOpenApiPhoneWithType.  # noqa: E501
        :rtype: int
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """Sets the order_number of this V4VmOpenApiPhoneWithType.

        The order of phone number.  # noqa: E501

        :param order_number: The order_number of this V4VmOpenApiPhoneWithType.  # noqa: E501
        :type: int
        """

        self._order_number = order_number

    @property
    def prefix_number(self):
        """Gets the prefix_number of this V4VmOpenApiPhoneWithType.  # noqa: E501

        Prefix for the phone number.  # noqa: E501

        :return: The prefix_number of this V4VmOpenApiPhoneWithType.  # noqa: E501
        :rtype: str
        """
        return self._prefix_number

    @prefix_number.setter
    def prefix_number(self, prefix_number):
        """Sets the prefix_number of this V4VmOpenApiPhoneWithType.

        Prefix for the phone number.  # noqa: E501

        :param prefix_number: The prefix_number of this V4VmOpenApiPhoneWithType.  # noqa: E501
        :type: str
        """

        self._prefix_number = prefix_number

    @property
    def is_finnish_service_number(self):
        """Gets the is_finnish_service_number of this V4VmOpenApiPhoneWithType.  # noqa: E501

        Defines if number is Finnish service number. If true prefix number can be left empty.  # noqa: E501

        :return: The is_finnish_service_number of this V4VmOpenApiPhoneWithType.  # noqa: E501
        :rtype: bool
        """
        return self._is_finnish_service_number

    @is_finnish_service_number.setter
    def is_finnish_service_number(self, is_finnish_service_number):
        """Sets the is_finnish_service_number of this V4VmOpenApiPhoneWithType.

        Defines if number is Finnish service number. If true prefix number can be left empty.  # noqa: E501

        :param is_finnish_service_number: The is_finnish_service_number of this V4VmOpenApiPhoneWithType.  # noqa: E501
        :type: bool
        """

        self._is_finnish_service_number = is_finnish_service_number

    @property
    def additional_information(self):
        """Gets the additional_information of this V4VmOpenApiPhoneWithType.  # noqa: E501

        Additional information. (Max.Length: 150).  # noqa: E501

        :return: The additional_information of this V4VmOpenApiPhoneWithType.  # noqa: E501
        :rtype: str
        """
        return self._additional_information

    @additional_information.setter
    def additional_information(self, additional_information):
        """Sets the additional_information of this V4VmOpenApiPhoneWithType.

        Additional information. (Max.Length: 150).  # noqa: E501

        :param additional_information: The additional_information of this V4VmOpenApiPhoneWithType.  # noqa: E501
        :type: str
        """

        self._additional_information = additional_information

    @property
    def service_charge_type(self):
        """Gets the service_charge_type of this V4VmOpenApiPhoneWithType.  # noqa: E501

        Service charge type. Possible values are: Chargeable, FreeOfCharge or Other.  In version 7 and older: Charged, Free or Other.  # noqa: E501

        :return: The service_charge_type of this V4VmOpenApiPhoneWithType.  # noqa: E501
        :rtype: str
        """
        return self._service_charge_type

    @service_charge_type.setter
    def service_charge_type(self, service_charge_type):
        """Sets the service_charge_type of this V4VmOpenApiPhoneWithType.

        Service charge type. Possible values are: Chargeable, FreeOfCharge or Other.  In version 7 and older: Charged, Free or Other.  # noqa: E501

        :param service_charge_type: The service_charge_type of this V4VmOpenApiPhoneWithType.  # noqa: E501
        :type: str
        """

        self._service_charge_type = service_charge_type

    @property
    def charge_description(self):
        """Gets the charge_description of this V4VmOpenApiPhoneWithType.  # noqa: E501

        Charge description. (Max.Length: 150).  # noqa: E501

        :return: The charge_description of this V4VmOpenApiPhoneWithType.  # noqa: E501
        :rtype: str
        """
        return self._charge_description

    @charge_description.setter
    def charge_description(self, charge_description):
        """Sets the charge_description of this V4VmOpenApiPhoneWithType.

        Charge description. (Max.Length: 150).  # noqa: E501

        :param charge_description: The charge_description of this V4VmOpenApiPhoneWithType.  # noqa: E501
        :type: str
        """

        self._charge_description = charge_description

    @property
    def type(self):
        """Gets the type of this V4VmOpenApiPhoneWithType.  # noqa: E501

        Phone number type (Phone, Sms or Fax).  # noqa: E501

        :return: The type of this V4VmOpenApiPhoneWithType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V4VmOpenApiPhoneWithType.

        Phone number type (Phone, Sms or Fax).  # noqa: E501

        :param type: The type of this V4VmOpenApiPhoneWithType.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if issubclass(V4VmOpenApiPhoneWithType, dict):
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
        if not isinstance(other, V4VmOpenApiPhoneWithType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
