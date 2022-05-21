from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from api.models import products


# 엘라스틱서치에 실제로 색인을 생성할 대상을 알려주는 인스턴스
@registry.register_document
class ProductDocuments(Document):
    # product = fields.ObjectField(
    #     properties={
    #         "name": fields.TextField()
    #     }
    # )

    class Index:
        name = "product"

    class Django:
        model = products.Product

        # drf와 함께 사용하는지 확인
        fields = [
            'id', 'name'
        ]
