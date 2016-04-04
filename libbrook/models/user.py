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


class User(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        User - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'email': 'str',
            'active': 'bool',
            'roles': 'list[Role]'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'email': 'email',
            'active': 'active',
            'roles': 'roles'
        }

        self._id = None
        self._name = None
        self._email = None
        self._active = None
        self._roles = None

    @property
    def id(self):
        """
        Gets the id of this User.
        User id

        :return: The id of this User.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this User.
        User id

        :param id: The id of this User.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this User.
        User name

        :return: The name of this User.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this User.
        User name

        :param name: The name of this User.
        :type: str
        """
        self._name = name

    @property
    def email(self):
        """
        Gets the email of this User.
        User email

        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this User.
        User email

        :param email: The email of this User.
        :type: str
        """
        self._email = email

    @property
    def active(self):
        """
        Gets the active of this User.
        User activation flag

        :return: The active of this User.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this User.
        User activation flag

        :param active: The active of this User.
        :type: bool
        """
        self._active = active

    @property
    def roles(self):
        """
        Gets the roles of this User.
        List of user roles

        :return: The roles of this User.
        :rtype: list[Role]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """
        Sets the roles of this User.
        List of user roles

        :param roles: The roles of this User.
        :type: list[Role]
        """
        self._roles = roles

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
