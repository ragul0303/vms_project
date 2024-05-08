# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Vendor,PurchaseOrder
from .serializers import VendorSerializer,PurchaseOrderSerializer,VendorPerformanceSerializer



class VendorList(APIView):
    def get(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VendorDetail(APIView):
    def get_object(self, vendor_id):
        try:
            return Vendor.objects.get(id=vendor_id)
        except Vendor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, vendor_id):
        vendor = self.get_object(vendor_id)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)

    def put(self, request, vendor_id):
        vendor = self.get_object(vendor_id)
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, vendor_id):
        vendor = self.get_object(vendor_id)
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



###purchase

class PurchaseOrderList(APIView):
    def get(self, request):
        if 'vendor_id' in request.query_params:
            purchase_orders = PurchaseOrder.objects.filter(vendor_id=request.query_params['vendor_id'])
        else:
            purchase_orders = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(purchase_orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PurchaseOrderDetail(APIView):
    def get_object(self, po_id):
        try:
            return PurchaseOrder.objects.get(id=po_id)
        except PurchaseOrder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, po_id):
        purchase_order = self.get_object(po_id)
        serializer = PurchaseOrderSerializer(purchase_order)
        return Response(serializer.data)

    def put(self, request, po_id):
        purchase_order = self.get_object(po_id)
        serializer = PurchaseOrderSerializer(purchase_order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, po_id):
        purchase_order = self.get_object(po_id)
        purchase_order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class VendorPerformance(APIView):
    def get(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(id=vendor_id)
        except Vendor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = VendorPerformanceSerializer(vendor)
        return Response(serializer.data)

