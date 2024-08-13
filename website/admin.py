from django.contrib import admin
from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['username','email','subject','created_date','updated_date']
    list_filter = ('email',)
    search_fields = ('name','meesage','lastname','username')

admin.site.register(Contact,ContactAdmin)