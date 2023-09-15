from django.urls import path
from .views.authuser import AuthUserListCreateView, AuthUserRetrieveUpdateDestroyView
from .views.order import OrderListCreateView, OrderRetrieveUpdateDestroy
from .views.like import LikeListCreateView, LikeRetrieveUpdateDestroyView

urlpatterns = [
    path('order/', OrderListCreateView.as_view()),
    path('order/<int:pk>/', OrderRetrieveUpdateDestroy.as_view()),
    path('like/', LikeListCreateView.as_view()),
    path('like/<int:pk>/', LikeRetrieveUpdateDestroyView.as_view()),
]