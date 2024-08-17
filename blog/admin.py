from django.contrib import admin
from .models import Post, AddRooms
from .models import Signup,Information
from .import models


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}




admin.site.register(Post, PostAdmin)
admin.site.register(Signup)
admin.site.register(Information)
admin.site.register(AddRooms)
admin.site.register(models.Category)


