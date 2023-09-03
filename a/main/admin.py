from django.contrib import admin
from .models import Blog, BlogCategory, PortfolioCategory, Portfolio, Quiz

admin.site.register(BlogCategory)
admin.site.register(Blog)
admin.site.register(PortfolioCategory)
admin.site.register(Portfolio)
admin.site.register(Quiz)
