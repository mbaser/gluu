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

class LdapConfiguration(object):
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
        'config_id': 'str',
        'bind_dn': 'str',
        'max_connections': 'int',
        'primary_key': 'str',
        'local_primary_key': 'str',
        'servers': 'list[str]',
        'base_d_ns': 'list[str]',
        'use_ssl': 'bool',
        'bind_password': 'str',
        'use_anonymous_bind': 'bool',
        'enabled': 'bool',
        'version': 'int'
    }

    attribute_map = {
        'config_id': 'configId',
        'bind_dn': 'bindDN',
        'max_connections': 'maxConnections',
        'primary_key': 'primaryKey',
        'local_primary_key': 'localPrimaryKey',
        'servers': 'servers',
        'base_d_ns': 'baseDNs',
        'use_ssl': 'useSSL',
        'bind_password': 'bindPassword',
        'use_anonymous_bind': 'useAnonymousBind',
        'enabled': 'enabled',
        'version': 'version'
    }

    def __init__(self, config_id=None, bind_dn=None, max_connections=2, primary_key=None, local_primary_key=None, servers=None, base_d_ns=None, use_ssl=None, bind_password=None, use_anonymous_bind=None, enabled=None, version=None):  # noqa: E501
        """LdapConfiguration - a model defined in Swagger"""  # noqa: E501
        self._config_id = None
        self._bind_dn = None
        self._max_connections = None
        self._primary_key = None
        self._local_primary_key = None
        self._servers = None
        self._base_d_ns = None
        self._use_ssl = None
        self._bind_password = None
        self._use_anonymous_bind = None
        self._enabled = None
        self._version = None
        self.discriminator = None
        self.config_id = config_id
        self.bind_dn = bind_dn
        self.max_connections = max_connections
        self.primary_key = primary_key
        self.local_primary_key = local_primary_key
        self.servers = servers
        self.base_d_ns = base_d_ns
        self.use_ssl = use_ssl
        if bind_password is not None:
            self.bind_password = bind_password
        if use_anonymous_bind is not None:
            self.use_anonymous_bind = use_anonymous_bind
        if enabled is not None:
            self.enabled = enabled
        if version is not None:
            self.version = version

    @property
    def config_id(self):
        """Gets the config_id of this LdapConfiguration.  # noqa: E501

        Unique identifier - Name  # noqa: E501

        :return: The config_id of this LdapConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        """Sets the config_id of this LdapConfiguration.

        Unique identifier - Name  # noqa: E501

        :param config_id: The config_id of this LdapConfiguration.  # noqa: E501
        :type: str
        """
        if config_id is None:
            raise ValueError("Invalid value for `config_id`, must not be `None`")  # noqa: E501

        self._config_id = config_id

    @property
    def bind_dn(self):
        """Gets the bind_dn of this LdapConfiguration.  # noqa: E501

        User Distingusihed Name for binding.  # noqa: E501

        :return: The bind_dn of this LdapConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._bind_dn

    @bind_dn.setter
    def bind_dn(self, bind_dn):
        """Sets the bind_dn of this LdapConfiguration.

        User Distingusihed Name for binding.  # noqa: E501

        :param bind_dn: The bind_dn of this LdapConfiguration.  # noqa: E501
        :type: str
        """
        if bind_dn is None:
            raise ValueError("Invalid value for `bind_dn`, must not be `None`")  # noqa: E501

        self._bind_dn = bind_dn

    @property
    def max_connections(self):
        """Gets the max_connections of this LdapConfiguration.  # noqa: E501

        Total number of simultaneous connections allowed.  # noqa: E501

        :return: The max_connections of this LdapConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._max_connections

    @max_connections.setter
    def max_connections(self, max_connections):
        """Sets the max_connections of this LdapConfiguration.

        Total number of simultaneous connections allowed.  # noqa: E501

        :param max_connections: The max_connections of this LdapConfiguration.  # noqa: E501
        :type: int
        """
        if max_connections is None:
            raise ValueError("Invalid value for `max_connections`, must not be `None`")  # noqa: E501

        self._max_connections = max_connections

    @property
    def primary_key(self):
        """Gets the primary_key of this LdapConfiguration.  # noqa: E501

        Used to search and bind operations in configured LDAP server.  # noqa: E501

        :return: The primary_key of this LdapConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._primary_key

    @primary_key.setter
    def primary_key(self, primary_key):
        """Sets the primary_key of this LdapConfiguration.

        Used to search and bind operations in configured LDAP server.  # noqa: E501

        :param primary_key: The primary_key of this LdapConfiguration.  # noqa: E501
        :type: str
        """
        if primary_key is None:
            raise ValueError("Invalid value for `primary_key`, must not be `None`")  # noqa: E501

        self._primary_key = primary_key

    @property
    def local_primary_key(self):
        """Gets the local_primary_key of this LdapConfiguration.  # noqa: E501

        Used to search local user entry in Gluu Server’s internal LDAP directory.  # noqa: E501

        :return: The local_primary_key of this LdapConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._local_primary_key

    @local_primary_key.setter
    def local_primary_key(self, local_primary_key):
        """Sets the local_primary_key of this LdapConfiguration.

        Used to search local user entry in Gluu Server’s internal LDAP directory.  # noqa: E501

        :param local_primary_key: The local_primary_key of this LdapConfiguration.  # noqa: E501
        :type: str
        """
        if local_primary_key is None:
            raise ValueError("Invalid value for `local_primary_key`, must not be `None`")  # noqa: E501

        self._local_primary_key = local_primary_key

    @property
    def servers(self):
        """Gets the servers of this LdapConfiguration.  # noqa: E501

        List of LDAP authentication servers.  # noqa: E501

        :return: The servers of this LdapConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this LdapConfiguration.

        List of LDAP authentication servers.  # noqa: E501

        :param servers: The servers of this LdapConfiguration.  # noqa: E501
        :type: list[str]
        """
        if servers is None:
            raise ValueError("Invalid value for `servers`, must not be `None`")  # noqa: E501

        self._servers = servers

    @property
    def base_d_ns(self):
        """Gets the base_d_ns of this LdapConfiguration.  # noqa: E501

        list of LDAP base Distingusihed Name  # noqa: E501

        :return: The base_d_ns of this LdapConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._base_d_ns

    @base_d_ns.setter
    def base_d_ns(self, base_d_ns):
        """Sets the base_d_ns of this LdapConfiguration.

        list of LDAP base Distingusihed Name  # noqa: E501

        :param base_d_ns: The base_d_ns of this LdapConfiguration.  # noqa: E501
        :type: list[str]
        """
        if base_d_ns is None:
            raise ValueError("Invalid value for `base_d_ns`, must not be `None`")  # noqa: E501

        self._base_d_ns = base_d_ns

    @property
    def use_ssl(self):
        """Gets the use_ssl of this LdapConfiguration.  # noqa: E501


        :return: The use_ssl of this LdapConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._use_ssl

    @use_ssl.setter
    def use_ssl(self, use_ssl):
        """Sets the use_ssl of this LdapConfiguration.


        :param use_ssl: The use_ssl of this LdapConfiguration.  # noqa: E501
        :type: bool
        """
        if use_ssl is None:
            raise ValueError("Invalid value for `use_ssl`, must not be `None`")  # noqa: E501

        self._use_ssl = use_ssl

    @property
    def bind_password(self):
        """Gets the bind_password of this LdapConfiguration.  # noqa: E501

        User password for binding.  # noqa: E501

        :return: The bind_password of this LdapConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._bind_password

    @bind_password.setter
    def bind_password(self, bind_password):
        """Sets the bind_password of this LdapConfiguration.

        User password for binding.  # noqa: E501

        :param bind_password: The bind_password of this LdapConfiguration.  # noqa: E501
        :type: str
        """

        self._bind_password = bind_password

    @property
    def use_anonymous_bind(self):
        """Gets the use_anonymous_bind of this LdapConfiguration.  # noqa: E501

        Boolean value used to indicate if the LDAP Server will allow anonymous bind request.  # noqa: E501

        :return: The use_anonymous_bind of this LdapConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._use_anonymous_bind

    @use_anonymous_bind.setter
    def use_anonymous_bind(self, use_anonymous_bind):
        """Sets the use_anonymous_bind of this LdapConfiguration.

        Boolean value used to indicate if the LDAP Server will allow anonymous bind request.  # noqa: E501

        :param use_anonymous_bind: The use_anonymous_bind of this LdapConfiguration.  # noqa: E501
        :type: bool
        """

        self._use_anonymous_bind = use_anonymous_bind

    @property
    def enabled(self):
        """Gets the enabled of this LdapConfiguration.  # noqa: E501


        :return: The enabled of this LdapConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this LdapConfiguration.


        :param enabled: The enabled of this LdapConfiguration.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def version(self):
        """Gets the version of this LdapConfiguration.  # noqa: E501


        :return: The version of this LdapConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this LdapConfiguration.


        :param version: The version of this LdapConfiguration.  # noqa: E501
        :type: int
        """

        self._version = version

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
        if issubclass(LdapConfiguration, dict):
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
        if not isinstance(other, LdapConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other