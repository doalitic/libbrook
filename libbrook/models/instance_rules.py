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


class InstanceRules(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        InstanceRules - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'proto': 'str',
            'port_begin': 'str',
            'port_end': 'str',
            'source': 'str'
        }

        self.attribute_map = {
            'proto': 'proto',
            'port_begin': 'port_begin',
            'port_end': 'port_end',
            'source': 'source'
        }

        self._proto = None
        self._port_begin = None
        self._port_end = None
        self._source = None

    @property
    def proto(self):
        """
        Gets the proto of this InstanceRules.
        The protocol to allow (such as TCP, UDP, or ICMP)

        :return: The proto of this InstanceRules.
        :rtype: str
        """
        return self._proto

    @proto.setter
    def proto(self, proto):
        """
        Sets the proto of this InstanceRules.
        The protocol to allow (such as TCP, UDP, or ICMP)

        :param proto: The proto of this InstanceRules.
        :type: str
        """
        self._proto = proto

    @property
    def port_begin(self):
        """
        Gets the port_begin of this InstanceRules.
        The initial port in the range of ports to allow

        :return: The port_begin of this InstanceRules.
        :rtype: str
        """
        return self._port_begin

    @port_begin.setter
    def port_begin(self, port_begin):
        """
        Sets the port_begin of this InstanceRules.
        The initial port in the range of ports to allow

        :param port_begin: The port_begin of this InstanceRules.
        :type: str
        """
        self._port_begin = port_begin

    @property
    def port_end(self):
        """
        Gets the port_end of this InstanceRules.
        The final port in the range of ports to allow

        :return: The port_end of this InstanceRules.
        :rtype: str
        """
        return self._port_end

    @port_end.setter
    def port_end(self, port_end):
        """
        Sets the port_end of this InstanceRules.
        The final port in the range of ports to allow

        :param port_end: The port_end of this InstanceRules.
        :type: str
        """
        self._port_end = port_end

    @property
    def source(self):
        """
        Gets the source of this InstanceRules.
        An IP address range, in CIDR notation (for example, 203.0.113.0/24)

        :return: The source of this InstanceRules.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this InstanceRules.
        An IP address range, in CIDR notation (for example, 203.0.113.0/24)

        :param source: The source of this InstanceRules.
        :type: str
        """
        self._source = source

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

