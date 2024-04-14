# BannerPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_ids** | **List[int]** | Идентификаторы тэгов | [optional] 
**feature_id** | **int** | Идентификатор фичи | [optional] 
**content** | **Dict[str, object]** | Содержимое баннера | [optional] 
**is_active** | **bool** | Флаг активности баннера | [optional] 

## Example

```python
from openapi_client.models.banner_post_request import BannerPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BannerPostRequest from a JSON string
banner_post_request_instance = BannerPostRequest.from_json(json)
# print the JSON string representation of the object
print(BannerPostRequest.to_json())

# convert the object into a dict
banner_post_request_dict = banner_post_request_instance.to_dict()
# create an instance of BannerPostRequest from a dict
banner_post_request_form_dict = banner_post_request.from_dict(banner_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


