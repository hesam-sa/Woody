from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(help_text='type something')
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    tags = TaggableManager()
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
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,default='3') 
    email = models.EmailField(help_text="A valid email address, please.")
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)  
    avatar = models.ImageField(upload_to='users/',default='users/un-user.jpg')  
    
    
 