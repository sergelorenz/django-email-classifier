from django.core.exceptions import ValidationError
from django.contrib import admin, messages
from django import forms

from .models import Classification, ClassificationResults
from .services.file_reader import LocalFileReader
from .services.mock_classifier_service import MockClassifier


admin.site.disable_action('delete_selected')


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

    # ########### PLEASE READ ####################
    # Due to time constraints, this is only done synchronously which would cause UI blocking Especially on using ML
    # Using Celery with Redis/RabbitMQ would drastically improve the user experience for this action
    @admin.action(description='Perform classification on the selected items')
    def perform_classification(self, request, queryset):
        if queryset.count() > 1:
            messages.error(request, 'You can only select one item at a time')
            return

        ClassificationResults.objects.all().delete()
        for obj in queryset:
            new_results = []
            classifier = MockClassifier()
            file_path = obj.email_file.email_file.path
            file_reader = LocalFileReader()
            for row in file_reader.read_line(file_path):
                if len(row) == 2:
                    subject, body = row
                    email_class = classifier.classify(subject + body)
                    result = ClassificationResults(
                        email_subject=subject,
                        email_body=body,
                        email_class=email_class.name
                    )
                    new_results.append(result)

            ClassificationResults.objects.bulk_create(new_results)
            messages.success(request, 'Successfully performed classification')


admin.site.register(Classification, ClassificationAdmin)
