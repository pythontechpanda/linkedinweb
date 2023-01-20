from django.db import models
from accounts.models import User
from datetime import datetime


# Create your models here.
class Country(models.Model):
    country = models.CharField(max_length=200)
    
    def __str__(self):
        return self.country
    
class State(models.Model):
    state = models.CharField(max_length=200)
    con_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.state
    
    
class City(models.Model):
    city = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.city
    
class Qualification(models.Model):
    opetion = models.CharField(max_length=100)
    
    def __str__(self):
        return self.opetion
    
    
class LookingFor(models.Model):
    opetion = models.CharField(max_length=100)
    
    def __str__(self):
        return self.opetion
    
    
class CoursesOptions(models.Model):
    opetion = models.CharField(max_length=100)
    
    def __str__(self):
        return self.opetion
    
    
class CompanyProfile(models.Model):
    name = models.CharField(max_length=200)
    display_picture = models.ImageField(upload_to='dp', blank=True, null=True)
    bg_picture = models.ImageField(upload_to='background', blank=True, null=True)
    email = models.CharField(max_length=200)
    service = models.CharField(max_length=300)
    discription = models.CharField(max_length=1000)
    contact = models.CharField(max_length=12)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    

class CreatePost(models.Model):
    name = models.CharField(max_length=100)
    post_img= models.ImageField(upload_to='post', blank=True, null=True)
    discription = models.CharField(max_length=300, null=True)
    like =  models.ManyToManyField(User, related_name="blog_posts", default=None, blank=True)
    comment = models.ManyToManyField(User, related_name="blog_comment", default=None, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now())
    body = models.TextField(max_length=300)
    
    
    def __str__(self):
        return self.author.first_name
    @property
    def num_likes(self):
        return self.like.all().count()
    
    def get_likes_given_no(self):
        likes = self.like_set.all()
        total_liked = 0
        for item in likes:
            if item.value=='Like':
                total_liked += 1
        return total_liked

    def get_likes_recieved_no(self):
        posts = self.posts.all()
        total_liked = 0
        for item in posts:
            total_liked += item.like.all().count()
        return total_liked
    
LIKE_CHOICES =(
    ('Like', 'Like'),
    ('Unlike','Unlike'),
)
    
class LikePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(CreatePost, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default="Like", max_length=10)
    
    def __str__(self):
        return str(self.post)