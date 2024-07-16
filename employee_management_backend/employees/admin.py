from django.contrib import admin
from .models import Employee, Salary

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'department')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'base_salary', 'bonus', 'total_amount', 'date')
    search_fields = ('employee__first_name', 'employee__last_name', 'base_salary', 'bonus')

    def total_amount(self, obj):
        return obj.base_salary + obj.bonus
    total_amount.short_description = 'Total Amount'
