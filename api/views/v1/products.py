from django.http import HttpResponse
from rest_framework import generics
from rest_framework.views import APIView

from api.models.products import Product
from api.serializers.products import ProductSerializer, BaseProductSerializer

from drf_spectacular.views import extend_schema
from rest_framework.pagination import LimitOffsetPagination
from search.documents import ProductDocuments
from elasticsearch_dsl import Q as ES_Q


@extend_schema(tags=['상품'], summary='숨김 상품을 제외한 제품 리스트')
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.visible_objects.all()    # 숨김 상품을 제외한 리스트
    serializer_class = ProductSerializer


@extend_schema(tags=['상품'], summary='상품 상세 정보')
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SearchProductAPIView(APIView, LimitOffsetPagination):
    product_base_serializer = BaseProductSerializer
    search_document = ProductDocuments

    def get(self, request, query):
        try:
            # fuzziness 글자 일치 수 (1개만 같아도 검색) ex) 1, 'auto'
            # minimum_should_match (선택 사항, 문자열) 문서가 반환되기 위해 일치해야 하는 최소 절 수
            q = ES_Q('multi_match', query=query, fields=['name'], fuzziness=1) & \
                ES_Q('bool', should=[ES_Q('match', is_default=True), ], minimum_should_match=1)

            search = self.search_document.search().query(q)
            response = search.execute()

            results = self.paginate_queryset(response, request, view=self)
            serializer = self.product_base_serializer(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return HttpResponse(e, status=500)
