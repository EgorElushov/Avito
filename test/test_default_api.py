# coding: utf-8

"""
    Сервис баннеров

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DefaultApi()

    def tearDown(self) -> None:
        pass

    def test_banner_get(self) -> None:
        """Test case for banner_get

        Получение всех баннеров c фильтрацией по фиче и/или тегу
        """
        pass

    def test_banner_id_delete(self) -> None:
        """Test case for banner_id_delete

        Удаление баннера по идентификатору
        """
        pass

    def test_banner_id_patch(self) -> None:
        """Test case for banner_id_patch

        Обновление содержимого баннера
        """
        pass

    def test_banner_post(self) -> None:
        """Test case for banner_post

        Создание нового баннера
        """
        pass

    def test_user_banner_get(self) -> None:
        """Test case for user_banner_get

        Получение баннера для пользователя
        """
        pass


if __name__ == '__main__':
    unittest.main()
