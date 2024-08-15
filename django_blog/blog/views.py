from typing import Any, Dict
from django.shortcuts import render
from .models import Post,Category
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import PostForm,EditForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from openai import OpenAI



# Create your views here.
class HomeView(ListView):
    model=Post
    template_name='home.html'
    ordering=['-post_date']
    
    def get_context_data(self,*args, **kwargs):
        cat_menu=Category.objects.all()
        context=super().get_context_data(*args, **kwargs)
        context["cat_menu"]=cat_menu
        return context
    
def CategoryListView(request):
    cat_menu_list=Category.objects.all()
    return render(request,'category_list.html',{'cat_menu_list':cat_menu_list})
    
    
class ArticleDetailView(DetailView):
    model=Post
    template_name='article_details.html'
    
class AddPostView(CreateView):
    model=Post
    form_class=PostForm
    template_name='add_post.html'
    
class AddCategoryView(CreateView):
    model=Category
    fields='__all__'
    template_name='add_category.html'
    
class UpdatePostView(UpdateView):
    model=Post
    form_class=EditForm
    template_name='update_post.html'
    
    
class DeletePostView(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url=reverse_lazy('home')
    
def CategoryView(request,cats):
    category_posts=Post.objects.filter(category=cats)
    return render(request,'categories.html',{'cats':cats.title(),'category_posts':category_posts})
    
    




def ChatbotView(request):
    if request.method == 'POST':
        chat = request.POST.get('message')
        response = query_comics(chat)  # Use the utility function
        return JsonResponse({'message': chat, 'response': response})
    return render(request, 'chatbot.html')
