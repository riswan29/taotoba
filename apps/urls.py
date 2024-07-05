from django.urls import path
from .views import *
urlpatterns = [
    path('login/', custom_login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('user/', user_dashboard, name='user_dash'),
    path('create-blog/', create_blog, name='create_blog'),
    path('blog-post/', blog_post, name='blog_post'),
]
