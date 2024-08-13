from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_date'
    list_display = ('id','title','counted_view','status','created_date','login_required')
    list_filter = ('status','login_required')
    search_fields = ('title','content')
    ordering = ('id',)

admin.site.register(Post,PostAdmin)