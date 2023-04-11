from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display=('pk','post_heading','post_text','post_author')

class LikeAdmin(admin.ModelAdmin):
    list_display=('pk','post')


admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)