# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class Image(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Image - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'os_name': 'str',
            'image_name': 'str',
            'details': 'list[str]'
        }

        self.attribute_map = {
            'id': 'id',
            'os_name': 'os_name',
            'image_name': 'image_name',
            'details': 'details'
        }

        self._id = None
        self._os_name = None
        self._image_name = None
        self._details = None

    @property
    def id(self):
        """
        Gets the id of this Image.
        Image id

        :return: The id of this Image.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Image.
        Image id

        :param id: The id of this Image.
        :type: str
        """
        self._id = id

    @property
    def os_name(self):
        """
        Gets the os_name of this Image.
        Operating system name (e.g. ‘Debian’, ‘Ubuntu’, ‘CentOS’, etc).

        :return: The os_name of this Image.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        """
        Sets the os_name of this Image.
        Operating system name (e.g. ‘Debian’, ‘Ubuntu’, ‘CentOS’, etc).

        :param os_name: The os_name of this Image.
        :type: str
        """
        self._os_name = os_name

    @property
    def image_name(self):
        """
        Gets the image_name of this Image.
        Name of the image within the provider.

        :return: The image_name of this Image.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """
        Sets the image_name of this Image.
        Name of the image within the provider.

        :param image_name: The image_name of this Image.
        :type: str
        """
        self._image_name = image_name

    @property
    def details(self):
        """
        Gets the details of this Image.
        Extra information provided at image creation.

        :return: The details of this Image.
        :rtype: list[str]
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this Image.
        Extra information provided at image creation.

        :param details: The details of this Image.
        :type: list[str]
        """
        self._details = details

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

