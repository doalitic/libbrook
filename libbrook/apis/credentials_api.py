# coding: utf-8

"""
CredentialsApi.py
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
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class CredentialsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_credential(self, provider_id, credential, **kwargs):
        """
        Create credential
        Create a new credential for the provider provider_id associated with the organization given in the do_org claim of the JWT.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_credential(provider_id, credential, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str provider_id: Provider identifier (required)
        :param StoreCredentialRequest credential: New credential data (required)
        :return: Credential
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['provider_id', 'credential']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_credential" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'provider_id' is set
        if ('provider_id' not in params) or (params['provider_id'] is None):
            raise ValueError("Missing the required parameter `provider_id` when calling `create_credential`")
        # verify the required parameter 'credential' is set
        if ('credential' not in params) or (params['credential'] is None):
            raise ValueError("Missing the required parameter `credential` when calling `create_credential`")

        resource_path = '/v1/providers/{providerId}/credentials'.replace('{format}', 'json')
        path_params = {}
        if 'provider_id' in params:
            path_params['providerId'] = params['provider_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'credential' in params:
            body_params = params['credential']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Credential',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def destroy_credential(self, provider_id, credential_id, **kwargs):
        """
        Delete credential
        Delete the credential credential_id for the provider provider_id associated with the organization given in the do_org claim of the JWT.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.destroy_credential(provider_id, credential_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str provider_id: Provider identifier (required)
        :param str credential_id: Credential identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['provider_id', 'credential_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method destroy_credential" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'provider_id' is set
        if ('provider_id' not in params) or (params['provider_id'] is None):
            raise ValueError("Missing the required parameter `provider_id` when calling `destroy_credential`")
        # verify the required parameter 'credential_id' is set
        if ('credential_id' not in params) or (params['credential_id'] is None):
            raise ValueError("Missing the required parameter `credential_id` when calling `destroy_credential`")

        resource_path = '/v1/providers/{providerId}/credentials/{credentialId}'.replace('{format}', 'json')
        path_params = {}
        if 'provider_id' in params:
            path_params['providerId'] = params['provider_id']
        if 'credential_id' in params:
            path_params['credentialId'] = params['credential_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def destroy_project_credential(self, project_id, credential_id, **kwargs):
        """
        Remove credential from project
        Remove the credential credentialId for the project projectId.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.destroy_project_credential(project_id, credential_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str project_id: Project identifier (required)
        :param str credential_id: Credential identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'credential_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method destroy_project_credential" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'project_id' is set
        if ('project_id' not in params) or (params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `destroy_project_credential`")
        # verify the required parameter 'credential_id' is set
        if ('credential_id' not in params) or (params['credential_id'] is None):
            raise ValueError("Missing the required parameter `credential_id` when calling `destroy_project_credential`")

        resource_path = '/v1/projects/{projectId}/credentials/{credentialId}'.replace('{format}', 'json')
        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']
        if 'credential_id' in params:
            path_params['credentialId'] = params['credential_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def index_credentials(self, provider_id, **kwargs):
        """
        List credentials
        Retrieve the list of credentials for the provider provider_id associated with the organization given in the do_org claim of the JWT.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.index_credentials(provider_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str provider_id: Provider identifier (required)
        :return: list[Credential]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['provider_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method index_credentials" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'provider_id' is set
        if ('provider_id' not in params) or (params['provider_id'] is None):
            raise ValueError("Missing the required parameter `provider_id` when calling `index_credentials`")

        resource_path = '/v1/providers/{providerId}/credentials'.replace('{format}', 'json')
        path_params = {}
        if 'provider_id' in params:
            path_params['providerId'] = params['provider_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Credential]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def index_project_credentials(self, project_id, **kwargs):
        """
        Retrieve project credentials
        Retrieve the collection of credentials bound to the project given in the uri.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.index_project_credentials(project_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str project_id: Project identifier (required)
        :return: list[Credential]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method index_project_credentials" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'project_id' is set
        if ('project_id' not in params) or (params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `index_project_credentials`")

        resource_path = '/v1/projects/{projectId}/credentials'.replace('{format}', 'json')
        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Credential]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def set_project_credential(self, credential, **kwargs):
        """
        Bind credential to project
        Bind provided credential to the project specified within the request uri.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.set_project_credential(credential, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SetProjectCredentialRequest credential: Credential to bind (required)
        :return: Credential
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['credential']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_project_credential" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'credential' is set
        if ('credential' not in params) or (params['credential'] is None):
            raise ValueError("Missing the required parameter `credential` when calling `set_project_credential`")

        resource_path = '/v1/projects/{projectId}/credentials'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'credential' in params:
            body_params = params['credential']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Credential',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def update_credential(self, provider_id, credential_id, credential, **kwargs):
        """
        Update credential
        Updates a credential for the provider provider_id associated with the organization given in the do_org claim of the JWT.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_credential(provider_id, credential_id, credential, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str provider_id: Provider identifier (required)
        :param str credential_id: Credential identifier (required)
        :param UpdateCredentialRequest credential: New credential data (required)
        :return: Credential
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['provider_id', 'credential_id', 'credential']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_credential" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'provider_id' is set
        if ('provider_id' not in params) or (params['provider_id'] is None):
            raise ValueError("Missing the required parameter `provider_id` when calling `update_credential`")
        # verify the required parameter 'credential_id' is set
        if ('credential_id' not in params) or (params['credential_id'] is None):
            raise ValueError("Missing the required parameter `credential_id` when calling `update_credential`")
        # verify the required parameter 'credential' is set
        if ('credential' not in params) or (params['credential'] is None):
            raise ValueError("Missing the required parameter `credential` when calling `update_credential`")

        resource_path = '/v1/providers/{providerId}/credentials/{credentialId}'.replace('{format}', 'json')
        path_params = {}
        if 'provider_id' in params:
            path_params['providerId'] = params['provider_id']
        if 'credential_id' in params:
            path_params['credentialId'] = params['credential_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'credential' in params:
            body_params = params['credential']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Credential',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
