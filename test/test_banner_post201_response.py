# coding: utf-8

"""
    Сервис баннеров

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.banner_post201_response import BannerPost201Response

class TestBannerPost201Response(unittest.TestCase):
    """BannerPost201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BannerPost201Response:
        """Test BannerPost201Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BannerPost201Response`
        """
        model = BannerPost201Response()
        if include_optional:
            return BannerPost201Response(
                banner_id = 56
            )
        else:
            return BannerPost201Response(
        )
        """

    def testBannerPost201Response(self):
        """Test BannerPost201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
