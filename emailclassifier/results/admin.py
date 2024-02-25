from django.contrib import admin
from django.utils.text import Truncator

from classifier.models import ClassificationResults


# Register your models here.
class ClassificationResultsAdmin(admin.ModelAdmin):
    list_display = ('email_subject', 'truncated_email_body', 'email_class')
    list_per_page = 20

    def truncated_email_body(self, obj):
        return Truncator(obj.email_body).words(100)

    truncated_email_body.short_description = 'Email Body'


admin.site.register(ClassificationResults, ClassificationResultsAdmin)