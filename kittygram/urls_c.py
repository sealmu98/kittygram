from django.urls import path

from cats.views_c import APICat, APICatDetail

urlpatterns = [
    path('cats/', APICat.as_view()),
    path('cats/<int:pk>/', APICatDetail.as_view()),
]
