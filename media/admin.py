from django.contrib import admin
from .models import Post,ChatPost,Comment,Save
# Register your models here.

admin.site.register(Post)
admin.site.register(ChatPost)
admin.site.register(Comment)
admin.site.register(Save)
