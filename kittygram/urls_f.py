from django.urls import path

from cats.views_f import cat_list, cat_detail

urlpatterns = [
    path('cats/', cat_list),
    path('cats/<int:pk>/', cat_detail),
]
