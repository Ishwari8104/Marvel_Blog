
from django.urls import path
from . import views
from .views import HomeView,ArticleDetailView,AddPostView,UpdatePostView,DeletePostView,AddCategoryView,CategoryView,CategoryListView,ChatbotView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('article/<int:pk>',ArticleDetailView.as_view(),name='article_details'),
    path('add_post/',AddPostView.as_view(),name='add_post'),
    path('add_category/',AddCategoryView.as_view(),name='add_category'),
    path('update_post/<int:pk>',UpdatePostView.as_view(),name='update_post'),
    path('delete_post/<int:pk>',DeletePostView.as_view(),name='delete_post'),
    path('category/<str:cats>/',CategoryView,name='category'),
    path('category_list/',CategoryListView,name='category_list'),
    path('chatbot/',ChatbotView,name='chatbot'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]