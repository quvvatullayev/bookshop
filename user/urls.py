from django.urls import path
from .views.authuser import AuthUserListCreateView, AuthUserRetrieveUpdateDestroyView
from .views.order import OrderListCreateView, OrderRetrieveUpdateDestroy

urlpatterns = [
    path('order/', OrderListCreateView.as_view()),
    path('order/<int:pk>/', OrderRetrieveUpdateDestroy.as_view()),
]