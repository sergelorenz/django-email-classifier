import csv
from django.http import HttpResponse
from django.contrib import admin
from django.utils.text import Truncator

from .models import ClassificationResult


# Register your models here.
class ClassificationResultsAdmin(admin.ModelAdmin):
    list_display = ('email_subject', 'truncated_email_body', 'email_class')
    readonly_fields = ('email_subject', 'email_body', 'email_class')
    search_fields = ('email_subject', 'email_body')
    list_filter = ('email_class',)
    list_per_page = 20
    actions = ['export_as_csv']

    def truncated_email_body(self, obj):
        return obj.email_body
        # return Truncator(obj.email_body).words(100)

    truncated_email_body.short_description = 'Email Body'

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    @admin.action(description='Export results as CSV')
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse()
        response['Content-Disposition'] = f'attachment; filename={meta}.csv'
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            _ = writer.writerow([getattr(obj, field) for field in field_names])

        return response


admin.site.register(ClassificationResult, ClassificationResultsAdmin)
