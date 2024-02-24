from django.contrib import admin
from .models import Email, EmailFile

# Register your models here.
admin.site.register(Email)


class EmailFileAdmin(admin.ModelAdmin):
    list_display = ('email_file', )


admin.site.register(EmailFile, EmailFileAdmin)