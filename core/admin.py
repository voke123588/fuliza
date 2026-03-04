from django.contrib import admin
from .models import FulizaRequest


@admin.register(FulizaRequest)
class FulizaRequestAdmin(admin.ModelAdmin):

    # Show these columns in admin list
    list_display = (
        'name',
        'phone_number',
        'selected_limit',
        'service_fee',
        'status',
        'created_at'
    )

    # Filter sidebar
    list_filter = ('status',)

    # Enable search by name & phone
    search_fields = ('name', 'phone_number')

    # Allow quick status editing from list page
    list_editable = ('status',)

    # Order: pending first, newest first
    ordering = ('status', '-created_at')

    # Custom dashboard counters template
    change_list_template = "admin/dashboard.html"

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}

        extra_context['total_requests'] = FulizaRequest.objects.count()
        extra_context['approved_count'] = FulizaRequest.objects.filter(status="approved").count()
        extra_context['pending_count'] = FulizaRequest.objects.filter(status="pending").count()
        extra_context['rejected_count'] = FulizaRequest.objects.filter(status="rejected").count()

        return super().changelist_view(request, extra_context=extra_context)