from django.contrib import admin
from .models import Contact,NewsLetter

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['name','email','subject','created_date','updated_date']
    list_filter = ('email',)
    search_fields = ('name','meesage','lastname')

admin.site.register(Contact,ContactAdmin)
admin.site.register(NewsLetter)