from django.contrib import admin


class MyAdminSite(admin.AdminSite):
    def get_app_list(self, request, app_label=None):
        app_list = list(self._build_app_dict(request).values())
        return app_list


customAdminSite = MyAdminSite()
admin.site = customAdminSite
admin.site.site_header = 'Django Email Classifier Administration'
admin.site.site_title = 'Email Classifier Admin'
admin.site.index_title = 'Email Classifier Admin'
