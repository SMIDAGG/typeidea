from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Category,Tag,Post
from .adminforms import PostAdminForm
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin
# Register your models here.

#设置在分类页面添加文章编辑
class PostInline(admin.TabularInline):
    fields = ('title','desc')
    extra = 1
    model = Post

@admin.register(Category,site = custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    inlines = (PostInline,)
    list_display = ('name','status','is_nav','owner','created_time','post_count')
    fields = ('name','status','is_nav','owner')

    def post_count(self,obj):
        return obj.post_set.count()
    post_count.short_description = '文章数量'


@admin.register(Tag,site = custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name','status','owner','created_time')
    fields = ['name','status']


#自定义过滤器
class CategoryOwnerFilter(admin.SimpleListFilter):
    title = '分类过滤器'
    parameter_name = 'category_owner'

    def lookups(self,request,admin_model):
        return Category.objects.filter(owner = request.user).values_list('id','name')

    def queryset(self,request,queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id = self.value())
        return queryset


@admin.register(Post,site = custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = ('title','status','category','owner','created_time','operator') #operator是自定义字段，需要下面的方法才行，不然会报错
    # list_display = ('title','desc','content','status','category','owner','created_time')
    # fields = (
    #     ('title','category'),
    #     'desc',
    #     'content',
    #     'status',
    #     'tag',
    # )
    exclude=('owner',)                     #如果这里设置了字段不显示，则在编辑页面就不会出现上述字段，fields里也不能有这个字段，不然会报错
    fieldsets = (
        ('基础配置',{
            'description':'碁础配置描述',
            'classes':('wide',),                #collapse作用是 表单隐藏
            'fields':(
                ('title','category'),
                'status',
            )
         }),
        ('内容',{
            'description':'内容编辑',
            'fields':(
                'desc',
                'content',
            )
        }),
        ('额外信息',{
            'classes':('wide',),
            'fields':(
                'tag',
            )
        })
    )
    list_filter = (CategoryOwnerFilter,)
    list_display_links=('title',)       #点击字段会进入编辑页面
    search_fields = ('title','category__name')          #添加搜索字段
    filter_horizontal = ('tag',)              #在新增或或者编辑页面会多对多时会出现一个效果框

    actions_on_top = True                               #在显示所有文章页面上下都有操作
    actions_on_bottom = True

    save_on_top = True                                  #在编辑或者新增页面会上面也会出现保存按钮

    def operator(self,obj):
        return format_html('<a href="{}">编辑</a>',
                         reverse('cus_admin:blog_post_change',args=(obj.id,)))
    operator.short_description = '操作'                 #指定表头

