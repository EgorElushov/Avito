# coding: utf-8

"""
    Сервис баннеров

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.banner_id_patch_request import BannerIdPatchRequest

class TestBannerIdPatchRequest(unittest.TestCase):
    """BannerIdPatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BannerIdPatchRequest:
        """Test BannerIdPatchRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BannerIdPatchRequest`
        """
        model = BannerIdPatchRequest()
        if include_optional:
            return BannerIdPatchRequest(
                tag_ids = [
                    56
                    ],
                feature_id = 56,
                content = {"title": "some_title", "text": "some_text", "url": "some_url"},
                is_active = True
            )
        else:
            return BannerIdPatchRequest(
        )
        """

    def testBannerIdPatchRequest(self):
        """Test BannerIdPatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()