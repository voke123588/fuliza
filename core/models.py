from django.db import models


class FulizaRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    selected_limit = models.IntegerField()
    service_fee = models.IntegerField(null=True, blank=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} - {self.selected_limit} - {self.status}"