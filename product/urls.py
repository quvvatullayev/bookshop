from django.urls import path
from .views.category import CategoryListCreateView, CategoryRetrieveUpdateDestroyView

app_name = 'category'
urlpatterns = [
    path('category/', CategoryListCreateView.as_view()),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view())
]