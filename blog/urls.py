from django.urls import path
from blog.views import index_view, single_view


app_name = 'blog'

urlpatterns = [
    path('', index_view, name='index'),
    path('single', single_view, name='single')
]
