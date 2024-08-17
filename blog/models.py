from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(null=True, blank = True,upload_to='picture')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title



class Signup(models.Model):
    username = models.TextField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.TextField(max_length=50)
    confirm_password = models.TextField(max_length=50)

    def __str__(self):
        return str(self.email)
    
    
class AddRooms(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    bed = models.IntegerField()
    bathroom = models.IntegerField()
    details = models.TextField(max_length=300)
    roomsleft = models.IntegerField()
    image1 = models.ImageField(null=True, blank = True,upload_to='picture1')

    def __str__(self):
        return str(self.name) 

class Information(models.Model):
    fullname = models.CharField(max_length=100)
    email_info = models.CharField(max_length=100)
    address_info = models.CharField(max_length=100)
    city_info = models.CharField(max_length=100)
    zip_info = models.CharField(max_length=100)
    state_info = models.CharField(max_length=100)      

    def __str__(self):
        return str(self.fullname) 