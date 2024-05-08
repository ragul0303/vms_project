from django.urls import path
from vms_app.views import VendorList, VendorDetail, PurchaseOrderList, PurchaseOrderDetail, VendorPerformance

urlpatterns = [
    path('api/vendors/', VendorList.as_view(), name='vendor-list'),
    path('api/vendors/<int:vendor_id>/', VendorDetail.as_view(), name='vendor-detail'),
    path('api/purchase_orders/', PurchaseOrderList.as_view(), name='purchase-order-list'),
    path('api/purchase_orders/<int:po_id>/', PurchaseOrderDetail.as_view(), name='purchase-order-detail'),
    path('api/vendors/<int:vendor_id>/performance/', VendorPerformance.as_view(), name='vendor-performance'),
]