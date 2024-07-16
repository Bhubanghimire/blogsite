from django.urls import path
from blog.views import blog_index, blog_category, blog_detail

urlpatterns = [
    path("", blog_index, name="blog_index"),
    path("post/<int:pk>/", blog_detail, name="blog_detail"),
    path("category/<category>/",blog_category, name="blog_category"),
]