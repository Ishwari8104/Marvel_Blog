from django import forms
from .models import Post,Category


#choices=[('Films','Films'),('TV Series','TV Series'),('Comics','Comics'),]
choices=Category.objects.all().values_list('name','name')
choice_list=[]
for item in choices:
    choice_list.append(item)
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','author','body','category')
        widgets={"title":forms.TextInput(attrs={'class':'form-control','placeholder':"Enter the title of your blog here!"}),
                "author":forms.TextInput(attrs={'class':'form-control','value':'','id':'identity','type':'hidden'}),
                "category":forms.Select(choices=choice_list,attrs={'class':'form-control'}),
                "body":forms.Textarea(attrs={'class':'form-control','placeholder':"Write your blog here!"}),
                
                
                }
        
class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','body','category')
        widgets={"title":forms.TextInput(attrs={'class':'form-control','placeholder':"Enter the title of your blog here!"}),
                
                "category":forms.Select(choices=choices,attrs={'class':'form-control'}),
                "body":forms.Textarea(attrs={'class':'form-control','placeholder':"Write your blog here!"}),
                
                
                }
        
