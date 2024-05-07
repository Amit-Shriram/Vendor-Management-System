from django.urls import path
from . import views

urlpatterns = [
    path('api/vendors/', views.VendorList.as_view(), name='vendor-list'),
    path('api/vendors/<int:vendor_id>/', views.VendorDetail.as_view(), name='vendor-detail'),
    path('api/purchase_orders/', views.PurchaseOrderList.as_view(), name='purchaseorder-list'),
    path('api/purchase_orders/<int:po_id>/', views.PurchaseOrderDetail.as_view(), name='purchaseorder-detail'),
]
