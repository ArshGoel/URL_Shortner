# admin.py
from django.contrib import admin
from .models import Url

class UrlAdmin(admin.ModelAdmin):
    # Define which fields to display in the list view
    list_display = ('user', 'target_url', 'alias', 'timestamp', 'clicks', 'clicks_per_day', 'clicks_per_month')

    # Add search functionality
    search_fields = ('user__username', 'target_url', 'alias')  # Search by user (username), target_url or alias

    # Add filters to make it easier to filter by date
    list_filter = ('timestamp', 'clicks_per_day', 'clicks_per_month')

    # Allow ordering of results
    ordering = ('-timestamp',)

    # Define which fields to be editable in the admin list view
    list_editable = ('clicks_per_day', 'clicks_per_month')

    # Display the number of clicks in a readable way
    def total_clicks(self, obj):
        return obj.clicks
    total_clicks.short_description = 'Total Clicks'

    # You can also configure inlines if you need to add other related models

# Register the model with the custom admin class
admin.site.register(Url, UrlAdmin)
