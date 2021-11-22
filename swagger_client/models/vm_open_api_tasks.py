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

class VmOpenApiTasks(object):
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
        'page_number': 'int',
        'page_size': 'int',
        'page_count': 'int',
        'item_list': 'list[VmOpenApiTask]'
    }

    attribute_map = {
        'page_number': 'pageNumber',
        'page_size': 'pageSize',
        'page_count': 'pageCount',
        'item_list': 'itemList'
    }

    def __init__(self, page_number=None, page_size=None, page_count=None, item_list=None):  # noqa: E501
        """VmOpenApiTasks - a model defined in Swagger"""  # noqa: E501
        self._page_number = None
        self._page_size = None
        self._page_count = None
        self._item_list = None
        self.discriminator = None
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if page_count is not None:
            self.page_count = page_count
        if item_list is not None:
            self.item_list = item_list

    @property
    def page_number(self):
        """Gets the page_number of this VmOpenApiTasks.  # noqa: E501

        Resultset page number (resultset paging). Page numbering starts from one.  # noqa: E501

        :return: The page_number of this VmOpenApiTasks.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this VmOpenApiTasks.

        Resultset page number (resultset paging). Page numbering starts from one.  # noqa: E501

        :param page_number: The page_number of this VmOpenApiTasks.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this VmOpenApiTasks.  # noqa: E501

        How many results per page are returned (resultset paging).  # noqa: E501

        :return: The page_size of this VmOpenApiTasks.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this VmOpenApiTasks.

        How many results per page are returned (resultset paging).  # noqa: E501

        :param page_size: The page_size of this VmOpenApiTasks.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def page_count(self):
        """Gets the page_count of this VmOpenApiTasks.  # noqa: E501

        Total count of pages the resultset has (resultset paging).  # noqa: E501

        :return: The page_count of this VmOpenApiTasks.  # noqa: E501
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """Sets the page_count of this VmOpenApiTasks.

        Total count of pages the resultset has (resultset paging).  # noqa: E501

        :param page_count: The page_count of this VmOpenApiTasks.  # noqa: E501
        :type: int
        """

        self._page_count = page_count

    @property
    def item_list(self):
        """Gets the item_list of this VmOpenApiTasks.  # noqa: E501

        List of entity Guids.  # noqa: E501

        :return: The item_list of this VmOpenApiTasks.  # noqa: E501
        :rtype: list[VmOpenApiTask]
        """
        return self._item_list

    @item_list.setter
    def item_list(self, item_list):
        """Sets the item_list of this VmOpenApiTasks.

        List of entity Guids.  # noqa: E501

        :param item_list: The item_list of this VmOpenApiTasks.  # noqa: E501
        :type: list[VmOpenApiTask]
        """

        self._item_list = item_list

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
        if issubclass(VmOpenApiTasks, dict):
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
        if not isinstance(other, VmOpenApiTasks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
