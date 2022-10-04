from django.urls import path
from . import views
from Blog.views import BlogListView,BlogDetailView,BlogCreateView,BlogUpdateView,BlogDeleteView,UseristView

urlpatterns = [
    path('',BlogListView.as_view(),name = 'blog_home'),
    path('post/<int:pk>/',BlogDetailView.as_view(),name = 'blog_details'),
    path('user/<str:username>/',UseristView.as_view(),name = 'user_details'),
    path('post/new/',BlogCreateView.as_view(),name = 'blog_create'),
    path('post/<int:pk>/update/',BlogUpdateView.as_view(),name = 'blog_update'),
    path('post/<int:pk>/delete/',BlogDeleteView.as_view(),name = 'blog_delete'),
    path('about/',views.about,name = 'blog_about'),
    path('contact/',views.contact,name = 'blog_contact')
]
