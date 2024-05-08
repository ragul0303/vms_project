from rest_framework import serializers
from .models import Vendor,PurchaseOrder,HistoricalPerformance


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'



class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'

class VendorPerformanceSerializer(serializers.ModelSerializer):
    historical_performance = HistoricalPerformanceSerializer(many=True, read_only=True)

    class Meta:
        model = Vendor
        fields = ['id', 'name', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate', 'historical_performance']
