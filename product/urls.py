from django.urls import path
from .views.category import CategoryListCreateView, CategoryRetrieveUpdateDestroyView
from .views.product import ProductListCreateView, ProductRetrieveUpdateDestroyView

app_name = 'category'
urlpatterns = [
    path('category/', CategoryListCreateView.as_view()),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view()),
    path('product/', ProductListCreateView.as_view()),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view()),
]