from django.contrib import admin

from .models import Comment


# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('target','content','nickname','website','email','status','created_time')
