from django.db import models


class BlogCategory(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name

    @property
    def get_count(self):
        return self.blog_category.count()


class Blog(models.Model):
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='blog_category')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    video = models.FileField(upload_to='files/', null=True, blank=True)
    title = models.CharField(max_length=233)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    introduction = models.CharField(max_length=233)
    introduction_text = models.TextField()
    main_big_image = models.ImageField(upload_to='images/')
    image_1 = models.ImageField(upload_to='images/')
    image_2 = models.ImageField(upload_to='images/')
    image_3 = models.ImageField(upload_to='images/')
    image_4 = models.ImageField(upload_to='images/')
    sub_title = models.CharField(max_length=233)
    sub_content = models.TextField()
    image_double_1 = models.ImageField(upload_to='images/', null=True, blank=True)
    image_double_2 = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title


class PortfolioCategory(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name

    @property
    def get_count(self):
        return self.port_category.count()


class Portfolio(models.Model):
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE, related_name='port_category')
    name = models.CharField(max_length=123)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Quiz(models.Model):
    type_site = models.CharField(max_length=123)
    logo = models.CharField(max_length=123)
    level_creative = models.CharField(max_length=123)
    level_functionality = models.CharField(max_length=123)
    site_exist = models.CharField(max_length=20)
    name = models.CharField(max_length=123)
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name
