from django.core.exceptions import ValidationError
from django.contrib import admin
from django import forms

from .models import Classification
from .services.file_reader import LocalFileReader


class ClassificationForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('classification_method') == 'ml' and cleaned_data.get('ml_classifier') == 'none':
            raise ValidationError('You must select ML classifier if you want to use Machine Learning Model')


# Register your models here.
class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('email_file', 'classification_method', 'ml_classifier', 'classification_status')
    actions = ['perform_classification']
    form = ClassificationForm

    def has_add_permission(self, request):
        return False

    def get_readonly_fields(self, request, obj=None):
        fields = ['email_file', 'classification_status']
        if obj.classification_method == 'logic':
            fields.append('ml_classifier')
            obj.ml_classifier = 'none'
        else:
            obj.ml_classifier = 'lr'

        obj.save()
        return fields

    @admin.action(description='Perform classification on the selected items')
    def perform_classification(self, request, queryset):
        for obj in queryset:
            file_path = obj.email_file.email_file.path
            file_reader = LocalFileReader()
            for row in file_reader.read_line(file_path):
                pass


admin.site.register(Classification, ClassificationAdmin)
