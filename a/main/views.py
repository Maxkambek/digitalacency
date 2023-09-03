from rest_framework import generics
from .models import Blog, BlogCategory, PortfolioCategory, Portfolio, Quiz
from .serializers import BlogSerializer, BlogCategorySerializer, PortCategorySerializer, \
    QuizSerializer, PortSerializer


class BlogCategoryListAPIView(generics.ListAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer


class BlogListAPIView(generics.ListAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        queryset = Blog.objects.all()
        pk = self.request.GET.get('pk')
        if pk:
            queryset = queryset.filter(category_id=pk)
        return queryset


class BlogRetrieveAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class PortCategoryListAPIView(generics.ListAPIView):
    queryset = PortfolioCategory.objects.all()
    serializer_class = PortCategorySerializer


class PortfolioListAPIView(generics.ListAPIView):
    serializer_class = PortSerializer

    def get_queryset(self):
        queryset = Portfolio.objects.all()
        pk = self.request.GET.get('pk')
        if pk:
            queryset = queryset.filter(category_id=pk)
        return queryset


class QuizCreateAPIView(generics.CreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
