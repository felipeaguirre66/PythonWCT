from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
#URLS para el Blog
urlpatterns = [
    path('blog/', views.PostList.as_view(), name='blog'),
    path('nuevo/', login_required(views.CreatePost.as_view()), name='New'),
    path('<pk>/', views.PostDetails.as_view(), name='Detail'),
    path('editar/<pk>/', login_required(views.ModifyPost.as_view()), name='post_Edit'),
    path('borrar/<pk>/', login_required(views.DeletePost.as_view()), name='post_Delete'),
]