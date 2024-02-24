from io import BytesIO
from django.contrib import admin
from .models import EmailFile
from .services.email_data_reader import EmailCSVReader


# Register your models here.
class EmailFileAdmin(admin.ModelAdmin):
    list_display = ('email_file', "file_type")

    def save_model(self, request, obj, form, change):
        file = obj.email_file.file.file
        io_reader = EmailCSVReader()
        processed_email_obj = io_reader.read_email(file)
        obj.email_file.file = processed_email_obj
        super().save_model(request, obj, form, change)


admin.site.register(EmailFile, EmailFileAdmin)
