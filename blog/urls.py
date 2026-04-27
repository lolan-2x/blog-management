from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('edit-blog/' ,views.edit_blog,name='edit-blog'),
    path('add-blog/', views.add_blog,name='add-blog'),
    path('view-all/', views.view_all,name='view-all'),
    path('edit-blog/<int:blog_id>/', views.edit_blog, name='edit-blog'),
    path('delete-blog/<int:id>/', views.delete_blog, name='delete-blog'),
    path('blog/<int:id>/', views.blog_detail, name='blog-detail'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]