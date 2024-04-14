# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**banner_get**](DefaultApi.md#banner_get) | **GET** /banner | Получение всех баннеров c фильтрацией по фиче и/или тегу
[**banner_id_delete**](DefaultApi.md#banner_id_delete) | **DELETE** /banner/{id} | Удаление баннера по идентификатору
[**banner_id_patch**](DefaultApi.md#banner_id_patch) | **PATCH** /banner/{id} | Обновление содержимого баннера
[**banner_post**](DefaultApi.md#banner_post) | **POST** /banner | Создание нового баннера
[**user_banner_get**](DefaultApi.md#user_banner_get) | **GET** /user_banner | Получение баннера для пользователя


# **banner_get**
> List[BannerGet200ResponseInner] banner_get(token=token, feature_id=feature_id, tag_id=tag_id, limit=limit, offset=offset)

Получение всех баннеров c фильтрацией по фиче и/или тегу

### Example


```python
import openapi_client
from openapi_client.models.banner_get200_response_inner import BannerGet200ResponseInner
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    token = 'admin_token' # str | Токен админа (optional)
    feature_id = 56 # int |  (optional)
    tag_id = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)

    try:
        # Получение всех баннеров c фильтрацией по фиче и/или тегу
        api_response = api_instance.banner_get(token=token, feature_id=feature_id, tag_id=tag_id, limit=limit, offset=offset)
        print("The response of DefaultApi->banner_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->banner_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Токен админа | [optional] 
 **feature_id** | **int**|  | [optional] 
 **tag_id** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 

### Return type

[**List[BannerGet200ResponseInner]**](BannerGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Пользователь не имеет доступа |  -  |
**500** | Внутренняя ошибка сервера |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **banner_id_delete**
> banner_id_delete(id, token=token)

Удаление баннера по идентификатору

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 56 # int | 
    token = 'admin_token' # str | Токен админа (optional)

    try:
        # Удаление баннера по идентификатору
        api_instance.banner_id_delete(id, token=token)
    except Exception as e:
        print("Exception when calling DefaultApi->banner_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **token** | **str**| Токен админа | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Баннер успешно удален |  -  |
**400** | Некорректные данные |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Пользователь не имеет доступа |  -  |
**404** | Баннер для тэга не найден |  -  |
**500** | Внутренняя ошибка сервера |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **banner_id_patch**
> banner_id_patch(id, banner_id_patch_request, token=token)

Обновление содержимого баннера

### Example


```python
import openapi_client
from openapi_client.models.banner_id_patch_request import BannerIdPatchRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 56 # int | 
    banner_id_patch_request = openapi_client.BannerIdPatchRequest() # BannerIdPatchRequest | 
    token = 'admin_token' # str | Токен админа (optional)

    try:
        # Обновление содержимого баннера
        api_instance.banner_id_patch(id, banner_id_patch_request, token=token)
    except Exception as e:
        print("Exception when calling DefaultApi->banner_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **banner_id_patch_request** | [**BannerIdPatchRequest**](BannerIdPatchRequest.md)|  | 
 **token** | **str**| Токен админа | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Некорректные данные |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Пользователь не имеет доступа |  -  |
**404** | Баннер не найден |  -  |
**500** | Внутренняя ошибка сервера |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **banner_post**
> BannerPost201Response banner_post(banner_post_request, token=token)

Создание нового баннера

### Example


```python
import openapi_client
from openapi_client.models.banner_post201_response import BannerPost201Response
from openapi_client.models.banner_post_request import BannerPostRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    banner_post_request = openapi_client.BannerPostRequest() # BannerPostRequest | 
    token = 'admin_token' # str | Токен админа (optional)

    try:
        # Создание нового баннера
        api_response = api_instance.banner_post(banner_post_request, token=token)
        print("The response of DefaultApi->banner_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->banner_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **banner_post_request** | [**BannerPostRequest**](BannerPostRequest.md)|  | 
 **token** | **str**| Токен админа | [optional] 

### Return type

[**BannerPost201Response**](BannerPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Некорректные данные |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Пользователь не имеет доступа |  -  |
**500** | Внутренняя ошибка сервера |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_banner_get**
> Dict[str, object] user_banner_get(tag_id, feature_id, use_last_revision=use_last_revision, token=token)

Получение баннера для пользователя

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    tag_id = 56 # int | 
    feature_id = 56 # int | 
    use_last_revision = False # bool |  (optional) (default to False)
    token = 'user_token' # str | Токен пользователя (optional)

    try:
        # Получение баннера для пользователя
        api_response = api_instance.user_banner_get(tag_id, feature_id, use_last_revision=use_last_revision, token=token)
        print("The response of DefaultApi->user_banner_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->user_banner_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **int**|  | 
 **feature_id** | **int**|  | 
 **use_last_revision** | **bool**|  | [optional] [default to False]
 **token** | **str**| Токен пользователя | [optional] 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Баннер пользователя |  -  |
**400** | Некорректные данные |  -  |
**401** | Пользователь не авторизован |  -  |
**403** | Пользователь не имеет доступа |  -  |
**404** | Баннер для не найден |  -  |
**500** | Внутренняя ошибка сервера |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

