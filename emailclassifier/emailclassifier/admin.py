from django.contrib import admin


class MyAdminSite(admin.AdminSite):
    def get_app_list(self, request):
        app_list = list(self._build_app_dict(request).values())
        return app_list


customAdminSite = MyAdminSite()
admin.site = customAdminSite
