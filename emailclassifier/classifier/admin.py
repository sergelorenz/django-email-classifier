from django.contrib import admin

from .models import Classification


# Register your models here.
class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('email_file', 'classification_method', 'ml_classifier', 'classification_status')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Classification, ClassificationAdmin)
