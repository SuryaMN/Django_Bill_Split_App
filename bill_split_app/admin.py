from django.contrib import admin
from .models import Member,Expenditure
# Register your models here.

class ExpenditureAdmin(admin.ModelAdmin):
    list_display = ('payer','payee','amount','description')

admin.site.register(Member)
admin.site.register(Expenditure,ExpenditureAdmin)