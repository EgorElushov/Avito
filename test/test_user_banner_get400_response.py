# coding: utf-8

"""
    Сервис баннеров

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.user_banner_get400_response import UserBannerGet400Response

class TestUserBannerGet400Response(unittest.TestCase):
    """UserBannerGet400Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserBannerGet400Response:
        """Test UserBannerGet400Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserBannerGet400Response`
        """
        model = UserBannerGet400Response()
        if include_optional:
            return UserBannerGet400Response(
                error = ''
            )
        else:
            return UserBannerGet400Response(
        )
        """

    def testUserBannerGet400Response(self):
        """Test UserBannerGet400Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
