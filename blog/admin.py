from django.contrib import admin
from .models import Post,Category,Comment,UserProfile
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
    date_hierarchy = 'published_date'
    list_display = ('id','title','counted_view','status','created_date','login_required')
    list_filter = ('status','login_required')
    search_fields = ('title','content')
    ordering = ('id',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('post','name','approved','created_date','user')
    list_filter = ('post','approved',)
    ordering = ['created_date']
    search_fields = ['title','content']

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Comment,CommentAdmin)
admin.site.register(UserProfile)