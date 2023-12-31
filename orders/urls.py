from django.urls import path
from .views import (OrderListView,
 OrderDetailView,
 OrderCreateView,
 OrderUpdateView,
 OrderDeleteView)
from . import views

urlpatterns = [
   path('', OrderListView.as_view(), name= 'orders-home'),
   path('order/<int:pk>/', OrderDetailView.as_view(), name= 'order-detail'),
   path('order/new/', OrderCreateView.as_view(), name= 'order-create'),
   path('order/<int:pk>/update', OrderUpdateView.as_view(), name= 'order-update'),
   path('order/<int:pk>/delete', OrderDeleteView.as_view(), name= 'order-delete'),
   ]