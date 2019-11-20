from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Category,Tag,Post
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','status','is_nav','owner','created_time')
    fields = ('name','status','is_nav')

    def save_model(self,request,obj,form,change):
        obj.owner = request.user
        return super().save_model(request,obj,form,change)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name','status','owner','created_time')
    fields = ['name','status']

    def save_model(self,request,obj,form,change):
        obj.owner = request.user
        return super().save_model(request,obj,form,change)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','desc','content','status','category','owner','created_time','operator') #operator是自定义字段，需要下面的方法才行，不然会报错
    # list_display = ('title','desc','content','status','category','owner','created_time')
    fields = (
        ('title','category'),
        'desc',
        'content',
        'status',
        'tag'
    )
    list_display_links=('title','desc','content')       #点击字段会进入编辑页面
    search_fields = ('title','category__name')          #添加搜索字段
    filter_horizontal = ('tag',)                        #在新增或或者编辑页面会多对多时会出现一个效果框

    actions_on_top = True                               #在显示所有文章页面上下都有操作
    actions_on_bottom = True

    save_on_top = True                                  #在编辑或者新增页面会上面也会出现保存按钮

    def operator(self,obj):
        return format_html('<a href="{}">编辑</a>',
                         reverse('admin:blog_post_change',args=(obj.id,)))
    operator.short_description = '操作'                 #指定表头

    def save_model(self,request,obj,form,change):
        obj.owner = request.user
        return super().save_model(request,obj,form,change)
