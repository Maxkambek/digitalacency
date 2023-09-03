from rest_framework import serializers
from .models import BlogCategory, Blog, Portfolio, PortfolioCategory, Quiz


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['id', 'name', 'get_count']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class PortCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioCategory
        fields = ['id', 'name', 'get_count']


class PortSerializer(serializers.ModelSerializer):
    category = PortCategorySerializer()

    class Meta:
        model = Portfolio
        fields = ['id', 'name', 'description', 'image', 'link', 'category']


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
