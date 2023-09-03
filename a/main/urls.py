from django.urls import path
from . import views

urlpatterns = [
    path('quiz/', views.QuizCreateAPIView.as_view()),
    path('blog-categroy/', views.BlogCategoryListAPIView.as_view()),
    path('blog/', views.BlogListAPIView.as_view()),
    path('blog/<int:pk>/', views.BlogRetrieveAPIView.as_view()),
    path('portfolio-category/', views.PortCategoryListAPIView.as_view()),
    path('portfolio/', views.PortfolioListAPIView.as_view())
]
