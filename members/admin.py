from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "firstname", "lastname", "email", "phone", "jobrole", "salary")
    search_fields = ("firstname", "lastname", "email", "jobrole")
    list_filter = ("jobrole",)
    ordering = ("id",)
admin.site.register(Employee, EmployeeAdmin)

