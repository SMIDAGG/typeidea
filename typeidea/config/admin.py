from django.contrib import admin

from .models import Link,SideBar
from typeidea.custom_site import custom_site
# Register your models here.


@admin.register(Link,site = custom_site)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title','href','status','weight','owner','created_time')
    fileds = ('title','href','status','weight')

    def save_model(self,request,obj,form,change):
        obj.owner = request.user
        return super().save_model(request,obj,form,change)


@admin.register(SideBar,site = custom_site)
class SideBarAdmin(admin.ModelAdmin):
    list_display = ('title','display_type','content','status','owner','created_time')
    fields = ('title','display_type','content','status')

    def save_model(self,request,obj,form,change):
        obj.owner = request.user
        return super().save_model(request,obj,form,change)