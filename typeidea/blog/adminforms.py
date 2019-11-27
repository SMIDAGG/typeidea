from django import forms


class PostAdminForm(forms.ModelForm):
    #这里的字段desc是post中的字段，会覆盖原来的字段,required = False非必填项
    desc = forms.CharField(widget = forms.Textarea,label = '摘要',required = False)
