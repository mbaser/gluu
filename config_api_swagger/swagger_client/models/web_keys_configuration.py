# coding: utf-8

"""
    jans-config-api

    jans-config-api - Authorization services  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: xxx@gluu.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class WebKeysConfiguration(object):
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
        'keys': 'list[JsonWebKey]',
        'jwks_algorithms_supported': 'list[str]'
    }

    attribute_map = {
        'keys': 'keys',
        'jwks_algorithms_supported': 'jwksAlgorithmsSupported'
    }

    def __init__(self, keys=None, jwks_algorithms_supported=None):  # noqa: E501
        """WebKeysConfiguration - a model defined in Swagger"""  # noqa: E501
        self._keys = None
        self._jwks_algorithms_supported = None
        self.discriminator = None
        self.keys = keys
        if jwks_algorithms_supported is not None:
            self.jwks_algorithms_supported = jwks_algorithms_supported

    @property
    def keys(self):
        """Gets the keys of this WebKeysConfiguration.  # noqa: E501

        List of JSON Web Key (JWK) - A JSON object that represents a cryptographic key. The members of the object represent properties of the key, including its value.  # noqa: E501

        :return: The keys of this WebKeysConfiguration.  # noqa: E501
        :rtype: list[JsonWebKey]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """Sets the keys of this WebKeysConfiguration.

        List of JSON Web Key (JWK) - A JSON object that represents a cryptographic key. The members of the object represent properties of the key, including its value.  # noqa: E501

        :param keys: The keys of this WebKeysConfiguration.  # noqa: E501
        :type: list[JsonWebKey]
        """
        if keys is None:
            raise ValueError("Invalid value for `keys`, must not be `None`")  # noqa: E501

        self._keys = keys

    @property
    def jwks_algorithms_supported(self):
        """Gets the jwks_algorithms_supported of this WebKeysConfiguration.  # noqa: E501

        A list of algorithms that will be used in JWKS endpoint.  # noqa: E501

        :return: The jwks_algorithms_supported of this WebKeysConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._jwks_algorithms_supported

    @jwks_algorithms_supported.setter
    def jwks_algorithms_supported(self, jwks_algorithms_supported):
        """Sets the jwks_algorithms_supported of this WebKeysConfiguration.

        A list of algorithms that will be used in JWKS endpoint.  # noqa: E501

        :param jwks_algorithms_supported: The jwks_algorithms_supported of this WebKeysConfiguration.  # noqa: E501
        :type: list[str]
        """

        self._jwks_algorithms_supported = jwks_algorithms_supported

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
        if issubclass(WebKeysConfiguration, dict):
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
        if not isinstance(other, WebKeysConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other