import os
from django.contrib import admin
from django.core.exceptions import ValidationError
from django import forms
from .models import EmailFile
from .services.email_data_reader import EmailCSVReader


class EmailFileForm(forms.ModelForm):
    class Meta:
        model = EmailFile
        fields = ['email_file', 'file_type']

    def clean(self):
        cleaned_data = super().clean()
        _, extension = os.path.splitext(cleaned_data.get('email_file').name)
        if extension != cleaned_data.get('file_type'):
            raise ValidationError('File Type does not match the uploaded file')


# Register your models here.
class EmailFileAdmin(admin.ModelAdmin):
    list_display = ('email_file', 'file_type')
    form = EmailFileForm

    def save_model(self, request, obj, form, change):
        file = obj.email_file.file.file
        io_reader = EmailCSVReader()
        processed_email_obj = io_reader.read_email(file)
        obj.email_file.file = processed_email_obj
        super().save_model(request, obj, form, change)


admin.site.register(EmailFile, EmailFileAdmin)
