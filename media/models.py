from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    Creature = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    Image = models.ImageField(upload_to="posts/")
    title = models.CharField(max_length=70)
    like = models.ManyToManyField(User, related_name='likes', blank=True)
    creat_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Save(models.Model):
    saver = models.ForeignKey(User,related_name="owner",on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="post")
    
    def __str__(self):
        return "saved"

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE) 
    commenter = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    commenting = models.CharField(max_length=230)
    commented_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'liked'

class ChatPost(models.Model):
    poster = models.ForeignKey(User,related_name="poster",on_delete=models.CASCADE)
    Chat = models.CharField(max_length = 500)
    posted_at = models.TimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Chat
    