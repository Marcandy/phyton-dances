from rest_framework import serializers

from Article.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        field = ('title', 'content')
