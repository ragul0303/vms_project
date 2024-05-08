from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder, Vendor, HistoricalPerformance
from django.utils import timezone
from django.db.models import Avg, Count

@receiver(post_save, sender=PurchaseOrder)
def update_performance_metrics(sender, instance, created, **kwargs):
    if instance.status == 'completed':
        # Update On-Time Delivery Rate
        completed_pos = PurchaseOrder.objects.filter(vendor=instance.vendor, status='completed')
        on_time_delivered_pos = completed_pos.filter(delivery_date__lte=instance.delivery_date)
        on_time_delivery_rate = on_time_delivered_pos.count() / completed_pos.count()
        instance.vendor.on_time_delivery_rate = on_time_delivery_rate

        # Update Quality Rating Average
        completed_pos_with_rating = completed_pos.exclude(quality_rating__isnull=True)
        quality_rating_avg = completed_pos_with_rating.aggregate(avg_quality=Avg('quality_rating'))['avg_quality'] or 0
        instance.vendor.quality_rating_avg = quality_rating_avg

        # Update Fulfillment Rate
        fulfilled_pos = completed_pos.exclude(issue_date__isnull=True)
        fulfillment_rate = fulfilled_pos.count() / PurchaseOrder.objects.filter(vendor=instance.vendor).count()
        instance.vendor.fulfillment_rate = fulfillment_rate

        instance.vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def update_average_response_time(sender, instance, created, **kwargs):
    if instance.acknowledgment_date:
        avg_response_time = PurchaseOrder.objects.filter(vendor=instance.vendor, acknowledgment_date__isnull=False).aggregate(avg_response=Avg('acknowledgment_date' - 'issue_date'))['avg_response']
        instance.vendor.average_response_time = avg_response_time
        instance.vendor.save()
