# article/serializers.py
# 0410 序列化 (自建)

from rest_framework import serializers
from appTest.models import Article

# class ArticalListSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(allow_blank=True, max_length=100)
#     body = serializers.CharField(allow_blank=True)
#     created = serializers.DateTimeField()
#     updated = serializers.DateTimeField()

#0414 代碼簡化
class ArticalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'created',
        ]

#0416 序列化器 for Class-View
class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # __all__ --> 使用所有欄位
        fields = '__all__'

