from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(help_text='type something')
    #image
    #catagory
    #author
    #tag
    counted_view = models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
    login_required = models.BooleanField(default=False)
  

    class Meta:
        verbose_name_plural = 'پست'

    def __str__(self):
        return self.title