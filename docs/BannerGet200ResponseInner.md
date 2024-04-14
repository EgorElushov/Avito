# BannerGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banner_id** | **int** | Идентификатор баннера | [optional] 
**tag_ids** | **List[int]** | Идентификаторы тэгов | [optional] 
**feature_id** | **int** | Идентификатор фичи | [optional] 
**content** | **Dict[str, object]** | Содержимое баннера | [optional] 
**is_active** | **bool** | Флаг активности баннера | [optional] 
**created_at** | **datetime** | Дата создания баннера | [optional] 
**updated_at** | **datetime** | Дата обновления баннера | [optional] 

## Example

```python
from openapi_client.models.banner_get200_response_inner import BannerGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of BannerGet200ResponseInner from a JSON string
banner_get200_response_inner_instance = BannerGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(BannerGet200ResponseInner.to_json())

# convert the object into a dict
banner_get200_response_inner_dict = banner_get200_response_inner_instance.to_dict()
# create an instance of BannerGet200ResponseInner from a dict
banner_get200_response_inner_form_dict = banner_get200_response_inner.from_dict(banner_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


